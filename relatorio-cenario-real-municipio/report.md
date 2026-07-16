# RELATÓRIO DE INVESTIGAÇÃO  
## Mapeamento de Superfície de Ataque via OSINT Passivo em Sistema de Gestão Pública Municipal

---  

**Autor:** Herbert Molina   
**Data:** 02 de Julho de 2026  
**Classificação:** Público (Dados Anonimizados)  
**Versão:** 1.0 - Final  
**Tipo de Investigação:** OSINT 100% Passivo (sem interação ativa com o alvo)  

---  

## ⚖️ AVISO ÉTICO E LEGAL  

Este relatório foi elaborado **exclusivamente para fins educacionais** e demonstração de habilidades em segurança da informação e inteligência de fontes abertas (OSINT).  

A investigação foi conduzida utilizando **APENAS técnicas passivas**, sem qualquer interação direta, exploração, teste de intrusão ou acesso não autorizado aos sistemas investigados. Nenhuma ferramenta de varredura ativa (Nmap, Nessus, Nikto, etc.) foi utilizada contra o alvo.  

**Todos os dados sensíveis foram anonimizados** para proteger a identidade do alvo. Qualquer semelhança com sistemas reais é coincidência.  

Este material **não deve ser utilizado** para atividades ilegais ou não autorizadas. O autor não se responsabiliza pelo uso indevido das informações aqui contidas.  

> **Para profissionais de segurança:** Sempre obtenha autorização por escrito (Regras de Engajamento) antes de realizar testes de intrusão em sistemas de terceiros. No Brasil, o acesso não autorizado a sistemas informáticos é tipificado como crime pela Lei 12.737/2012 (Art. 154-A do Código Penal).  

---

## 📊 SUMÁRIO EXECUTIVO

### Contexto

Foi realizada uma investigação de segurança passiva em um sistema de gestão municipal brasileiro, com o objetivo de mapear a superfície de ataque exposta publicamente na internet e identificar vulnerabilidades potenciais utilizando exclusivamente fontes abertas e técnicas de OSINT.

### Escopo da Investigação

- Domínio principal e todos os subdomínios públicos
- Registros DNS (A, AAAA, MX, TXT, NS, SOA, CNAME)
- Serviços expostos na internet (HTTP/HTTPS, SMTP, DNS)
- Painéis administrativos publicamente acessíveis
- Informações disponíveis em bases públicas (WHOIS/RDAP, crt.sh, Shodan, Censys)
- Tecnologias identificadas via análise de cabeçalhos HTTP e Wappalyzer
- Configurações de segurança HTTP e email (SPF/DKIM/DMARC)
- Vazamento de credenciais em bases públicas

### Metodologia

A investigação utilizou abordagem **100% passiva**, empregando ferramentas de inteligência de fontes abertas para coleta de informações sobre infraestrutura, serviços expostos, configurações de DNS e painéis administrativos. **Nenhuma interação ativa ou exploração foi realizada contra os sistemas.**

### Principais Achados

A investigação identificou **120, porém aqui serão apresentadas as principais - 15 vulnerabilidades** distribuídas em diferentes níveis de severidade:

| Severidade | Quantidade | Descrição |
|---|---|---|
| 🔴 Crítico | 5 | RCE em sistema de terceiros, vCenter exposto, múltiplos painéis administrativos expostos |
| 🟠 Alto | 5 | GLPI exposto, ausência de segmentação, ausência de headers de segurança |
| 🟡 Médio | 3 | Ausência de DNSSEC, informações expostas via SOA, possível exposição de .env |
| 🟢 Baixo | 2 | Subdomínios órfãos, vazamento de emails corporativos |

### Impacto Potencial

As vulnerabilidades identificadas, se exploradas, poderiam resultar em:

- Comprometimento total da infraestrutura virtualizada (via vCenter)
- Exposição de dados sensíveis de milhares de cidadãos e empresas
- Violação da Lei Geral de Proteção de Dados (LGPD)
- Interrupção de serviços públicos essenciais
- Acesso a processos administrativos, licitações e contratos
- Danos reputacionais e financeiros significativos ao município

### Nível de Risco Geral

**🔴 CRÍTICO** — Múltiplas vulnerabilidades críticas identificadas, com potencial de comprometimento total do sistema e exposição massiva de dados sensíveis. Ação imediata recomendada.

---

## 🎯 1. OBJETIVOS E ESCOPO

### 1.1 Objetivos da Investigação

- Mapear a superfície de ataque exposta publicamente
- Identificar tecnologias e serviços em execução
- Detectar configurações inseguras e vulnerabilidades conhecidas
- Avaliar a postura de segurança da infraestrutura
- Demonstrar capacidades de OSINT e reconhecimento passivo
- Correlacionar descobertas para identificar padrões de risco

### 1.2 Escopo da Investigação

**Incluído:**

- Domínio principal e todos os subdomínios públicos
- Registros DNS (A, AAAA, MX, TXT, NS, SOA, CNAME)
- Serviços expostos na internet (HTTP/HTTPS, SMTP, DNS)
- Painéis administrativos publicamente acessíveis
- Informações disponíveis em bases públicas (WHOIS/RDAP, crt.sh, Shodan, Censys)
- Tecnologias identificadas via análise de cabeçalhos HTTP e Wappalyzer
- Configurações de segurança HTTP e email (SPF/DKIM/DMARC)
- Vazamento de credenciais em bases públicas (Hunter.io)

**Excluído:**

- Testes de intrusão ativos
- Exploração de vulnerabilidades
- Acesso não autorizado a sistemas
- Engenharia social
- Varredura ativa de portas ou serviços
- Qualquer atividade que viole a confidencialidade, integridade ou disponibilidade dos sistemas

### 1.3 Restrições Éticas

- Investigação 100% passiva (sem envio de pacotes maliciosos)
- Nenhuma tentativa de autenticação ou acesso
- Nenhum teste de vulnerabilidade ativo
- Respeito aos termos de uso de todas as ferramentas utilizadas
- Anonimização completa de dados sensíveis

---

## 🛠️ 2. METODOLOGIA

### 2.1 Abordagem

A investigação seguiu o framework **PTES (Penetration Testing Execution Standard)** adaptado para OSINT passivo, com foco nas fases de:

1. **Reconhecimento Passivo:** Coleta de informações sem interação direta
2. **Análise de Superfície de Ataque:** Mapeamento de serviços expostos
3. **Identificação de Vulnerabilidades:** Correlação com bases de CVEs
4. **Análise de Risco:** Avaliação de impacto e probabilidade
5. **Documentação:** Elaboração de relatório técnico

### 2.2 Ferramentas Utilizadas

| Ferramenta | Categoria | Uso Específico |
|---|---|---|
| **Shodan** | Busca de Dispositivos | Identificação de serviços expostos, versões, CVEs |
| **Censys** | Análise de Certificados | Histórico de certificados SSL/TLS, configurações criptográficas |
| **RDAP/WHOIS** | Registro de Domínios | Informações de registrante, nameservers, datas |
| **theHarvester** | Coleta de OSINT | Subdomínios, emails, nomes em fontes públicas |
| **crt.sh** | Certificados SSL | Mapeamento de subdomínios via certificados |
| **DNSDumpster** | Análise de DNS | Visualização de infraestrutura DNS |
| **Wappalyzer** | Identificação de Tecnologias | Detecção de frameworks, CMS, servidores |
| **SecurityTrails** | DNS Passivo | Histórico de registros DNS |
| **Hunter.io** | OSINT de Emails | Descoberta de emails corporativos |
| **VirusTotal** | Análise de Relações | Domínios relacionados, IPs, URLs |
| **curl** | Análise de Headers | Verificação de headers de segurança HTTP |
| **dig/nslookup** | Consultas DNS | Verificação de registros específicos |

### 2.3 Fontes de Inteligência

**Fontes Primárias:**

- Servidores DNS públicos (8.8.8.8, 1.1.1.1)
- Bases de dados de certificados SSL (Let's Encrypt, crt.sh)
- Motores de busca especializados (Shodan, Censys, FOFA)
- Registros de domínio (Registro.br, RDAP)

**Fontes Secundárias:**

- Bases de dados de vulnerabilidades (NVD, CVE Details)
- Fóruns e repositórios públicos (GitHub, Exploit-DB)
- Redes sociais profissionais (LinkedIn)
- Wayback Machine (arquivos históricos)
- Bases de vazamento de credenciais (Hunter.io)

### 2.4 Processo de Anonimização

Para proteger a identidade do alvo, todos os dados sensíveis foram substituídos por valores genéricos:

| Dado Original | Substituição |
|---|---|
| Nome do domínio real | `municipio.gov.br` |
| Endereços IP reais | `XX.XX.XX.XX` |
| Nome do vendor | `Sistema de Gestão Municipal (Vendor X)` |
| Nome do provedor | `Provedor de Hospedagem` |
| Nomes de cidades | `Município de Médio Porte` |
| Nomes de pessoas | `[REDACTED]` |
| Emails reais | `usuario@municipio.gov.br` (genérico) |

---

## 🏗️ 3. MAPEAMENTO DE INFRAESTRUTURA

### 3.1 Informações de Registro (RDAP/WHOIS)

**Domínio:** municipio.gov.br  
**Status:** Publicado  
**Registrante:** [REDACTED]  
**Nameservers:**

- ns1.municipio.gov.br
- ns2.municipio.gov.br
- ns3.municipio.gov.br

**Observação:** Os nameservers utilizam o mesmo domínio principal (Glue Record), indicando que estão hospedados na mesma infraestrutura do site principal.

### 3.2 Arquitetura de Rede Identificada

```
┌─────────────────────────────────────────────────────────────┐
│                    INTERNET PÚBLICA                          │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
┌──────────────┐         ┌──────────────────┐
│  Cloudflare  │         │  AWS (IIS)       │
│  (CDN/WAF)   │         │  Windows Server  │
└──────┬───────┘         └────────┬─────────┘
       │                          │
       ▼                          ▼
┌─────────────────────────────────────────────────────────┐
│              SERVIDORES PRINCIPAIS                      │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │   Apache    │  │   GLPI      │  │  vCenter    │      │
│  │   PHP 8     │  │   (ITSM)    │  │  (VMware)   │      │
│  │   Conam     │  │   ti.mun... │  │  vcenter... │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │  Protocolo  │  │             │  │Transparência│      │
│  │  29+28 CRIT │  │  (Processos)│  │ login.html  │      │
│  │  75+75 MED  │  │             │  │             │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │   cPanel    │  │  phpMyAdmin │  │   Webmail   │      │
│  │  (EXPOSTO)  │  │  (EXPOSTO)  │  │  (EXPOSTO)  │      │ 
│  └─────────────┘  └─────────────┘  └─────────────┘      │
│                                                         │
│  ┌─────────────────────────────────────────────────┐    │
│  │  Banco de Dados (MySQL/MariaDB)                 │    │
│  │  + Arquivo .env (POSSIVELMENTE EXISTENTE)       │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

### 3.3 Subdomínios Identificados

| Subdomínio | Função | Status | Risco |
|---|---|---|---|
| `www.municipio.gov.br` | Site principal | Ativo | Médio |
| `municipio.gov.br` | Redireciona para www | Ativo | Baixo |
| `ns1.municipio.gov.br` | Nameserver primário | Ativo | Alto |
| `ns2.municipio.gov.br` | Nameserver secundário | Ativo | Alto |
| `ns3.municipio.gov.br` | Nameserver secundário | Ativo | Alto |
| `mail.municipio.gov.br` | Servidor de email | Redireciona | Médio |
| `webmail.municipio.gov.br` | Interface web de email | Ativo (login) | Alto |
| `cpanel.municipio.gov.br` | Painel de hospedagem | Ativo (login) | Crítico |
| `phpmyadmin.municipio.gov.br` | Administração de banco | Ativo (login) | Crítico |
| `ti.municipio.gov.br` | GLPI (ITSM) | Ativo (login) | Alto |
| `vcenter.municipio.gov.br` | VMware vCenter | Ativo (login) | Crítico |
| `transparencia.municipio.gov.br` | Portal da Transparência | Ativo (login.html) | Alto |
| `protocolo.municipio.gov.br` | Sistema de Protocolo | Ativo | Crítico |
**Total:** 15 subdomínios identificados

### 3.4 Tecnologias Identificadas

**Via Análise de Cabeçalhos HTTP e Wappalyzer:**

| Componente | Tecnologia | Versão | Status |
|---|---|---|---|
| Servidor Web Principal | Apache | 2.4.x | Desatualizado |
| Linguagem | PHP | 8.x | Atualizado |
| Sistema de Gestão | Vendor X (Conam) | [REDACTED] | Desatualizado (CVE crítico) |
| Banco de Dados | MySQL/MariaDB | [REDACTED] | Não identificada |
| Painel de Controle | cPanel | [REDACTED] | Não identificada |
| Sistema de ITSM | GLPI | [REDACTED] | A verificar |
| Virtualização | VMware vCenter | [REDACTED] | Crítico (CVEs conhecidas) |
| Processos Eletrônicos | SEI | [REDACTED] | A verificar |
| Servidor Secundário | Microsoft IIS | [REDACTED] | Em AWS |
| CDN/Proxy | Cloudflare | - | Ativo |
| Certificado SSL | Let's Encrypt | - | Válido |

### 3.5 Infraestrutura Híbrida Identificada

A investigação revelou uma infraestrutura **híbrida** distribuída entre:

1. **Hospedagem Tradicional (Linux/Apache):** Sistema principal Conam, cPanel, banco de dados
2. **AWS (Windows/IIS):** Portal da Transparência e possivelmente outros serviços
3. **Cloudflare:** CDN/WAF para o site principal

Esta distribuição indica:

- Múltiplos provedores e tecnologias (aumenta a superfície de ataque)
- Possível falta de padronização e governança
- Diferentes níveis de maturidade em segurança entre os ambientes

---

## ⚠️ 4. VULNERABILIDADES IDENTIFICADAS

### 4.1 [CRÍTICO] CVE-2026-44631 - Execução Remota de Código (RCE)

**Classificação:** 🔴 CRÍTICO  
**CVSS Score:** 9.8 (Crítico)  
**Vetor de Ataque:** Network / Low Complexity / No Authentication  
**CWE:** CWE-94 (Code Injection)  
**Sistema Afetado:** Sistema de Gestão Municipal (Vendor X/Conam)

**Descrição:**

O sistema de gestão municipal identificado está rodando uma versão desatualizada que possui uma vulnerabilidade de Execução Remota de Código catalogada como CVE-2026-44631. Esta falha permite que um atacante remoto execute comandos arbitrários no servidor sem necessidade de autenticação.

**Metodologia de Descoberta:**

Identificado via Shodan ao correlacionar a versão do software (obtida via análise de cabeçalhos HTTP) com a base de dados do NVD (National Vulnerability Database). A busca foi realizada utilizando o filtro `hostname:"municipio.gov.br"` e cruzamento com a CVE específica.

**Evidência:**

```
Shodan Query: hostname:"municipio.gov.br"
Result: Versão identificada via cabeçalhos HTTP
CVE Correlacionado: CVE-2026-44631
CVSS: 9.8 (Critical)
Vetor: Network/Low Complexity/No Authentication
```

**Impacto:**

- Execução arbitrária de código com privilégios do usuário do servidor web (www-data)
- Possibilidade de escalação de privilégios para root
- Acesso completo ao sistema de arquivos
- Comprometimento de todos os dados armazenados
- Possibilidade de movimentação lateral para outros sistemas na mesma rede
- Instalação de backdoors e persistência

**Recomendações:**

**Imediato:**
- Atualizar o sistema de gestão para a versão mais recente
- Aplicar todos os patches de segurança disponíveis
- Isolar o sistema da internet até a atualização ser concluída

**Curto Prazo:**
- Implementar WAF (Web Application Firewall) para filtrar requisições maliciosas
- Habilitar logs detalhados e monitoramento de atividades suspeitas
- Realizar auditoria completa do sistema em busca de backdoors

**Longo Prazo:**
- Estabelecer processo de gestão de vulnerabilidades
- Assinar contratos de manutenção com o vendor do sistema
- Implementar testes de penetração periódicos

**Referências:**
- NVD: https://nvd.nist.gov/vuln/detail/CVE-2026-44631
- MITRE ATT&CK: T1190 (Exploit Public-Facing Application)

---

### 4.2 [CRÍTICO] VMware vCenter Exposto na Internet

**Classificação:** 🔴 CRÍTICO  
**CVSS Score:** 9.8 (Crítico)  
**Vetor de Ataque:** Network / Low Complexity / Requires Authentication  
**CWE:** CWE-306 (Missing Authentication for Critical Function)  
**Sistema Afetado:** VMware vCenter (`vcenter.municipio.gov.br`)

**Descrição:**

O painel de gerenciamento VMware vCenter está acessível publicamente na internet através do subdomínio `vcenter.municipio.gov.br`. O vCenter é o sistema central de gerenciamento de toda a infraestrutura de virtualização da organização, controlando todas as máquinas virtuais do ambiente.

**Metodologia de Descoberta:**

Identificado durante o mapeamento de subdomínios via crt.sh e theHarvester. A confirmação do serviço foi realizada via Shodan e Censys, que identificaram a tecnologia VMware vCenter rodando no subdomínio.

**Evidência:**

```
Subdomínio: vcenter.municipio.gov.br
Status: HTTP 200 OK
Título: VMware vCenter - Login
Tecnologia: VMware vCenter
Portas: 443 (HTTPS)
Autenticação: Solicita usuário/senha
```

**Impacto:**

- **Comprometimento total da infraestrutura virtualizada**
- Acesso a todas as máquinas virtuais do ambiente
- Extração de snapshots, discos virtuais e credenciais
- Possibilidade de desligar ou modificar qualquer VM
- Acesso a dados sensíveis de todos os sistemas virtualizados
- Movimento lateral para qualquer sistema conectado

**Contexto de Risco:**

VMware vCenter teve **CVEs gravíssimas nos últimos anos**, incluindo:
- CVE-2023-20867 (Critical - Heap Overflow)
- CVE-2023-34048 (Critical - Authentication Bypass)
- CVE-2021-21985 (Critical - RCE)

**Recomendações:**

**Imediato:**
- **REMOVER O vCenter DA INTERNET IMEDIATAMENTE**
- Restringir acesso apenas à rede interna administrativa
- Implementar VPN obrigatória para acesso remoto

**Curto Prazo:**
- Verificar e atualizar a versão do vCenter
- Implementar MFA obrigatório
- Habilitar logs detalhados de acesso

**Longo Prazo:**
- Implementar segmentação de rede rigorosa
- Realizar auditoria regular de todas as VMs
- Estabelecer políticas de backup e recuperação

**Referências:**
- VMware Security Advisories: https://www.vmware.com/security/advisories
- CISA Alert: https://www.cisa.gov/news-events/cybersecurity-advisories

---

### 4.3 [CRÍTICO] Sistema de Protocolo com Múltiplas Vulnerabilidades Críticas

**Classificação:** 🔴 CRÍTICO  
**CVSS Score:** 9.1 (Crítico - múltiplas CVEs)  
**Vetor de Ataque:** Network / Low Complexity  
**Sistema Afetado:** Sistema de Protocolo (`protocolo.municipio.gov.br`)

**Descrição:**

O sistema de protocolo municipal apresenta **29 vulnerabilidades críticas na porta 80** e **28 vulnerabilidades críticas na porta 443**, além de **75 vulnerabilidades médias em cada porta**, totalizando **214 vulnerabilidades** identificadas pelo Shodan neste único subdomínio.

**Metodologia de Descoberta:**

Identificado via Shodan ao buscar pelo hostname principal e correlacionar com subdomínios relacionados. O Shodan realizou a correlação automática das versões de software identificadas com sua base de dados de CVEs.

**Evidência:**

```
Shodan Query: hostname:"protocolo.municipio.gov.br"
Result:
- Porta 80: 29 vulnerabilidades críticas + 75 médias
- Porta 443: 28 vulnerabilidades críticas + 75 médias
- Total: 214 vulnerabilidades identificadas
- ISP: [Provedor de Internet identificado]
```

**Impacto:**

- Superfície de ataque extremamente ampla
- Múltiplos vetores de comprometimento disponíveis
- Alta probabilidade de exploração bem-sucedida
- Sistema de protocolo é crítico para operações municipais
- Dados de documentos oficiais podem ser comprometidos

**Recomendações:**

**Imediato:**
- Realizar inventário completo de todas as vulnerabilidades identificadas
- Priorizar correção das 57 vulnerabilidades críticas
- Considerar isolamento do sistema até correção

**Curto Prazo:**
- Atualizar todos os componentes do sistema
- Implementar WAF para proteção adicional
- Habilitar monitoramento contínuo

**Longo Prazo:**
- Estabelecer programa de gestão de vulnerabilidades
- Realizar pentests periódicos
- Implementar processo de patch management

---

### 4.4 [CRÍTICO] Painel de Administração de Banco de Dados Exposto

**Classificação:** 🔴 CRÍTICO  
**CVSS Score:** 9.1 (Crítico)  
**Vetor de Ataque:** Network / Low Complexity / Requires Authentication  
**CWE:** CWE-200 (Exposure of Sensitive Information)  
**Sistema Afetado:** phpMyAdmin (`phpmyadmin.municipio.gov.br`)

**Descrição:**

O painel phpMyAdmin (interface web para administração de bancos de dados MySQL/MariaDB) está acessível publicamente na internet. Esta configuração permite que qualquer pessoa na internet tente autenticar-se no banco de dados.

**Metodologia de Descoberta:**

Identificado durante o mapeamento de subdomínios via crt.sh e confirmado via Shodan. O painel foi detectado pelo título da página e pela assinatura característica do phpMyAdmin nos cabeçalhos HTTP.

**Evidência:**

```
URL: https://phpmyadmin.municipio.gov.br
Status: HTTP 200 OK
Título: phpMyAdmin
Versão: Identificada no rodapé
Autenticação: Solicita usuário/senha
Protocolo: HTTPS (válido)
```

**Impacto:**

- Tentativas de brute force contra credenciais do banco de dados
- Se credenciais forem fracas ou padrão, acesso direto aos dados
- Exportação completa do banco de dados (dados de cidadãos, empresas, notas fiscais)
- Modificação ou deleção de dados críticos
- Criação de novos usuários com privilégios administrativos
- Violação massiva da LGPD

**Recomendações:**

**Imediato:**
- Remover o phpMyAdmin do acesso público imediatamente
- Restringir acesso apenas à rede interna (localhost ou IPs específicos)
- Alterar todas as senhas do banco de dados

**Curto Prazo:**
- Implementar VPN para acesso remoto ao banco de dados
- Habilitar autenticação de dois fatores
- Configurar firewall para bloquear acesso externo à porta 3306

**Referências:**
- OWASP: A01:2021 – Broken Access Control
- CIS Benchmark: MySQL Database

---

### 4.5 [CRÍTICO] cPanel Exposto sem Restrições

**Classificação:** 🔴 CRÍTICO  
**CVSS Score:** 9.0 (Crítico)  
**Vetor de Ataque:** Network / Low Complexity / Requires Authentication  
**CWE:** CWE-306 (Missing Authentication for Critical Function)  
**Sistema Afetado:** cPanel (`cpanel.municipio.gov.br`)

**Descrição:**

O painel de controle cPanel (interface administrativa da hospedagem) está acessível publicamente na internet sem restrições de IP ou autenticação de dois fatores. O cPanel fornece controle total sobre a hospedagem, incluindo arquivos, bancos de dados, emails, DNS e backups.

**Metodologia de Descoberta:**

Identificado durante o mapeamento de subdomínios via crt.sh e theHarvester. A confirmação do serviço foi realizada via Shodan, que identificou as portas características do cPanel (2082, 2083, 2086, 2087) abertas e acessíveis.

**Evidência:**

```
URL: https://cpanel.municipio.gov.br:2083
Status: HTTP 200 OK
Título: cPanel - Login
Portas: 2082 (HTTP), 2083 (HTTPS), 2086 (WHM HTTP), 2087 (WHM HTTPS)
Autenticação: Solicita usuário/senha
MFA: Não identificado
Restrição de IP: Não identificada
```

**Impacto:**

- Controle total da hospedagem se credenciais forem comprometidas
- Acesso a todos os arquivos do site e sistema
- Acesso ao phpMyAdmin e bancos de dados
- Gerenciamento de contas de email (leitura, envio, criação)
- Alteração de registros DNS (redirecionamento de tráfego)
- Download de backups completos (dados históricos)
- Criação de contas FTP/SSH para persistência
- Instalação de webshells e backdoors

**Recomendações:**

**Imediato:**
- Restringir acesso ao cPanel por IP (apenas IPs da prefeitura)
- Habilitar MFA obrigatório para todas as contas
- Alterar todas as senhas do cPanel e contas associadas

**Curto Prazo:**
- Alterar a URL padrão do cPanel para algo não óbvio
- Desabilitar acesso SSH/FTP se não for necessário
- Implementar monitoramento de tentativas de login

**Referências:**
- cPanel Security Advisor: https://docs.cpanel.net/
- OWASP: A07:2021 – Identification and Authentication Failures

---

### 4.6 [ALTO] GLPI (Sistema de ITSM) Exposto

**Classificação:** 🟠 ALTO  
**CVSS Score:** 8.1 (Alto)  
**Vetor de Ataque:** Network / Low Complexity / Requires Authentication  
**Sistema Afetado:** GLPI (`ti.municipio.gov.br`)

**Descrição:**

O sistema GLPI (Gestionnaire Libre de Parc Informatique) está acessível publicamente na internet através do subdomínio `ti.municipio.gov.br`. O GLPI é um sistema de ITSM utilizado para gestão de chamados, inventário de TI e helpdesk.

**Metodologia de Descoberta:**

Identificado durante o mapeamento de subdomínios via crt.sh e confirmado via Shodan, que identificou a assinatura característica do GLPI nos cabeçalhos HTTP e no título da página.

**Evidência:**

```
Subdomínio: ti.municipio.gov.br
Status: HTTP 200 OK
Título: GLPI - Login
Tecnologia: GLPI (ITSM)
Autenticação: Solicita usuário/senha
```

**Impacto:**

- GLPI possui histórico de CVEs críticas (SQL Injection, RCE, Auth Bypass)
- Guarda dados de todos os equipamentos de TI da prefeitura
- Contém credenciais de administradores e técnicos
- Pode ter integrações com Active Directory/LDAP
- Dados de inventário expostos (hardware, software, licenças)

**Contexto de Risco:**

GLPI teve múltiplas CVEs críticas nos últimos anos, incluindo:
- CVE-2023-39155 (SQL Injection)
- CVE-2022-25288 (RCE via plugin)
- CVE-2021-43778 (Auth Bypass)

**Recomendações:**

**Imediato:**
- Restringir acesso ao GLPI apenas à rede interna
- Verificar e atualizar a versão do GLPI
- Implementar MFA obrigatório

**Curto Prazo:**
- Implementar VPN para acesso remoto
- Revisar plugins instalados e remover os desnecessários
- Habilitar logs detalhados de acesso

**Referências:**
- GLPI Security Advisories: https://github.com/glpi-project/glpi/security

---

### 4.7 [ALTO] Ausência de Headers de Segurança HTTP

**Classificação:** 🟠 ALTO  
**CVSS Score:** 7.5 (Alto)  
**Vetor de Ataque:** Network / Low Complexity  
**CWE:** CWE-693 (Protection Mechanism Failure)  
**Sistema Afetado:** Site principal (`www.municipio.gov.br`)

**Descrição:**

Análise dos cabeçalhos HTTP de resposta revelou a **ausência completa** de headers de segurança recomendados, deixando a aplicação vulnerável a ataques comuns como XSS, clickjacking e SSL stripping.

**Metodologia de Descoberta:**

Verificação realizada utilizando o comando `curl -I https://municipio.gov.br` para análise dos cabeçalhos HTTP de resposta. Os headers de segurança foram comparados com as recomendações do OWASP Secure Headers Project.

**Evidência:**

```
Comando: curl -I https://municipio.gov.br
Resultado: Headers de segurança ausentes

Headers verificados:
- Strict-Transport-Security (HSTS): ❌ AUSENTE
- Content-Security-Policy (CSP): ❌ AUSENTE
- X-Frame-Options: ❌ AUSENTE
- X-Content-Type-Options: ❌ AUSENTE
- X-XSS-Protection: ❌ AUSENTE
- Referrer-Policy: ❌ AUSENTE
```

**Impacto:**

- **XSS (Cross-Site Scripting)** facilitado pela ausência de CSP
- **Clickjacking** possível pela ausência de X-Frame-Options
- **Downgrade attacks (SSL stripping)** pela ausência de HSTS
- **MIME sniffing attacks** pela ausência de X-Content-Type-Options
- **Vazamento de informações** via Referrer-Policy ausente

**Recomendações:**

**Imediato:**

Implementar todos os headers de segurança recomendados:

```apache
# No arquivo .htaccess ou configuração do Apache
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
Header always set Content-Security-Policy "default-src 'self'"
Header always set X-Frame-Options "DENY"
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set Permissions-Policy "geolocation=(), microphone=()"
```

**Referências:**
- OWASP Secure Headers Project: https://owasp.org/www-project-secure-headers/
- Mozilla Observatory: https://observatory.mozilla.org/

---

### 4.8 [ALTO] Ausência de Segmentação de Rede

**Classificação:** 🟠 ALTO  
**CVSS Score:** 7.0 (Alto)  
**Vetor de Ataque:** Adjacent Network / Low Complexity  
**CWE:** CWE-1021 (Improper Restriction of Rendered UI Layers)

**Descrição:**

Todos os serviços críticos (web, DNS, email, banco de dados, painéis administrativos) estão hospedados no mesmo servidor físico/virtual, sem evidências de segmentação de rede, VLANs ou firewalls internos.

**Metodologia de Descoberta:**

Análise de IPs via Shodan e consultas DNS revelou que todos os serviços estão no mesmo endereço IP ou na mesma sub-rede (XX.XX.XX.0/24), sem separação lógica ou física.

**Impacto:**

- Ponto único de falha (SPOF)
- Comprometimento em cascata (um serviço afeta todos)
- Movimentação lateral facilitada para atacantes
- Dificuldade de contenção de incidentes
- Impossibilidade de aplicar políticas de segurança granulares

**Recomendações:**

**Curto Prazo:**
- Separar serviços em servidores distintos (web, banco, email)
- Implementar VLANs para segmentação lógica
- Configurar firewalls internos entre segmentos

**Longo Prazo:**
- Migrar para arquitetura em nuvem com microserviços
- Implementar Zero Trust Network Architecture
- Realizar auditoria regular de segmentação

---

### 4.9 [ALTO] Vazamento de Emails Corporativos

**Classificação:** 🟠 ALTO  
**CVSS Score:** 7.5 (Alto)  
**Vetor de Ataque:** Network / Low Complexity  
**CWE:** CWE-200 (Exposure of Sensitive Information)

**Descrição:**

Através da ferramenta Hunter.io, foram identificados **75 emails corporativos** associados ao domínio investigado, incluindo emails de técnicos, executivos e pessoal administrativo.

**Metodologia de Descoberta:**

Busca realizada no Hunter.io utilizando o domínio `municipio.gov.br`. A ferramenta correlacionou emails encontrados em fontes públicas (LinkedIn, sites institucionais, bases de dados públicas).

**Evidência:**

```
Ferramenta: Hunter.io
Domínio: municipio.gov.br
Emails encontrados: 75
Categorias identificadas:
- Técnico/TI: [REDACTED]
- Executivo: [REDACTED]
- Administrativo: [REDACTED]
```

**Impacto:**

- Facilita ataques de spear phishing direcionados
- Revela a estrutura organizacional da TI e administração
- Permite identificação de padrões de nomenclatura de emails
- Emails de executivos são alvos prioritários para ataques
- Possível reutilização de credenciais em outros serviços

**Recomendações:**

**Curto Prazo:**
- Implementar filtros anti-phishing avançados
- Treinar equipe sobre ataques de spear phishing
- Implementar DMARC para prevenir spoofing de email

**Longo Prazo:**
- Implementar solução de email com segurança avançada
- Realizar exercícios simulados de phishing
- Estabelecer política de conscientização em segurança

---

### 4.10 [ALTO] Centralização de Serviços (Ponto Único de Falha)

**Classificação:** 🟠 ALTO  
**CVSS Score:** 7.0 (Alto)  
**Vetor de Ataque:** Physical / High Complexity  
**CWE:** CWE-664 (Improper Control of a Resource Through its Lifetime)

**Descrição:**

O servidor principal hospeda simultaneamente o site, nameservers, servidor de email e painéis administrativos. Esta centralização cria um ponto único de falha que pode comprometer toda a infraestrutura.

**Impacto:**

- Se o servidor cair, todos os serviços caem
- Se o servidor for comprometido, todos os serviços são comprometidos
- Dificuldade de backup e recuperação de desastres
- Impossibilidade de escalar serviços individualmente

**Recomendações:**

**Longo Prazo:**
- Migrar serviços para servidores dedicados
- Implementar redundância e alta disponibilidade
- Utilizar serviços gerenciados (DNS, email, banco)

---

### 4.11 [MÉDIO] Possível Exposição de Arquivo de Configuração (.env)

**Classificação:** 🟡 MÉDIO  
**CVSS Score:** 5.3 (Médio)  
**Vetor de Ataque:** Network / Low Complexity  
**CWE:** CWE-538 (Insertion of Sensitive Information into Externally-Accessible File or Directory)

**Descrição:**

Tentativa de acesso ao arquivo `.env` (comumente utilizado para armazenar credenciais e configurações sensíveis) retornou HTTP 406 (Not Acceptable) ao invés de HTTP 404 (Not Found), sugerindo que o arquivo existe no servidor mas está sendo bloqueado por configuração do servidor.

**Metodologia de Descoberta:**

Teste passivo realizado utilizando `curl -I https://municipio.gov.br/.env`. O código HTTP retornado foi analisado e comparado com o comportamento esperado para arquivos inexistentes.

**Evidência:**

```
Comando: curl -I https://municipio.gov.br/.env
Resposta: HTTP/1.1 406 Not Acceptable
Mensagem: "An appropriate representation of the requested resource 
could not be found on this server."

Análise: O código 406 indica que o servidor reconhece a existência 
do recurso mas não pode servir o conteúdo no formato solicitado.
```

**Análise:**

O código HTTP 406 indica que o servidor reconhece a existência do recurso mas não pode servir o conteúdo no formato solicitado. Isso é consistente com:

1. Arquivo .env existente com regras de bloqueio no .htaccess
2. Configuração do Apache para não servir arquivos ocultos
3. Possível WAF bloqueando tentativas de acesso

**Impacto Potencial:**

Se o arquivo .env existe, pode conter:

- Credenciais de banco de dados em texto claro
- Chaves de API e tokens de acesso
- Configurações sensíveis do sistema
- Credenciais de serviços de terceiros

**Recomendações:**

**Imediato:**
- Verificar se o arquivo .env existe e remover do diretório web
- Mover arquivos de configuração para fora do document root
- Implementar controles de acesso rigorosos
- Rotacionar todas as credenciais potencialmente expostas

**Referências:**
- OWASP: A05:2021 – Security Misconfiguration

---

### 4.12 [MÉDIO] Ausência de DNSSEC

**Classificação:** 🟡 MÉDIO  
**CVSS Score:** 5.3 (Médio)  
**Vetor de Ataque:** Network / High Complexity  
**CWE:** CWE-345 (Insufficient Verification of Data Authenticity)

**Descrição:**

Os registros DNS do domínio não estão assinados criptograficamente com DNSSEC, tornando-os vulneráveis a ataques de DNS Spoofing e Cache Poisoning.

**Metodologia de Descoberta:**

Verificação realizada utilizando o comando `dig +dnssec municipio.gov.br @8.8.8.8` e validação via DNSSEC Analyzer (dnssec-analyzer.verisign.com).

**Evidência:**

```
Comando: dig +dnssec municipio.gov.br @8.8.8.8
Resultado: Sem registros RRSIG encontrados
DNSSEC Analyzer: Falha na validação
```

**Impacto:**

- Redirecionamento de usuários para sites falsos
- Interceptação de comunicações
- Phishing facilitado
- Violação de integridade de DNS

**Recomendações:**

**Curto Prazo:**
- Implementar DNSSEC no domínio
- Monitorar alterações de DNS
- Utilizar provedores de DNS com suporte a DNSSEC

---

### 4.13 [BAIXO] Subdomínios Órfãos e Mal Configurados

**Classificação:** 🟢 BAIXO  
**CVSS Score:** 3.7 (Baixo)  
**Vetor de Ataque:** Network / High Complexity  
**CWE:** CWE-1021 (Improper Restriction of Rendered UI Layers)

**Descrição:**

Foram identificados subdomínios que redirecionam para o site principal ou não possuem configuração adequada, indicando falta de revisão periódica da infraestrutura DNS.

**Evidência:**

Subdomínio `mail.municipio.gov.br` redireciona para `www.municipio.gov.br`, sugerindo que foi criado para o registro MX mas não possui servidor de email dedicado.

**Impacto:**

- Indica desorganização na gestão de DNS
- Pode confundir usuários e sistemas
- Potencial para subdomain takeover se não for revisado

**Recomendações:**

**Curto Prazo:**
- Revisar todos os subdomínios e remover os desnecessários
- Documentar a função de cada subdomínio
- Implementar processo de revisão periódica

---

### 4.14 [BAIXO] Ausência de Configurações de Email (SPF/DKIM/DMARC)

**Classificação:** 🟢 BAIXO  
**CVSS Score:** 3.7 (Baixo)  
**Vetor de Ataque:** Network / Low Complexity  
**CWE:** CWE-290 (Authentication Bypass by Spoofing)

**Descrição:**

Análise dos registros DNS TXT revelou ausência ou configuração inadequada de SPF, DKIM e DMARC, deixando o domínio vulnerável a spoofing de email.

**Metodologia de Descoberta:**

Consultas DNS realizadas utilizando `dig TXT` para verificar os registros SPF, DKIM e DMARC do domínio.

**Impacto:**

- Facilita spoofing de email em nome do domínio
- Emails fraudulentos podem ser entregues como legítimos
- Aumenta risco de phishing contra cidadãos e parceiros

**Recomendações:**

**Curto Prazo:**
- Implementar SPF para autorizar servidores legítimos
- Configurar DKIM para assinatura criptográfica de emails
- Implementar DMARC com política de rejeição

**Referências:**
- DMARC.org: https://dmarc.org/
- Google Postmaster Guidelines

---

## 📊 5. ANÁLISE DE RISCO

### 5.1 Matriz de Risco

| Vulnerabilidade | Probabilidade | Impacto | Nível de Risco |
|---|---|---|---|
| CVE-2026-44631 (RCE) | Alta | Crítico | 🔴 Crítico |
| vCenter Exposto | Alta | Crítico | 🔴 Crítico |
| Protocolo com 214 CVEs | Alta | Crítico | 🔴 Crítico |
| phpMyAdmin Exposto | Alta | Crítico | 🔴 Crítico |
| cPanel Exposto | Alta | Crítico | 🔴 Crítico |
| GLPI Exposto | Média | Alto | 🟠 Alto |
| Ausência de Headers | Alta | Alto | 🟠 Alto |
| Ausência de Segmentação | Alta | Alto | 🟠 Alto |
| Vazamento de Emails | Alta | Alto | 🟠 Alto |
| Centralização de Serviços | Média | Alto | 🟠 Alto |
| Possível .env Exposto | Média | Médio | 🟡 Médio |
| Ausência de DNSSEC | Baixa | Médio | 🟡 Médio |
| Subdomínios Órfãos | Baixa | Baixo | 🟢 Baixo |
| Ausência de SPF/DKIM/DMARC | Baixa | Baixo | 🟢 Baixo |

### 5.2 Distribuição por Severidade

```
🔴 Crítico:  5 vulnerabilidades (33%)
🟠 Alto:     5 vulnerabilidades (33%)
🟡 Médio:    3 vulnerabilidades (20%)
🟢 Baixo:    2 vulnerabilidades (14%)
```

### 5.3 Análise de Causa Raiz

**Fatores Técnicos:**

- Configurações padrão inseguras não alteradas pós-instalação
- Ausência de hardening de sistemas
- Falta de monitoramento de vulnerabilidades
- Não aplicação de patches de segurança
- Ausência de headers de segurança HTTP

**Fatores Processuais:**

- Ausência de política de segurança da informação
- Falta de processo de gestão de vulnerabilidades
- Nenhum procedimento de revisão periódica de configurações
- Ausência de plano de resposta a incidentes
- Falta de processo de patch management

**Fatores Humanos:**

- Equipe técnica sobrecarregada
- Falta de especialização em segurança da informação
- Ausência de treinamento em segurança
- Cultura de "se funciona, não mexe"

**Fatores Organizacionais:**

- Orçamento limitado para segurança
- Priorização de funcionalidade sobre segurança
- Contratação de hospedagem por menor preço
- Ausência de requisitos de segurança em contratos
- Infraestrutura híbrida sem governança unificada

---

## 🛡️ 6. RECOMENDAÇÕES

### 6.1 Prioridade Imediata (0-7 dias)

1. **REMOVER vCenter DA INTERNET**
   - Restringir acesso apenas à rede interna
   - Implementar VPN obrigatória para acesso remoto

2. **Remover phpMyAdmin do acesso público**
   - Restringir acesso apenas à rede interna
   - Ou desativar completamente se não for necessário

3. **Restringir acesso ao cPanel**
   - Configurar whitelist de IPs (apenas IPs da prefeitura)
   - Habilitar MFA obrigatório

4. **Atualizar sistema de gestão (Conam)**
   - Aplicar patch da CVE-2026-44631
   - Testar em ambiente de homologação antes de produção

5. **Isolar sistema de Protocolo**
   - Realizar inventário das 214 vulnerabilidades
   - Priorizar correção das 57 críticas

6. **Implementar Headers de Segurança HTTP**
   - Adicionar todos os headers recomendados pelo OWASP

7. **Alterar todas as senhas**
   - cPanel, banco de dados, email, painéis administrativos
   - Utilizar senhas fortes e únicas

### 6.2 Prioridade Curto Prazo (7-30 dias)

1. **Implementar MFA em todos os painéis**
   - Webmail, cPanel, admin, banco de dados, GLPI, vCenter

2. **Configurar firewall e segmentação**
   - Bloquear portas desnecessárias
   - Separar serviços em VLANs

3. **Implementar DNSSEC**
   - Assinar registros DNS criptograficamente

4. **Configurar SPF/DKIM/DMARC**
   - Prevenir spoofing de email

5. **Habilitar logs e monitoramento**
   - Logs de acesso a todos os painéis
   - Alertas de tentativas suspeitas

6. **Revisar subdomínios**
   - Remover subdomínios órfãos
   - Documentar função de cada um

7. **Verificar e atualizar GLPI**
   - Aplicar patches de segurança
   - Revisar plugins instalados

### 6.3 Prioridade Médio Prazo (30-90 dias)

1. **Migrar para hospedagem gerenciada**
   - Contratar provedor com SLA de segurança
   - Incluir requisitos de hardening no contrato

2. **Implementar WAF**
   - Filtrar requisições maliciosas
   - Proteger contra exploits conhecidos

3. **Separar serviços**
   - Banco de dados em servidor dedicado
   - Email em serviço gerenciado
   - DNS em provedor especializado

4. **Capacitar equipe**
   - Treinamento em segurança da informação
   - Certificações relevantes

5. **Desenvolver políticas**
   - Política de segurança da informação
   - Política de senhas
   - Plano de resposta a incidentes

6. **Unificar governança da infraestrutura híbrida**
   - Padronizar configurações entre AWS e hospedagem tradicional
   - Implementar ferramentas de gestão centralizada

### 6.4 Prioridade Longo Prazo (90+ dias)

1. **Implementar SOC ou monitoramento 24/7**
   - Detecção e resposta a incidentes
   - Análise de logs em tempo real

2. **Realizar pentests periódicos**
   - Trimestralmente ou após mudanças significativas
   - Contratar empresa especializada

3. **Implementar conformidade com LGPD**
   - Mapeamento de dados pessoais
   - Implementação de controles técnicos
   - Nomeação de DPO (Encarregado)

4. **Arquitetura Zero Trust**
   - Nunca confiar, sempre verificar
   - Microssegmentação de rede
   - Identidade como perímetro

5. **Programa de Bug Bounty**
   - Incentivar responsible disclosure
   - Estabelecer canal de comunicação com pesquisadores

---

## 📚 7. LIÇÕES APRENDIDAS

### 7.1 Para Profissionais de Segurança

1. **OSINT é subutilizado na defesa**
   - Se um atacante pode achar essas falhas passivamente, a defesa também pode
   - Use OSINT proativamente para identificar exposição

2. **Configurações padrão são o maior inimigo**
   - A maioria das vulnerabilidades vem de configurações não alteradas
   - Sempre faça hardening pós-instalação

3. **Infraestrutura híbrida requer governança unificada**
   - Múltiplos provedores e tecnologias aumentam a superfície de ataque
   - Padronização é essencial

4. **Sistemas críticos merecem atenção especial**
   - vCenter, GLPI, SEI são alvos de alto valor
   - Devem ser isolados e protegidos com rigor

5. **Documentação é essencial**
   - Um bom relatório não é só listar falhas
   - É explicar impacto, causa raiz e como resolver

6. **Ética é inegociável**
   - Mesmo com conhecimento técnico, respeite limites legais
   - Sempre obtenha autorização antes de testar

### 7.2 Para Gestores Públicos

1. **Segurança é investimento, não custo**
   - O barato sai caro em segurança
   - Hospedagem gerenciada é mais segura que a mais barata

2. **Equipe especializada é essencial**
   - Sistemas críticos precisam de profissionais de segurança
   - Capacitação contínua é obrigatória

3. **Requisitos de segurança em contratos**
   - Licitações devem incluir requisitos de segurança
   - SLA de segurança é tão importante quanto SLA de disponibilidade

4. **Infraestrutura crítica merece investimento proporcional**
   - vCenter, banco de dados, sistemas de protocolo são alvos prioritários
   - Isolamento e segmentação são obrigatórios

### 7.3 Para a Comunidade

1. **Sistemas municipais são alvos frequentes**
   - Muitas vezes negligenciados por serem "pequenos"
   - Mas armazenam dados sensíveis de milhares de cidadãos

2. **Compartilhamento de conhecimento fortalece a segurança**
   - Responsible disclosure ajuda a melhorar a segurança coletiva
   - Bug bounty incentiva a identificação de falhas

3. **Segurança por design é o caminho**
   - Não adianta corrigir depois, tem que ser seguro desde o início
   - Think secure, not just functional

---

## 📎 8. APÊNDICES

### Apêndice A: Glossário de Termos Técnicos

- **OSINT:** Open Source Intelligence - Inteligência de fontes abertas
- **RCE:** Remote Code Execution - Execução Remota de Código
- **MFA:** Multi-Factor Authentication - Autenticação de Múltiplos Fatores
- **CVE:** Common Vulnerabilities and Exposures - Base de dados de vulnerabilidades
- **CVSS:** Common Vulnerability Scoring System - Sistema de pontuação de vulnerabilidades
- **WAF:** Web Application Firewall - Firewall de Aplicação Web
- **DNSSEC:** Domain Name System Security Extensions - Extensões de segurança do DNS
- **LGPD:** Lei Geral de Proteção de Dados - Legislação brasileira de proteção de dados
- **ITSM:** IT Service Management - Gestão de Serviços de TI
- **SPOF:** Single Point of Failure - Ponto Único de Falha
- **SPF/DKIM/DMARC:** Mecanismos de autenticação de email

### Apêndice B: Referências

- OWASP Top 10: https://owasp.org/www-project-top-ten/
- OWASP Secure Headers: https://owasp.org/www-project-secure-headers/
- NVD (National Vulnerability Database): https://nvd.nist.gov/
- MITRE ATT&CK: https://attack.mitre.org/
- CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks/
- CERT.br: https://cert.br/
- VMware Security Advisories: https://www.vmware.com/security/advisories
- DMARC.org: https://dmarc.org/
- Mozilla Observatory: https://observatory.mozilla.org/

### Apêndice C: Ferramentas Utilizadas

- Shodan: https://www.shodan.io/
- Censys: https://search.censys.io/
- theHarvester: https://github.com/laramies/theHarvester
- crt.sh: https://crt.sh/
- DNSDumpster: https://dnsdumpster.com/
- Wappalyzer: https://www.wappalyzer.com/
- SecurityTrails: https://securitytrails.com/
- Hunter.io: https://hunter.io/
- VirusTotal: https://www.virustotal.com/
- DNSSEC Analyzer: https://dnssec-analyzer.verisign.com/

### Apêndice D: Checklist de Hardening para cPanel

- [ ] Restringir acesso por IP
- [ ] Habilitar MFA obrigatório
- [ ] Alterar URL padrão
- [ ] Desabilitar serviços desnecessários (FTP, SSH se não usado)
- [ ] Configurar firewall
- [ ] Habilitar logs de acesso
- [ ] Atualizar regularmente
- [ ] Revisar permissões de arquivos
- [ ] Implementar backups automatizados
- [ ] Monitorar tentativas de login

### Apêndice E: Modelo de Política de Senhas

**Requisitos Mínimos:**

- Comprimento mínimo: 12 caracteres
- Complexidade: Maiúsculas, minúsculas, números e símbolos
- Histórico: Não repetir as últimas 10 senhas
- Expiração: Troca a cada 90 dias
- Bloqueio: Após 5 tentativas falhas
- MFA: Obrigatório para sistemas críticos

### Apêndice F: Headers de Segurança Recomendados

```apache
# Apache Configuration
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
Header always set Content-Security-Policy "default-src 'self'; script-src 'self'"
Header always set X-Frame-Options "DENY"
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set Permissions-Policy "geolocation=(), microphone=(), camera=()"
```

### Apêndice G: Configurações SPF/DKIM/DMARC Recomendadas

```dns
# SPF Record
"v=spf1 include:_spf.google.com ~all"

# DMARC Record
"v=DMARC1; p=reject; rua=mailto:dmarc@municipio.gov.br"

# DKIM (configurar no provedor de email)
```

---

**Fim do Relatório**

**Contato do Autor:** herbertluizmolinaperfil@gmail.com
**LinkedIn:** https://www.linkedin.com/in/herbert-molina

---

*Relatório gerado em 02 de Julho de 2026*  
*Versão 2.0 - Final*
