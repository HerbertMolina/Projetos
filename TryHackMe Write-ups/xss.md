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

### 🔵 **Task 5: Vulnerable Web Application 1**

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

