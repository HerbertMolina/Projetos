# RELATÓRIO DE INVESTIGAÇÃO

## Mapeamento de Superfície de Ataque via OSINT Passivo em Ambiente Web (WordPress)

**Autor:** Herbert Molina

**Data:** 15 de Julho de 2026

**Classificação:** Confidencial / Público (Dados Anonimizados)

**Versão:** 1.0 - Final

**Tipo de Investigação:** OSINT 100% Passivo (sem interação ativa ou exploração)

---

## ⚖️ AVISO ÉTICO E LEGAL

Este relatório foi elaborado exclusivamente para fins educacionais e demonstração de habilidades em segurança da informação e inteligência de fontes abertas (OSINT).

A investigação foi conduzida utilizando **APENAS técnicas passivas**, sem qualquer interação direta, exploração, teste de intrusão ou acesso não autorizado aos sistemas investigados. Nenhuma ferramenta de varredura ativa intrusiva foi utilizada contra o alvo.

Todos os dados sensíveis (domínios, IPs, nomes) foram anonimizados para proteger a identidade do alvo. Qualquer semelhança com sistemas reais é coincidência. Este material não deve ser utilizado para atividades ilegais.

---

## 📊 1. SUMÁRIO EXECUTIVO

### 1.1 Contexto

Foi realizada uma investigação de segurança passiva em um website privado com o objetivo de mapear sua superfície de ataque, identificar a pilha tecnológica e avaliar a postura de segurança da infraestrutura de hospedagem, utilizando exclusivamente fontes abertas.

### 1.2 Principais Achados

A investigação revelou um ambiente de **hospedagem compartilhada** com múltiplas configurações inseguras e serviços expostos desnecessariamente. Foram identificadas **6 vulnerabilidades principais**, sendo **2 classificadas como Críticas**.

| Severidade | Quantidade | Descrição Resumida |
| --- | --- | --- |
| 🔴 Crítico | 3 | Banco de dados (MariaDB) exposto  e divulgação de erros na internet; Enumeração de usuários via API REST. |
| 🟠 Alto | 2 | Múltiplos painéis administrativos (cPanel, Webmail) expostos sem MFA. |
| 🟡 Médio | 1 | Ausência de Headers de Segurança HTTP e configuração de e-mail. |
| 🟢 Baixo | 1 | Exposição de metadados e versões de plugins (JetEngine/Elementor). |

### 1.3 Nível de Risco Geral

🔴 **CRÍTICO** — A combinação de um banco de dados acessível externamente com a enumeração pública de usuários e painéis administrativos expostos cria um cenário de alto risco para comprometimento total do sistema e vazamento de dados (LGPD).

---

## 🎯 2. OBJETIVOS E ESCOPO

### 2.1 Objetivos

- Mapear a pilha tecnológica (stack) do website.
- Identificar o provedor de hospedagem e o modelo de infraestrutura (compartilhada vs. dedicada).
- Detectar serviços, portas e painéis administrativos expostos publicamente.
- Avaliar configurações de segurança do WordPress e do servidor web.

### 2.2 Escopo

- Domínio alvo: `[DOMINIO_ALVO.com.br]`
- Endereço IP do servidor: `[XX.XX.XX.XX]`
- Análise de registros DNS, cabeçalhos HTTP, respostas de serviços e metadados públicos.

---

## 🛠️ 3. METODOLOGIA E FERRAMENTAS

A investigação seguiu o framework de Reconhecimento Passivo, utilizando:

- **Wappalyzer:** Identificação de tecnologias do lado do cliente e servidor.
- **Shodan / Censys:** Identificação de serviços expostos, versões e correlação de IP.
- **Nmap (Script `mysql-info`):** Verificação passiva de banner e capacidades do serviço de banco de dados.
- **curl / dig:** Análise de cabeçalhos HTTP e registros DNS.
- **ViewDNS / HackerTarget:** Verificação de hospedagem compartilhada (Reverse IP).

---

## 🏗️ 4. MAPEAMENTO DE INFRAESTRUTURA

### 4.1 Pilha Tecnológica Identificada

| Componente | Tecnologia | Versão | Status |
| --- | --- | --- | --- |
| **CMS** | WordPress | Não exposta | ⚠️ Alvo comum de exploits |
| **Page Builder** | Elementor | 3.21 | ⚠️ Verificar CVEs específicas |
| **Plugin Adicional** | JetEngine | Não exposta | ⚠️ Lida com dados dinâmicos e formulários |
| **Linguagem Backend** | PHP | 8.3 | ✅ Versão recente e suportada |
| **Servidor Web** | Apache | Oculta | ⚠️ Necessário identificar via Shodan |
| **Banco de Dados** | MariaDB | 10.6.27 | 🔴 **Exposto na porta 3306** |

### 4.2 Modelo de Hospedagem

A análise do WHOIS do IP e do DNS Reverso (`rDNS: server.servidordohost.net.br`) confirma que o alvo está em um ambiente de **Hospedagem Compartilhada** (provavelmente utilizando cPanel).
Múltiplos domínios (incluindo sites de cidades vizinhas) compartilham o mesmo endereço IP e infraestrutura física, introduzindo o risco de "contaminação cruzada" (noisy neighbor).

---

## ⚠️ 5. VULNERABILIDADES IDENTIFICADAS

### 5.1 🔴 [CRÍTICO] Banco de Dados MariaDB Exposto na Internet

- **Classificação:** Crítico
- **CVSS Estimado:** 9.1
- **Vetor de Ataque:** Network / Low Complexity
- **CWE:** CWE-200 (Exposure of Sensitive Information)

**Descrição:** O serviço de banco de dados MariaDB está acessível publicamente através da porta TCP 3306, respondendo a sondagens externas com seu banner e capacidades de autenticação.

**Evidência (Nmap `mysql-info`):**

3306/tcp open  mysql
| mysql-info:
|   Protocol: 10
|   Version: 5.5.5-10.6.27-MariaDB
|   Thread ID: 936033
|   Capabilities flags: 63486
|   Status: Autocommit
|   Salt: DL3YH<518cjl]o5ZE,Lw
|_  Auth Plugin Name: mysql_native_password

**Impacto:** Permite ataques de força bruta contra credenciais do banco de dados. Em caso de sucesso, o atacante tem acesso total a todos os dados do site (usuários, pedidos de e-commerce, configurações), configurando um grave vazamento de dados.

**Recomendação:** Bloquear imediatamente o acesso externo à porta 3306 no firewall do servidor, permitindo conexões apenas a partir de localhost (`127.0.0.1`) ou IPs de aplicação autorizados.

---

### 5.1.2 🔴 [CRÍTICO] Divulgação de Erros de Banco de Dados (WP_DEBUG Ativo)

**Classificação:** 🔴 CRÍTICO

**CVSS Score:** 7.5 (Alto)

**Vetor de Ataque:** Network / Low Complexity / No Authentication

**CWE:** CWE-209 (Generation of Error Message Containing Sensitive Information)

**Sistema Afetado:** WordPress Search e REST API

**Descrição:**

A aplicação está configurada com o modo de depuração (`WP_DEBUG`) ativo em ambiente de produção. Ao injetar caracteres especiais (como aspas simples `'`) nos parâmetros de busca, o servidor retorna HTTP 200 OK, mas exibe erros técnicos detalhados do banco de dados ou do PHP na interface do usuário.

**Evidência:**
Teste passivo no endpoint de busca padrão

curl -I "https://[DOMINIO]/?s=test'"

Resultado: HTTP/1.1 200 OK (O site exibe erro de banco de dados/PHP no navegador)

Teste passivo na API REST

curl -I "https://[DOMINIO]/wp-json/wp/v2/posts?search=test'"

Resultado: HTTP/1.1 200 OK

---

---

### 5.2 🔴 [CRÍTICO] Enumeração de Usuários via API REST do WordPress

- **Classificação:** Crítico
- **CVSS Estimado:** 7.5
- **Vetor de Ataque:** Network / Low Complexity / No Authentication
- **CWE:** CWE-200 (Exposure of Sensitive Information)

**Descrição:** O endpoint `/wp-json/wp/v2/users` da API REST do WordPress está acessível sem autenticação, retornando uma lista (JSON) com nomes de usuário, IDs e avatares dos administradores e editores do site.

**Impacto:** Reduz drasticamente a complexidade de ataques de força bruta no `wp-login.php`, pois o atacante já possui metade das credenciais (o nome de usuário). Facilita também ataques de phishing direcionado (*spear phishing*).

**Recomendação:** Desabilitar a listagem de usuários na API REST. Isso pode ser feito via plugin de segurança (ex: Wordfence, iThemes Security) ou adicionando um filtro no `functions.php` do tema ativo.

---

### 5.3 🟠 [ALTO] Painéis Administrativos Padrão Expostos (cPanel)

- **Classificação:** Alto
- **CVSS Estimado:** 7.0
- **Vetor de Ataque:** Network / Low Complexity

**Descrição:** Foram identificados múltiplos subdomínios e portas padrão do cPanel acessíveis publicamente:

- `webmail.[DOMINIO]` (Portas 2095/2096)
- `cpanel.[DOMINIO]` (Portas 2082/2083)
- `webdisk.[DOMINIO]` (Porta 2078)

**Impacto:** Aumenta a superfície de ataque para tentativas de login (*brute force*). Se as credenciais forem reutilizadas ou fracas, o atacante obtém controle total sobre arquivos, e-mails e configurações de DNS do domínio.

**Recomendação:** Restringir o acesso a esses painéis por endereço IP (whitelist). Implementar Autenticação de Múltiplos Fatores (MFA/2FA) obrigatória para todas as contas de hospedagem.

---

### 5.4 🟡 [MÉDIO] Ausência de Headers de Segurança HTTP

- **Classificação:** Médio
- **CVSS Estimado:** 5.3
- **CWE:** CWE-693 (Protection Mechanism Failure)

**Descrição:** A análise dos cabeçalhos de resposta HTTP (`curl -I`) revelou a ausência de headers de segurança modernos, como *Strict-Transport-Security* (HSTS), *Content-Security-Policy* (CSP) e *X-Frame-Options*.

**Impacto:** Deixa o site vulnerável a ataques do lado do cliente, como Clickjacking, XSS (*Cross-Site Scripting*) e SSL Stripping.

**Recomendação:** Configurar o servidor Apache (via `.htaccess` ou `httpd.conf`) para incluir os headers de segurança recomendados pelo OWASP.

---

### 5.5 🟢 [BAIXO] Exposição de Metadados de Plugins

- **Classificação:** Baixo
- **CVSS Estimado:** 3.7

**Descrição:** A análise via Wappalyzer e inspeção de código identificou o uso dos plugins Elementor (v3.21) e JetEngine. Embora o JetEngine não exponha sua versão diretamente, a presença de plugins complexos que lidam com formulários e dados dinâmicos requer atenção constante.

**Impacto:** Se uma vulnerabilidade for descoberta nessas versões específicas, o site se torna um alvo imediato até que a atualização seja aplicada.

**Recomendação:** Manter todos os plugins e temas do WordPress rigorosamente atualizados. Remover plugins não utilizados.  

### 🚨 ANÁLISE CRÍTICA:

**Porta 21 (FTP):**

- 🔴 **CRÍTICO** - Se credenciais forem fracas, atacante pode:
    - Upload de webshells
    - Download de backups
    - Modificação de arquivos do site

**Portas 25, 110, 143 (Email):**

- 🟠 **ALTO** - Servidor de email COMPLETO exposto
- Confirma que o cPanel está rodando email
- Possível spam relay se mal configurado

## ⚠️Vetores de ataque potenciais no robos.txt:
disallow /wp-admin/
allow /wp-admi/admin-ajax.php


Isso pode causar 

**Ataques de força bruta
Exploração de vulnerabilidades em plugins que usam AJAX
Enumeração de usuários (em algumas configurações)**

**Não é uma vulnerabilidade por si só**, mas é uma **exposição desnecessária** que aumenta a superfície de ataque.

---

## 📊 6. ANÁLISE DE RISCO E IMPACTO NOS NEGÓCIOS (BIA) - Contexto do Negócio

Diferente de grandes corporações, o impacto de um incidente de segurança em um comércio local de assistência técnica está diretamente ligado à **continuidade operacional** e à **reputação local**. A perda de confiança dos clientes e a indisponibilidade do canal de vendas/agendamento são os maiores riscos.

---

## 🛡️ 7. RECOMENDAÇÕES E ROADMAP DE CORREÇÃO

Para um comércio de pequeno/médio porte, as recomendações focam em **baixo custo de implementação e alto impacto na mitigação de riscos**.

### 7.1 Fase 1: Estancamento Imediato

*Foco: Eliminar as vulnerabilidades críticas que permitem acesso remoto fácil.*

- [ ]  **Bloquear a porta 3306 (MySQL):** Configurar o firewall do servidor para aceitar conexões ao banco de dados apenas via `localhost` (127.0.0.1). *Esta é a ação mais urgente.*
- [ ]  **Proteger a API REST:** Instalar um plugin de segurança (ex: Wordfence ou iThemes Security) e ativar a opção "Disable REST API for non-logged-in users" para impedir a enumeração de usuários.
- [ ]  **Higienização de Acessos:** Alterar todas as senhas do cPanel, WordPress e e-mails para senhas fortes (16+ caracteres, geradas por gerenciador de senhas).
- [ ]  **Ativar MFA (2FA):** Habilitar autenticação de dois fatores no login do cPanel e do WordPress.

### 7.2 Fase 2: Fortalecimento e Resiliência

*Foco: Prevenir incidentes e garantir recuperação em caso de falha.*

- [ ]  **Implementar Backups Automatizados Externos:** Configurar backups diários do site e do banco de dados enviados para um local externo (ex: Google Drive, AWS S3 ou serviço de backup da própria hospedagem), garantindo que, em caso de ataque, o site possa ser restaurado em horas.
- [ ]  **Atualização Controlada:** Atualizar o core do WordPress, o tema e os plugins (Elementor, JetEngine) para as versões mais recentes, preferencialmente em um ambiente de teste (staging) antes da produção.
- [ ]  **Ocultar Painéis Padrão:** Alterar a URL de login do WordPress (ex: de `/wp-admin` para `/portal-interno`) usando plugins de segurança, reduzindo ruído de ataques automatizados.

### 7.3 Fase 3: Maturidade e Conformidade

*Foco: Cultura de segurança e conformidade básica.*

- [ ]  **Adequação Básica à LGPD:** Revisar o formulário de contato e checkout para garantir que haja um checkbox de consentimento de privacidade e uma Política de Privacidade visível.
- [ ]  **Treinamento de Conscientização:** Orientar a equipe a não abrir anexos suspeitos no e-mail e a verificar a URL antes de inserir senhas, mitigando riscos de phishing.
- [ ]  **Avaliação de Hospedagem:** Se o provedor atual não permitir o fechamento da porta 3306 ou a implementação de MFA, avaliar a migração para uma hospedagem WordPress gerenciada (ex: Hostinger Business, KingHost, etc.), que já inclui essas proteções nativamente.

---

## 📊 8. ANÁLISE DE RISCO E CAUSA RAIZ

As vulnerabilidades identificadas não são falhas complexas de "zero-day", mas sim falhas de configuração e arquitetura:

- **Modelo de Hospedagem:** A escolha por hospedagem compartilhada de baixo custo sem *hardening* personalizado.
- **Falta de Segmentação:** O banco de dados não está isolado da rede pública.
- **Configuração Padrão do WordPress:** A API REST vem habilitada por padrão e raramente é restrita por administradores iniciantes.

---

## 🎯 9. CONCLUSÃO

A investigação passiva demonstrou que, embora o site utilize tecnologias modernas (PHP 8.3, Elementor), a infraestrutura subjacente apresenta falhas críticas de configuração. A exposição direta do banco de dados MariaDB à internet, combinada com a facilidade de enumeração de usuários, cria um vetor de ataque direto e de alta probabilidade de sucesso.

A boa notícia é que todas as vulnerabilidades identificadas podem ser remediadas com configurações de firewall e plugins de segurança, sem a necessidade de reescrever o código do site. Recomenda-se a aplicação imediata das correções de prioridade crítica.
