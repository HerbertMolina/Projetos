# ViewDNS Recon

Ferramenta de linha de comando que automatiza a coleta de informações de domínios e IPs no [ViewDNS.info](https://viewdns.info) e **correlaciona os resultados** num relatório único.

Em vez de abrir uma ferramenta do site por vez, você digita o alvo uma vez e recebe tudo organizado, com uma análise no final.

---

## Para que serve

Em uma investigação de domínio ou IP, é comum repetir sempre as mesmas consultas, uma por uma, copiando e colando o alvo em cada ferramenta e juntando os resultados na mão.

O ViewDNS Recon faz esse trabalho repetitivo:

1. Consulta 7 ferramentas de uma só vez.
2. Mostra cada resultado em um painel separado e fácil de ler.
3. Cruza os dados e aponta ligações entre eles, riscos e próximos passos.

**Ganho prático:** o que levava vários minutos de abas abertas e cópia de dados vira um único comando.

---

## O que ele consulta

| # | Módulo | O que mostra |
|---|--------|--------------|
| ① | Reverse IP Lookup | Outros domínios hospedados no mesmo IP |
| ② | Reverse WHOIS Lookup | Domínios ligados ao mesmo registrante (nome ou e-mail) |
| ③ | IP History | Histórico de IPs e provedores do domínio |
| ④ | Subdomain Discovery | Subdomínios conhecidos, com marcação dos mais sensíveis (dev, admin, vpn, git...) |
| ⑤ | Reverse NS Lookup | Domínios que usam o mesmo servidor de nomes |
| ⑥ | Port Scanner | Portas comuns abertas, com alerta para as de risco |
| ⑦ | DNSSEC Test | Se o domínio tem DNSSEC e se ele está válido |

> O DNSSEC não existe na API do ViewDNS. Essa checagem usa DNS-over-HTTPS (dns.google) e não gasta sua cota da API.

---

## A análise correlacionada

Depois das consultas, o programa cruza os dados e gera quatro blocos:

- **Mapa de correlação:** árvore com hospedagem, nameservers, domínios ligados e subdomínios sensíveis.
- **Exposição e riscos:** portas perigosas abertas (RDP, MySQL, SMB...), ambientes de teste expostos, ausência de DNSSEC. Cada item tem nível alto, médio, baixo ou informativo.
- **Pistas de correlação:** por exemplo, domínios criados no mesmo dia, nameserver pouco compartilhado, provável IP de origem por trás de uma CDN, nomes parecidos com a marca (possível phishing).
- **Domínios correlacionados:** tabela dos domínios que aparecem em mais de uma fonte (IP, NS, WHOIS). Quanto mais fontes, mais forte o indício.

No fim, o programa sugere **próximos passos** da investigação.

---

## Como usar

**1. Instalar** (Python 3.9 ou superior)

```bash
pip install -r requirements.txt
```

**2. Configurar a chave da API**

Abra o `viewdns_recon.py`, localize o bloco marcado no topo e cole a chave:

```python
API_KEY = "sua-chave-aqui"
```

Ou, se preferir não escrever a chave no código, use uma variável de ambiente:

```bash
export VIEWDNS_API_KEY="sua-chave-aqui"     # Linux/Mac
setx VIEWDNS_API_KEY "sua-chave-aqui"       # Windows
```

**3. Rodar**

```bash
python viewdns_recon.py exemplo.com
```

### Exemplos

```bash
# Investigação completa
python viewdns_recon.py exemplo.com

# Alvo é um IP (roda só os módulos que fazem sentido para IP)
python viewdns_recon.py 203.0.113.10

# Só alguns módulos, para economizar cota da API
python viewdns_recon.py exemplo.com --only iphistory,subdomains,portscan

# Reverse WHOIS por e-mail do registrante
python viewdns_recon.py exemplo.com --whois-q contato@exemplo.com

# Salvar relatório visual (HTML) e dados brutos (JSON)
python viewdns_recon.py exemplo.com --html relatorio.html --json dados.json

# Ver como fica a saída sem usar a API (dados fictícios)
python viewdns_recon.py --demo
```

### Opções

| Opção | Função |
|-------|--------|
| `--demo` | Usa dados fictícios, sem chamar a API |
| `--only` | Roda só os módulos indicados |
| `--whois-q` | Termo do reverse WHOIS (e-mail ou nome) |
| `--ns` | Define o nameserver do reverse NS (pode repetir) |
| `--force-ns` | Consulta reverse NS mesmo em provedores gigantes |
| `--max-rows` | Linhas por tabela (padrão 12) |
| `--workers` | Consultas em paralelo (padrão 3) |
| `--timeout` | Tempo limite por consulta, em segundos |
| `--json` / `--html` | Salva o resultado em arquivo |

---

## Praticidade

- **Um comando só** para todas as consultas.
- **Consultas em paralelo**, com nova tentativa automática se a API falhar ou limitar.
- **Falha isolada:** se um módulo der erro, os outros continuam e o relatório sai mesmo assim.
- **Saída organizada** no terminal, com cores e tabelas, e exportável em HTML e JSON.
- **Modo demo** para testar e apresentar a ferramenta sem gastar a API.
- **Chave protegida:** a chave nunca aparece nas mensagens de erro.

---

## Cuidados e limitações

- **Indício não é prova.** Estar no mesmo IP ou usar o mesmo nameserver não prova que dois domínios têm o mesmo dono. A ferramenta mostra o grau de confiança de cada pista, mas a confirmação depende de outras fontes.
- **CDN muda o resultado.** Se o alvo está atrás de uma CDN (Cloudflare, Akamai...), o IP e as portas vistos são do proxy, não do servidor de origem. O programa avisa quando detecta isso.
- **Cota da API.** Cada execução completa faz 5 consultas na API do ViewDNS, mais uma por nameserver (o reverse NS consulta até 4). Consulte os limites do seu plano no site deles.
- **Provedores de DNS gigantes** (Cloudflare, AWS, GoDaddy...) têm milhões de domínios por nameserver, então o reverse NS é pulado por padrão, porque não ajuda a correlacionar.
- **Uso autorizado.** Use apenas em alvos que você tem permissão para investigar e respeite os [Termos de Serviço da API](https://viewdns.info/api/terms/).
- **Nunca publique sua chave.** Não suba o arquivo com a chave preenchida para um repositório público.

---

## Tecnologias

Python, `requests` (chamadas HTTP) e `rich` (saída formatada no terminal), mais threads para consultas em paralelo.

---

## Próximas ideias

- Testes automatizados com respostas simuladas da API.
- Novas fontes de dados (crt.sh, VirusTotal, Shodan) para enriquecer a correlação.
- Cache local dos resultados para economizar cota.
- Lista de alvos em arquivo, para investigar vários domínios em sequência.
