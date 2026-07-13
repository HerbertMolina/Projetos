# Google Dorking - TryHackMe  

## 📊 Info  
- Dificuldade: Fácil  
- Categoria: Básico  
- Data: 08/07/2026  
- Link: `https://tryhackme.com/room/googledorking`    

## 🔍 Resumo  
O objetivo é explicar como funcionam os motores de busca e aproveitá-los para encontrar conteúdos ocultos!  


## 🛠️ Processo  

### 🔵 **Task 1: Search Engines**  

O foco desta tarefa é introduzir a importância da pesquisa (Research) no contexto de pentest e explicar o funcionamento básico dos motores de busca (como o Google), 
que atuam como grandes indexadores de conteúdo da World Wide Web.  

  Conceitos explorados:  
  **Search Engines / Indexers:** Ferramentas fundamentais para navegação e coleta de informações, capazes de indexar conteúdos espalhados pela web de forma muito mais profunda do que wordlists tradicionais.  
  **Crawlers / Spiders:** Os "rastreadores" utilizados pelos motores de busca para varrer e indexar o conteúdo da World Wide Web nos bastidores.  

### 🔵 **Task 2: Aprendendo sobre os Crawlers** 

O foco desta tarefa é entender a teoria por trás dos motores de busca, explicando como os "Crawlers" (rastreadores) descobrem, percorrem e armazenam informações da web para criar índices de pesquisa. 

  Conceitos explorados: 
  **Crawling / Spidering:** A técnica de percorrer a web, seguindo URLs e links para descobrir novos conteúdos e domínios, semelhante à propagação de um vírus. 
  **Indexing:** O processo de coletar, analisar (buscando palavras-chave) e armazenar os recursos e suas localizações em um banco de dados (o índice do motor de busca). 
  **Keywords:** Os termos e palavras-chave extraídos do conteúdo de um site que permitem ao motor de busca exibi-lo quando um usuário fizer uma consulta específica. 

- **Pergunta:** Nomeie o termo chave para o que um "Crawler" é usado para fazer. Isso é conhecido como uma coleção de recursos e suas localizações.   
**Resposta:** 'Index'  
***Nota: O ato de coletar recursos e mapear suas localizações para formar o dicionário do motor de busca é o processo de indexação.***  

- **Pergunta:** Qual é o nome da técnica que os "Motores de Busca" usam para recuperar essas informações sobre sites?        
**Resposta:** 'Crawling'  
***Nota: É o termo técnico para o rastreamento automatizado da web em busca de novos links e conteúdos.***  

- **Pergunta:** Qual é um exemplo do tipo de conteúdo que pode ser coletado de um site?       
**Resposta:** 'Keywords'  
***Nota: Conforme o texto ilustra, os crawlers extraem palavras-chave (como "Apple", "Banana", "Tomatoes") e URLs para compor o índice de busca.***

### 🔵 **Task 3: Otimização de motor de busca (SEO)**

O foco desta tarefa é compreender como os motores de busca priorizam e classificam os domínios (SEO) e como os administradores de sistemas podem restringir o acesso de crawlers a áreas sensíveis do site.

  Conceitos e Ferramentas explorados:  
  **SEO (Search Engine Optimization):** Conjunto de fatores (como responsividade, sitemaps e palavras-chave) que determinam a "pontuação" e a hierarquia de um site nos resultados de busca.  
  
  **robots.txt:** Arquivo de configuração na raiz do servidor web que dita quais diretórios, arquivos ou rotas os crawlers têm permissão para indexar (fundamental para ocultar páginas de login administrativo ou diretórios privados).  
  **Ferramentas de Análise de SEO (ex: Google Lighthouse):** Utilizadas para auditar a pontuação de SEO, performance e acessibilidade de um domínio.  

***Nota: Esta task é um exercício de observação. Ao observar a pontuação de SEO sites diferentes, fica evidente como a estrutura, responsividade e otimização de palavras-chave impactam diretamente a facilidade com que os crawlers indexam o conteúdo e a posição do site nos resultados de busca.***  

### 🔵 **Task 4: Beepboop robots.txt**

O foco desta tarefa é entender a função do arquivo 'robots.txt', como ele controla as permissões dos crawlers e como pode ser usado (ou abusado) para descobrir diretórios e arquivos ocultos.

  Conceitos explorados:
  **robots.txt:** Arquivo de texto localizado na raiz do domínio que define as regras de indexação para os crawlers.
  **User-agent:** Especifica qual crawler (ex: Googlebot, Bingbot, ou `*` para todos) a regra se aplica.
  **Allow / Disallow:** Diretivas que permitem ou bloqueiam a indexação de diretórios ou arquivos específicos.
  **Sitemap:** Diretiva que fornece a localização do mapa do site para melhorar o SEO.

- **Pergunta:** Onde o "robots.txt" estaria localizado no domínio "ablog.com"?    
**Resposta:** 'ablog.com/robots.txt'  
***Nota: O arquivo robots.txt deve ser servido obrigatoriamente no diretório raiz (root) do domínio.***  

- **Pergunta:** Se um site tivesse um sitemap, onde ele estaria localizado?  
**Resposta:** 'sitemap.xml'  
***Nota: Assim como o robots.txt, o sitemap (geralmente sitemap.xml) é tipicamente colocado no diretório raiz e referenciado dentro do próprio robots.txt.***  

- **Pergunta:** Como permitiríamos apenas o "Bingbot" de indexar o site?    
**Resposta:** 'User-agent: Bingbot' (seguido de 'Allow: /')  
***Nota: A diretiva User-agent define o alvo da regra, e o Allow: / concede permissão total de indexação para aquele crawler específico.***  

- **Pergunta:** Como impediríamos um "Crawler" de indexar o diretório "/dont-index-me/"?  
**Resposta:** 'Disallow: /dont-index-me/'  
***Nota: A diretiva Disallow é usada para criar uma "lista negra" (blacklist) de caminhos que o crawler não deve acessar ou indexar.***  

- **Pergunta:** Qual é a extensão de um arquivo de configuração de sistema Unix/Linux que poderíamos querer ocultar dos "Crawlers"?  
**Resposta:** '.conf'  
***Nota: O texto cita explicitamente arquivos .ini como exemplos de arquivos que contêm detalhes sensíveis de configuração e que, portanto, devem ser protegidos da indexação.***



