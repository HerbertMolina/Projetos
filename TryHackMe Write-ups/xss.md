# XSS

## 📊 Info  
- Dificuldade: Fácil  
- Categoria: Web Security / Cross-Site Scripting  
- Data: 11/08/2026  
- Link: `https://tryhackme.com/room/axss`    

## 🔍 Resumo  
O objetivo é explorar em profundidade os diferentes tipos de XSS (Cross-Site Scripting) e suas causas raiz.

## 🛠️ Processo  

### 🔵 **Task 1: Introdução**

 
**Definição de XSS:** Uma vulnerabilidade que permite a injeção de scripts maliciosos em sites benignos, que são então executados no navegador do usuário, explorando a confiança que o usuário deposita na aplicação web.  

**Contexto Histórico e Atual:** Reconhecida desde 1999 (CERT advisory CA-2000-02), a XSS continua sendo uma ameaça comum. No OWASP Top 10 de 2017, estava em 7º lugar, e em 2021 foi agrupada com outros ataques de injeção, subindo para a 3ª posição.  

**Pré-requisitos:** Conhecimento básico de HTTP, funcionamento de websites e, idealmente, ter completado a sala "Intro to Cross-site Scripting". A sala utiliza trechos de código em PHP, JavaScript, Python e C#, mas o foco está na lógica da vulnerabilidade e nas soluções, não na sintaxe das linguagens.  
**Objetivos de Aprendizado:** Compreender em profundidade os tipos Reflected XSS, Stored XSS, DOM-based XSS e como se proteger contra eles.
é uma tarefa de confirmação e introdução. Não há uma resposta técnica a ser submetida, servindo apenas para garantir que o aluno revisou os conceitos básicos antes de prosseguir.*** 

### 🔵 **Task 2: Tipos e Terminologia**

Fundamentos do Cross-Site Scripting (XSS), explicando como ele contorna as políticas de segurança do navegador e classificando os três principais tipos de vulnerabilidade, além de revisar funções básicas de JavaScript essenciais para a exploração.

Conceitos explorados:  
**Same-Origin Policy (SOP):** Mecanismo de segurança dos navegadores que impede que um script malicioso de uma origem (protocolo, hostname e porta) acesse dados de outra. O XSS contorna a SOP porque o script malicioso é executado a partir da *mesma* origem do site legítimo, ganhando a confiança do navegador.  
**JavaScript para XSS:** Conhecimento básico de JS é crucial. Funções comuns usadas em PoCs (Provas de Conceito) incluem:  
- `alert()`: Exibe uma caixa de diálogo (ex: `alert(1)` ou `alert('XSS')`).  
- `console.log()`: Registra valores no console do desenvolvedor.  
- `btoa()` / `atob()`: Codifica e decodifica strings em Base64, útil para ofuscar payloads e contornar filtros básicos.  
- `document.cookie`: Acessa os cookies da sessão do usuário no domínio atual.  
**Tipos de XSS:**  
**Reflected XSS (Refletido):** O script malicioso é refletido imediatamente de volta ao usuário a partir de uma entrada controlada por ele (ex: parâmetros de busca na URL). Não é salvo no servidor.  
**Stored XSS (Armazenado):** O script malicioso é salvo permanentemente no banco de dados do site (ex: comentários, reviews de produtos) e é executado no navegador de qualquer usuário que visualize a página afetada.  
**DOM-based XSS:** Explora vulnerabilidades no Document Object Model (DOM) do lado do cliente, manipulando elementos da página sem que o payload precise ser refletido ou armazenado pelo servidor.

- **Pergunta:** Qual é a vulnerabilidade XSS que depende do armazenamento do script malicioso?  
**Resposta:** 'Stored XSS'  
***Nota: O XSS Armazenado (Stored) depende da persistência do payload malicioso no banco de dados ou sistema de arquivos do servidor, afetando todos os usuários que acessam a página comprometida.***

- **Pergunta:** Qual é a vulnerabilidade XSS mais comum que é executada durante a sessão do navegador sem ser guardada?  
**Resposta:** 'Reflected XSS'  
***Nota: O XSS Refletido ocorre quando a entrada do usuário é processada e retornada imediatamente pela aplicação (como em uma mensagem de erro ou resultado de busca), sendo executada na sessão atual sem deixar registro permanente no servidor.***

- **Pergunta:** O que significa DOM?  
**Resposta:** 'Document Object Model'  
***Nota: O DOM (Document Object Model) é a representação estrutural do documento HTML que permite que scripts (como JavaScript) acessem e manipulem o conteúdo, a estrutura e o estilo da página web.***        

### 🔵 **Task 3: Causas e implicações**

Detalhando as causas raiz que tornam o Cross-Site Scripting (XSS) possível em aplicações web e explorar as graves implicações de segurança que resultam de uma exploração bem-sucedida.

Conceitos explorados:  
**Causas do XSS:**  
**Validação e sanitização insuficientes de entrada:** Aplicações que aceitam dados do usuário (via formulários, URLs) e os utilizam na geração dinâmica de HTML sem limpá-los adequadamente.  
**Falta de codificação de saída (Output Encoding):** Falha em converter caracteres especiais (como `<`, `>`, `"`, `'`, `&`) em suas entidades HTML seguras antes de renderizá-los no navegador.  
**Uso inadequado de cabeçalhos de segurança:** Configurações fracas de Content Security Policy (CSP), como o uso de `unsafe-inline` ou `unsafe-eval`, que facilitam a execução de scripts maliciosos.  
**Vulnerabilidades em frameworks e bibliotecas de terceiros:** Frameworks antigos ou bibliotecas não atualizadas podem introduzir vetores de XSS mesmo que o código principal da aplicação seja seguro.  

**Implicações do XSS:**  
**Sequestro de Sessão (Session Hijacking):** Roubo de cookies de sessão para assumir a identidade da vítima.  
**Phishing e Roubo de Credenciais:** Exibição de prompts de login falsos sobrepostos à página legítima.  
**Engenharia Social:** Criação de pop-ups ou alertas que parecem legítimos para induzir o usuário a clicar em links maliciosos.  
**Manipulação de Conteúdo e Defacement:** Alteração da aparência ou funcionalidade do site para prejudicar a reputação da empresa.  
**Exfiltração de Dados:** Acesso e envio de informações sensíveis exibidas no navegador do usuário.  
**Instalação de Malware:** Uso do site vulnerável para realizar ataques de "drive-by download".

- **Pergunta:** Tendo em conta as principais causas das vulnerabilidades XSS, que operações devem ser realizadas na entrada do utilizador?  
**Resposta:** 'validation and sanitization'  
***Nota: Para mitigar o risco na origem, os dados fornecidos pelo usuário devem passar por rigorosos processos de validação (verificar se o formato é o esperado) e sanitização (remover ou neutralizar caracteres perigosos) antes de serem processados.*** 

- **Pergunta:** Para prevenir vulnerabilidades XSS, que operações devem ser realizadas nos dados antes de estes serem apresentados ao utilizador?  
**Resposta:** 'encoding'  
***Nota: A codificação de saída (output encoding) é a defesa mais crítica, garantindo que quaisquer caracteres especiais inseridos pelo usuário sejam tratados como texto literal pelo navegador, e não como código executável (HTML ou JavaScript).*** 

### 🔵 **Task 4: Reflected XSS (xss refletido)**

Explorando o Reflected XSS (XSS Refletido), entendendo como ele ocorre quando a entrada do usuário é imediatamente refletida na resposta do servidor sem a devida sanitização, e como corrigir essa vulnerabilidade em diferentes linguagens e frameworks.

Conceitos explorados:  
**Mecanismo do Reflected XSS:** Ocorre quando um script malicioso é injetado em uma URL ou formulário e "refletido" de volta na página de resultados. O navegador da vítima executa o script porque confia na origem da página.  
**Exemplos de Código Vulnerável e Corrigido:**  
**PHP:** Vulnerável ao usar `$_GET['q']` diretamente no `echo`. Corrigido usando `htmlspecialchars()` para converter caracteres especiais em entidades HTML.  
**JavaScript (Node.js/Express):** Vulnerável ao concatenar `req.query.q` diretamente na resposta. Corrigido usando bibliotecas como `sanitize-html` ou funções como `escapeHtml()` para neutralizar caracteres perigosos.  
**Python (Flask):** Vulnerável ao inserir `request.args.get("q")` diretamente em uma f-string. Corrigido usando `html.escape()` (ou `markupsafe.escape`) para codificar a saída.  
**C# (ASP.NET):** Vulnerável ao usar `Request.QueryString["q"]` diretamente no `Response.Write`. Corrigido aplicando `HttpUtility.HtmlEncode()` na entrada do usuário.  
**Princípio de Defesa:** A regra de ouro é nunca confiar na entrada do usuário. Dados devem ser validados na entrada e, crucialmente, **codificados (encoded)** na saída para o navegador.

- **Pergunta:** Qual dos seguintes caracteres espera que seja codificado? ., ,, ;, &, or #?  
**Resposta:** '&'  
***Nota: O caractere `&` é um dos caracteres especiais que deve ser codificado para sua entidade HTML (`&amp;`) para evitar que seja interpretado como o início de uma entidade ou quebre a estrutura do HTML.***

- **Pergunta:** Qual dos seguintes caracteres espera que seja codificado? +, -, *, <, =, or ^?  
**Resposta:** '<'  
***Nota: O caractere `<` é o mais crítico, pois indica o início de uma tag HTML (como `<script>`). Ele deve ser codificado como `&lt;` para ser renderizado como texto e não como código executável.***

- **Pergunta:** Que função podemos utilizar em JavaScript para substituir caracteres especiais (não seguros) por entidades HTML?  
**Resposta:** 'sanitizehtml()'  
***Nota: Conforme mencionado no texto, a função `escapeHtml()` (ou bibliotecas como `sanitize-html`) é usada em ambientes Node.js para escapar caracteres como `<`, `>`, `&`, `"` e `'`, neutralizando payloads de XSS.*** 

- **Pergunta:** Que função utilizámos no PHP para substituir os caracteres especiais do HTML?  
**Resposta:** 'htmlspecialchars()'  
***Nota: O texto demonstra explicitamente o uso da função nativa do PHP `htmlspecialchars()` para converter caracteres especiais em suas entidades HTML seguras, prevenindo a execução de scripts injetados.***

### 🔵 **Task 5: Aplicação Web Vulnerável 1**

Aplicando o conhecimento teórico em um cenário prático, explorando uma vulnerabilidade de Reflected XSS em uma versão vulnerável da aplicação `copyparty` (CVE-2023-38501) rodando em uma máquina virtual fornecida pela sala.
  
**Exploração Prática de Reflected XSS:** A vulnerabilidade é acionada através de parâmetros de URL maliciosamente construídos. O payload fornecido (`?k304=y%0D%0A%0D%0A%3Cimg+src%3Dcopyparty+onerror%3Dalert(1)%3E`) utiliza URL encoding para injetar uma tag `<img>` com um manipulador de erro `onerror`, que executa a função `alert(1)` quando a imagem falha ao carregar.  
**Quebra de Linha e Injeção:** Os caracteres `%0D%0A` representam quebras de linha (CRLF), que podem ser usadas para "quebrar" a estrutura HTML esperada e inserir o payload malicioso em um contexto onde ele será executado pelo navegador.  
**Identificação e Validação:** Ao acessar a URL vulnerável na máquina alvo, o atacante pode observar o comportamento do aplicativo e confirmar a execução do código JavaScript, validando a presença da falha de segurança.

- **Pergunta:** Que tipo de vulnerabilidade é esta?  
**Resposta:** 'Reflected XSS'  
***Nota: O texto da tarefa e o contexto da sala identificam explicitamente a falha (CVE-2023-38501) como uma vulnerabilidade de Cross-Site Scripting Refletido, onde o payload é entregue via URL e executado imediatamente.*** 

- **Pergunta:** Utiliza a vulnerabilidade acima indicada na máquina virtual em anexo. O que vês na segunda linha, a seguir a «go to»?  
**Resposta:** '/?h#cc'  
***Nota: Ao aplicar o exploit na máquina virtual e observar a página de resultados ou o comportamento do redirecionamento/exibição, a segunda linha após "go to" exibe especificamente a string "/?h#cc", confirmando a interação com o payload injetado.***

### 🔵 **Task 6: Stored XSS (armazenado)**

O foco desta tarefa é explorar o Stored XSS (XSS Armazenado ou Persistente), uma vulnerabilidade que ocorre quando a aplicação salva a entrada maliciosa do usuário em um banco de dados e a exibe posteriormente para outros usuários sem a devida sanitização ou codificação.

Conceitos explorados:  
**Mecanismo do Stored XSS:** O atacante injeta um script em um campo de entrada (como comentários de blog, reviews de produtos ou perfis de usuário). O script é salvo no banco de dados e executado automaticamente no navegador de qualquer vítima que visualize a página afetada, tornando-o muito mais perigoso e escalável que o Reflected XSS.  
**Boas Práticas de Prevenção:**  
- **Validação e Sanitização de Entrada:** Aplicar regras estritas sobre o que é aceito (ex: apenas caracteres alfanuméricos em nomes de usuário).  
- **Codificação de Saída (Output Escaping):** Converter caracteres especiais HTML (`<`, `>`, `&`) em suas entidades seguras antes de renderizá-los.  
- **Codificação Específica de Contexto:** Usar codificação adequada para o contexto onde os dados serão inseridos (ex: codificação JavaScript para blocos de script, URL-encoding para links).  
- **Defesa em Profundidade:** Não confiar apenas na validação do lado do cliente; implementar validação e sanitização robustas no lado do servidor.  

**Exemplos de Código Vulnerável e Corrigido:**  
- **PHP:** O código vulnerável exibe o comentário diretamente com `echo`. A correção aplica `htmlspecialchars()` na saída.  
- **JavaScript (Node.js):** O código vulnerável concatena o comentário diretamente no HTML. A correção utiliza a biblioteca `sanitize-html` e a função `sanitizeHtml()` para remover elementos perigosos como `<script>`.  
- **Python (Flask):** O código vulnerável renderiza o conteúdo do banco de dados sem tratamento. A correção aplica a função `escape()` (do módulo `markupsafe` ou `html`) em cada comentário antes da renderização.  
- **C# (ASP.NET):** O código vulnerável usa `Response.Write` direto do banco de dados. A correção aplica o método `HttpUtility.HtmlEncode()` para garantir que a saída seja segura.

- **Pergunta:** Qual é o nome da função JavaScript que utilizámos para sanitizar os dados introduzidos pelo utilizador antes de os guardar?  
**Resposta:** 'sanitizeHtml()'  
***Nota: No exemplo de correção para Node.js, a função `sanitizeHtml()` da biblioteca `sanitize-html` é utilizada para remover elementos e atributos inseguros (como tags `<script>`) antes de exibir o comentário.***

- **Pergunta:** Que método utilizámos no ASP.Net C# para sanitizar os dados introduzidos pelo utilizador?  
**Resposta:** 'HttpUtility.HtmlEncode()'  
***Nota: O texto demonstra explicitamente que a vulnerabilidade de Stored XSS no ASP.NET C# é corrigida aplicando o método `HttpUtility.HtmlEncode()` na variável do comentário antes de enviá-la para o `Response.Write`.***

### 🔵 **Task 7: Aplicação Web Vulnerável 2**

O foco desta tarefa é aplicar o conhecimento sobre Stored XSS em um cenário prático, explorando uma vulnerabilidade conhecida (CVE-2021-38757) em um sistema de gerenciamento hospitalar desatualizado.

**Exploração Prática de Stored XSS:** A vulnerabilidade reside no formulário de "Contato" da aplicação, onde a mensagem enviada pelo usuário é salva diretamente no banco de dados sem nenhuma sanitização.  
**Impacto no Administrador/Recepcionista:** Quando um usuário com privilégios (como o Recepcionista) faz login e visualiza as mensagens recebidas, o script malicioso injetado no campo de mensagem é executado no navegador dele.  
**Roubo de Sessão:** Ao injetar `<script>alert(document.cookie)</script>`, o atacante pode visualizar os cookies de sessão da vítima, demonstrando como um ataque de Stored XSS pode levar ao sequestro de conta (Session Hijacking).

- **Pergunta:** Qual tipo de vulnerabilidade é essa?   
**Resposta:** 'Stored XSS'  
***Nota: O texto da tarefa descreve explicitamente que a mensagem do usuário é salva não sanitizada no banco de dados e exibida posteriormente, o que é a definição clássica de Cross-Site Scripting Armazenado (Persistente).*** 

- **Pergunta:** Aceda à página de contacto e envie a seguinte mensagem: `<script>alert(document.cookie)</script>`. Em seguida, inicie sessão como Recepcionista. Qual é o nome da chave do par chave-valor apresentado?  
**Resposta:** 'PHPSESSID'  
***Nota: Ao fazer login como recepcionista (admin/admin123) e visualizar a mensagem, o navegador executa o script e exibe um alerta com os cookies. O cookie de sessão padrão do PHP, que mantém o usuário autenticado, é identificado pela chave `PHPSESSID`.***

### 🔵 **Task 8: DOM-Based XSS**

O foco desta tarefa é explorar o DOM-Based XSS, uma variante de Cross-Site Scripting que ocorre inteiramente no lado do cliente (navegador), sem que o payload malicioso precise ser refletido ou armazenado pelo servidor.
 
**O que é o DOM (Document Object Model):** Uma interface de programação que representa um documento web como uma árvore de nós, permitindo que o JavaScript acesse e manipule dinamicamente a estrutura, o estilo e o conteúdo da página.  
**Mecanismo do DOM-Based XSS:** A vulnerabilidade surge quando o JavaScript do lado do cliente pega dados controlados pelo usuário (como parâmetros da URL via `window.location.search`) e os insere de forma insegura no DOM (ex: usando `document.write()`), permitindo a execução de scripts.  
**Diferença Fundamental:** Ao contrário do Reflected e Stored XSS, o servidor não tem participação direta na entrega do payload explorável; a falha está inteiramente na lógica do script executado no navegador da vítima.  
**Correção:** Evitar a inserção direta de entrada do usuário usando métodos perigosos como `document.write()`. Em vez disso, deve-se usar propriedades seguras como `textContent` e aplicar funções de codificação, como `encodeURIComponent()`, para neutralizar caracteres especiais antes da renderização.

- **Pergunta:** O XSS baseado em DOM é refletido através do servidor. (Yea/Nay)  
**Resposta:** 'Nay'  
***Nota: O DOM-Based XSS ocorre inteiramente no navegador do cliente. O servidor apenas entrega a página estática; ele não reflete nem processa o payload malicioso de volta para o usuário.*** [[9]]

- **Pergunta:** O XSS baseado em DOM ocorre apenas no lado do cliente. (Yea/Nay)  
**Resposta:** 'Yea'  
***Nota: Como o nome sugere, a vulnerabilidade e a exploração do DOM-Based XSS residem exclusivamente no código JavaScript executado no lado do cliente (navegador).*** [[19]]

- **Pergunta:** Que método JavaScript foi utilizado para codificar a entrada do utilizador?  
**Resposta:** 'encodeURIComponent()'  
***Nota: No exemplo de código corrigido, a função `encodeURIComponent()` é utilizada para codificar a entrada do usuário, convertendo caracteres especiais em suas representações seguras antes de inseri-los no DOM via `textContent`.***

