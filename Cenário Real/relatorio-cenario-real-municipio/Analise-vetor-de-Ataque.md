# RELATÓRIO DE ANÁLISE DE VETORES DE ATAQUE (THREAT MODELING)
## Perspectiva Ofensiva: Como um Atacante Exploraria a Infraestrutura do Município

**Autor:** Herbert Molina  
**Data:** 05 de Julho de 2026  
**Classificação:** CONFIDENCIAL (Apenas para fins educacionais e de defesa)  
**Alvo:** Prefeitura Municipal (Cenário 1 - Sistema Conam/vCenter/GLPI)  
**Tipo de Documento:** Simulação de Cadeia de Ataque (Kill Chain) e Análise de Impacto no Setor Público

---

##  AVISO ÉTICO E LEGAL

Este documento foi elaborado **exclusivamente para fins educacionais** e para demonstrar a mentalidade ofensiva (Red Teaming) com o objetivo de fortalecer a defesa de infraestruturas públicas críticas. **Nenhuma das técnicas, comandos ou payloads descritos aqui deve ser executada contra o alvo ou qualquer outro sistema sem autorização explícita, formal e por escrito do gestor público responsável.**

A execução não autorizada configura crime previsto no Art. 154-A do Código Penal Brasileiro (Lei 12.737/2012), agravado quando o alvo é infraestrutura pública essencial (Lei 14.155/2021 - crimes cibernéticos contra infraestrutura crítica).

---

## QUE ESTÁ FALTANDO? (Lacunas de Inteligência)

Com base nos dados coletados até agora sobre a infraestrutura municipal, um atacante experiente (especialmente um *APT* focado em setor público) buscaria ativamente as seguintes peças adicionais:

| Dado Faltante | Por que o Atacante Quer Isso? | Como Obter (Passivo/Semi-Passivo) |
| :--- | :--- | :--- |
| **Versão exata do Conam** | A CVE-2026-44631 (RCE) depende da build específica. | Analisar headers HTTP, rodapé do sistema, ou metadados de PDFs gerados pelo Conam. |
| **Versão do vCenter** | CVEs de *privilege escalation* no vSphere variam por versão (6.5, 6.7, 7.0, 8.0). | Banner do serviço na porta 443, ou análise do certificado SSL do vCenter. |
| **Lista de emails completa** | Os 75 emails do Hunter.io são só a ponta. O atacante quer a lista de *todos* os funcionários (especialmente TI e gabinete). | Combinação de LinkedIn + scraping de Diário Oficial + engenharia social. |
| **Diário Oficial do Município** | Contém nomes de servidores, cargos, salários e contratos de TI (fornecedores, valores). | Busca pública no site da prefeitura ou portais de transparência. |
| **Contratos de Fornecedores de TI** | Saber quem mantém o sistema (Conam, GLPI) revela a cadeia de suprimentos e possíveis vetores de ataque terceirizados. | Portal da Transparência (Lei de Acesso à Informação). |
| **Topologia interna da rede** | Para planejar movimentação lateral após o acesso inicial. | Inferir via traceroute, análise de IPs dos subdomínios, e padrões de nomenclatura. |
| **Credenciais padrão de sistemas municipais** | Muitos municípios usam senhas padrão de fornecedores (ex: `admin/admin` no GLPI, `root/vmware` no vCenter). | Manuais públicos de instalação, fóruns de suporte dos fornecedores. |

---

## COMO UM ATACANTE EXPLORARIA CADA VULNERABILIDADE

Abaixo está a lógica passo a passo de como os dados já coletados seriam *weaponizados* (transformados em armas) contra uma infraestrutura pública.

### RCE no Conam (CVE-2026-44631) - CRÍTICO
**O Dado:** Sistema Conam (usado para NFS-e e protocolo) com vulnerabilidade de Execução Remota de Código.

*   **Como o atacante pensa:** "O Conam é o coração administrativo do município. Ele emite NFS-e, gerencia protocolo e provavelmente tem acesso a dados fiscais. Se eu conseguir RCE aqui, tenho o controle da operação financeira."
*   **Ação de Exploração:**
    1. O atacante identifica a versão do Conam via análise de cookies, headers ou rodapé.
    2. Busca no GitHub/Exploit-DB um PoC (Proof of Concept) público para a CVE-2026-44631.
    3. Envia uma requisição HTTP maliciosa para o endpoint vulnerável (ex: `/conam/api/upload` com payload PHP).
    4. O servidor executa o código PHP enviado, criando uma *web shell* (ex: `shell.php`).
*   **Por que afeta o município:**
    *   **Paralisação da NFS-e:** Empresas locais não conseguem emitir notas, gerando caos econômico.
    *   **Acesso a dados fiscais:** Alíquotas, valores de ISS, informações de contribuintes.
    *   **Ponto de entrada para a rede interna:** A web shell permite escanear a rede municipal a partir de dentro.

### vCenter Exposto Publicamente - CRÍTICO
**O Dado:** VMware vCenter acessível via internet sem MFA.

*   **Como o atacante pensa:** "O vCenter gerencia TODAS as máquinas virtuais do município. Se eu entrar aqui, não preciso hackear cada sistema individualmente - eu controlo o hypervisor."
*   **Ação de Exploração:**
    1. Acessa `https://vcenter.municipio.gov.br` e encontra a tela de login.
    2. Testa credenciais padrão: `administrator@vsphere.local` / `vmware`, `root` / `root`.
    3. Se falhar, usa *Credential Stuffing* com senhas vazadas de outros órgãos públicos (comum em fóruns de hacking).
    4. Se conseguir acesso, tem controle total sobre:
        *   Liga/desliga de VMs (pode derrubar o sistema de protocolo, NFS-e, site da prefeitura).
        *   Clonagem de VMs (copia o servidor de banco de dados para extrair dados offline).
        *   Injeção de ISO maliciosa em VMs (instala backdoor persistente).
*   **Por que afeta o município:**
    *   **Ransomware em escala:** Criptografa todas as VMs de uma vez, paralisando a prefeitura inteira.
    *   **Sequestro de dados:** Copia bancos de dados de saúde (SUS), educação, assistência social.
    *   **Tempo de recuperação:** Sem backup offline, a prefeitura pode ficar semanas sem sistemas.

### phpMyAdmin Exposto - CRÍTICO
**O Dado:** Painel de banco de dados acessível publicamente.

*   **Como o atacante pensa:** "phpMyAdmin é a porta dos fundos para todos os dados do município. Se eu entrar, tenho acesso direto aos bancos do Conam, GLPI, site, etc."
*   **Ação de Exploração:**
    1. Acessa `https://phpmyadmin.municipio.gov.br`.
    2. Testa credenciais padrão: `root` / `root`, `root` / `mysql`, `admin` / `admin`.
    3. Se conseguir acesso, executa queries SQL diretamente:
        ```sql
        -- Listar todos os bancos de dados
        SHOW DATABASES;
        
        -- Extrair usuários e senhas do sistema de protocolo
        SELECT username, password FROM protocolo.users;
        
        -- Exportar dados de contribuintes da NFS-e
        SELECT * FROM nfse.contribuintes INTO OUTFILE '/tmp/dados.csv';
        ```
    4. Usa a função `INTO OUTFILE` para escrever uma web shell no servidor web.
*   **Por que afeta o município:**
    *   **Vazamento de dados pessoais:** CPF, endereço, valor de ISS de todos os contribuintes (LGPD).
    *   **Manipulação de dados:** Alterar valores de notas fiscais, zerar dívidas ativas.
    *   **Destruição de dados:** `DROP DATABASE` em todos os bancos.

### cPanel Exposto (4 painéis) - ALTO
**O Dado:** cPanel, Webmail, WebDisk, CPCalendars acessíveis publicamente.

*   **Como o atacante pensa:** "O cPanel dá controle total sobre a hospedagem. Posso interceptar e-mails do prefeito, modificar o site, criar backdoors."
*   **Ação de Exploração:**
    1. Acessa `https://cpanel.municipio.gov.br:2083`.
    2. Testa credenciais do administrador de TI (obtidas via phishing ou vazamento).
    3. Se conseguir acesso:
        *   **Intercepta e-mails:** Acessa webmail e lê comunicações internas (gabinete, licitações).
        *   **Modifica o site:** Adiciona código malicioso no `index.php` da prefeitura.
        *   **Cria contas de e-mail falsas:** `prefeito@municipio.gov.br` para aplicar golpes em fornecedores.
        *   **Altera registros DNS:** Redireciona o domínio para um servidor controlado pelo atacante (DNS Hijacking).
*   **Por que afeta o município:**
    *   **Golpes contra fornecedores:** E-mails falsos solicitando alteração de dados bancários em licitações.
    *   **Defacement do site:** Pichação do site da prefeitura com mensagens políticas.
    *   **Espionagem:** Interceptação de e-mails de licitações e contratos.

### GLPI Exposto (Sistema de TI) - ALTO
**O Dado:** GLPI (sistema de helpdesk/inventário de TI) acessível.

*   **Como o atacante pensa:** "O GLPI tem o inventário completo da TI do município: IPs internos, nomes de servidores, usuários, senhas em chamados, topologia de rede."
*   **Ação de Exploração:**
    1. Acessa `https://ti.municipio.gov.br` (GLPI).
    2. Testa credenciais padrão: `glpi` / `glpi`, `tech` / `tech`.
    3. Se conseguir acesso, navega pelos chamados de TI:
        *   Encontra senhas de servidores em chamados abertos (ex: "Senha do servidor de backup: admin123").
        *   Vê a topologia completa da rede municipal.
        *   Identifica quais funcionários têm acesso a quais sistemas.
*   **Por que afeta o município:**
    *   **Mapa completo da infraestrutura:** O atacante agora sabe exatamente onde atacar.
    *   **Credenciais expostas:** Senhas de sistemas críticos em chamados de TI.
    *   **Engenharia social aprimorada:** Sabe nomes, cargos e ramais de todos os funcionários de TI.

### 75 Emails Corporativos + Padrão de Nomenclatura - ALTO
**O Dado:** Hunter.io revelou 75 emails com padrão `nome.sobrenome@municipio.gov.br`.

*   **Como o atacante pensa:** "Com 75 emails válidos, posso fazer phishing direcionado (Spear Phishing) contra funcionários específicos, especialmente os de TI e gabinete."
*   **Ação de Exploração:**
    1. Cria uma campanha de phishing direcionada:
        *   **Alvo:** Funcionários de TI (ex: `joao.silva@municipio.gov.br`).
        *   **Assunto:** "Urgente: Atualização de segurança do sistema Conam - Ação necessária".
        *   **Corpo:** "Prezado João, identificamos uma vulnerabilidade crítica no Conam. Por favor, acesse o link abaixo para aplicar o patch: [link falso para página de login clonada]".
    2. Quando o funcionário clica e digita a senha, o atacante captura as credenciais.
    3. Usa as credenciais para acessar o sistema real (Conam, GLPI, cPanel).
*   **Por que afeta o município:**
    *   **Funcionários públicos são alvos fáceis:** Muitos não têm treinamento em segurança.
    *   **Acesso a sistemas internos:** Uma credencial comprometida pode dar acesso a múltiplos sistemas (SSO).
    *   **Golpes financeiros:** Phishing contra o setor financeiro para desviar verbas públicas.

---

## CADEIA DE ATAQUE HIPOTÉTICA (KILL CHAIN)

Como um atacante sofisticado (ex: grupo de ransomware focado em setor público) combinaria essas falhas para um comprometimento total da prefeitura:

### Fase 1: Reconhecimento (1-3 dias)
```
✓ Mapeia todos os subdomínios via crt.sh e Shodan
✓ Identifica: Conam, vCenter, phpMyAdmin, cPanel, GLPI expostos
✓ Coleta 75 emails via Hunter.io
✓ Baixa Diário Oficial para mapear funcionários e contratos de TI
✓ Identifica que o município usa Conam para NFS-e (fornecedor conhecido)
```

### Fase 2: Armação (1 dia)
```
✓ Prepara campanha de Spear Phishing contra 5 funcionários de TI
✓ Clona a página de login do Conam em servidor próprio
✓ Prepara exploit da CVE-2026-44631 (RCE) como backup
✓ Cria lista de senhas comuns de municípios (admin123, municipio2024, etc.)
```

### Fase 3: Entrega (Dia 1 do ataque)
```
1. Envia e-mails de phishing para joao.silva@, maria.santos@ (TI)
2. Simultaneamente, testa credenciais padrão no vCenter e phpMyAdmin
3. Monitora qual vetor funciona primeiro
```

### Fase 4: Exploração (Dia 1-2)
```
Cenário A (Phishing bem-sucedido):
- Funcionário de TI clica no link e digita credenciais
- Atacante captura: usuario.ti / Senha@2024
- Usa essas credenciais no GLPI (reutilização de senha)
- Dentro do GLPI, encontra senhas de servidores em chamados abertos

Cenário B (vCenter com senha padrão):
- Atacante acessa vCenter com administrator@vsphere.local / vmware
- Clona a VM do banco de dados do Conam
- Extrai offline todos os dados de contribuintes
```

### Fase 5: Escalação (Dia 2-3)
```
1. A partir do GLPI, mapeia toda a rede interna (192.168.x.x)
2. Identifica o servidor de backup (onde estão os backups dos últimos 6 meses)
3. Acessa o cPanel e intercepta e-mails do gabinete do prefeito
4. Encontra no e-mail: "Precisamos aprovar a licitação de R$ 2 milhões até sexta"
```

### Fase 6: Ações sobre Objetivos (Dia 3-5)
```
OPÇÃO 1 - RANSOMWARE (mais comum em setor público):
- Criptografa todas as VMs via vCenter
- Deixa nota de resgate: "Paguem 50 BTC ou perdemos os dados de 50.000 cidadãos"
- Paralisa: NFS-e, protocolo, site, e-mail, sistemas de saúde e educação

OPÇÃO 2 - ESPIONAGEM/FRAUDE:
- Intercepta e-mails de licitações por 3 meses
- Envia e-mails falsos para fornecedores alterando dados bancários
- Desvia R$ 500.000 de pagamentos de contratos públicos

OPÇÃO 3 - VAZAMENTO DE DADOS (hacktivismo):
- Extrai banco completo de contribuintes (CPF, endereço, dívidas)
- Vaza na darkweb ou envia para a imprensa
- Expõe dados de saúde (SUS) de cidadãos
```

---

## IMPACTO REAL NO MUNICÍPIO (SETOR PÚBLICO)

### Impacto Social e Operacional

| Cenário | Consequência para o Cidadão |
| :--- | :--- |
| **Paralisação da NFS-e** | Empresas locais não emitem notas, comércio para, arrecadação de ISS cai 70% |
| **Sistema de Protocolo fora** | Cidadãos não abrem processos, não acompanham requerimentos, serviços travam |
| **Dados de saúde vazados** | Exames, diagnósticos, tratamentos de pacientes do SUS expostos publicamente |
| **Site da prefeitura defaced** | População perde acesso a informações oficiais, boatos se espalham |
| **E-mails interceptados** | Licitações fraudadas, contratos direcionados, prejuízo ao erário |

### Impacto Financeiro e Legal

| Tipo de Impacto | Estimativa |
| :--- | :--- |
| **Ransomware (resgate)** | R$ 500.000 a R$ 5.000.000 (valores comuns em prefeituras) |
| **Multas LGPD (ANPD)** | Até R$ 50 milhões por infração (vazamento de dados de cidadãos) |
| **TCU/TCE (responsabilização)** | Gestores podem responder por improbidade administrativa |
| **Recuperação de sistemas** | R$ 200.000 a R$ 1.000.000 (contratação emergencial de empresa de TI) |
| **Ações judiciais de cidadãos** | Indenizações por vazamento de dados pessoais |
| **Perda de repasse federal** | Convênios suspensos por irregularidades |

### Impacto Político e Reputacional

- **Manchetes nacionais:** "Prefeitura de [cidade] tem dados de 100.000 cidadãos vazados"
- **Perda de confiança:** População não acredita mais em serviços digitais do município
- **Investigação do MP:** Ministério Público abre inquérito sobre negligência na segurança
- **Cassação de mandato:** Em casos graves, vereador/prefeito pode perder o cargo por improbidade

---

## COMO SE PROTEGER (Resposta Defensiva para Setor Público)

### Prioridade Imediata (0-24 horas) - "Estancar o Sangramento"

1. **Remover sistemas críticos da internet:**
   - vCenter, phpMyAdmin, GLPI **NÃO** devem estar acessíveis publicamente
   - Mover para VPN ou rede interna
   - *Justificativa:* Nenhum desses sistemas precisa de acesso público

2. **Alterar todas as senhas padrão:**
   - vCenter: `administrator@vsphere.local`
   - phpMyAdmin: `root`
   - GLPI: `glpi`, `tech`, `normal`
   - cPanel: senha do administrador
   - *Justificativa:* Senhas padrão são o vetor #1 de ataques a órgãos públicos

3. **Ativar MFA (Autenticação Multifator):**
   - Em todos os painéis administrativos
   - Especialmente no vCenter e cPanel
   - *Justificativa:* MFA bloqueia 99% dos ataques de credential stuffing

### Prioridade Curto Prazo (1-7 dias)

1. **Atualizar o Conam:**
   - Aplicar patch da CVE-2026-44631 imediatamente
   - Coordenar com o fornecedor (Conam) para atualização
   - *Justificativa:* RCE em sistema de NFS-e é risco crítico

2. **Segmentar a rede:**
   - Separar rede administrativa (TI, gabinete) da rede de servidores
   - Implementar firewall interno entre VLANs
   - *Justificativa:* Contém movimentação lateral em caso de invasão

3. **Auditar logs de acesso:**
   - Verificar se há acessos suspeitos nos últimos 30 dias
   - Buscar por logins em horários incomuns (madrugada, fins de semana)
   - *Justificativa:* Pode indicar que o atacante já está dentro

### Prioridade Médio Prazo (7-30 dias)

1. **Implementar monitoramento contínuo:**
   - SIEM (Security Information and Event Management) para correlacionar logs
   - Alertas para tentativas de login falhas em sistemas críticos
   - *Justificativa:* Detecta ataques em andamento, não só depois

2. **Treinamento de conscientização:**
   - Todos os funcionários de TI e gabinete
   - Foco em phishing e engenharia social
   - *Justificativa:* O elo mais fraco é humano, não tecnológico

3. **Plano de resposta a incidentes:**
   - Documento formal com passos a seguir em caso de invasão
   - Contatos de emergência (PF, ANPD, empresa de forense)
   - *Justificativa:* Prefeitura precisa saber o que fazer ANTES do incidente

### Prioridade Longo Prazo (30+ dias)

1. **Contratação de pentest anual:**
   - Teste de intrusão autorizado por empresa especializada
   - Relatório detalhado com recomendações
   - *Justificativa:* Lei Geral de Proteção de Dados exige medidas técnicas adequadas

2. **Certificação ISO 27001:**
   - Implementar Sistema de Gestão de Segurança da Informação
   - *Justificativa:* Boa prática para órgãos públicos, reduz risco de responsabilização

3. **Backup offline e imutável:**
   - Backups em mídia desconectada da rede (fitas, HDs externos)
   - Testar restauração trimestralmente
   - *Justificativa:* Única defesa real contra ransomware

---

## MATRIZ DE PROBABILIDADE VS IMPACTO (Setor Público)

| Vetor de Ataque | Probabilidade | Impacto | Prioridade |
| :--- | :--- | :--- | :--- |
| vCenter com senha padrão | **Muito Alta** (comum em municípios) | **Crítico** (controle total) | 🔴 Imediata |
| RCE no Conam (CVE-2026-44631) | **Alta** (exploit público) | **Crítico** (NFS-e paralisada) | 🔴 Imediata |
| phpMyAdmin exposto | **Alta** (senha fraca) | **Crítico** (todos os bancos) | 🔴 Imediata |
| Spear Phishing via emails vazados | **Alta** (75 emails válidos) | **Alto** (acesso inicial) | 🟠 Alta |
| cPanel interceptando e-mails | **Média** (requer acesso) | **Alto** (espionagem/golpes) | 🟠 Alta |
| GLPI com inventário exposto | **Média** (senha padrão) | **Alto** (mapa da rede) | 🟠 Alta |

---

## Perspectiva do Atacante

### O Que um Atacante Real Faria Contra Este Município

Um grupo de ransomware focado em setor público **não precisaria de sofisticação técnica**. A combinação de:

1. **Sistemas críticos expostos** (vCenter, phpMyAdmin, Conam)
2. **Senhas padrão ou fracas** (prática comum em municípios)
3. **Falta de MFA** (ausência de segunda barreira)
4. **Funcionários sem treinamento** (alvos fáceis de phishing)

...cria um cenário onde o atacante pode comprometer **toda a infraestrutura municipal em menos de 72 horas**, com ferramentas públicas e conhecimento básico.

### Por Que Isso É Ainda Mais Grave no Setor Público

- **Dados sensíveis em escala:** CPF, endereço, saúde, finanças de **todos os cidadãos**
- **Serviços essenciais:** Saúde (SUS), educação, assistência social podem parar
- **Recursos limitados:** Municípios pequenos não têm equipe de TI dedicada 24/7
- **Responsabilização pessoal:** Gestores podem responder criminalmente por negligência
- **Impacto social:** Cidadãos mais vulneráveis (idosos, baixa renda) são os mais afetados por paralisação de serviços

### A Boa Notícia

**80% das vulnerabilidades identificadas podem ser corrigidas em 24 horas:**
- Remover vCenter/phpMyAdmin/GLPI da internet: **30 minutos**
- Alterar senhas padrão: **1 hora**
- Ativar MFA: **2 horas**
- Aplicar patch do Conam: **4 horas** (com fornecedor)

**O custo dessas correções é próximo de zero** (apenas tempo da equipe de TI). O custo de **NÃO** corrigir pode ser a **paralisação total do município** por semanas, com prejuízos de milhões e responsabilização criminal dos gestores.

---

## RECURSOS PARA DEFENSORES (Setor Público)

### Para Gestores Públicos:
- **Cartilha de Segurança para Órgãos Públicos:** https://www.gov.br/gsi/pt-br/assuntos/noticias/cartilha-de-seguranca
- **LGPD no Setor Público:** https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-publica-guia-orientativo-para-orgaos-publicos
- **Acórdão TCU 2638/2021:** Determina gestão de vulnerabilidades em órgãos públicos

### Para Equipes de TI Municipais:
- **Centro de Estudos, Resposta e Tratamento de Incidentes de Segurança no Brasil (CERT.br):** https://www.cert.br/
- **Guia de Hardening para Servidores Públicos:** https://www.gov.br/gsi/pt-br/assuntos/publicacoes
- **Framework de Segurança para Governo (NIST CSF):** https://www.nist.gov/cyberframework

### Para Denúncias de Incidentes:
- **Polícia Federal (Divisão de Crimes Cibernéticos):** https://www.gov.br/pf/pt-br
- **ANPD (Autoridade Nacional de Proteção de Dados):** https://www.gov.br/anpd/pt-br
- **CERT.br (Reportar Incidentes):** https://www.cert.br/site/report/

---

**Fim do Relatório de Análise de Vetores de Ataque - Caso 1 (Sistema Municipal)**

**Contato do Autor:** herbertluizmolinaperfil@gmail.com  
**LinkedIn:** https://www.linkedin.com/in/herbert-molina/

---
