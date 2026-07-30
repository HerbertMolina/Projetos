# Content Discovery - TryHackMe

## 📊 Info  
- Dificuldade: Fácil  
- Categoria: Web Security / Content Discovery  
- Data: 31/07/2026  
- Link: `https://tryhackme.com/room/contentdiscoveryx`    

## 🔍 Resumo  
Descobrindo conteúdos ocultos na Web utilizando técnicas manuais, OSINT e ferramentas de enumeração automatizada como o Gobuster, mapeando a superfície de ataque de uma aplicação.

## 🛠️ Processo  

### 🔵 **Task 2: Descoberta manual - Ficheiros comuns**

Introdução e verificação manual de arquivos convencionais expostos por servidores web, que frequentemente revelam muito mais do que o pretendido e devem ser o primeiro passo em qualquer engajamento de descoberta de conteúdo.

Conceitos explorados:  
**robots.txt:** Arquivo que orienta os crawlers de mecanismos de busca sobre quais páginas podem ser indexadas. Proprietários de sites muitas vezes listam diretórios sensíveis aqui para evitar que apareçam nos resultados de pesquisa, criando uma "lista pronta" de locais interessantes para testadores de penetração. É importante notar que isso é apenas uma diretriz, não um controle de segurança.  
**sitemap.xml:** Arquivo que informa aos mecanismos de busca quais páginas o proprietário deseja que sejam listadas. Frequentemente inclui páginas de staging, conteúdo antigo ou URLs difíceis de alcançar pela navegação normal, revelando endpoints sensíveis ou parâmetros de entrada valiosos para o reconhecimento.  
**Mapeamento da Superfície de Ataque:** Uso de arquivos de configuração padrão para identificar caminhos ocultos (como portais de login ou áreas administrativas) que não seriam facilmente descobertos apenas navegando pelo site.

- **Pergunta:** Qual é o diretório no ficheiro robots.txt cujo acesso não é permitido aos rastreadores da Web?  
**Resposta:** '/staff-portal'  
***Nota: O texto da tarefa menciona explicitamente que o arquivo robots.txt "asks them not to visit /staff-portal", indicando que este é o diretório restrito para crawlers.***

- **Pergunta:** Qual é o caminho da área secreta que se encontra no ficheiro sitemap.xml?  
**Resposta:** '/s3cr3t-area'  
***Nota: A descrição do sitemap.xml destaca que ele revela caminhos sensíveis ou interessantes, citando especificamente "/customers/login" e "/s3cr3t-area" como exemplos de áreas ocultas mapeadas no arquivo.***

### 🔵 **Task 3: Descoberta manual - Cabeçalhos e pilha de frameworksk**

O foco é demonstrar como os cabeçalhos de resposta HTTP e o código-fonte da página podem revelar detalhes técnicos valiosos sobre a pilha de tecnologia (framework stack) do servidor, além de esconder pistas ou flags intencionais.

Conceitos explorados:  
**Análise de Cabeçalhos HTTP:** Uso de ferramentas como `curl -v` para inspecionar cabeçalhos de resposta (ex: `Server`, `X-Powered-By`), que frequentemente expõem o software do servidor web e a linguagem ou framework da aplicação.  
**Custom Headers (X-FLAG):** Cabeçalhos personalizados que, em ambientes de CTF, podem ser usados intencionalmente para esconder flags ou informações de depuração que não deveriam estar visíveis em produção.  
**Identificação de Framework:** Busca por pistas no código-fonte HTML, como comentários de rodapé, avisos de direitos autorais ou ícones (favicon), para identificar a tecnologia subjacente (ex: "THM Framework v1.2").  
**Exploração de Documentação e Credenciais Padrão:** Uma vez identificado o framework, consultar sua documentação oficial para descobrir estruturas de diretórios padrão (como o caminho do portal de administração) e testar credenciais padrão (ex: `admin`/`admin`) para obter acesso não autorizado.

- **Pergunta:** Qual é o valor do sinalizador do cabeçalho X-FLAG?  
**Resposta:** 'THM{HEADER_FLAG}'  
***Nota: Ao executar `curl -v http://MACHINE_IP`, a saída detalhada dos cabeçalhos de resposta revela um cabeçalho personalizado `X-FLAG` contendo a flag do desafio.***

- **Pergunta:** O que significa o indicador no portal de administração do framework?  
**Resposta:** 'THM{CHANGE_DEFAULT_CREDENTIALS}'  
***Nota: O comentário no rodapé do código-fonte aponta para a documentação do "THM Framework". Ao consultar essa documentação, descobre-se o caminho do portal de administração. Acessando esse caminho no site alvo e fazendo login com as credenciais padrão (admin/admin), a flag é exibida no painel.***

### 🔵 **Task 4: OSINT - Motores de busca e ferramentas da Web**

O foco é introduzir recursos externos de Inteligência de Fontes Abertas (OSINT) que auxiliam na descoberta de informações sobre um site alvo.

Conceitos explorados:  
**Google Hacking / Dorking:** Técnica que utiliza operadores de busca avançada do Google para filtrar resultados e revelar conteúdo sensível indexado (como painéis de administração, documentos vazados e páginas de login) que o proprietário do site não pretendia tornar público. Operadores comuns incluem `site:`, `inurl:`, `filetype:`, `intitle:`, `intext:` e `cache:`.  
**Wappalyzer:** Extensão de navegador e ferramenta online que identifica automaticamente a pilha de tecnologias de um site, incluindo frameworks, plataformas, CDNs, ferramentas de análise e processadores de pagamento. É valiosa por frequentemente detectar números de versão, facilitando a busca por vulnerabilidades conhecidas (CVEs).  
**Combinação de Operadores:** Capacidade de unir múltiplos filtros em uma única consulta (ex: `site:tryhackme.com filetype:pdf`) para refinar drasticamente os resultados da pesquisa.

- **Pergunta:** Qual é o operador «dork» do Google que limita os resultados a um site específico?  
**Resposta:** 'site:'  
***Nota: O operador `site:` restringe os resultados da busca exclusivamente ao domínio especificado, sendo fundamental para focar a enumeração apenas no alvo desejado.***

- **Pergunta:** Que ferramenta online e extensão de navegador permitem identificar quais as tecnologias que um site utiliza?  
**Resposta:** 'Wappalyzer'  
***Nota: Conforme descrito no texto, o Wappalyzer é a ferramenta e extensão padrão do setor para identificar rapidamente a stack tecnológica (frameworks, servidores, CDNs, etc.) de qualquer site visitado.***

### 🔵 **Task 5: OSINT - Repositórios e Arquivos**

Explorando recursos externos de armazenamento e versionamento (como arquivos históricos da web, repositórios de código e buckets de nuvem) que frequentemente expõem dados sensíveis, endpoints esquecidos ou configurações incorretas.

Conceitos explorados:  
**Wayback Machine:** Arquivo histórico da Internet que armazena snapshots de sites ao longo do tempo. É extremamente útil para encontrar páginas removidas do site ativo, como formulários de login antigos, endpoints esquecidos ou conteúdo publicado brevemente.  
**GitHub:** Plataforma de controle de versão onde desenvolvedores podem, acidentalmente, cometer (commit) dados sensíveis como chaves de API, credenciais, arquivos de configuração e `.env`. A análise do histórico de commits (e não apenas dos arquivos atuais) é crucial, pois dados removidos em commits posteriores ainda permanecem no histórico.  
**S3 Buckets (Amazon S3):** Serviço de armazenamento em nuvem frequentemente usado para hospedar arquivos e conteúdo estático. A URL padrão segue o formato `https://{nome}.s3.amazonaws.com`. Erros de configuração de permissão são comuns, podendo expor buckets publicamente. Padrões de nomenclatura como `{empresa}-assets`, `{empresa}-backup` ou `{empresa}-dev` são alvos frequentes de enumeração.

- **Pergunta:** Qual é o endereço do site da Wayback Machine?  
**Resposta:** 'https://web.archive.org/'  
***Nota: O endereço principal do projeto de arquivo da Internet é archive.org (sendo web.archive.org o subdomínio específico para a ferramenta de busca de snapshots).***

- **Pergunta:** Qual é o formato de URL com que terminam os buckets do Amazon S3? (A resposta começa por um .)  
**Resposta:** '.s3.amazonaws.com'  
***Nota: Conforme descrito no texto, o formato padrão de URL para um bucket do Amazon S3 termina com este sufixo, o que é essencial para montar URLs válidas durante a enumeração de buckets mal configurados.***

