# KaffeeSec - SoMeSINT

## 📊 Info  
- Dificuldade: Média  
- Categoria: OSINT / SOCMINT  
- Data: 11/08/2026  
- Link: `https://tryhackme.com/room/somesint`    

## 🔍 Resumo  
O objetivo é introduzir técnicas e ferramentas de SOCMINT (Social Media Intelligence/Investigation), aplicando habilidades de OSINT para realizar uma investigação online sobre um "marido misterioso", preparando o aluno para desafios de CTF e pesquisas do mundo real.

## 🛠️ Processo  

### 🔵 **Task 1: Overview**

O foco desta tarefa é apresentar o escopo da sala, os pré-requisitos necessários e as regras do jogo, estabelecendo as expectativas para a investigação de inteligência em mídias sociais que será conduzida.

Conceitos explorados:  
**SOCMINT (Social Media Intelligence):** A prática de coletar e analisar informações de plataformas de mídia social para construir um perfil ou responder a perguntas contextuais sobre um alvo.  
**Técnicas Fundamentais:** Uso de Google Dorking, arquivamento de sites (website archiving), enumeração e análise de mídias sociais, e metodologias básicas de OSINT aplicadas a investigações sociais.  
**Pré-requisitos:** Pensamento crítico, afinidade com investigações profundas ("rabbit-holes"), entendimento básico do Google e Python 3.7+ (para algumas ferramentas opcionais, mas recomendadas para iniciantes).  

### 🔵 **Task 2: História**

Apresentação do cenário da investigação, estabelecendo o personagem do jogador, o cliente e o alvo da investigação de SOCMINT que será conduzida ao longo da sala.

Conceitos explorados:  
**Contexto da Investigação:** O aluno assume o papel de Aleks Juulut, um detetive particular da Groenlândia que está utilizando técnicas de OSINT para conduzir uma investigação remotamente.  
**O Cliente:** Uma pessoa misteriosa que usa o monônimo "H", que contratou o detetive após uma breve ligação com sua esposa.  
**O Alvo:** Thomas Straussman, suspeito de estar traindo sua esposa, Francesca Hodgerint, e apresentando comportamento suspeito recentemente.  
**Restrição Operacional:** A investigação deve ser feita 100% de forma digital, pois o detetive está fora do país devido a uma emergência familiar e não pode retornar à Groenlândia a tempo.

- **Pergunta:** Quem é que te contratou?  
**Resposta:** ks{H}  
***Nota: O texto afirma explicitamente: "You were recently hired by a mysterious person under the moniker 'H'".***

- **Pergunta:** Quem é que estás a investigar? (ks{--- ---})  
**Resposta:** 'ks{Thomas Straussman}'  
***Nota: O texto identifica o alvo da investigação como "a suspected cheater, named Thomas Straussman". A resposta deve seguir o formato de flag solicitado.***

### 🔵 **Task 3: Vamos começar!!**

O foco desta tarefa é iniciar a investigação prática utilizando o handle online do alvo (`tstraussman`) para enumerar suas contas de mídia social (Twitter e Reddit) e extrair informações pessoais básicas por meio de análise passiva.

Conceitos explorados:  
**Enumeração de Mídias Sociais:** O processo de encontrar contas associadas a um nome ou handle específico. Pode ser automatizado com ferramentas CLI ou realizado manualmente via Google Dorking (ex: `site:twitter.com tstraussman`).  
**Análise de Perfil (Twitter/X):** Exame da biografia, foto de fundo (header), seguidores e interações para responder a perguntas contextuais sobre o alvo.  
**Análise de Perfil (Reddit):** Verificação do histórico de posts e do "Cake Day" (aniversário da conta no Reddit), que frequentemente coincide com a data de nascimento real do usuário ou fornece uma pista temporal valiosa.  
**Investigação Passiva:** Coleta de informações sem interagir diretamente com as contas (sem seguir, curtir ou enviar mensagens), mantendo o sigilo da operação.

**Perfil do x encontrado pelo google:** - 'https://x.com/TStraussman'  

- **Pergunta:** Qual é o feriado preferido do Thomas?  
**Resposta:** 'christmas'  
***Nota: A biografia da conta do Twitter (@TStraussman) contém a frase: "But for me it comes from X-mas", indicando claramente que o Natal é sua festa favorita.*** 

- **Pergunta:** Qual é a data de nascimento do Thomas?  
**Resposta:** '12-20-1990'  
***Nota: Ao verificar o perfil do Reddit do alvo (u/Tstraussman), o "Cake Day" (aniversário da conta) é exibido como 20 de dezembro 2020, -30 de idade, que corresponde à data de nascimento solicitada no formato MM-DD.*** 

- **Pergunta:** Qual é o nome de utilizador no Twitter da noiva do Thomas?  
**Resposta:** '@FHodgelink'  
***Nota: Ao analisar os seguidores, seguidos ou interações na conta do Twitter de Thomas, é possível identificar a conta de sua noiva, Francesca.*** 

- **Pergunta:** O que é que a imagem de fundo do Thomas representa?  
**Resposta:** 'Buddha'  
***Nota: A imagem de cabeçalho do perfil do Twitter de Thomas exibe claramente uma estátua ou imagem de Buda, o que também é reforçado pela citação na biografia que menciona "Buddha used to say...".***

### 🔵 **Task 4: Spider... O que?**

O foco desta tarefa é introduzir o uso do **SpiderFoot**, uma ferramenta automatizada de reconhecimento de código aberto, para enumerar contas e informações associadas a um alvo específico, refinando os resultados para eliminar falsos positivos.

Conceitos explorados:  
**SpiderFoot:** Ferramenta de inteligência de fontes abertas (OSINT) que automatiza a coleta de dados de mais de 100 módulos públicos. Pode ser executada localmente via interface web (ex: `localhost:5001`).  
**Configuração de Varredura:** Ao criar um novo scan, é possível definir o alvo (ex: "Thomas Straussman" ou "tstraussman") e selecionar o caso de uso "All" para uma varredura abrangente.  
**Filtragem de Resultados:** A análise dos resultados requer a identificação e descarte de falsos positivos, focando apenas nas plataformas relevantes para a investigação (neste caso, Twitter e Reddit).  
**APIs de Verificação de Conta:** Uso de serviços externos, como a API do shadowban.eu, para verificar o status de uma conta no Twitter, fornecendo metadados adicionais (como o ID de busca) que podem ser úteis na investigação.

- **Pergunta:** Qual foi o módulo de origem utilizado para localizar estas contas?  
**Resposta:** 'sfp_accounts'  
***Nota: Ao analisar os resultados da varredura do SpiderFoot, a coluna "Source Module" indica qual módulo específico foi responsável por descobrir as contas de mídia social.*** 

- **Pergunta:** Verifica a API do shadowban. Qual é o valor de «search»?  
**Resposta:** 'ks{1346173539712380929}'  
***Nota: Ao acessar a API de verificação de shadowban para o usuário (ex: `https://shadowban.eu/.api/tstraussman`), o JSON de retorno contém um campo "search" com um valor numérico específico.***

### 🔵 **Task 5: Ligações, ligações...**

"pivot" (mudança de foco) da investigação do alvo principal (Thomas) para sua noiva (Francesca), extraindo informações pessoais valiosas de sua conta de mídia social através de análise de posts, imagens e metadados.

Conceitos explorados:  
**Pivot de Investigação:** Técnica de OSINT onde, após identificar uma conta relevante, o investigador muda o foco para conexões do alvo (familiares, amigos, colegas) para obter informações adicionais.  
**Busca Reversa de Imagem (Reverse Image Search):** Uso de ferramentas como RevEye para identificar locais geográficos específicos a partir de fotos postadas, permitindo determinar onde o casal fez férias.  
**Análise de Conteúdo de Posts:** Exame detalhado de tweets e publicações para extrair informações pessoais como datas comemorativas, nomes de animais de estimação, preferências de entretenimento e hábitos pessoais.  
**Metadados e Inspeção de Elementos:** Uso de ferramentas de desenvolvedor do navegador (Ctrl+Shift+C) para inspecionar o código-fonte da página e extrair metadados de imagens que podem revelar informações adicionais.

- **Pergunta:** Para onde é que o Thomas e a sua noiva foram de férias?  
**Resposta:** 'Koblenz, Germany'  
***Nota: Ao analisar os tweets de Francesca e realizar uma busca reversa de imagem na foto da viagem de férias, é possível identificar que o casal visitou Koblenz, Alemanha, uma cidade conhecida por seu rio icônico.*** 

- **Pergunta:** Quando é o aniversário da mãe da Francesca? (sem indicar o ano)  
**Resposta:** 'December 25th'  
***Nota: Ao examinar os tweets de Francesca, é possível encontrar referências ao aniversário de sua mãe, que ocorre no dia de Natal (25 de dezembro).*** 

- **Pergunta:** Como se chama o gato deles?  
**Resposta:** 'Gotank'  
***Nota: Francesca menciona o nome de seu gato de estimação em um de seus tweets, referindo-se a ele como "My precious lil furbaby", revelando o nome "Gotank".*** 

- **Pergunta:** Que série é que a Francesca gosta de ver?  
**Resposta:** '90 Day Fiance'  
***Nota: Ao analisar os tweets mais recentes de Francesca, é evidente que ela é fã do programa de realidade "90 Day Fiance", chegando a twittar sobre o show.***

### 🔵 **Task 6: Voltemos atrás no tempo!!**

O foco desta tarefa é utilizar o **Wayback Machine** para investigar versões arquivadas de perfis do Reddit, revelando informações históricas que podem ter sido alteradas ou removidas, e descobrir novas conexões (como um colega de trabalho) que servem como fontes adicionais de inteligência.

Conceitos explorados:  
**Wayback Machine (Internet Archive):** Ferramenta que armazena snapshots históricos de páginas web, permitindo visualizar como um site ou perfil era em datas específicas. Fundamental para recuperar informações que foram deletadas ou modificadas.  
**Reddit (Old vs. New):** O uso da versão antiga do Reddit (`old.reddit.com`) é preferível para o Wayback Machine, pois tem melhor compatibilidade com o arquivamento histórico.  
**Descoberta de Conexões:** Ao analisar posts antigos, é possível descobrir novas pessoas relacionadas ao alvo (como colegas de trabalho), criando novos vetores de investigação.  
**Pastebin e Vazamentos de Dados:** Links para serviços de paste (como Pastebin) frequentemente contêm informações sensíveis, credenciais ou dados vazados que são cruciais para a investigação.

- **Pergunta:** Como se chama o colega de trabalho do Thomas?  
**Resposta:** 'Hans Minik'  
***Nota: Ao visualizar a versão arquivada do Reddit de Thomas (especificamente o post de aniversário), é possível encontrar referências a um colega de trabalho chamado Hans Minik (username: minikhans).*** 

- **Pergunta:** Onde é que o colega dele mora?  
**Resposta:** 'Nuuk, Greenland'  
***Nota: Analisando os posts de Hans e considerando que ele é colega de trabalho de Thomas (que vive em Nuuk, Groenlândia), conclui-se que Hans também reside na mesma cidade.*** 

- **Pergunta:** Qual é o ID da publicação correspondente ao link que encontrámos? (formato de sinalização)  
**Resposta:** 'ks{ww4ju}'  
***Nota: Ao investigar o histórico do Wayback Machine do perfil de Hans, é possível encontrar um link para um paste (provavelmente Pastebin) com o ID "ww4ju" na URL.*** 

- **Pergunta:** Senha para o próximo link? (formato de bandeira)  
**Resposta:** 'ks{1qaz2wsx}'  
***Nota: Dentro do paste encontrado, há referências a outro link protegido por senha. A senha revelada é "1qaz2wsx", uma sequência comum de teclado.*** 

- **Pergunta:** Como se chama a amante do Thomas?  
**Resposta:** 'Emilia Moller'  
***Nota: Ao acessar o paste protegido pela senha encontrada, são reveladas informações sobre um caso extraconjugal de Thomas com uma mulher chamada Emilia Moller.*** 

- **Pergunta:** Qual é o endereço de e-mail do Thomas?  
**Resposta:** 'straussmanthom@mail.com'  
***Nota: Os pastes analisados contêm informações de contato, incluindo o endereço de e-mail de Thomas, que segue o formato "straussmanthom@mail.com".***

Conclusão e fim de CTF!
