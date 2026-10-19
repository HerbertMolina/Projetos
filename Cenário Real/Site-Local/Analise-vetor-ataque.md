# ANÁLISE DE VETORES DE ATAQUE (THREAT MODELING)

## Perspectiva Ofensiva: Como um Atacante Exploraria a Infraestrutura de um Comércio/Serviço (WordPress/cPanel)

**Autor:** Herbert Molina

**Classificação:** CONFIDENCIAL (Apenas para fins educacionais e de defesa)

**Alvo:** Comércio/Serviços Local (Cenário 2 - WordPress, Elementor, cPanel)

**Tipo de Documento:** Simulação de Cadeia de Ataque (Kill Chain) e Análise de Impacto no Setor Privado

---

## AVISO ÉTICO E LEGAL

Este documento foi elaborado **exclusivamente para fins educacionais** e para demonstrar a mentalidade ofensiva (Red Teaming) com o objetivo de fortalecer a defesa de infraestruturas comerciais. **Nenhuma das técnicas, comandos ou payloads descritos aqui deve ser executada contra o alvo ou qualquer outro sistema sem autorização explícita, formal e por escrito do gestor responsável.**

A execução não autorizada configura crime previsto no Art. 154-A do Código Penal Brasileiro (Lei 12.737/2012), além de possíveis infrações civis e trabalhistas.

---

## O QUE ESTÁ FALTANDO? (Lacunas de Inteligência)

Com base nos dados coletados até agora sobre a infraestrutura do comércio, um atacante (ou, mais comumente, um *botnet* automatizado) buscaria ativamente as seguintes peças adicionais para refinar o ataque:

| Dado Faltante | Por que o Atacante Quer Isso? | Como Obter (Passivo/Semi-Passivo) |
| --- | --- | --- |
| **Versão exata do WordPress e Plugins** | CVEs específicas (ex: falhas no Elementor ou WooCommerce) dependem da versão exata. | Ler o arquivo `readme.html`, rodapé do site, ou analisar o código-fonte de scripts CSS/JS. |
| **Nome de usuário do cPanel** | Em hospedagens compartilhadas, o usuário do cPanel é frequentemente os primeiros 8 caracteres do domínio (ex: `dominio1`). | Inferência via padrões da hospedagem (Hostgator, Locaweb, etc.) ou vazamentos antigos. |
| **Arquivos de Backup (.sql, .zip, .bak)** | Desenvolvedores frequentemente deixam backups do site ou do banco de dados na raiz do servidor. | Ferramentas de fuzzing de diretórios (ex: Gobuster, Dirb) buscando por `backup.zip`, `site.sql`, `wp-config.bak`. |
| **Perfis de Funcionários no LinkedIn** | Para criar ataques de *Spear Phishing* ou *Vishing* (ligação telefônica) convincentes. | Busca manual no LinkedIn filtrando por "Cargo" + "Nome da Empresa". |
| **Histórico de WHOIS** | Para encontrar e-mails pessoais antigos dos donos que possam ter senhas reutilizadas. | ViewDNS ou DomainTools (Histórico de WHOIS). |

---

## COMO UM ATACANTE EXPLORARIA CADA VULNERABILIDADE

Abaixo está a lógica passo a passo de como os dados já coletados seriam *weaponizados* (transformados em vetores de ataque) contra este comércio.

### Enumeração de Usuários via API REST - ALTO

**O Dado:** A API `/wp-json/wp/v2/users` retorna a lista de todos os usuários (slugs) do WordPress.

- **Como o atacante pensa:** "Metade da batalha de um ataque de força bruta é saber o nome de usuário correto. O WordPress me deu isso de bandeja."
- **Ação de Exploração:**
    1. O atacante acessa a URL da API e salva a lista de usuários (ex: `admin`, `joao.silva`, `financeiro`).
    2. Usa uma ferramenta como `WPScan` ou um script Python para realizar *Credential Stuffing* (testar milhares de senhas vazadas de outros sites) especificamente contra esses usuários válidos no `wp-login.php`.
    3. Alternativamente, envia um e-mail de *Phishing* direcionado: "Olá João, detectamos um login suspeito no site. Clique aqui para redefinir sua senha".
- **Por que afeta o comércio:**
    - Reduz drasticamente o tempo e o "ruído" de um ataque de força bruta.
    - Facilita a tomada de controle da conta de um administrador ou do setor financeiro.

### phpMyAdmin Exposto Publicamente - CRÍTICO

**O Dado:** Painel de gerenciamento de banco de dados acessível diretamente pela internet.

- **Como o atacante pensa:** "Se eu entrar aqui, não preciso hackear o WordPress. Eu tenho acesso direto e bruto a TODOS os dados: clientes, pedidos, senhas (hash) e configurações."
- **Ação de Exploração:**
    1. Acessa a URL do phpMyAdmin.
    2. Testa credenciais padrão ou óbvias: `root` / `root`, `root` / `mysql`, `admin` / `admin`, ou o nome do domínio como senha.
    3. Se conseguir acesso, executa comandos SQL diretos:
        
        ```sql
        -- Roubar todos os e-mails e telefones de clientes
        SELECT user_email, meta_value FROM wp_users JOIN wp_usermeta ON wp_users.ID = wp_usermeta.user_id;
        
        -- Alterar a senha do administrador do WordPress diretamente no banco
        UPDATE wp_users SET user_pass = MD5('NovaSenha123') WHERE user_login = 'admin';
        ```
        
- **Por que afeta o comércio:**
    - **Vazamento em massa de dados (LGPD):** Nomes, e-mails, telefones e endereços de clientes expostos.
    - **Sequestro do site:** O atacante pode criar um novo usuário administrador em segundos, mesmo que o dono mude a senha pelo painel do WordPress.

### cPanel e Subdomínios de Gerenciamento Expostos - ALTO

**O Dado:** `cpanel`, `webmail`, `webdisk` acessíveis sem restrição de IP ou MFA.

- **Como o atacante pensa:** "O cPanel é o 'Deus' da hospedagem. Com ele, eu controlo os arquivos, os e-mails e o DNS. O WordPress é apenas um detalhe."
- **Ação de Exploração:**
    1. Realiza ataque de força bruta na porta 2083 (cPanel) ou 2096 (Webmail).
    2. Ao obter acesso, abre o **Gerenciador de Arquivos**.
    3. Edita o arquivo `wp-config.php` para inserir suas próprias credenciais de banco de dados, ou adiciona um código malicioso (backdoor) no arquivo `functions.php` do tema ativo.
    4. Acessa o Webmail para ler e-mails internos ou criar regras de encaminhamento para interceptar comunicações com clientes.
- **Por que afeta o comércio:**
    - **Controle total do domínio:** O atacante pode alterar os registros DNS, apontando o site para uma página de *phishing* ou pornografia (Defacement).
    - **Golpes em clientes:** O atacante envia e-mails a partir do domínio legítimo (`contato@empresa.com.br`) cobrando "atualização de dados bancários" dos clientes.

### WP_DEBUG Ativo (Information Disclosure) - MÉDIO/ALTO

**O Dado:** O modo de depuração do WordPress está ativo, exibindo erros detalhados na tela.

- **Como o atacante pensa:** "O site está me dizendo exatamente como ele funciona por dentro e onde ele falha."
- **Ação de Exploração:**
    1. O atacante insere um caractere especial (ex: `'` ou `"<script>"`) em campos de busca, formulários de contato ou parâmetros de URL.
    2. O site quebra e exibe um erro fatal do PHP ou do MySQL, revelando:
        - O caminho absoluto do servidor (ex: `/home/usuario/public_html/...`).
        - Nomes de tabelas do banco de dados.
        - Trechos da *query* SQL que falhou.
    3. O atacante usa essas informações para montar um ataque de **SQL Injection (SQLi)** preciso, sabendo exatamente o nome das colunas e tabelas para extrair dados.
- **Por que afeta o comércio:**
    - Transforma uma falha genérica em um ataque direcionado e bem-sucedido.
    - Expõe a lógica interna do sistema, facilitando a exploração de outras vulnerabilidades.

---

## CADEIA DE ATAQUE HIPOTÉTICA (KILL CHAIN)

Como um atacante (ou um bot automatizado) combinaria essas falhas para comprometer o negócio:

### Fase 1: Reconhecimento (Automatizado - Minutos)

```
✓ Bot varre a internet procurando por portas 2083 (cPanel) e /wp-json/
✓ Identifica o alvo e confirma: WordPress ativo, cPanel aberto, phpMyAdmin acessível.
✓ Extrai a lista de usuários via API REST (ex: 'admin', 'gerente').
✓ Testa inserção de aspas simples (') no formulário de busca e confirma que o WP_DEBUG está ativo, revelando o caminho do servidor.
```

### Fase 2: Armação (Automatizado - Segundos)

```
✓ O bot carrega uma lista de 10.000 senhas comuns (ex: 123456, nome_da_empresa2024, admin123).
✓ Prepara o payload de SQL Injection baseado nos nomes de tabela revelados pelo erro do WP_DEBUG.
```

### Fase 3: Entrega e Exploração (Minutos)

```
Cenário A (Força Bruta no cPanel - Mais Provável):
- O bot testa as 10.000 senhas no cPanel.
- Encontra a senha fraca do proprietário.
- Faz login no cPanel com sucesso.

Cenário B (Enumeração + Phishing):
- Atacante humano vê o usuário 'gerente' na API REST.
- Envia e-mail: "Prezado Gerente, seu acesso ao site expirou. Clique aqui para renovar: [link falso]".
- Gerente clica e digita a senha. Atacante a captura.
```

### Fase 4: Escalação e Persistência (Horas)

```
1. A partir do cPanel, o atacante abre o Gerenciador de Arquivos.
2. Edita o arquivo index.php ou functions.php do tema, inserindo um script JavaScript que redireciona 10% dos visitantes para um site de phishing de bancos.
3. Acessa o phpMyAdmin (cuja senha ele agora sabe, pois está no wp-config.php) e faz um dump (cópia) completo da tabela de clientes.
4. Cria um novo usuário WordPress oculto como "backup_admin" com privilégios de Administrador.
```

### Fase 5: Ações sobre Objetivos (Dias/Semanas)

```
OPÇÃO 1 - RANSOMWARE DE DADOS:
- Criptografa todos os arquivos da pasta public_html via cPanel.
- Deixa um arquivo LEIA-ME.txt exigindo R$ 5.000,00 em Bitcoin para devolver o site.

OPÇÃO 2 - FRAUDE E VENDA DE DADOS:
- Vende a lista de clientes (nome, telefone, e-mail, histórico de compras) para grupos de spam ou golpistas.
- Usa o e-mail corporativo para aplicar golpes nos fornecedores da empresa.

OPÇÃO 3 - SEO SPAM (Invisível):
- O site continua no ar, mas o atacante injeta milhares de páginas ocultas sobre "comprar remédios" ou "apostas".
- O Google indexa essas páginas. O site do comércio perde todo o ranking orgânico e é marcado como "Perigoso" pelo Google Safe Browsing.
```

---

## IMPACTO REAL NO COMÉRCIO

### Impacto Operacional e Reputacional

| Cenário | Consequência para o Negócio |
| --- | --- |
| **Site Marcado como Perigoso** | O Google Chrome exibe uma tela vermelha de alerta para qualquer cliente que tentar acessar. As vendas/caem para zero imediatamente. |
| **E-mails Comprometidos** | Clientes recebem cobranças falsas vindas do e-mail oficial da empresa. A confiança na marca é destruída. |
| **Perda de Ranking (SEO)** | Se o site for usado para *SEO Spam*, pode levar meses ou anos para recuperar a posição nas buscas do Google, mesmo após a limpeza. |

### Impacto Financeiro e Legal

| Tipo de Impacto | Estimativa / Consequência |
| --- | --- |
| **Multas e Processos (LGPD)** | Vazamento de dados de clientes pode gerar multas da ANPD e ações judiciais individuais por danos morais. |
| **Custo de Recuperação** | Contratação emergencial de especialista em segurança para limpar o site, remover backdoors e restaurar backups (R$ 2.000 a R$ 10.000+). |
| **Perda de Faturamento** | Dias ou semanas com o site fora do ar ou sem credibilidade, resultando em perda direta de vendas e orçamentos. |
| **Resgate (Ransomware)** | Se os arquivos forem criptografados, o valor pedido pode variar, mas o custo real inclui o tempo de inatividade, mesmo que se pague o resgate (o que não garante a recuperação). |

---

## COMO SE PROTEGER (Resposta Defensiva)

### Prioridade Imediata (0-24 horas) - "Estancar o Sangramento"

1. **Desativar o WP_DEBUG:** Editar o arquivo `wp-config.php` e garantir que `define('WP_DEBUG', false);` e `define('WP_DEBUG_DISPLAY', false);` estejam definidos.
2. **Restringir Acesso ao cPanel e phpMyAdmin:** Configurar o firewall da hospedagem para permitir acesso a essas ferramentas **apenas** a partir do endereço IP fixo da empresa ou do administrador.
3. **Alterar Senhas:** Mudar imediatamente a senha do cPanel, do e-mail principal e do administrador do WordPress para uma senha forte e única (16+ caracteres).

### Prioridade Curto Prazo (1-7 dias)

1. **Ocultar a API REST de Usuários:** Instalar um plugin de segurança (ex: Wordfence, Solid Security) para desativar a enumeração de usuários via `/wp-json/wp/v2/users`.
2. **Ativar MFA (Autenticação de Dois Fatores):** Obrigatório para o login no WordPress e, crucialmente, para o acesso ao cPanel.
3. **Verificar Integridade dos Arquivos:** Usar um plugin para escanear o site em busca de arquivos modificados ou backdoors já existentes.

### Prioridade Médio Prazo (7-30 dias)

1. **Migrar para Hospedagem Gerenciada:** Sair de hospedagens compartilhadas genéricas que expõem o cPanel. Migrar para um serviço de "Hospedagem WordPress Gerenciada" (ex: Hostinger Cloud, Kinsta, WP Engine), onde o painel administrativo é isolado e o endurecimento (hardening) do servidor é feito pelo provedor.
2. **Implementar Backups Off-site:** Configurar backups diários que são enviados para um local externo (ex: Google Drive, AWS S3), não apenas no mesmo servidor do site.

### Prioridade Longo Prazo (30+ dias)

1. **Política de Senhas e Treinamento:** Garantir que todos os funcionários com acesso ao site usem gerenciadores de senhas (ex: Bitwarden, 1Password) e saibam identificar e-mails de *phishing*.
2. **Monitoramento de Segurança:** Assinar um serviço que monitore a integridade do site e avise imediatamente se arquivos forem alterados ou se o site for listado no Google Safe Browsing.

---

## MATRIZ DE PROBABILIDADE VS IMPACTO

| Vetor de Ataque | Probabilidade | Impacto | Prioridade |
| --- | --- | --- | --- |
| **Força Bruta no cPanel/phpMyAdmin** | **Muito Alta** (alvo constante de bots) | **Crítico** (controle total do servidor) | Imediata |
| **Enumeração de Usuários + Phishing** | **Alta** (fácil de executar) | **Alto** (acesso ao painel do site) | Alta |
| **Exploração via WP_DEBUG (SQLi)** | **Média** (requer interação manual) | **Alto** (roubo de banco de dados) | Alta |
| **Vazamento de Dados (LGPD)** | **Média** (consequência dos itens acima) | **Crítico** (multas e processos) | Imediata |

---

## PERSPECTIVA DO ATACANTE

### O Que um Atacante Real Faria Contra Este Comércio

Ao contrário de grandes corporações, pequenos e médios comércios **não são atacados por hackers sofisticados sentados em um quarto escuro**. Eles são atacados por **botnets automatizadas** que varrem a internet 24 horas por dia, 7 dias por semana, procurando por portas abertas (cPanel), painéis de login sem proteção (WordPress) e configurações erradas (WP_DEBUG).

É um jogo de números: o bot testa 10.000 sites por hora. Se 9.999 estiverem seguros, mas **um** tiver o cPanel com a senha "123456" ou o `WP_DEBUG` ativo, esse único site é comprometido.

### Por Que Isso É Grave para o Negócio

- **O custo da prevenção é baixo:** Um plugin de segurança, uma senha forte e o bloqueio de IP do cPanel custam **zero reais** e alguns minutos de configuração.
- **O custo da cura é altíssimo:** Recuperar a reputação da marca, pagar um especialista para limpar o site e lidar com clientes insatisfeis ou processos da LGPD pode custar milhares de reais e, em alguns casos, levar ao fechamento do negócio.

---

## RECURSOS PARA DEFENSORES

### Para o Proprietário/Gestor:

- **Guia Básico de Segurança para Sites WordPress:** https://wordpress.org/documentation/article/hardening-wordpress/
- **Cartilha de Segurança para Pequenos Negócios (CERT.br):** https://www.cert.br/cartilhas/

### Para a Equipe de TI/Desenvolvimento:

- **Wordfence / Solid Security:** Plugins essenciais para *hardening* do WordPress.
- **NIST Cybersecurity Framework (CSF):** Para entender as boas práticas de proteger, detectar e responder a incidentes.
- **Ferramenta de Verificação de Cabeçalhos:** https://securityheaders.com/ (para garantir que HSTS, CSP, etc., estejam ativos).

---

**Fim do Relatório de Análise de Vetores de Ataque - Caso 2 (WordPress/cPanel)**

**Contato do Autor:** herbertluizmolinaperfil@gmail.com

**LinkedIn:** https://www.linkedin.com/in/herbert-molina/
