#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
viewdns_recon.py
================
Coleta automatizada de inteligência de domínio/IP via API oficial do ViewDNS.info,
com saída formatada por módulo e uma análise que correlaciona os resultados.

Módulos:
  1) Reverse IP Lookup        4) Subdomain Discovery     7) DNSSEC Test*
  2) Reverse WHOIS Lookup     5) Reverse NS Lookup
  3) IP History               6) Port Scanner

  * O ViewDNS não oferece DNSSEC na API; a checagem é feita via DNS-over-HTTPS (dns.google).

Uso:
  python viewdns_recon.py exemplo.com
  python viewdns_recon.py 203.0.113.10
  python viewdns_recon.py exemplo.com --html relatorio.html --json dados.json
  python viewdns_recon.py --demo            # sem API, com dados fictícios

Use apenas em alvos que você tem autorização para investigar e respeite os
Termos de Serviço da API do ViewDNS.
"""
from __future__ import annotations

import argparse
import difflib
import ipaddress
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Any, Callable

import requests
from rich import box
from rich.console import Console, Group
from rich.markup import escape
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.tree import Tree

# ══════════════════════════════════════════════════════════════════════════════
#  ▶▶▶  COLE SUA CHAVE DA API DO VIEWDNS ENTRE AS ASPAS ABAIXO  ◀◀◀
# ══════════════════════════════════════════════════════════════════════════════
API_KEY = ""  # <<<<<<<<<<  COLE_SUA_CHAVE_AQUI  >>>>>>>>>>
# ══════════════════════════════════════════════════════════════════════════════
# (Opcional) em vez de colar no código, defina a variável de ambiente
# VIEWDNS_API_KEY. NUNCA suba sua chave para um repositório público.
API_KEY = os.getenv("VIEWDNS_API_KEY", API_KEY).strip()

BASE_URL = "https://api.viewdns.info"
DOH_URL = "https://dns.google/resolve"

ORDER = ["reverseip", "reversewhois", "iphistory", "subdomains", "reversens", "portscan", "dnssec"]
TITLES = {
    "reverseip": "Reverse IP Lookup",
    "reversewhois": "Reverse WHOIS Lookup",
    "iphistory": "IP History",
    "subdomains": "Subdomain Discovery",
    "reversens": "Reverse NS Lookup",
    "portscan": "Port Scanner",
    "dnssec": "DNSSEC Test",
}
NUMS = {k: n for k, n in zip(ORDER, "①②③④⑤⑥⑦")}
IP_ONLY_MODULES = {"reverseip", "portscan"}  # módulos que fazem sentido para um IP

CDN_HINTS = ("cloudflare", "akamai", "fastly", "cloudfront", "incapsula", "imperva",
             "sucuri", "stackpath", "edgecast", "cdn77", "bunny", "limelight")
SHARED_NS_HINTS = ("cloudflare.com", "awsdns", "googledomains", "domaincontrol.com",
                   "azure-dns", "dnsmadeeasy", "registrar-servers.com", "nsone.net",
                   "ultradns", "dynect", "google.com", "worldnic.com", "hichina.com")

RISKY_PORTS = {
    21: ("médio", "FTP trafega credenciais em texto claro"),
    22: ("baixo", "SSH exposto: restrinja por IP/chave e monitore tentativas de login"),
    23: ("alto", "Telnet sem criptografia"),
    25: ("baixo", "SMTP aberto: confirme que não há open relay"),
    110: ("médio", "POP3 (sem TLS por padrão)"),
    139: ("alto", "NetBIOS exposto à internet"),
    445: ("alto", "SMB exposto à internet"),
    1433: ("alto", "SQL Server exposto à internet"),
    1521: ("alto", "Oracle DB exposto à internet"),
    3306: ("alto", "MySQL exposto à internet"),
    3389: ("alto", "RDP exposto: alvo frequente de brute force e ransomware"),
    8080: ("baixo", "HTTP alternativo: costuma esconder painéis/aplicações secundárias"),
    8443: ("baixo", "HTTPS alternativo: costuma esconder painéis/aplicações secundárias"),
}

SUB_CATS = [
    ("ambientes dev/teste", ("dev", "test", "stage", "staging", "qa", "hml", "homolog", "uat", "sandbox", "demo", "beta"),
     "médio", "Ambientes não produtivos costumam ter controles mais fracos"),
    ("painéis administrativos", ("admin", "painel", "panel", "cpanel", "whm", "manage", "console", "backoffice", "webmin", "phpmyadmin"),
     "médio", "Painéis de administração expostos"),
    ("acesso remoto", ("vpn", "rdp", "remote", "citrix", "gateway", "ssh", "bastion", "rdweb"),
     "médio", "Pontos de entrada remotos (alvos de credential stuffing)"),
    ("ferramentas internas", ("git", "gitlab", "jenkins", "jira", "confluence", "svn", "ci", "grafana", "kibana", "sonar", "nexus", "wiki"),
     "médio", "Ferramentas internas acessíveis pela internet"),
    ("dados/legado", ("db", "sql", "mysql", "backup", "bkp", "old", "legacy", "ftp", "files"),
     "médio", "Nomes sugerem dados, backups ou sistemas legados"),
    ("e-mail", ("mail", "smtp", "imap", "pop", "webmail", "mx", "owa", "autodiscover"),
     "info", "Infraestrutura de e-mail (confira SPF/DKIM/DMARC)"),
    ("APIs", ("api", "graphql", "gw"),
     "info", "Endpoints de API"),
]

SEV_STYLE = {"alto": "bold red", "médio": "bold yellow", "baixo": "cyan", "info": "dim",
             "alta": "bold green", "média": "bold yellow", "baixa": "cyan"}
SEV_ORDER = {"alto": 0, "alta": 0, "médio": 1, "média": 1, "baixo": 2, "baixa": 2, "info": 3}


# ══════════════════════════════════════════════════════════════════════════════
#  Modelos
# ══════════════════════════════════════════════════════════════════════════════
class ApiError(Exception):
    pass


class ModuleSkip(Exception):
    pass


@dataclass
class ModuleResult:
    key: str
    status: str                      # ok | error | skip
    data: dict = field(default_factory=dict)
    message: str = ""
    seconds: float = 0.0


@dataclass
class Ctx:
    api: "ViewDNS | None"
    target: str
    apex: str
    is_ip: bool
    ns_list: list
    ns_override: list
    whois_q: str | None
    force_ns: bool
    current_ips: list = field(default_factory=list)


@dataclass
class Finding:
    level: str
    title: str
    detail: str


@dataclass
class Analysis:
    risks: list = field(default_factory=list)
    clues: list = field(default_factory=list)
    linked: list = field(default_factory=list)
    pivots: list = field(default_factory=list)


# ══════════════════════════════════════════════════════════════════════════════
#  Utilitários
# ══════════════════════════════════════════════════════════════════════════════
def is_ip(value: str) -> bool:
    try:
        ipaddress.ip_address(value)
        return True
    except ValueError:
        return False


def clean_target(raw: str) -> str:
    v = re.sub(r"^[a-z][a-z0-9+.-]*://", "", raw.strip().lower())
    v = v.split("/")[0]
    if v.count(":") <= 1:          # tira porta (mas preserva IPv6)
        v = v.split(":")[0]
    return v.rstrip(".")


def e(v: Any) -> str:
    """Escapa texto vindo da API para o markup do rich."""
    return "-" if v in (None, "") else escape(str(v))


def to_int(v: Any, default: int = 0) -> int:
    try:
        return int(str(v).replace(",", ""))
    except (TypeError, ValueError):
        return default


def as_list(v: Any) -> list:
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def is_cdn(owner: str | None) -> bool:
    o = (owner or "").lower()
    return any(h in o for h in CDN_HINTS)


def is_shared_ns(ns: str) -> bool:
    return any(h in ns.lower() for h in SHARED_NS_HINTS)


def is_lookalike(domain: str, brand: str | None) -> bool:
    if not brand or len(brand) < 4:
        return False
    label = domain.split(".")[0]
    if label == brand:
        return False
    flat, b = label.replace("-", ""), brand.replace("-", "")
    if b in flat:
        return True
    return difflib.SequenceMatcher(None, flat, b).ratio() >= 0.84


# ══════════════════════════════════════════════════════════════════════════════
#  Cliente ViewDNS
# ══════════════════════════════════════════════════════════════════════════════
class ViewDNS:
    def __init__(self, key: str, timeout: int = 30, retries: int = 3):
        self.key = key
        self.timeout = timeout
        self.retries = retries
        self.session = requests.Session()
        self.session.headers["User-Agent"] = "viewdns-recon/1.0"

    def _scrub(self, msg: str) -> str:
        return msg.replace(self.key, "***") if self.key else msg   # nunca vazar a chave

    @staticmethod
    def _extract_error(data: Any) -> str | None:
        if not isinstance(data, dict):
            return None
        resp = data.get("response")
        if isinstance(resp, str):
            return resp
        for src in (data, resp if isinstance(resp, dict) else {}):
            for k in ("error", "error_message", "errormsg"):
                if src.get(k):
                    return str(src[k])
        return None

    def call(self, tool: str, **params: Any) -> dict:
        params = {**params, "apikey": self.key, "output": "json"}
        url = f"{BASE_URL}/{tool}/"
        last = "falha desconhecida"
        for attempt in range(1, self.retries + 1):
            try:
                r = self.session.get(url, params=params, timeout=self.timeout)
                if r.status_code in (429, 500, 502, 503, 504):
                    last = f"HTTP {r.status_code} (limite de requisições ou instabilidade)"
                    time.sleep(2 ** attempt)
                    continue
                r.raise_for_status()
                data = r.json()
                err = self._extract_error(data)
                if err:
                    raise ApiError(err)
                resp = data.get("response", data)
                return resp if isinstance(resp, dict) else {}
            except ApiError:
                raise
            except (requests.RequestException, ValueError) as exc:
                last = self._scrub(str(exc))
                time.sleep(2 ** attempt)
        raise ApiError(self._scrub(last))


# ══════════════════════════════════════════════════════════════════════════════
#  DNS-over-HTTPS (descoberta de NS, IPs atuais e DNSSEC)
# ══════════════════════════════════════════════════════════════════════════════
def doh(name: str, rtype: str, dnssec: bool = False, timeout: int = 10) -> dict:
    r = requests.get(DOH_URL, params={"name": name, "type": rtype, "do": "1" if dnssec else "0"},
                     headers={"accept": "application/dns-json"}, timeout=timeout)
    r.raise_for_status()
    return r.json()


def find_apex_and_ns(domain: str) -> tuple[str, list]:
    """Sobe os rótulos até achar a zona que tem NS (ex.: www.exemplo.com.br -> exemplo.com.br)."""
    labels = domain.split(".")
    for i in range(max(len(labels) - 1, 1)):
        name = ".".join(labels[i:])
        try:
            ans = [a["data"].rstrip(".").lower() for a in doh(name, "NS").get("Answer", []) if a.get("type") == 2]
        except requests.RequestException:
            ans = []
        if ans:
            return name, sorted(set(ans))
    return domain, []


def resolve_ips(name: str) -> list:
    try:
        return sorted({a["data"] for a in doh(name, "A").get("Answer", []) if a.get("type") == 1})
    except requests.RequestException:
        return []


# ══════════════════════════════════════════════════════════════════════════════
#  Módulos de coleta
# ══════════════════════════════════════════════════════════════════════════════
def run_reverseip(c: Ctx) -> dict:
    resp = c.api.call("reverseip", host=c.target)
    items = [{"name": d.get("name"), "last_resolved": d.get("last_resolved")} for d in as_list(resp.get("domains"))]
    return {"host": c.target, "count": to_int(resp.get("domain_count"), len(items)), "domains": items}


def run_reversewhois(c: Ctx) -> dict:
    q = c.whois_q or c.apex
    resp = c.api.call("reversewhois", q=q)
    items = [{"domain": m.get("domain"), "created": m.get("created_date"), "registrar": m.get("registrar")}
             for m in as_list(resp.get("matches"))]
    return {"query": q, "count": to_int(resp.get("result_count"), len(items)), "matches": items}


def run_iphistory(c: Ctx) -> dict:
    resp = c.api.call("iphistory", domain=c.apex)
    return build_history(as_list(resp.get("records")))


def build_history(records: list) -> dict:
    per_ip: dict = {}
    for r in records:
        ip, seen = r.get("ip"), r.get("lastseen") or ""
        if not ip:
            continue
        x = per_ip.setdefault(ip, {"ip": ip, "owner": r.get("owner") or "?", "location": r.get("location") or "?",
                                   "first": "", "last": "", "hits": 0})
        if seen:
            x["first"] = min(x["first"], seen) if x["first"] else seen
            x["last"] = max(x["last"], seen)
        x["hits"] += 1
    ips = sorted(per_ip.values(), key=lambda v: v["last"], reverse=True)
    per_owner: dict = {}
    for x in ips:
        o = per_owner.setdefault(x["owner"], {"owner": x["owner"], "ips": 0, "first": "", "last": ""})
        o["ips"] += 1
        if x["first"]:
            o["first"] = min(o["first"], x["first"]) if o["first"] else x["first"]
        o["last"] = max(o["last"], x["last"])
    owners = sorted(per_owner.values(), key=lambda v: v["last"], reverse=True)
    return {"total_records": len(records), "ips": ips, "owners": owners}


def run_subdomains(c: Ctx) -> dict:
    resp = c.api.call("subdomains", domain=c.apex)
    items = [{"name": s.get("name"), "ips": [str(i) for i in as_list(s.get("ips"))], "last_resolved": s.get("last_resolved")}
             for s in as_list(resp.get("subdomains"))]
    return {"count": to_int(resp.get("subdomain_count"), len(items)), "subdomains": items}


def run_reversens(c: Ctx) -> dict:
    servers = c.ns_override or c.ns_list
    if not servers:
        raise ModuleSkip("nenhum nameserver encontrado para o domínio (use --ns)")
    out, queried = [], 0
    for ns in servers[:4]:
        if is_shared_ns(ns) and not (c.force_ns or c.ns_override):
            out.append({"ns": ns, "count": None, "domains": [], "note": "infra compartilhada (milhões de domínios) — ignorado; use --force-ns"})
            continue
        resp = c.api.call("reversens", ns=ns)
        doms = [d.get("domain") for d in as_list(resp.get("domains")) if d.get("domain")]
        out.append({"ns": ns, "count": to_int(resp.get("domain_count"), len(doms)), "domains": doms, "note": ""})
        queried += 1
    if queried == 0:
        raise ModuleSkip("todos os NS são de provedores compartilhados (baixo valor de correlação); use --force-ns")
    return {"by_ns": out}


def run_portscan(c: Ctx) -> dict:
    resp = c.api.call("portscan", host=c.target)
    ports = [{"number": to_int(p.get("number")), "service": p.get("service"), "status": (p.get("status") or "").lower()}
             for p in as_list(resp.get("port"))]
    return {"host": c.target, "ports": ports}


def run_dnssec(c: Ctx) -> dict:
    """DNSSEC via DoH. DS = elo no domínio pai; DNSKEY = chaves da zona; AD = resolvedor validou a cadeia."""
    ds = [a for a in doh(c.apex, "DS", dnssec=True).get("Answer", []) if a.get("type") == 43]
    key = [a for a in doh(c.apex, "DNSKEY", dnssec=True).get("Answer", []) if a.get("type") == 48]
    probe = doh(c.apex, "SOA", dnssec=True)
    ad, status = bool(probe.get("AD")), probe.get("Status")
    if status == 2:
        verdict, label = "validation_fail", "SERVFAIL — possível DNSSEC quebrado (falha de validação)"
    elif ds and key and ad:
        verdict, label = "signed_valid", "Assinado e validado (cadeia de confiança OK)"
    elif key and not ds:
        verdict, label = "broken_chain", "DNSKEY presente, mas sem DS no domínio pai (cadeia incompleta)"
    elif ds and not key:
        verdict, label = "broken_chain", "DS no pai, mas zona sem DNSKEY (configuração inconsistente)"
    elif ds and key and not ad:
        verdict, label = "validation_fail", "DS e DNSKEY presentes, mas a validação não foi confirmada"
    else:
        verdict, label = "unsigned", "Não assinado (sem DNSSEC)"
    return {"domain": c.apex, "verdict": verdict, "label": label, "ds": len(ds), "dnskey": len(key), "ad": ad, "rcode": status}


FUNCS: dict[str, Callable[[Ctx], dict]] = {
    "reverseip": run_reverseip, "reversewhois": run_reversewhois, "iphistory": run_iphistory,
    "subdomains": run_subdomains, "reversens": run_reversens, "portscan": run_portscan, "dnssec": run_dnssec,
}


def summarize(key: str, d: dict) -> str:
    if key == "reverseip":
        return f"{d['count']} domínio(s) no host"
    if key == "reversewhois":
        return f"{d['count']} domínio(s) · q={d['query']}"
    if key == "iphistory":
        return f"{len(d['ips'])} IP(s) únicos · {len(d['owners'])} provedor(es)"
    if key == "subdomains":
        return f"{d['count']} subdomínio(s)"
    if key == "reversens":
        parts = [f"{x['ns']}: {x['count']}" if x["count"] is not None else f"{x['ns']}: ignorado" for x in d["by_ns"]]
        return " · ".join(parts)
    if key == "portscan":
        n_open = sum(1 for p in d["ports"] if p["status"] == "open")
        return f"{n_open} aberta(s) de {len(d['ports'])}"
    if key == "dnssec":
        return d["label"]
    return ""


def execute(ctx: Ctx, keys: list, workers: int) -> dict:
    def job(k: str) -> ModuleResult:
        t0 = time.time()
        try:
            data = FUNCS[k](ctx)
            return ModuleResult(k, "ok", data, summarize(k, data), time.time() - t0)
        except ModuleSkip as exc:
            return ModuleResult(k, "skip", {}, str(exc), time.time() - t0)
        except Exception as exc:                       # noqa: BLE001
            msg = ctx.api._scrub(str(exc)) if ctx.api else str(exc)
            return ModuleResult(k, "error", {}, msg, time.time() - t0)

    results: dict = {}
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futs = {pool.submit(job, k): k for k in keys}
        for f in as_completed(futs):
            r = f.result()
            results[r.key] = r
    return results


# ══════════════════════════════════════════════════════════════════════════════
#  Dados fictícios (modo --demo) — IPs de documentação (RFC 5737), TLD .example
# ══════════════════════════════════════════════════════════════════════════════
def demo_context() -> tuple[Ctx, dict]:
    ctx = Ctx(api=None, target="acmecorp.example", apex="acmecorp.example", is_ip=False,
              ns_list=["ns1.acmedns.example", "ns2.acmedns.example"], ns_override=[], whois_q=None,
              force_ns=False, current_ips=["203.0.113.45"])
    R: dict = {}

    def ok(k, d):
        R[k] = ModuleResult(k, "ok", d, summarize(k, d), 0.4)

    filler = [f"loja-exemplo-{i:02d}.example" for i in range(1, 12)]
    rip = ["acmecorp.example", "acmecorp-store.example", "acme-corp-login.example"] + filler
    ok("reverseip", {"host": ctx.target, "count": len(rip),
                     "domains": [{"name": d, "last_resolved": "2026-10-0%d" % (1 + i % 6)} for i, d in enumerate(rip)]})

    ok("reversewhois", {"query": ctx.apex, "count": 4, "matches": [
        {"domain": "acmecorp.example", "created": "2014-03-18", "registrar": "Example Registrar, Inc."},
        {"domain": "acmecorp-store.example", "created": "2021-07-09", "registrar": "Example Registrar, Inc."},
        {"domain": "acmecorp-mail.example", "created": "2021-07-09", "registrar": "Example Registrar, Inc."},
        {"domain": "acmeholding.example", "created": "2021-07-09", "registrar": "Other Registrar LLC"},
    ]})

    recs = []
    for ip, loc, own, dates in [
        ("203.0.113.45", "Exampletown - EX", "HostingProviderA Ltd", ["2026-10-04", "2026-06-11", "2025-03-02", "2024-04-20"]),
        ("198.51.100.10", "Unknown", "Cloudflare, Inc", ["2024-03-30", "2023-08-14", "2022-09-01"]),
        ("198.51.100.11", "Unknown", "Cloudflare, Inc", ["2024-03-29", "2023-08-14", "2022-09-02"]),
        ("192.0.2.77", "Sampleville - EX", "LegacyHost SA", ["2022-08-20", "2021-05-05", "2019-11-30"]),
    ]:
        recs += [{"ip": ip, "location": loc, "owner": own, "lastseen": d} for d in dates]
    ok("iphistory", build_history(recs))

    subs = [("www", ["203.0.113.45"]), ("mail", ["203.0.113.60"]), ("api", ["203.0.113.45"]), ("dev", ["203.0.113.99"]),
            ("staging", ["203.0.113.99"]), ("vpn", ["203.0.113.70"]), ("admin", ["203.0.113.45"]), ("git", ["203.0.113.81"]),
            ("portal", ["203.0.113.45"]), ("blog", []), ("shop", ["203.0.113.45"]), ("cdn", [])]
    ok("subdomains", {"count": len(subs), "subdomains": [{"name": f"{s}.{ctx.apex}", "ips": ips, "last_resolved": "2026-09-28"} for s, ips in subs]})

    shared = ["acmecorp.example", "acmecorp-store.example", "acmecorp-mail.example", "acmeholding.example"] + \
             [f"parceiro-{i:02d}.example" for i in range(1, 8)]
    ok("reversens", {"by_ns": [{"ns": n, "count": len(shared), "domains": shared, "note": ""} for n in ctx.ns_list]})

    open_ports = {22, 80, 443, 3306}
    svc = [(21, "FTP"), (22, "SSH"), (23, "Telnet"), (25, "SMTP"), (53, "DNS"), (80, "HTTP"), (110, "POP3"), (139, "NETBIOS"),
           (143, "IMAP"), (443, "HTTPS"), (445, "SMB"), (1433, "MSSQL"), (1521, "ORACLE"), (3306, "MySQL"),
           (3389, "Remote Desktop"), (8080, "HTTP Alt"), (8443, "HTTPS Alt")]
    ok("portscan", {"host": ctx.target, "ports": [{"number": n, "service": s, "status": "open" if n in open_ports else "closed"} for n, s in svc]})

    ok("dnssec", {"domain": ctx.apex, "verdict": "unsigned", "label": "Não assinado (sem DNSSEC)", "ds": 0, "dnskey": 0, "ad": False, "rcode": 0})
    return ctx, R


# ══════════════════════════════════════════════════════════════════════════════
#  Correlação e análise
# ══════════════════════════════════════════════════════════════════════════════
def categorize_subdomains(ctx: Ctx, subs: list) -> dict:
    found: dict = defaultdict(list)
    for s in subs:
        name = (s["name"] or "").lower()
        prefix = name[: -len(ctx.apex)].rstrip(".") if name.endswith(ctx.apex) else name
        tokens = {t for t in re.split(r"[.\-_0-9]+", prefix) if t}
        for cat, words, level, why in SUB_CATS:
            if tokens & set(words):
                found[cat].append(name)
    return found


def correlate(ctx: Ctx, R: dict) -> Analysis:
    A = Analysis()

    def D(k):
        return R[k].data if k in R and R[k].status == "ok" else None

    brand = None if ctx.is_ip else ctx.apex.split(".")[0]
    behind_cdn_now = False
    hist = D("iphistory")

    # ── Histórico de IP ─────────────────────────────────────────────
    if hist and hist["ips"]:
        ips, owners = hist["ips"], hist["owners"]
        latest = ips[0]
        behind_cdn_now = is_cdn(latest["owner"])
        non_cdn_old = [x for x in ips if not is_cdn(x["owner"]) and x["ip"] != latest["ip"]]
        if non_cdn_old:
            top = ", ".join(f"{x['ip']} ({x['owner']}, até {x['last'] or '?'})" for x in non_cdn_old[:3])
            if behind_cdn_now:
                A.clues.append(Finding("média", "Possível IP de origem fora da CDN",
                                       f"Hoje o domínio está atrás de CDN; IPs anteriores fora de CDN: {top}. Valide antes de afirmar."))
            else:
                A.clues.append(Finding("baixa", "IPs anteriores de hospedagem", f"{top}. Úteis para pivotar (reverse IP / port scan)."))
            A.pivots.append("Rodar o script (ou reverse IP/port scan) nos IPs históricos: " + ", ".join(x["ip"] for x in non_cdn_old[:3]))
        if len(owners) >= 2:
            chain = "  ←  ".join(f"{o['owner']} ({(o['first'] or '?')[:7]}→{(o['last'] or '?')[:7]})" for o in owners[:4])
            A.clues.append(Finding("baixa", f"Migrou entre {len(owners)} provedores", chain))
        if ctx.current_ips and latest["ip"] not in ctx.current_ips:
            A.clues.append(Finding("baixa", "IP atual difere do último registro histórico",
                                   f"DNS agora: {', '.join(ctx.current_ips)} · último no histórico: {latest['ip']}. Pode indicar migração recente."))

    # ── Reverse IP ──────────────────────────────────────────────────
    rip = D("reverseip")
    if rip:
        c = rip["count"]
        if c >= 200:
            A.clues.append(Finding("baixa", "IP muito compartilhado", f"~{c} domínios no mesmo IP: co-hospedagem sozinha é indício fraco (hosting compartilhado/CDN)."))
        elif c > 25:
            A.clues.append(Finding("baixa", "IP moderadamente compartilhado", f"{c} domínios: valide com NS/WHOIS antes de concluir vínculo."))
        elif c > 0:
            A.clues.append(Finding("média", "IP pouco compartilhado", f"Apenas {c} domínio(s) no IP: co-hospedados são bons candidatos a mesmo operador."))

    # ── Reverse NS ──────────────────────────────────────────────────
    rns = D("reversens")
    if rns:
        for x in rns["by_ns"]:
            if x["count"] is not None and 0 < x["count"] <= 300:
                A.clues.append(Finding("média", f"NS pouco compartilhado: {x['ns']}", f"{x['count']} domínios usam este nameserver — provável mesmo operador."))

    # ── Reverse WHOIS ───────────────────────────────────────────────
    rw = D("reversewhois")
    if rw:
        if rw["count"] == 0:
            A.clues.append(Finding("baixa", "Reverse WHOIS sem retorno", "Provável proteção de privacidade (WHOIS redigido)."))
            A.pivots.append("Pegar e-mail/nome do registrante no WHOIS e rodar com --whois-q 'email@dominio'.")
        else:
            days = Counter(m["created"] for m in rw["matches"] if m.get("created"))
            if days:
                day, n = days.most_common(1)[0]
                if n >= 3:
                    A.clues.append(Finding("média", "Registro em lote", f"{n} domínios criados no mesmo dia ({day}) — padrão típico de um mesmo registrante."))
            regs = Counter(m["registrar"] for m in rw["matches"] if m.get("registrar"))
            if regs:
                reg, n = regs.most_common(1)[0]
                A.clues.append(Finding("baixa", "Registrar predominante", f"{reg} ({n}/{rw['count']} domínios)"))
        if rw["count"] <= 3:
            A.pivots.append("Poucos resultados no reverse WHOIS: tente --whois-q com e-mail, telefone ou nome da organização.")

    # ── Domínios correlacionados (interseção entre fontes) ─────────
    linked: dict = defaultdict(set)

    def add(domain: str | None, src: str):
        d = (domain or "").lower().rstrip(".")
        if d and d != ctx.apex and d != ctx.target:
            linked[d].add(src)

    if rip:
        for x in rip["domains"]:
            add(x["name"], "IP")
    if rns:
        for x in rns["by_ns"]:
            for d in x["domains"]:
                add(d, "NS")
    if rw:
        for m in rw["matches"]:
            add(m["domain"], "WHOIS")

    rows = []
    for d, srcs in linked.items():
        look = is_lookalike(d, brand)
        if len(srcs) >= 2 or look:
            rows.append({"domain": d, "sources": sorted(srcs), "score": len(srcs), "lookalike": look})
    rows.sort(key=lambda r: (-r["score"], not r["lookalike"], r["domain"]))
    A.linked = rows
    strong = [r for r in rows if r["score"] >= 3]
    medium = [r for r in rows if r["score"] == 2]
    look_only = [r for r in rows if r["score"] == 1 and r["lookalike"]]
    if strong:
        A.clues.insert(0, Finding("alta", f"{len(strong)} domínio(s) em 3 fontes", ", ".join(r["domain"] for r in strong[:5]) + " — IP + NS + WHOIS convergem."))
    if medium:
        A.clues.insert(len(strong) > 0, Finding("média", f"{len(medium)} domínio(s) em 2 fontes", ", ".join(r["domain"] for r in medium[:5])))
    if look_only:
        A.clues.append(Finding("baixa", f"{len(look_only)} possível(is) look-alike(s)",
                               ", ".join(r["domain"] for r in look_only[:5]) + " — nome parecido com a marca; avaliar phishing/typosquatting."))
    top_linked = [r["domain"] for r in rows if r["score"] >= 2][:3]
    if top_linked:
        A.pivots.append("Reexecutar o script nos domínios com ≥2 fontes: " + ", ".join(top_linked))

    # ── Subdomínios ────────────────────────────────────────────────
    sd = D("subdomains")
    if sd:
        for cat, names in categorize_subdomains(ctx, sd["subdomains"]).items():
            level, why = next((l, w) for c, _, l, w in SUB_CATS if c == cat)
            ex = ", ".join(sorted(set(names))[:4]) + (f" (+{len(set(names)) - 4})" if len(set(names)) > 4 else "")
            A.risks.append(Finding(level, f"Subdomínios de {cat}", f"{ex} — {why}."))
        sub_ips = {i for s in sd["subdomains"] for i in s["ips"]}
        if len(sub_ips) >= 3:
            A.clues.append(Finding("baixa", f"Subdomínios espalhados em {len(sub_ips)} IPs", "Infra distribuída: " + ", ".join(sorted(sub_ips)[:5])))
            A.pivots.append("Rodar port scan nos IPs dos subdomínios sensíveis (dev/vpn/git), não só no domínio principal.")

    # ── Portas ─────────────────────────────────────────────────────
    ps = D("portscan")
    if ps:
        open_ports = [p for p in ps["ports"] if p["status"] == "open"]
        for p in open_ports:
            if p["number"] in RISKY_PORTS:
                lvl, why = RISKY_PORTS[p["number"]]
                A.risks.append(Finding(lvl, f"Porta {p['number']}/{p['service']} aberta", why))
        if len(open_ports) > 4:
            A.risks.append(Finding("médio", "Superfície de rede ampla", f"{len(open_ports)} portas abertas entre as comuns verificadas."))
        elif open_ports and all(p["number"] in (80, 443) for p in open_ports):
            A.risks.append(Finding("info", "Superfície mínima", "Apenas 80/443 abertas entre as portas comuns."))
        if behind_cdn_now and open_ports:
            A.risks.append(Finding("info", "Resultado reflete o edge da CDN", "Portas abertas são do proxy, não necessariamente da origem."))

    # ── DNSSEC ─────────────────────────────────────────────────────
    ds = D("dnssec")
    if ds:
        v = ds["verdict"]
        if v == "unsigned":
            A.risks.append(Finding("baixo", "Sem DNSSEC", "Zona não assinada: sem proteção contra spoofing/cache poisoning de DNS."))
        elif v in ("broken_chain", "validation_fail"):
            A.risks.append(Finding("médio", "DNSSEC inconsistente", ds["label"]))
        else:
            A.risks.append(Finding("info", "DNSSEC válido", ds["label"]))

    A.risks.sort(key=lambda f: SEV_ORDER.get(f.level, 9))
    A.clues.sort(key=lambda f: SEV_ORDER.get(f.level, 9))
    A.pivots.append("Co-hospedagem e nameserver em comum são indícios, não prova de propriedade: confirme com outras fontes.")
    return A


# ══════════════════════════════════════════════════════════════════════════════
#  Renderização
# ══════════════════════════════════════════════════════════════════════════════
def tbl(*cols: str, caption: str | None = None) -> Table:
    t = Table(box=box.SIMPLE_HEAVY, header_style="bold", pad_edge=False, expand=True, caption=caption, caption_style="dim")
    for c in cols:
        t.add_column(c, overflow="fold")
    return t


def box_panel(key: str, body: Any, subtitle: str = "", style: str = "cyan") -> Panel:
    return Panel(body, title=f"[bold]{NUMS[key]} {TITLES[key]}[/]", subtitle=subtitle or None,
                 border_style=style, box=box.ROUNDED, padding=(0, 1))


def cap(items: list, n: int) -> tuple[list, str | None]:
    extra = len(items) - n
    return items[:n], (f"+{extra} omitido(s) — use --max-rows" if extra > 0 else None)


def render_module(res: ModuleResult, ctx: Ctx, n: int) -> Panel:
    k, d = res.key, res.data
    if res.status != "ok":
        icon, style = ("⏭", "yellow") if res.status == "skip" else ("✖", "red")
        return box_panel(k, Text(f"{icon} {res.message}", style=style), style=style)

    if k == "reverseip":
        rows, caption = cap(d["domains"], n)
        t = tbl("#", "Domínio", "Última resolução", caption=caption)
        for i, x in enumerate(rows, 1):
            t.add_row(str(i), e(x["name"]), e(x["last_resolved"]))
        tld = Counter(x["name"].rsplit(".", 1)[-1] for x in d["domains"] if x.get("name") and "." in x["name"])
        top = "  ".join(f"[cyan].{k2}[/] ×{v}" for k2, v in tld.most_common(5)) or "-"
        body = Group(Text.from_markup(f"[bold]{d['count']}[/] domínio(s) em [bold]{e(d['host'])}[/]   ·   TLDs: {top}"), t)
        return box_panel(k, body, style="cyan")

    if k == "reversewhois":
        rows, caption = cap(d["matches"], n)
        t = tbl("Domínio", "Criado em", "Registrar", caption=caption)
        for m in rows:
            t.add_row(e(m["domain"]), e(m["created"]), e(m["registrar"]))
        head = Text.from_markup(f"[bold]{d['count']}[/] domínio(s) para q=[bold]{e(d['query'])}[/]")
        return box_panel(k, Group(head, t) if d["matches"] else Group(head, Text("Sem resultados (WHOIS possivelmente protegido).", style="dim")), style="magenta")

    if k == "iphistory":
        t1 = tbl("Provedor (dono)", "IPs", "Primeiro registro", "Último registro")
        for o in d["owners"]:
            tag = " [yellow]CDN[/]" if is_cdn(o["owner"]) else ""
            t1.add_row(e(o["owner"]) + tag, str(o["ips"]), e(o["first"]), e(o["last"]))
        rows, caption = cap(d["ips"], n)
        t2 = tbl("IP", "Local", "Dono", "Visto de → até", "Obs.", caption=caption)
        for x in rows:
            t2.add_row(e(x["ip"]), e(x["location"]), e(x["owner"]), f"{e(x['first'])} → {e(x['last'])}", str(x["hits"]))
        head = Text.from_markup(f"[bold]{d['total_records']}[/] registro(s) · [bold]{len(d['ips'])}[/] IP(s) únicos")
        return box_panel(k, Group(head, Text("Linha do tempo por provedor", style="bold dim"), t1, Text("IPs", style="bold dim"), t2), style="green")

    if k == "subdomains":
        cats = categorize_subdomains(ctx, d["subdomains"])
        tag_of: dict = defaultdict(list)
        for cat, names in cats.items():
            for nme in names:
                tag_of[nme].append(cat)
        items = sorted(d["subdomains"], key=lambda s: (not tag_of.get((s["name"] or "").lower()), s["name"] or ""))
        rows, caption = cap(items, n)
        t = tbl("Subdomínio", "IPs", "Marcação", caption=caption)
        for s in rows:
            tags = ", ".join(tag_of.get((s["name"] or "").lower(), []))
            t.add_row(e(s["name"]), e(", ".join(s["ips"])) if s["ips"] else "[dim]sem IP[/]", f"[yellow]{e(tags)}[/]" if tags else "")
        return box_panel(k, Group(Text.from_markup(f"[bold]{d['count']}[/] subdomínio(s) conhecidos"), t), style="blue")

    if k == "reversens":
        t = tbl("Nameserver", "Domínios", "Observação")
        for x in d["by_ns"]:
            t.add_row(e(x["ns"]), "-" if x["count"] is None else str(x["count"]), e(x["note"]))
        parts: list = [t]
        best = min((x for x in d["by_ns"] if x["count"]), key=lambda x: x["count"], default=None)
        if best:
            rows, caption = cap(best["domains"], n)
            t2 = tbl("Domínios em " + best["ns"], caption=caption)
            for dom in rows:
                t2.add_row(e(dom))
            parts.append(t2)
        return box_panel(k, Group(*parts), style="yellow")

    if k == "portscan":
        t = tbl("Porta", "Serviço", "Status", "Nota")
        for p in d["ports"]:
            is_open = p["status"] == "open"
            note = ""
            if is_open and p["number"] in RISKY_PORTS:
                lvl, why = RISKY_PORTS[p["number"]]
                note = f"[{SEV_STYLE[lvl]}]{why}[/]"
            t.add_row(str(p["number"]), e(p["service"]),
                      "[bold red]● aberta[/]" if is_open and p["number"] in RISKY_PORTS and RISKY_PORTS[p["number"]][0] == "alto"
                      else "[bold yellow]● aberta[/]" if is_open else "[dim]○ fechada[/]", note)
        n_open = sum(1 for p in d["ports"] if p["status"] == "open")
        return box_panel(k, Group(Text.from_markup(f"[bold]{n_open}[/] aberta(s) em [bold]{e(d['host'])}[/] (portas comuns)"), t), style="red")

    if k == "dnssec":
        style = {"signed_valid": "green", "unsigned": "yellow"}.get(d["verdict"], "red")
        t = Table.grid(padding=(0, 2))
        t.add_row("[bold]Domínio[/]", e(d["domain"]))
        t.add_row("[bold]Veredito[/]", f"[{style}]{e(d['label'])}[/]")
        t.add_row("[bold]Registros DS (no pai)[/]", str(d["ds"]))
        t.add_row("[bold]Registros DNSKEY[/]", str(d["dnskey"]))
        t.add_row("[bold]Validado pelo resolvedor (AD)[/]", "sim" if d["ad"] else "não")
        return box_panel(k, t, style=style)
    return box_panel(k, Text("sem renderizador"))


def render_status(R: dict, keys: list) -> Panel:
    t = tbl("", "Módulo", "Resultado", "Tempo")
    for k in keys:
        r = R[k]
        icon = {"ok": "[green]✔[/]", "skip": "[yellow]⏭[/]", "error": "[red]✖[/]"}[r.status]
        t.add_row(icon, f"{NUMS[k]} {TITLES[k]}", e(r.message), f"{r.seconds:.1f}s")
    return Panel(t, title="[bold]Coleta[/]", border_style="white", box=box.ROUNDED, padding=(0, 1))


def lvl_text(level: str) -> str:
    return f"[{SEV_STYLE.get(level, '')}]{level.upper()}[/]"


def render_analysis(ctx: Ctx, R: dict, A: Analysis, n: int) -> list:
    out: list = []

    # Mapa de correlação (árvore)
    tree = Tree(f"[bold cyan]{e(ctx.target)}[/]")
    hist = R.get("iphistory")
    if hist and hist.status == "ok" and hist.data["ips"]:
        br = tree.add("[bold]Hospedagem[/]")
        for x in hist.data["ips"][:3]:
            br.add(f"{e(x['ip'])}  [dim]{e(x['owner'])} · até {e(x['last'])}[/]")
    elif ctx.current_ips:
        br = tree.add("[bold]Hospedagem (DNS atual)[/]")
        for ip in ctx.current_ips[:3]:
            br.add(e(ip))
    if ctx.ns_list or ctx.ns_override:
        br = tree.add("[bold]Nameservers[/]")
        for ns in (ctx.ns_override or ctx.ns_list)[:4]:
            br.add(e(ns))
    strong = [r for r in A.linked if r["score"] >= 2]
    if strong:
        br = tree.add("[bold]Domínios correlacionados[/]")
        for r in strong[:6]:
            br.add(f"[green]{e(r['domain'])}[/]  [dim]{'+'.join(r['sources'])}[/]")
    sens = []
    if "subdomains" in R and R["subdomains"].status == "ok":
        for cat, names in categorize_subdomains(ctx, R["subdomains"].data["subdomains"]).items():
            if next(l for c, _, l, _ in SUB_CATS if c == cat) != "info":   # e-mail/API são só informativos
                sens += names
    if sens:
        br = tree.add("[bold]Subdomínios sensíveis[/]")
        for nme in sorted(set(sens))[:6]:
            br.add(f"[yellow]{e(nme)}[/]")
    out.append(Panel(tree, title="[bold]⑧ Mapa de correlação[/]", border_style="bright_cyan", box=box.ROUNDED, padding=(0, 1)))

    # Riscos
    if A.risks:
        t = tbl("Nível", "Achado", "Detalhe")
        for f in A.risks:
            t.add_row(lvl_text(f.level), e(f.title), e(f.detail))
        counts = Counter(f.level for f in A.risks)
        head = "  ".join(f"[{SEV_STYLE[k]}]{counts[k]} {k}[/]" for k in ("alto", "médio", "baixo", "info") if counts[k])
        out.append(Panel(Group(Text.from_markup(head), t), title="[bold]⑨ Exposição e riscos[/]", border_style="red", box=box.ROUNDED, padding=(0, 1)))

    # Pistas
    if A.clues:
        t = tbl("Confiança", "Pista", "Detalhe")
        for f in A.clues:
            t.add_row(lvl_text(f.level), e(f.title), e(f.detail))
        out.append(Panel(t, title="[bold]⑩ Pistas de correlação[/]", border_style="green", box=box.ROUNDED, padding=(0, 1)))

    # Domínios correlacionados
    if A.linked:
        rows, caption = cap(A.linked, n)
        t = tbl("Domínio", "IP", "NS", "WHOIS", "Fontes", "Observação", caption=caption)
        for r in rows:
            mark = lambda s: "[green]●[/]" if s in r["sources"] else "[dim]·[/]"
            obs = "[yellow]nome semelhante à marca[/]" if r["lookalike"] else ""
            t.add_row(e(r["domain"]), mark("IP"), mark("NS"), mark("WHOIS"), f"[bold]{r['score']}/3[/]", obs)
        out.append(Panel(t, title="[bold]⑪ Domínios correlacionados (interseção entre fontes)[/]", border_style="bright_green", box=box.ROUNDED, padding=(0, 1)))

    # Próximos passos
    steps = Text()
    for i, p in enumerate(A.pivots, 1):
        steps.append(f"{i}. {p}\n")
    out.append(Panel(steps, title="[bold]Próximos passos sugeridos[/]", border_style="white", box=box.ROUNDED, padding=(0, 1)))
    return out


def render_header(ctx: Ctx, keys: list, demo: bool) -> Panel:
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    t = Table.grid(padding=(0, 2))
    t.add_row("[bold]Alvo[/]", f"[bold cyan]{e(ctx.target)}[/]" + ("  [dim](IP)[/]" if ctx.is_ip else ""))
    if not ctx.is_ip and ctx.apex != ctx.target:
        t.add_row("[bold]Domínio base[/]", e(ctx.apex))
    if ctx.current_ips:
        t.add_row("[bold]IPs atuais (DNS)[/]", e(", ".join(ctx.current_ips)))
    if ctx.ns_list:
        t.add_row("[bold]Nameservers[/]", e(", ".join(ctx.ns_list)))
    t.add_row("[bold]Data[/]", now)
    t.add_row("[bold]Módulos[/]", " ".join(f"{NUMS[k]}" for k in keys))
    sub = "[bold yellow]MODO DEMO — dados fictícios (nenhuma chamada à API)[/]" if demo else None
    return Panel(t, title="[bold white on blue] VIEWDNS RECON [/]", subtitle=sub, border_style="blue", box=box.DOUBLE, padding=(1, 2))


# ══════════════════════════════════════════════════════════════════════════════
#  CLI
# ══════════════════════════════════════════════════════════════════════════════
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Coleta via ViewDNS API + correlação dos resultados.")
    p.add_argument("target", nargs="?", help="domínio ou IP (ex.: exemplo.com, 203.0.113.10)")
    p.add_argument("--demo", action="store_true", help="usa dados fictícios (não consome a API)")
    p.add_argument("--only", help="módulos separados por vírgula: " + ",".join(ORDER))
    p.add_argument("--whois-q", help="termo do reverse WHOIS (e-mail/nome); padrão = domínio")
    p.add_argument("--ns", action="append", help="nameserver para o reverse NS (repetível)")
    p.add_argument("--force-ns", action="store_true", help="consulta reverse NS mesmo em provedores compartilhados")
    p.add_argument("--max-rows", type=int, default=12, help="linhas por tabela (padrão 12)")
    p.add_argument("--workers", type=int, default=3, help="consultas em paralelo (padrão 3)")
    p.add_argument("--timeout", type=int, default=30, help="timeout por requisição, em segundos")
    p.add_argument("--json", metavar="ARQ", help="salva os dados brutos + análise em JSON")
    p.add_argument("--html", metavar="ARQ", help="salva o relatório visual em HTML")
    p.add_argument("--width", type=int, help="largura do terminal/relatório")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    console = Console(record=bool(args.html), width=args.width)

    if not args.demo and not args.target:
        console.print("[red]Informe um alvo (domínio ou IP) ou use --demo.[/]")
        return 2
    if not args.demo and not API_KEY:
        console.print(Panel("[bold]Chave da API não configurada.[/]\n\nAbra [cyan]viewdns_recon.py[/], localize o bloco "
                            "[bold]COLE SUA CHAVE DA API[/] no topo e cole a chave entre as aspas de [cyan]API_KEY = \"\"[/].\n"
                            "Ou defina a variável de ambiente [cyan]VIEWDNS_API_KEY[/].", border_style="red", title="Falta a chave"))
        return 2

    keys = [k for k in ORDER if not args.only or k in {s.strip() for s in args.only.split(",")}]
    if not keys:
        console.print("[red]Nenhum módulo válido em --only.[/]")
        return 2

    if args.demo:
        ctx, R = demo_context()
        keys = [k for k in keys if k in R]
    else:
        target = clean_target(args.target)
        ip_mode = is_ip(target)
        apex, ns_list = (target, []) if ip_mode else find_apex_and_ns(target)
        ctx = Ctx(api=ViewDNS(API_KEY, timeout=args.timeout), target=target, apex=apex, is_ip=ip_mode,
                  ns_list=ns_list, ns_override=[clean_target(x) for x in (args.ns or [])],
                  whois_q=args.whois_q, force_ns=args.force_ns,
                  current_ips=[target] if ip_mode else resolve_ips(target))
        run_keys = []
        pre: dict = {}
        for k in keys:
            if ip_mode and k not in IP_ONLY_MODULES and not (k == "reversewhois" and args.whois_q):
                pre[k] = ModuleResult(k, "skip", {}, "não se aplica a IP (precisa de um domínio)")
            else:
                run_keys.append(k)
        console.print(render_header(ctx, keys, demo=False))
        with console.status("[bold cyan]Consultando ViewDNS…[/]"):
            R = execute(ctx, run_keys, max(1, args.workers))
        R.update(pre)

    if args.demo:
        console.print(render_header(ctx, keys, demo=True))
    console.print(render_status(R, keys))
    for k in keys:
        console.print(render_module(R[k], ctx, args.max_rows))

    analysis = correlate(ctx, R)
    console.rule("[bold]ANÁLISE CORRELACIONADA[/]")
    for panel in render_analysis(ctx, R, analysis, args.max_rows):
        console.print(panel)

    if args.json:
        payload = {"target": ctx.target, "apex": ctx.apex, "generated_at": datetime.now().isoformat(timespec="seconds"),
                   "modules": {k: asdict(R[k]) for k in keys}, "analysis": asdict(analysis)}
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=2)
        console.print(f"[dim]JSON salvo em {escape(args.json)}[/]")
    if args.html:
        console.save_html(args.html)
        console.print(f"[dim]HTML salvo em {escape(args.html)}[/]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
