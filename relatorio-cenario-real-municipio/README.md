# 🔍 Mapeamento de Superfície de Ataque via OSINT Passivo

## 📊 Resumo Executivo

Investigação passiva em sistema de gestão municipal brasileiro, identificando **15 vulnerabilidades** utilizando exclusivamente fontes abertas e técnicas de OSINT.

**Tipo:** OSINT 100% Passivo (sem interação ativa com o alvo)  
**Data:** Julho 2026  
**Ferramentas:** Shodan, Censys, theHarvester, crt.sh, Wappalyzer, Hunter.io

---

## 🎯 Objetivos

- Mapear superfície de ataque exposta publicamente
- Identificar tecnologias e serviços em execução
- Detectar configurações inseguras e CVEs conhecidas
- Demonstrar capacidades de OSINT e reconhecimento passivo

---

## 🛠️ Metodologia

### Ferramentas Utilizadas

| Ferramenta | Uso |
|------------|-----|
| Shodan | Identificação de serviços e CVEs |
| Censys | Análise de certificados SSL/TLS |
| theHarvester | Subdomínios e emails |
| crt.sh | Mapeamento via certificados |
| Wappalyzer | Identificação de tecnologias |
| Hunter.io | Emails corporativos |

### Abordagem

1. **Reconhecimento Passivo** - Coleta via fontes públicas
2. **Análise de Superfície** - Mapeamento de serviços
3. **Identificação de Vulns** - Correlação com CVEs
4. **Análise de Risco** - Avaliação de impacto
5. **Documentação** - Relatório técnico

---

## 🎯 Principais Achados

### 🔴 Críticos (5)

1. **CVE-2026-44631 (RCE)** - Execução remota de código no sistema de gestão
2. **VMware vCenter exposto** - Risco de comprometimento total da virtualização
3. **Sistema de Protocolo com 214 CVEs** - Superfície massiva
4. **phpMyAdmin exposto** - Acesso público ao banco de dados
5. **cPanel sem restrições** - Painel administrativo exposto

### 🟠 Altos (5)

- GLPI (ITSM) exposto
- Ausência de headers de segurança HTTP
- Ausência de segmentação de rede
- Vazamento de 75 emails corporativos
- Centralização de serviços (SPOF)

### 🟡 Médios (3)

- Possível exposição de arquivo .env
- Ausência de DNSSEC
- Informações expostas via SOA

### 🟢 Baixos (2)

- Subdomínios órfãos
- Ausência de SPF/DKIM/DMARC

---

## 📈 Impacto Potencial

- Comprometimento total da infraestrutura virtualizada
- Exposição de dados de milhares de cidadãos
- Violação de LGPD
- Interrupção de serviços públicos essenciais
- Danos reputacionais e financeiros

---

## 📄 Relatório Completo

Este projeto possui dois formatos do relatório completo:

- **[📖 Ler em Markdown](./relatorio-completo.md)** - Versão navegável, ideal para leitura online
- **[📥 Download PDF](./relatorio-completo.pdf)** - Versão formatada, ideal para impressão e compartilhamento

---

## 💡 Lições Aprendidas

1. **OSINT é subutilizado na defesa** - Se eu achei passivamente, atacante também acha
2. **Configurações padrão são o maior inimigo** - Hardening pós-instalação é essencial
3. **Sistemas municipais são alvos frequentes** - Mas muitas vezes negligenciados
4. **Infraestrutura híbrida requer governança** - Múltiplos provedores = mais superfície
5. **Ética é inegociável** - Sempre dentro dos limites legais

---

## ⚖️ Aviso Ético

Esta investigação foi conduzida utilizando **APENAS técnicas passivas**, sem qualquer interação direta, exploração ou acesso não autorizado aos sistemas. Todos os dados sensíveis foram anonimizados.

---

## 🏷️ Tags

`#OSINT` `#Reconhecimento` `#Vulnerabilidades` `#SetorPúblico` `#Shodan` `#Censys` `#EthicalHacking` `#SecurityResearch`
