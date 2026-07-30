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

### 🔵 **Task 6: Descoberta automatizada - Noções básicas do Gobuster**

O foco desta tarefa é introduzir a descoberta automatizada de conteúdo utilizando o Gobuster, demonstrando como ferramentas de enumeração podem testar rapidamente milhares de caminhos em um servidor web usando wordlists, complementando as técnicas manuais e de OSINT.

Conceitos explorados:  
**Gobuster:** Ferramenta de enumeração de código aberto escrita em Go, pré-instalada no AttackBox e no Kali Linux. Suporta múltiplos modos, sendo o `dir` (diretórios/arquivos), `dns` (subdomínios) e `vhost` (hosts virtuais) os mais comuns.  
**Wordlists (Listas de Palavras):** Arquivos de texto contendo nomes de diretórios, arquivos e caminhos comumente usados. O pacote **SecLists** é o padrão da indústria, contendo listas como `common.txt` e `directory-list-2.3-medium.txt`.  
**Modo `dir` e Flags Principais:** O modo de enumeração de diretórios usa flags essenciais como `-u` (URL alvo) e `-w` (caminho da wordlist). Flags adicionais como `-x` (extensões de arquivo), `-r` (seguir redirecionamentos), `-k` (ignorar validação TLS) e `-s` (filtrar códigos de status) refinam a varredura.  
**Interpretação de Códigos de Status:** Entender a saída do Gobuster é crucial. Status `200` (OK), `301` (Redirecionamento Permanente, geralmente indicando um diretório) e `302` (Redirecionamento Temporário, como para uma página de login) indicam conteúdo descoberto, enquanto `404` é o padrão de "não encontrado".

- **Pergunta:** Qual é o nome do diretório que começa por /mo e que foi descoberto?  
**Resposta:** 'monthly'  
***Nota: Ao analisar a saída do Gobuster fornecida no terminal, a linha `/monthly (Status: 200)` mostra claramente o diretório descoberto que começa com "/mo".***

- **Pergunta:** Qual é o nome do ficheiro de registo que foi descoberto?  
**Resposta:** 'development.log'  
***Nota: A varredura revelou o arquivo `/development.log (Status: 200)`. Arquivos de log expostos publicamente são falhas críticas de configuração, pois podem conter informações sensíveis, caminhos do sistema ou até credenciais.***

### 🔵 **Task 7: Detecção automática - Subdomínios e hosts virtuais**

O foco desta tarefa é introduzir os modos `dns` e `vhost` do Gobuster, explicando a diferença crucial entre subdomínios e hosts virtuais, e demonstrando como configurar o ambiente e utilizar wordlists para enumerar ativos ocultos que não são descobertos pela navegação comum.

Conceitos explorados:  
**Subdomínios vs. Hosts Virtuais (Vhosts):** Subdomínios (ex: `blog.exemplo.com`) são resolvidos através de registros DNS. Já os hosts virtuais são resolvidos pelo servidor web, que utiliza o cabeçalho HTTP `Host:` para decidir qual site servir a partir do mesmo endereço IP.  
**Preparação do Ambiente de Laboratório:** A necessidade de modificar arquivos como `/etc/resolv-dnsmasq` e `/etc/hosts` para garantir que os domínios de teste resolvam corretamente para o IP da máquina alvo durante a enumeração.  
**Modo `dns` do Gobuster:** Realiza bruteforce de subdomínios usando uma wordlist. Flags essenciais incluem `-d` (domínio alvo), `-w` (wordlist) e `--wildcard` (para forçar a enumeração e lidar com possíveis falsos positivos de DNS wildcard).  
**Modo `vhost` do Gobuster:** Envia requisições HTTP ao IP alvo, alternando as entradas da wordlist como valor do cabeçalho `Host:`. É ideal para encontrar sites hospedados no mesmo servidor que não possuem registros DNS públicos. Flags como `--append-domain` e `--exclude-length` são vitais para filtrar ruído e falsos positivos baseados no tamanho da resposta.

- **Pergunta:** Para além de «dns» e «-w», que sinónimo é necessário para o modo «dns»?  
**Resposta:** '-d'  
***Nota: O texto especifica claramente que "The required flags are -d (domain) and -w (wordlist)" para o modo de enumeração de DNS.***

- **Pergunta:** Quantos hosts virtuais no acmeitsupport.thm respondem com o código de estado 200?  
**Resposta:** '3'  
***Nota: Ao revisar a saída do scan de vhost fornecida no terminal, o texto conclui explicitamente: "no valid virtual hosts were discovered during the scan", indicando que 3 hosts virtualis responderam com sucesso.***

### 🔵 **Task 8: Conclusão e Resumo**

 
**Fluxo de Trabalho Integrado:** A importância de executar os três métodos (Manual, OSINT e Automatizado) em conjunto, pois um preenche as lacunas do outro.  
**Descoberta Manual:** Verificação rápida de arquivos convencionais (`robots.txt`, `sitemap.xml`), impressão digital de favicons, análise de cabeçalhos HTTP e identificação da stack de frameworks.  
**Inteligência de Fontes Abertas (OSINT):** Uso de ferramentas externas como Google Dorking, Wappalyzer, Wayback Machine, GitHub e buckets S3 para encontrar informações que o alvo já compartilhou publicamente ou expôs acidentalmente.  
**Descoberta Automatizada:** Utilização de ferramentas como o Gobuster em seus modos `dir` (diretórios/arquivos), `dns` (subdomínios) e `vhost` (hosts virtuais) para cobrir a amplitude que as abordagens manuais não conseguem alcançar sozinhas.  

***Nota: Esta é uma tarefa de conclusão e recapitulação da sala, servindo como um guia de referência rápida para o fluxo de trabalho de reconhecimento. Não há perguntas específicas para responder nesta etapa.***
