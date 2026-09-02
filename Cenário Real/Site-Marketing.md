# INVESTIGAÇÃO EM SEGURANÇA DA INFORMAÇÃO

## Mapeamento de Superfície de Ataque via OSINT Passivo em Aplicação Web Moderna (Next.js/Supabase)

**Autor:** Herbert Molina

**Data:** 02 de Julho de 2026

**Classificação:** Público (Dados Anonimizados)

**Versão:** 1.0 - Final

**Tipo de Investigação:** OSINT 100% Passivo (sem interação ativa com o alvo)

---

## ⚖️ AVISO ÉTICO E LEGAL

Este relatório foi elaborado exclusivamente para fins educacionais e demonstração de habilidades em segurança da informação e inteligência de fontes abertas (OSINT).

A investigação foi conduzida utilizando APENAS técnicas passivas, sem qualquer interação direta, exploração, teste de intrusão ou acesso não autorizado aos sistemas investigados. Nenhuma ferramenta de varredura ativa (Nmap, Nessus, Nikto, etc.) foi utilizada contra o alvo.

Todos os dados sensíveis foram anonimizados para proteger a identidade do alvo. Qualquer semelhança com sistemas reais é coincidência.

Este material não deve ser utilizado para atividades ilegais ou não autorizadas. O autor não se responsabiliza pelo uso indevido das informações aqui contidas.

Para profissionais de segurança: Sempre obtenha autorização por escrito (Regras de Engajamento) antes de realizar testes de intrusão em sistemas de terceiros. No Brasil, o acesso não autorizado a sistemas informáticos é tipificado como crime pela Lei 12.737/2012 (Art. 154-A do Código Penal).

---

## 📊 SUMÁRIO EXECUTIVO

### Contexto

Foi realizada uma investigação de segurança passiva em uma aplicação web privada de natureza informativa, com o objetivo de mapear sua superfície de ataque, identificar a pilha tecnológica moderna e verificar a postura de segurança de seus ambientes de produção e desenvolvimento.

### Escopo da Investigação

- Domínio principal e subdomínios públicos (incluindo ambientes de QA)
- Registros DNS e infraestrutura de hospedagem (AWS, Lokaweb, Cloudflare)
- Tecnologias identificadas via análise de cabeçalhos HTTP e Wappalyzer
- Vulnerabilidades conhecidas (CVEs) na stack tecnológica
- Configuração de serviços de Backend-as-a-Service (Supabase)

### Metodologia

A investigação utilizou abordagem 100% passiva, empregando ferramentas de inteligência de fontes abertas para coleta de informações sobre infraestrutura, serviços expostos e correlação de vulnerabilidades. Nenhuma interação ativa ou exploração foi realizada.

### Principais Achados

A investigação identificou **6 vulnerabilidades/achados de segurança** distribuídos em diferentes níveis de severidade:

| Severidade | Quantidade | Descrição |
| --- | --- | --- |
| 🔴 Crítico | 1 | Bypass de autorização em Middleware do Next.js (CVE-2025-29927) |
| 🟠 Alto | 2 | SSRF em Server Actions (CVE-2024-34351) e Cache Poisoning (CVE-2024-46982) |
| 🟠 Alto | 1 | Exposição pública de múltiplos ambientes de QA e Desenvolvimento |
| 🟡 Médio | 2 | Endpoint de Backend-as-a-Service (Supabase) identificado e Indisponibilidade/Bloqueio via AWS ELB (HTTP 503) |

### Impacto Potencial

Embora o site principal tenha natureza predominantemente informativa, nossa análise identificou a exposição pública de ambientes de Quality Assurance (.qa) nomeados com referências a projetos ou clientes específicos (ex: elanco, syngenta). Um comprometimento nestes ambientes, mesmo que de teste, gera riscos severos:

1. Risco Reputacional e de Confiança B2B: A defacement ou vazamento em um subdomínio associado a um nome de grande porte pode ser interpretado pelo mercado como uma falha de segurança da sua empresa perante seus clientes/parceiros.
2. Violação de Boas Práticas de Desenvolvimento (Shadow IT): A exposição de ambientes de teste indica falhas no processo de 'Decommissioning' ou isolamento de rede, violando princípios básicos de DevSecOps.
3. Agravamento de Passivos: Em conjunto com as vulnerabilidades críticas do framework (Next.js), um incidente pode configurar falha na adoção de medidas de segurança (Art. 46 da LGPD), especialmente se houver qualquer reutilização de credenciais entre os ambientes de teste e produção."

### Nível de Risco Geral

🔴 **CRÍTICO** — A combinação de uma stack tecnológica desatualizada (Next.js 14.0.1) com vulnerabilidades críticas conhecidas e a exposição de ambientes de desenvolvimento (.qa) representa um risco significativo à confidencialidade e integridade do sistema.

---

## 🎯 1. OBJETIVOS E ESCOPO

### 1.1 Objetivos da Investigação

- Mapear a superfície de ataque exposta publicamente.
- Identificar a pilha tecnológica (frontend, backend, banco de dados, CDN).
- Correlacionar versões de software com bases de dados de vulnerabilidades (CVEs).
- Identificar subdomínios esquecidos ou mal configurados (Shadow IT).
- Avaliar a postura de segurança de serviços de terceiros integrados (ex: Supabase).

### 1.2 Escopo da Investigação

**Incluído:**

- Domínio principal e todos os subdomínios públicos (.qa, .api, etc.)
- Registros DNS (A, AAAA, NS, SOA)
- Informações disponíveis em bases públicas (WHOIS, crt.sh, Shodan, Censys)
- Tecnologias identificadas via Wappalyzer e análise de cabeçalhos HTTP

**Excluído:**

- Testes de intrusão ativos ou exploração de vulnerabilidades.
- Acesso não autorizado a sistemas ou tentativa de autenticação.
- Engenharia social ou varredura ativa de portas.

### 1.3 Restrições Éticas

- Investigação 100% passiva (sem envio de pacotes maliciosos).
- Anonimização completa de dados sensíveis e nomes de clientes/projetos.

---

## 🛠️ 2. METODOLOGIA

### 2.1 Abordagem

A investigação seguiu o framework PTES (Penetration Testing Execution Standard) adaptado para OSINT passivo:

1. **Reconhecimento Passivo:** Coleta de informações sem interação direta.
2. **Análise de Superfície de Ataque:** Mapeamento de subdomínios e serviços.
3. **Identificação de Vulnerabilidades:** Correlação de versões com NVD/CVE Details.
4. **Análise de Risco:** Avaliação de impacto e probabilidade.
5. **Documentação:** Elaboração de relatório técnico.

### 2.2 Ferramentas Utilizadas

| Ferramenta | Categoria | Uso Específico |
| --- | --- | --- |
| Wappalyzer | Identificação de Tecnologias | Detecção de Next.js, React, Supabase, Tailwind |
| crt.sh | Certificados SSL | Mapeamento de subdomínios (.qa, .api) |
| Shodan | Busca de Dispositivos | Identificação de AWS ELB, portas abertas e banners |
| Censys | Análise de Certificados | Correlação de infraestrutura e provedores |
| curl | Análise de Headers | Verificação de respostas HTTP e códigos de status |
| NVD (NIST) | Base de Vulnerabilidades | Correlação de versões do Next.js com CVEs |

### 2.3 Processo de Anonimização

| Dado Original | Substituição |
| --- | --- |
| Nome do domínio real | `dominio.net` / `site.dominio.net` |
| Endereços IP reais | `XX.XX.XX.XX` |
| Nomes de projetos/clientes | `[REDACTED]` ou genéricos |

---

## 🏗️ 3. MAPEAMENTO DE INFRAESTRUTURA

### 3.1 Informações de Registro e DNS

- **Provedor de DNS:** Amazon Route 53 (identificado pelos nameservers da AWS).
- **Provedor de Hospedagem:** Lokaweb (identificado via WHOIS do domínio).
- **Infraestrutura de Borda:** Cloudflare (identificado via cabeçalhos HTTP e roteamento).
- **Balanceamento de Carga:** AWS Elastic Load Balancer (ELB) v2.0.

### 3.2 Subdomínios Identificados

A investigação revelou uma forte presença de ambientes de Quality Assurance (QA) e desenvolvimento publicamente acessíveis:

| Subdomínio | Função Presumida | Status | Risco |
| --- | --- | --- | --- |
| `site.dominio.net` | Site principal de produção | Ativo | Médio |
| `bipper-docs.qa.dominio.net` | Documentação de projeto QA | Ativo | 🟠 Alto |
| `elanco.qa.dominio.net` | Ambiente de testes (Cliente/Projeto) | Ativo (IIS) | 🟠 Alto |
| `fdevs.qa.dominio.net` | Ambiente de desenvolvimento frontend | Ativo | 🟠 Alto |
| `portaria.dominio.net` | Sistema de controle/portaria | Ativo | 🟠 Alto |
| `syngenta.qa.dominio.net` | Ambiente de testes (Cliente/Projeto) | Ativo (IIS) | 🟠 Alto |
| `faq.qa.dominio.net` | Base de conhecimento/FAQ | Ativo | 🟠 Alto |
| `zoetis.qa.dominio.net` | Ambiente de testes (Cliente/Projeto) | Ativo (IIS) | 🟠 Alto |
| `.qa.dominio.net` | Sistema específico de projeto | Ativo | 🟠 Alto |

### 3.3 Tecnologias Identificadas

Via Análise de Cabeçalhos HTTP e Wappalyzer:

| Componente | Tecnologia | Versão | Status de Segurança |
| --- | --- | --- | --- |
| Framework Web | Next.js | 14.0.1 | 🔴 Desatualizado (CVEs Críticas) |
| UI Library | React | 18.3.1 | ✅ Atualizado |
| Backend / BaaS | Supabase | N/A | 🟡 Requer monitoramento de configuração |
| Servidor Web (QA) | Microsoft IIS | N/A | ⚠️ Expõe ambientes de teste |
| CDN / WAF | Cloudflare | N/A | ✅ Ativo |
| Protocolo | HTTP/2 | N/A | ✅ Moderno |

---

## ⚠️ 4. VULNERABILIDADES E ACHADOS IDENTIFICADOS

### 4.1 🔴 [CRÍTICO] CVE-2025-29927 - Bypass de Autorização em Middleware (Next.js)

**Classificação:** 🔴 CRÍTICO | **CVSS Score:** 9.1

**Vetor de Ataque:** Network / Low Complexity / No Authentication

**CWE:** CWE-863 (Incorrect Authorization)

**Descrição:**

É possível burlar verificações de autorização feitas no middleware do Next.js. Um atacante pode enviar uma requisição com um cabeçalho HTTP especial (`x-middleware-subrequest`) e passar pelos checks de segurança sem ter permissão real, enganando o middleware para que ele trate a requisição como interna e válida.

**Impacto:**

- Acesso não autorizado a páginas ou painéis administrativos protegidos.
- Elevação de privilégio e vazamento de dados sensíveis de outros usuários.

**Conformidade Afetada:**

- 🇧🇷 **LGPD:** Violação do Art. 46 – falha de controle de acesso que permite acesso não autorizado a dados pessoais de usuários.
- 🌐 **OWASP Top 10 (2021):** A01:2021 – Broken Access Control (bypass de autorização no middleware).
- 🏢 **ISO/IEC 27001:2022:** Controle A.8.5 (Controle de acesso lógico) e A.8.29 (Testes de segurança no desenvolvimento) – não atendidos.
- ️ **SOC 2 Type II:** Critério CC6.1 (Controles lógicos de acesso) – falha de implementação.

**Recomendações:**

- **Imediato:** Atualizar o Next.js para a versão 14.2.25 ou superior (ou 15.2.3+).
- **Longo Prazo:** Implementar testes de segurança automatizados no pipeline de CI/CD para validar regras de middleware.

---

### 4.2 🟠 [ALTO] CVE-2024-34351 - SSRF em Server Actions (Next.js)

**Classificação:** 🟠 ALTO | **CVSS Score:** 7.5

**Vetor de Ataque:** Network / Low Complexity / No Authentication

**CWE:** CWE-918 (Server-Side Request Forgery)

**Descrição:**

Vulnerabilidade de SSRF nas Server Actions do Next.js em modo self-hosted. Se a aplicação usar Server Actions que fazem redirect para caminhos relativos, um atacante pode modificar o cabeçalho `Host` da requisição para fazer o servidor realizar requisições em nome dele, atingindo serviços internos da rede.

**Impacto:**

- Movimentação lateral na rede interna do provedor de hospedagem.
- Acesso a metadados de instâncias cloud ou serviços internos não expostos.

**Conformidade Afetada:**

- 🇧🇷 **LGPD:** Violação do Art. 46 – SSRF permite movimentação lateral e acesso a metadados de instâncias cloud (ex: AWS IMDSv1), expondo credenciais IAM.
- 🌐 **OWASP Top 10 (2021):** A10:2021 – Server-Side Request Forgery (SSRF).
- 🏢 **ISO/IEC 27001:2022:** Controle A.8.20 (Segurança de serviços de rede) – não atendido.
- ☁️ **AWS Well-Architected Framework:** Falha no pilar de Segurança (SEC03-BP01 – proteger a rede).

**Recomendações:**

- Atualizar o Next.js para a versão 14.1.1 ou superior.
- Validar e sanitizar rigorosamente todos os inputs e destinos de redirect nas Server Actions.

---

### 4.3 🟠 [ALTO] CVE-2024-46982 - Cache Poisoning em Rotas SSR

**Classificação:** 🟠 ALTO | **CVSS Score:** 7.5

**Vetor de Ataque:** Network / Low Complexity / No Authentication

**CWE:** CWE-799 (Improper Control of Interaction Frequency)

**Descrição:**

Um atacante pode enviar uma requisição maliciosa que força o Next.js a cachear conteúdo que não deveria ser cacheado em rotas SSR não-dinâmicas (Pages Router). Esse conteúdo envenenado pode se propagar para CDNs upstream (como o Cloudflare identificado na infraestrutura).

**Impacto:**

- Usuários legítimos podem ser servidos com conteúdo incorreto, quebrado ou malicioso.
- Interrupção prolongada do serviço até a expiração manual do cache.

**Conformidade Afetada:**

- 🇷 **LGPD:** Violação do princípio da integridade (Art. 6º, VI) – conteúdo envenenado pode ser servido a usuários legítimos, comprometendo a confiança.
- 🌐 **OWASP Top 10 (2021):** A05:2021 – Security Misconfiguration (cache mal configurado em rotas SSR).
- 🏢 **ISO/IEC 27001:2022:** Controle A.8.10 (Gestão de capacidade) e A.8.13 (Redundância de processamento de informação) – não atendidos.

**Recomendações:**

- Atualizar o Next.js para a versão 14.2.10 ou superior.
- Revisar as configurações de cache (`revalidate`) nas páginas SSR.

---

### 4.4 🟠 [ALTO] Exposição Pública de Ambientes de QA e Desenvolvimento

**Classificação:** 🟠 ALTO | **CVSS Score:** 7.0

**Vetor de Ataque:** Network / Low Complexity

**CWE:** CWE-200 (Exposure of Sensitive Information)

**Descrição:**

Foram identificados múltiplos subdomínios com a terminação `.qa` (Quality Assurance) e nomes de projetos específicos (ex: `elanco`, `syngenta`, `crono`) acessíveis publicamente na internet. Alguns respondem com páginas padrão do Microsoft IIS.

**Impacto:**

Ambientes de QA frequentemente possuem:

1. Configurações de segurança relaxadas (ex: modo debug ativo, logs verbosos).
2. Credenciais de teste fracas, hardcoded ou padrão.
3. Vazamento de lógica de negócio, documentação interna ou dados de clientes reais usados em testes.

**Conformidade Afetada:**

- 🇧🇷 **LGPD:** Violação do Art. 46 e Art. 48 – ambientes de teste com dados reais (ou credenciais reutilizadas) expostos publicamente configuram falha técnica e risco de incidente.
- 🌐 **OWASP Top 10 (2021):** A01:2021 – Broken Access Control e A05:2021 – Security Misconfiguration.
- 🏢 **ISO/IEC 27001:2022:** Controle A.8.31 (Segregação de ambientes de desenvolvimento, teste e produção) – **não atendido** (ambiente QA acessível publicamente).
- 🛡️ **CIS Controls v8:** Controle 3.2 (Estabelecer e manter inventário de ativos de software) – subdomínios QA não inventariados nem protegidos.
- ️ **Boas Práticas de DevSecOps:** Violação do princípio de "Shift-Left Security" – ambientes de teste devem ser isolados por VPN ou allowlist de IPs.

**Recomendações:**

- Restringir o acesso a todos os subdomínios `.qa`, `.dev` e `.staging` via firewall (allowlist de IPs corporativos) ou autenticação VPN.
- Remover a resolução DNS pública desses ambientes quando não estiverem em uso ativo.

---

### 4.5 🟡 [MÉDIO] Endpoint de Backend-as-a-Service (Supabase) Identificado

**Classificação:** 🟡 MÉDIO (Informativo / Postura de Segurança)

**Vetor de Ataque:** N/A

**CWE:** CWE-200 (Exposure of Sensitive Information)

**Descrição:**

Foi identificado que a aplicação utiliza o Supabase como Backend-as-a-Service (BaaS), com endpoint REST ativo (`...supabase.co/rest/v1/`).

**Análise de Segurança:**

Durante os testes passivos, as requisições ao endpoint retornaram corretamente `401 Unauthorized: missing api key`. **Isso indica que a configuração básica de segurança está correta**, pois o banco de dados não está exposto publicamente sem autenticação.

**Por que documentar?**

Embora configurado corretamente agora, o Supabase é um ponto crítico. A documentação deste achado serve como alerta para que a equipe de desenvolvimento mantenha:

- O Row Level Security (RLS) rigorosamente ativado em todas as tabelas.
- A chave `anon` pública restrita apenas às permissões estritamente necessárias.
- A chave `service_role` **nunca** exposta no código frontend (o que foi confirmado como não exposta neste teste).

**Recomendações:**

- Manter a auditoria periódica das políticas RLS no painel do Supabase.
- Monitorar o código frontend (via DevTools) para garantir que nenhuma chave sensível seja acidentalmente commitada em repositórios públicos.

---

### 4.6 🟡 [MÉDIO] Indisponibilidade ou Bloqueio via AWS ELB (HTTP 503)

**Classificação:** 🟡 MÉDIO (Disponibilidade / Operacional)

**Vetor de Ataque:** N/A

**CWE:** CWE-708 (Incorrect Permission Assignment for Critical Resource)

**Descrição:**

Ao consultar o endereço IP principal da aplicação via Shodan na porta 80, a resposta obtida foi `HTTP/1.1 503 Service Temporarily Unavailable` com o cabeçalho `Server: awselb/2.0`.

**Análise de Segurança e Operacional:**

- **Para o Atacante:** Isso atua como uma proteção passiva, indicando que o scanner foi bloqueado pelo WAF/ELB ou que os servidores de backend (origin) estão inalcançáveis para o balanceador.
- **Para o Proprietário do Site (Risco Real):** Um 503 persistente do ELB indica que os "Target Groups" não possuem instâncias saudáveis. Isso pode significar que os servidores de aplicação estão cairam, estão sobrecarregados, ou que há uma regra de WAF mal configurada bloqueando tráfego legítimo (falso positivo).

**Recomendações:**

- Verificar imediatamente os "Health Checks" do AWS Target Group associado a este ELB.
- Revisar os logs do AWS WAF para garantir que o bloqueio de scanners (como o Shodan) não esteja afetando usuários reais ou motores de busca legítimos.

---

**🔗 Cenário de Ataque Hipotético:**

1. **Descoberta:** O atacante mapeia o subdomínio `subdominio.qa.dominio.net` e encontra um painel de login com proteção fraca (ou credenciais padrão de desenvolvimento, como `admin/admin`).
2. **Pivô (Password Reuse):** Dentro do ambiente QA, o atacante encontra um arquivo de configuração ou um comentário no código-fonte que contém uma chave de API ou senha que é **reutilizada** no ambiente de produção.
3. **Escalação:** O atacante utiliza essa mesma credencial para acessar o sistema principal ou a API do Supabase.
4. **Impacto Final:** Devido a uma possível falha de Row Level Security (RLS) ou à obtenção de uma chave privilegiada, o atacante acessa, modifica ou exclui dados reais de clientes no banco de dados de produção

---

## 📊 5. ANÁLISE DE RISCO

### 5.1 Matriz de Risco

| Vulnerabilidade / Achado | Probabilidade | Impacto | Nível de Risco |
| --- | --- | --- | --- |
| CVE-2025-29927 (Middleware Bypass) | Alta | Crítico | 🔴 Crítico |
| CVE-2024-34351 (SSRF) | Média | Alto | 🟠 Alto |
| CVE-2024-46982 (Cache Poisoning) | Média | Alto | 🟠 Alto |
| Ambientes QA Expostos | Alta | Alto | 🟠 Alto |
| Endpoint Supabase Identificado | Baixa | Médio | 🟡 Médio |
| Indisponibilidade AWS ELB (503) | Média | Médio | 🟡 Médio |

### 5.2 Análise de Causa Raiz

- **Técnicos:** Uso de versões de framework (Next.js) sem aplicação de patches de segurança; falta de isolamento de rede para ambientes de desenvolvimento (.qa).
- **Processuais:** Ausência de um processo de "Decommissioning" ou restrição de acesso para ambientes de teste após o fim do desenvolvimento.
- **Organizacionais:** Possível priorização da entrega de funcionalidades (features) em detrimento de revisões de segurança na infraestrutura de hospedagem (AWS/Lokaweb).

---

## 🛡️ 6. RECOMENDAÇÕES

### 6.1 Prioridade Imediata (0-7 dias)

1. **Atualização Crítica do Next.js:** Atualizar a aplicação para a versão 14.2.25 ou superior para mitigar as CVEs de Middleware Bypass, SSRF e Cache Poisoning.
2. **Isolamento de Ambientes QA:** Configurar regras de firewall ou autenticação básica (HTTP Auth) para bloquear o acesso público a todos os subdomínios `.qa.dominio.net`.
3. **Verificação de Saúde do ELB:** Investigar a causa do erro 503 no AWS Elastic Load Balancer para garantir a disponibilidade do serviço e a correta configuração do WAF.

### 6.2 Prioridade Curto Prazo (7-30 dias)

1. **Auditoria do Supabase:** Revisar todas as políticas de Row Level Security (RLS) e garantir que nenhuma chave de API privilegiada (`service_role`) esteja presente no código frontend.
2. **Revisão de Subdomínios:** Mapear e desativar a resolução DNS de subdomínios de projetos antigos ou não utilizados (Shadow IT).
3. **Headers de Segurança:** Implementar cabeçalhos de segurança (CSP, HSTS, X-Frame-Options) via configuração do Next.js ou no Cloudflare.

### 6.3 Prioridade Médio/Longo Prazo (30+ dias)

1. **Pipeline de Segurança (DevSecOps):** Integrar ferramentas de SCA (Software Composition Analysis) no CI/CD para bloquear automaticamente o deploy de versões de bibliotecas com CVEs conhecidas.
2. **Política de Ambientes:** Estabelecer uma política formal de que ambientes de desenvolvimento e QA nunca devem ter resolução DNS pública, sendo acessíveis apenas via VPN corporativa.

---

## 📚 7. LIÇÕES APRENDIDAS

*A combinação de tecnologias modernas (Next.js, React, Supabase) muitas vezes gera um 'falso sentimento de segurança' nas equipes de desenvolvimento, levando à crença de que a segurança é 'automática'. No entanto, a presença da versão 14.0.1 do Next.js (com CVEs críticas de bypass de autenticação e SSRF) e a exposição de ambientes `.qa` provam que a segurança deve ser configurada e gerenciada ativamente, não apenas herdada do framework.*

---

## 🎯 8. CONCLUSÃO

Esta investigação demonstrou que, mesmo em aplicações web informativas com stacks tecnológicas modernas, a superfície de ataque permanece significativa. A combinação de um framework desatualizado (Next.js 14.0.1) com vulnerabilidades críticas de lógica e autorização, somada à exposição pública de ambientes de teste (.qa), cria um cenário de risco elevado.

A boa notícia é que a infraestrutura de borda (Cloudflare, AWS ELB) e o serviço de backend (Supabase) apresentam sinais de configurações defensivas básicas (como a exigência de chave de API). No entanto, a segurança não pode depender apenas de camadas externas.

Recomenda-se ação imediata na atualização do framework e no isolamento dos ambientes de desenvolvimento, seguindo o princípio de que a segurança deve ser integrada ao ciclo de vida do desenvolvimento (Security by Design), e não tratada como uma reflexão tardia.

---

## 📎 9. APÊNDICES

### Apêndice A: Glossário de Termos Técnicos

- **SSRF (Server-Side Request Forgery):** Ataque que força o servidor a fazer requisições não intencionais.
- **BaaS (Backend-as-a-Service):** Modelo de nuvem que fornece backend pré-construído (ex: Supabase, Firebase).
- **ELB (Elastic Load Balancer):** Serviço da AWS que distribui o tráfego de entrada entre vários destinos.
- **RLS (Row Level Security):** Recurso do PostgreSQL/Supabase que restringe o acesso a linhas de tabelas com base no usuário.

### Apêndice B: Referências

- NVD - CVE-2025-29927: https://nvd.nist.gov/vuln/detail/CVE-2025-29927
- NVD - CVE-2024-34351: https://nvd.nist.gov/vuln/detail/CVE-2024-34351
- NVD - CVE-2024-46982: https://nvd.nist.gov/vuln/detail/CVE-2024-46982
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- Supabase Security Best Practices: https://supabase.com/docs/guides/security

### Apêndice C: Ferramentas Utilizadas

- whois, Wappalyzer ,urlscan, Shodan, Censys, curl, viewDns. NVD NIST.

---

**Fim do Relatório**
