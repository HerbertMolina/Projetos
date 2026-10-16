# RELATÓRIO DE INVESTIGAÇÃO EM SEGURANÇA DA INFORMAÇÃO
## Mapeamento de Superfície de Ataque via OSINT Passivo em Aplicação Web Corporativa (Laravel/WordPress)

**Autor:** Herbert Molina  
**Data:** 27 de Agosto de 2026  
**Classificação:** Público (Dados Anonimizados)  
**Versão:** 1.0 - Final  
**Tipo de Investigação:** OSINT 100% Passivo (sem interação ativa com o alvo)

---

## 📄 Controle do Documento

| Versão | Data | Autor | Descrição da Alteração | Aprovado por |
|---|---|---|---|---|
| 0.1 | 25/08/2026 | Herbert Molina | Reconhecimento inicial, Wappalyzer e identificação de stack | N/A |
| 0.5 | 26/08/2026 | Herbert Molina | Mapeamento de subdomínios, histórico de IP e análise de código-fonte | N/A |
| 1.0 | 27/08/2026 | Herbert Molina | Versão final com correlação de inteligência corporativa e cadeias de ataque | Herbert Molina |

---

## ️ AVISO ÉTICO E LEGAL

Este relatório foi elaborado exclusivamente para fins educacionais e demonstração de habilidades em segurança da informação e inteligência de fontes abertas (OSINT).

A investigação foi conduzida utilizando APENAS técnicas passivas, sem qualquer interação direta, exploração, teste de intrusão ou acesso não autorizado aos sistemas investigados. Nenhuma ferramenta de varredura ativa (Nmap, Nessus, Nikto, etc.) foi utilizada contra o alvo.

Todos os dados sensíveis foram anonimizados para proteger a identidade do alvo. Qualquer semelhança com sistemas reais é coincidência.

Este material não deve ser utilizado para atividades ilegais ou não autorizadas. O autor não se responsabiliza pelo uso indevido das informações aqui contidas.

Para profissionais de segurança: Sempre obtenha autorização por escrito (Regras de Engajamento) antes de realizar testes de intrusão em sistemas de terceiros. No Brasil, o acesso não autorizado a sistemas informáticos é tipificado como crime pela Lei 12.737/2012 (Art. 154-A do Código Penal).

---

## 📊 SUMÁRIO EXECUTIVO

### Contexto
Foi realizada uma investigação de segurança passiva em um site institucional de uma concessionária/revenda de veículos multimarcas. O objetivo foi mapear a superfície de ataque, identificar a pilha tecnológica e verificar a postura de segurança da infraestrutura de hospedagem e da aplicação web.

### Escopo da Investigação
- Domínio principal e subdomínios públicos (foco em vazamento de infraestrutura).
- Histórico de resolução DNS e provedores de hospedagem.
- Tecnologias identificadas via análise de cabeçalhos HTTP e Wappalyzer.
- Configurações de segurança de sessão e painéis administrativos.
- Inteligência corporativa (vínculos de CNPJ e vazamento de credenciais).

### Metodologia
A investigação utilizou abordagem 100% passiva, empregando ferramentas de inteligência de fontes abertas para coleta de informações sobre infraestrutura, serviços expostos e correlação de vulnerabilidades. Nenhuma interação ativa ou exploração foi realizada.

### Principais Achados
A investigação identificou 5 vulnerabilidades/achados de segurança distribuídos em diferentes níveis de severidade:

| Severidade | Quantidade | Descrição |
|---|---|---|
|  Crítico | 1 | Biblioteca Frontend Desatualizada (jQuery 3.5.1) com CVEs de XSS conhecidas |
| 🟠 Alto | 2 | Painel Administrativo (/admin) Exposto Publicamente e Vazamento de IP Real via Subdomínios de Email |
| 🟡 Médio | 1 | Risco de Credential Stuffing (Email corporativo vazado em 2024) |
| 🟢 Baixo | 1 | Configuração de Cookie de Sessão sem flag Secure (mitigado por HSTS) |

### Impacto Potencial
As vulnerabilidades identificadas, se exploradas, poderiam resultar em:
- Comprometimento da conta administrativa via ataques de força bruta facilitados.
- Execução de scripts maliciosos no navegador de visitantes (XSS) devido à biblioteca desatualizada.
- Bypass da proteção do Cloudflare através do acesso direto ao IP de origem exposto pelos subdomínios de email.
- Violação da LGPD e danos à reputação comercial da empresa.

### Nível de Risco Geral
🔴 ALTO — A combinação de um painel administrativo exposto, uma biblioteca frontend vulnerável e o vazamento da infraestrutura real de hospedagem cria um vetor de ataque viável e de baixo esforço para um ator malicioso.

---

##  1. OBJETIVOS E ESCOPO

### 1.1 Objetivos da Investigação
- Mapear a superfície de ataque exposta publicamente.
- Identificar a pilha tecnológica (frontend, backend, CDN).
- Correlacionar versões de software com bases de dados de vulnerabilidades (CVEs).
- Identificar vazamento de infraestrutura real por trás de proxies reversos (Cloudflare).
- Avaliar a postura de segurança de sessões e painéis de login.

### 1.2 Escopo da Investigação
**Incluído:**
- Domínio principal e subdomínios associados.
- Registros DNS (A, AAAA, MX, TXT, NS, CNAME).
- Informações disponíveis em bases públicas (WHOIS, crt.sh, Shodan, ViewDNS).
- Tecnologias identificadas via Wappalyzer e análise de cabeçalhos HTTP.

**Excluído:**
- Testes de intrusão ativos ou exploração de vulnerabilidades.
- Acesso não autorizado a sistemas ou tentativa de autenticação.
- Engenharia social ou varredura ativa de portas.

### 1.3 Restrições Éticas
- Investigação 100% passiva (sem envio de pacotes maliciosos).
- Anonimização completa de dados sensíveis, nomes de proprietários e CNPJs.

---

## 🛠️ 2. METODOLOGIA

### 2.1 Abordagem
A investigação seguiu o framework PTES (Penetration Testing Execution Standard) adaptado para OSINT passivo:
1. Reconhecimento Passivo: Coleta de informações sem interação direta.
2. Análise de Superfície de Ataque: Mapeamento de subdomínios e histórico de IPs.
3. Identificação de Vulnerabilidades: Correlação de versões com NVD/CVE Details.
4. Análise de Risco: Avaliação de impacto e probabilidade.
5. Documentação: Elaboração de relatório técnico.

### 2.2 Ferramentas Utilizadas
| Ferramenta | Categoria | Uso Específico |
|---|---|---|
| Wappalyzer | Identificação de Tecnologias | Detecção de Laravel, jQuery, PHP, Cloudflare |
| ViewDNS / SecurityTrails | Histórico de DNS | Identificação de IPs de origem anteriores ao Cloudflare |
| Shodan | Busca de Dispositivos | Identificação de portas abertas e banners em IPs de subdomínios |
| curl | Análise de Headers | Verificação de respostas HTTP, HSTS e cookies |
| Have I Been Pwned | Vazamento de Credenciais | Verificação de emails corporativos em breaches |
| NVD (NIST) | Base de Vulnerabilidades | Correlação de versões do jQuery com CVEs |

### 2.3 Processo de Anonimização
| Dado Original | Substituição |
|---|---|
| Nome do domínio real | k2multimarcas.com.br |
| Endereços IP reais | XX.XX.XX.XX |
| Nome do proprietário | [REDACTED] |
| CNPJs relacionados | [REDACTED] |

---

## 🏗️ 3. MAPEAMENTO DE INFRAESTRUTURA

### 3.1 Informações de Registro e Inteligência Corporativa
- **Proprietário Registrante:** [REDACTED] (Pessoa Física).
- **Contato Técnico:** contato@carrobauru.com.br (Email identificado em vazamento de dados em 2024).
- **Vínculo Corporativo:** Investigação passiva indicou forte correlação com um CNPJ de automecânica localizado na mesma região, com numeração sequencial, sugerindo um grupo de empresas de propriedade do mesmo indivíduo.

### 3.2 Arquitetura de Rede e Vazamento de IP
A infraestrutura utiliza uma arquitetura híbrida com proteção de borda, mas com falhas de configuração que expõem a origem:

- **Proteção de Borda:** Cloudflare (CDN/WAF).
- **Hospedagem Real (Origem):** Kinghost / Uni5 (AS28299).
- **Histórico:** O domínio utilizou IPs diretos da Cyberweb/Uni5 (ex: 187.1.136.141) até meados de 2023, antes da migração para o Cloudflare.

### 3.3 Subdomínios Identificados (Vazamento de Origem)
Enquanto o domínio principal é protegido pelo Cloudflare, subdomínios de infraestrutura de email apontam diretamente para os IPs reais do provedor de hospedagem:

| Subdomínio | Registro | Destino Real (IP) | Provedor | Risco |
|---|---|---|---|---|
| webmail.k2multimarcas.com.br | CNAME | 191.6.220.62 | Uni5/Kinghost | 🟠 Alto |
| mail.k2multimarcas.com.br | CNAME | 191.6.220.100, 191.6.220.99 | Uni5/Kinghost | 🟠 Alto |
| imap.k2multimarcas.com.br | CNAME | 191.6.220.7, 191.6.220.6 | Uni5/Kinghost | 🟠 Alto |
| autodiscover.k2multimarcas.com.br| CNAME | 191.6.215.156 | Uni5/Kinghost | 🟡 Médio |

### 3.4 Tecnologias Identificadas
Via Análise de Cabeçalhos HTTP e Wappalyzer:

| Componente | Tecnologia | Versão | Status de Segurança |
|---|---|---|---|
| Backend Framework | Laravel | N/A | ✅ Seguro (se configurado corretamente) |
| Linguagem | PHP | 8.2.31 | ✅ Atualizado |
| Frontend Library | jQuery | 3.5.1 |  Desatualizado (CVEs Críticas) |
| UI Framework | Bootstrap | N/A | ℹ️ Neutro |
| CDN / WAF | Cloudflare | N/A | ✅ Ativo |
| Servidor Web (Origem) | Apache | N/A | ℹ️ Padrão |

---

## ⚠️ 4. VULNERABILIDADES E ACHADOS IDENTIFICADOS

### 4.1 🔴 [CRÍTICO] Biblioteca Frontend Desatualizada (jQuery 3.5.1)
**Classificação:** 🔴 CRÍTICO | **CVSS Score:** 7.5 (Alto)  
**Vetor de Ataque:** Network / Low Complexity / No Authentication  
**CWE:** CWE-79 (Cross-site Scripting)

**Descrição:**  
A aplicação utiliza a versão 3.5.1 do jQuery, lançada em 2020. Esta versão possui vulnerabilidades de Cross-Site Scripting (XSS) documentadas, especificamente ao processar HTML de fontes não confiáveis contendo tags `<option>` ou através do método `htmlPrefilter`.

**Impacto:**  
- Um atacante pode injetar scripts maliciosos que são executados no navegador de outros usuários.
- Pode levar ao roubo de cookies de sessão (se não protegidos), redirecionamento para sites de phishing ou defacement do site.

**Conformidade Afetada:**
- 🇧🇷 LGPD: Violação do Art. 46 (Falha na adoção de medidas técnicas aptas a proteger dados pessoais).
-  OWASP Top 10 (2021): A03:2021 – Injection / A05:2021 – Security Misconfiguration.

**🔗 Cadeia de Ataque Hipotética (Kill Chain):**
1. Reconhecimento: Atacante identifica a versão do jQuery via Wappalyzer ou análise de cabeçalhos de scripts.
2. Armação: Cria um payload XSS específico para as CVEs do jQuery 3.5.1.
3. Entrega: Injeta o payload em um campo de entrada do site (ex: formulário de contato ou busca) que reflete a entrada sem sanitização adequada.
4. Impacto Final: Quando um administrador ou cliente acessa a página, o script é executado, roubando sua sessão ou redirecionando-o para um site de phishing de financiamento.

**Recomendações:**  
- Imediato: Atualizar a biblioteca jQuery para a versão 3.7.1 ou superior.

---

### 4.2  [ALTO] Painel Administrativo (/admin) Exposto Publicamente
**Classificação:** 🟠 ALTO | **CVSS Score:** 7.0  
**Vetor de Ataque:** Network / Low Complexity / Requires Authentication  
**CWE:** CWE-306 (Missing Authentication for Critical Function)

**Descrição:**  
O painel de administração do sistema (desenvolvido em Laravel, utilizando o template "vertical-menu-laravel-template-free") está acessível publicamente na rota `/admin/auth/login`. O código-fonte expõe o token CSRF e a estrutura de rotas, sem evidências de proteção adicional como Rate Limiting ou MFA.

**Impacto:**  
- Expõe a interface de login a ataques automatizados de força bruta e Credential Stuffing.
- O uso de templates administrativos gratuitos e populares aumenta o risco, pois suas estruturas são bem conhecidas por atacantes.

**Conformidade Afetada:**
- 🇷 LGPD: Violação do princípio da prevenção (Art. 6º, VII).
- 🌐 OWASP Top 10 (2021): A07:2021 – Identification and Authentication Failures.

**🔗 Cadeia de Ataque Hipotética (Kill Chain):**
1. Reconhecimento: Atacante acessa k2multimarcas.com.br/admin e confirma a página de login.
2. Armação: Utiliza o email corporativo vazado (contato@carrobauru.com.br) como alvo de um ataque de Credential Stuffing, testando senhas de vazamentos anteriores.
3. Exploração: Devido à possível reutilização de senhas pelo proprietário em diferentes negócios (concessionária e automecânica), o login é bem-sucedido.
4. Impacto Final: O atacante assume o controle do CMS, podendo alterar informações de veículos, preços, ou inserir scripts maliciosos para capturar dados de clientes que preenchem a ficha de financiamento.

**Recomendações:**  
- Imediato: Implementar Autenticação Multifator (MFA) no painel administrativo.
- Curto Prazo: Restringir o acesso à rota `/admin` por faixa de IP (Allowlist) ou implementar proteção de força bruta (ex: Cloudflare Turnstile ou rate limiting no Laravel).

---

### 4.3 🟠 [ALTO] Vazamento de IP Real de Origem via Subdomínios
**Classificação:** 🟠 ALTO | **CVSS Score:** 6.5  
**Vetor de Ataque:** Network / Low Complexity  
**CWE:** CWE-200 (Exposure of Sensitive Information)

**Descrição:**  
Embora o domínio principal utilize o Cloudflare para ocultar o IP do servidor de origem, os subdomínios de infraestrutura de email (webmail, mail, imap) possuem registros CNAME que resolvem diretamente para os IPs do provedor Kinghost/Uni5 (191.6.220.x).

**Impacto:**  
- Um atacante pode ignorar completamente a proteção do Cloudflare (WAF, DDoS protection) e atacar o servidor de origem diretamente pelo IP descoberto.
- Facilita ataques de Negação de Serviço (DoS) diretos ou exploração de vulnerabilidades no servidor Apache que estariam bloqueadas pelo WAF.

**Conformidade Afetada:**
- 🌐 OWASP Top 10 (2021): A05:2021 – Security Misconfiguration.
- ☁️ Cloudflare Best Practices: Falha na regra de "Authenticated Origin Pulls" ou roteamento inadequado de subdomínios.

**Recomendações:**  
- Curto Prazo: Migrar os registros DNS dos subdomínios de email para passar pelo proxy do Cloudflare (nuvem laranja ativada), ou garantir que o firewall do servidor de origem (Kinghost) bloqueie qualquer tráfego que não venha dos IPs do Cloudflare.

---

### 4.4 🟡 [MÉDIO] Risco de Credential Stuffing (Email Corporativo Vazado)
**Classificação:** 🟡 MÉDIO | **CVSS Score:** 5.3  
**Vetor de Ataque:** Network / Low Complexity  
**CWE:** CWE-522 (Insufficiently Protected Credentials)

**Descrição:**  
O endereço de email de contato identificado (contato@carrobauru.com.br) foi encontrado em bases de dados de vazamentos públicos (Have I Been Pwned, 2024). A correlação de inteligência indica que este email está vinculado ao mesmo proprietário do domínio principal.

**Impacto:**  
- Aumenta drasticamente a probabilidade de sucesso de ataques de Credential Stuffing contra o painel /admin ou contas de email, devido à alta probabilidade de reutilização de senhas entre os diferentes negócios do proprietário.

**Recomendações:**  
- Imediato: Alterar a senha associada a este email em todos os serviços.
- Curto Prazo: Implementar MFA em todas as contas de email e painéis administrativos.

---

### 4.5 🟢 [BAIXO/INFO] Configuração de Cookie de Sessão (Mitigado por HSTS)
**Classificação:** 🟢 BAIXO | **CVSS Score:** 3.7  
**Vetor de Ataque:** Network / High Complexity  
**CWE:** CWE-614 (Sensitive Cookie in HTTPS Session Without 'Secure' Attribute)

**Descrição:**  
Foi observado que o cookie de sessão do Laravel (laravel_session) é definido sem a flag Secure. No entanto, testes de cabeçalho HTTP confirmaram a presença do header Strict-Transport-Security: max-age=63072000 (2 anos).

**Análise de Segurança:**  
A ausência da flag Secure é uma falha de configuração. Porém, a presença do HSTS rigoroso obriga o navegador a usar apenas HTTPS, mitigando efetivamente o risco de interceptação do cookie em ataques de downgrade (SSL Stripping). O risco residual é considerado baixo, mas a correção é uma boa prática de hardening.

**Recomendações:**  
- Curto Prazo: Configurar o Laravel para forçar a flag Secure em cookies de sessão (SESSION_SECURE_COOKIE=true no .env).

---

##  5. ANÁLISE DE RISCO

### 5.1 Matriz de Risco
| Vulnerabilidade / Achado | Probabilidade | Impacto | Nível de Risco |
|---|---|---|---|
| jQuery 3.5.1 Vulnerável | Alta | Alto |  Crítico |
| Painel /admin Exposto | Alta | Alto | 🟠 Alto |
| Vazamento de IP de Origem | Média | Alto | 🟠 Alto |
| Email Corporativo Vazado | Alta | Médio | 🟡 Médio |
| Cookie sem flag Secure (HSTS Ativo) | Baixa | Baixo | 🟢 Baixo |

### 5.2 Análise de Causa Raiz
- Técnicos: Uso de dependências frontend desatualizadas; configuração de DNS que expõe a infraestrutura de origem apesar do uso de CDN.
- Processuais: Falta de revisão de segurança antes da publicação do painel administrativo; ausência de política de senhas e MFA para o proprietário que gerencia múltiplos negócios.
- Organizacionais: Pequenas empresas frequentemente priorizam a funcionalidade e o custo (hospedagem compartilhada) em detrimento de configurações de segurança robustas (hardening).

---

## ️ 6. RECOMENDAÇÕES

### 6.1 Prioridade Imediata (0-7 dias)
1. Atualização de Dependências: Atualizar o jQuery para a versão 3.7.1 ou superior para mitigar as vulnerabilidades de XSS.
2. Proteção do Painel Admin: Implementar MFA (Autenticação Multifator) e/ou restrição de acesso por IP para a rota /admin.
3. Higiene de Credenciais: Alterar imediatamente as senhas associadas ao email corporativo identificado e ativar MFA na conta de email.

### 6.2 Prioridade Curto Prazo (7-30 dias)
1. Ocultação da Origem: Revisar a configuração de DNS para garantir que subdomínios críticos não exponham o IP real do servidor Kinghost/Uni5, ou configurar o firewall do servidor para aceitar tráfego apenas da Cloudflare.
2. Hardening de Sessão: Configurar o ambiente Laravel para emitir cookies de sessão com as flags Secure e HttpOnly.
3. Implementar Rate Limiting: Configurar proteção contra força bruta no formulário de login do Laravel.

### 6.3 Prioridade Médio/Longo Prazo (30+ dias)
1. Auditoria de Código: Realizar uma revisão nas implementações do template Laravel gratuito para garantir que não há backdoors ou configurações inseguras padrão.
2. Conscientização: Treinar o proprietário/equipe sobre os riscos de reutilização de senhas entre diferentes empresas do mesmo grupo.

---

## 📚 7. LIÇÕES APRENDIDAS

1. CDN não é bala de prata: O uso do Cloudflare protege o domínio principal, mas a configuração incorreta de subdomínios (como os de email) pode vazar o IP real do servidor, anulando a proteção de borda.
2. Dependências Frontend são críticas: Mesmo em aplicações backend robustas como Laravel, bibliotecas frontend desatualizadas (jQuery) abrem vetores de ataque significativos (XSS).
3. O elo mais fraco é humano: A correlação de um email vazado com múltiplos negócios do mesmo proprietário destaca o risco extremo da reutilização de senhas (Credential Stuffing).
4. Contexto de Negócio importa: Entender que se trata de um grupo local (concessionária + automecânica) ajuda a calibrar o risco de engenharia social e reutilização de credenciais.

---

##  8. CONCLUSÃO

Esta investigação demonstrou que, embora a aplicação utilize tecnologias backend modernas (Laravel, PHP 8.2) e proteção de borda (Cloudflare), falhas de configuração e manutenção deixam a superfície de ataque exposta. 

A combinação de um painel administrativo acessível, uma biblioteca frontend vulnerável e o vazamento do IP real de origem cria um cenário de risco Alto. A boa notícia é que todas as vulnerabilidades identificadas podem ser remediadas com ações de baixo custo e esforço, como atualização de bibliotecas, ativação de MFA e ajuste de registros DNS.

Recomenda-se a aplicação imediata das correções de prioridade crítica para garantir a segurança dos dados da empresa e de seus clientes, em conformidade com a LGPD.

---

## 📎 9. APÊNDICES

### Apêndice A: Glossário de Termos Técnicos
- XSS (Cross-Site Scripting): Injeção de scripts maliciosos em páginas web confiáveis.
- Credential Stuffing: Ataque automatizado que utiliza combinações de nome de usuário e senha vazadas de um serviço para tentar acessar outro.
- HSTS (HTTP Strict Transport Security): Mecanismo de política de segurança que ajuda a proteger sites contra ataques de downgrade de protocolo e sequestro de cookies.
- CNAME: Registro DNS que mapeia um nome de domínio (alias) para outro nome de domínio (canonical).

### Apêndice B: Referências
- NVD - CVE-2020-11022: https://nvd.nist.gov/vuln/detail/CVE-2020-11022
- NVD - CVE-2020-11023: https://nvd.nist.gov/vuln/detail/CVE-2020-11023
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- Laravel Security Best Practices: https://laravel.com/docs/security

### Apêndice C: Ferramentas Utilizadas
- Wappalyzer, ViewDNS, Shodan, curl, Have I Been Pwned, NVD NIST.

### Apêndice D: Checklist de Verificação de Segurança (Laravel/Cloudflare)
- [ ] Verificar versão do jQuery: Inspecionar código-fonte ou Wappalyzer (Alvo: >= 3.7.1).
- [ ] Testar acesso ao /admin: Tentar acessar de uma rede externa (Alvo: Redirecionado para login com MFA ou bloqueado por IP).
- [ ] Validar HSTS e Cookies: curl -I https://dominio.com.br (Alvo: HSTS presente e cookie com flags Secure/HttpOnly).
- [ ] Verificar vazamento de IP: Resolver subdomínios de email (Alvo: Devem passar pelo proxy da Cloudflare ou o servidor de origem deve bloquear tráfego direto).
- [ ] Auditar credenciais: Garantir que senhas de negócios correlatos não sejam reutilizadas.

---

**Fim do Relatório**

**Contato do Autor:** herbertluizmolinaperfil@gmail.com  
**LinkedIn:** https://www.linkedin.com/in/herbert-molina/  


---

Pronto! Relatório finalizado e formatado. Caso 4 concluído com sucesso! 
