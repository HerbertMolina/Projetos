# Searchlight - IMINT

## 📊 Info  
- Dificuldade: Fácil  
- Categoria: OSINT / IMINT  
- Data: 21/07/2026  
- Link: `https://tryhackme.com/room/searchlightosint`    

## 🔍 Resumo  
O objetivo é introduzir a disciplina de IMINT/GEOINT (Inteligência de Imagem e Geoespacial), ensinando metodologias e ferramentas para extrair dados visuais, 
geolocalizar imagens e responder a perguntas de contexto.

## 🛠️ Processo  

### 🔵 **Task 1: Bem-vindo!**  

O foco desta tarefa é apresentar a disciplina de IMINT/GEOINT para iniciantes, estabelecendo as expectativas do que será aprendido, a mentalidade necessária e as regras do jogo (como o formato das flags(sl{flag})).  

Conceitos explorados:  
**IMINT/GEOINT:** Abreviações para *Image Intelligence* (Inteligência de Imagem) e *Geospatial Intelligence* (Inteligência Geoespacial), disciplinas focadas na extração de informações valiosas a partir de mídia visual.  
**Mentalidade Analítica:** A importância de desenvolver um olhar crítico para extrair visualmente pontos de dados-chave (como placas, vegetação, arquitetura, etc.) de uma imagem ou vídeo.  

### 🔵 **Task 2: O primeiro desafio**

O foco desta tarefa é introduzir a primeira prática de geolocalização, enfatizando que a ferramenta mais importante inicialmente são os próprios olhos do analista para extrair dados visuais antes de aplicar metodologias ou ferramentas complexas.

Conceitos explorados:  
**Análise Visual Primária:** A importância de escanear a imagem manualmente em busca de informações óbvias (nomes de ruas, placas, arquitetura) antes de recorrer a ferramentas automatizadas.  
**Os 5 Elementos do IMINT (Benjamin Strick):** Metodologia estruturada para análise de imagens composta por: Contexto, Primeiro Plano (Foreground), Plano de Fundo (Background), Marcações de Mapa e Tentativa e Erro.  
**Context Clues:** Pistas contextuais sobre a origem ou fonte da imagem que ajudam na geolocalização; em desafios CTF, essas pistas podem estar nos títulos, descrições ou hints.  
**Indicadores Geográficos:** Elementos visuais que revelam a localização, como lado da via de direção, idioma em placas, estilo de sinalização, características ambientais, qualidade da infraestrutura (asfalto vs. cascalho) e marcos únicos (pontes, estátuas, montanhas).

- **Pergunta:** Qual é o nome da rua onde esta fotografia foi tirada?  
**Resposta:** 'sl{carnaby street}'  
***Nota: Deve-se fazer o download e aplicar os 5 elementos do IMINT (especialmente Foreground e Background) para identificar placas de rua, nomes de estabelecimentos ou outros indicadores visuais que revelem o nome da rua exata onde a foto foi tirada.***

### 🔵 **Task 3: Basta pesquisar no Google!**

O foco desta tarefa é introduzir o Google como a primeira ferramenta prática de OSINT, ensinando a extrair palavras-chave das imagens e utilizar consultas de busca (incluindo "dorking") para geolocalizar e responder perguntas de contexto sobre os locais identificados.

Conceitos explorados:  
**Google Dorking:** A arte de usar consultas de busca avançadas no Google para retornar tipos específicos de dados e informações precisas a partir de palavras-chave extraídas das imagens.  
**Extração de Keywords:** Habilidade de identificar e isolar elementos visuais convertíveis em termos de busca, como nomes de empresas, números de telefone, frases, placas ou nomes de estações.  
**Context Questions:** Perguntas adicionais sobre o local ou imagem que vão além da simples geolocalização, exigindo pesquisa complementar para responder detalhes históricos, estruturais ou operacionais.  
**Metodologia de Busca:** Processo de escanear a imagem, extrair dados visuais, formular consultas no Google e validar as informações encontradas para responder múltiplas questões sobre um único local.

- **Pergunta:** Em que cidade fica a estação de metro?  
**Resposta:** 'sl{Londres}'  
***Nota: Identificar a cidade requer analisar pistas visuais na imagem (como estilo da estação, sinalização, idioma) e validar através de busca no Google para confirmar a localização geográfica.
  Hoje com a ferramenta de busca por imagem, o processo facilita muito em alguns casos***

- **Pergunta:** A que estação de metro conduzem estas escadas?  
**Resposta:** 'sl{piccadily circus}'  
***Nota: O nome específico da estação de metrô deve ser extraído da imagem (placas, arquitetura característica) ou descoberto através de pesquisa reversa e consultas direcionadas no Google.***

- **Pergunta:** Em que ano é que esta estação foi inaugurada?  
**Resposta:** 'sl{1906}'  
***Nota: Esta é uma "context question" que exige pesquisa histórica sobre a estação identificada, normalmente encontrada em artigos da Wikipedia, sites oficiais de transporte ou bases de dados históricas.***

- **Pergunta:** Quantas plataformas há nesta estação?  
**Resposta:** 'sl{4}'  
***Nota: Outra pergunta de contexto que requer pesquisa detalhada sobre a infraestrutura da estação, disponível em fontes oficiais, Wikipedia ou sites especializados em transporte público.***

### 🔵 **Task 4: Não desista!**

Aqui vamos reforçar as habilidades de geolocalização e o uso de "Google dorking".

Conceitos explorados:  
**Refinamento de Busca (Google Dorking):** Aplicação prática de operadores de busca e combinações de palavras-chave extraídas da imagem para reduzir a localização potencial de forma eficiente.  
**Análise Arquitetônica e Visual:** Identificação de características únicas de edifícios, como estilo da fachada, logotipos, placas, materiais de construção ou elementos de design que permitam nomear o local exato.  
**Contexto Geográfico:** Dedução do país e da cidade com base em indicadores visuais (idioma nas placas, estilo de sinalização, arquitetura regional, tráfego, etc.) para validar os resultados da busca.  

- **Pergunta:** Em que edifício foi tirada esta fotografia?  
**Resposta:** 'sl{vancouver international airport}'  
***Nota: Identifique o nome específico do edifício ou estabelecimento observando detalhes como fachada, logotipos ou placas visíveis na imagem e confirmando via busca no Google.***

- **Pergunta:** Em que país se situa este edifício?  
**Resposta:** 'sl{canada}'  
***Nota: Determine o país com base em pistas visuais (como idioma, estilo de placas de trânsito ou arquitetura) e valide com a pesquisa sobre o edifício identificado.***

- **Pergunta:** Em que cidade se situa este edifício?  
**Resposta:** 'sl{richmond}'  
***Nota: A cidade é geralmente descoberta como parte do endereço ou localização do edifício encontrado durante a pesquisa de validação no Google.***

### 🔵 **Task 5: Café e almoço leve**

O foco desta tarefa é aplicar as técnicas aprendidas em um cenário mais próximo do mundo real: usar inteligência visual para localizar um estabelecimento comercial específico (uma cafeteria na Escócia) a partir de duas imagens e extrair informações de contato detalhadas.

Conceitos explorados:  
**Aplicação Prática de OSINT:** Uso de habilidades de geolocalização para resolver solicitações do mundo real, como encontrar um negócio específico com base em pistas visuais limitadas.  
**Análise de Múltiplas Imagens:** Correlacionar detalhes entre duas ou mais fotos do mesmo local para maximizar a extração de dados (ex: uma foto mostra a fachada, outra pode mostrar um cardápio ou detalhe interno).  
**Extração de Inteligência de Negócios:** Identificação de dados de contato específicos (telefone, e-mail, nomes de proprietários) que geralmente são encontrados após geolocalizar o local e acessar seu site oficial ou perfis em redes sociais.  
**Filtro Geográfico:** Uso da pista fornecida ("Scotland") para restringir as buscas e validar se os resultados fazem sentido dentro daquela região.

- **Pergunta:** Em que cidade fica esta cafetaria?  
**Resposta:** 'sl{Blairgowrie}'  
***Nota: Use as pistas visuais das imagens (arquitetura, placas, paisagem) combinadas com a dica "Scotland" para identificar a cidade através de busca reversa de imagem ou pesquisa por palavras-chave.***

- **Pergunta:** Em que rua fica este café?  
**Resposta:** 'sl{allan street}'  
***Nota: Após identificar o nome ou a cidade da cafeteria, uma busca direta no Google Maps ou no site do estabelecimento revelará o endereço completo e o nome da rua.***

- **Pergunta:** Qual é o número de telefone deles?  
**Resposta:** 'sl{+447878 839128}'  
***Nota: O número de telefone pode estar visível em uma placa na própria imagem ou, mais provavelmente, na seção de contato do site oficial da cafeteria após a geolocalização.***

- **Pergunta:** Qual é o endereço de e-mail?  
**Resposta:** '[RESPOSTA A SER ENCONTRADA]'  
***Nota: Assim como o telefone, o e-mail de contato é uma informação padrão encontrada no rodapé ou na página de "Contato" do site do negócio identificado.***

- **Pergunta:** Qual é o apelido dos proprietários?  
**Resposta:** '[RESPOSTA A SER ENCONTRADA]'  
***Nota: Esta é uma pergunta de contexto mais profunda. Pode ser resolvida verificando a página "About Us" (Sobre Nós) do site da cafeteria, posts de redes sociais ou artigos locais que mencionem os fundadores/proprietários pelo sobrenome.***

### 🔵 **Task 6: Mude a sua forma de pensar**

Técnicas de busca reversa de imagens como metodologia de geolocalização, ensinando a utilizar motores de busca especializados e extensões de navegador para encontrar imagens idênticas ou similares indexadas na web.

Conceitos explorados:  
**Reverse Image Search:** Técnica de pesquisar pela própria imagem online em vez de palavras-chave, permitindo encontrar a imagem exata ou versões similares que foram indexadas por motores de busca.  
**Visual/Crop Search:** Busca visual que permite ajustar o recorte (crop) da imagem e variar palavras-chave para obter resultados diferentes e mais precisos nos motores de busca.  
**Motores de Busca de Imagem:** Utilização de múltiplas plataformas especializadas como Google Images, Bing Visual Search, Yandex Images, TinEye e Baidu para maximizar as chances de sucesso na identificação.  
**Extensões de Produtividade (RevEye):** Ferramentas que facilitam o fluxo de trabalho permitindo realizar buscas reversas em múltiplos motores de busca diretamente do navegador com um clique.  
**Referências Especializadas:** Guias técnicos de especialistas como Aric Toler (Bellingcat) e OSINT Curious que detalham metodologias avançadas de busca reversa de imagens.

- **Pergunta:** Em que restaurante foi tirada esta fotografia?  
**Resposta:** 'sl{katz's deli}'  
***Nota: Utilize a busca reversa de imagem (com RevEye ou upload direto no Google Images/Yandex/TinEye) para identificar o restaurante. Testar diferentes crops da imagem pode revelar resultados mais precisos.***

- **Pergunta:** Qual é o nome do editor da Bon Appétit que trabalhou 24 horas neste restaurante?  
**Resposta:** 'sl{Andrew Knowlton}'  
***Nota: Esta é uma pergunta que requer encontrar um artigo ou vídeo da Bon Appétit sobre o restaurante identificado. Após geolocalizar o local, pesquise por "Bon Appétit 24 hours" para encontrar o nome.***

### 🔵 **Task 7: Localize esta escultura**
Consolidando técnicas aprendidas até o momento (análise visual, busca reversa de imagem e Google dorking) em um desafio de geolocalização de uma estátua/escultura.

Conceitos explorados:  
**Combinação de Técnicas:** Integração de múltiplas metodologias de OSINT (visual clues + reverse image search + dorking) para resolver desafios complexos de geolocalização.  
**Análise Visual de Esculturas:** Identificação de características únicas de estátuas como estilo artístico, material, pose, inscrições, base/monumento e elementos decorativos que facilitam a identificação.  
**Busca Reversa Aplicada:** Uso estratégico de reverse image search em esculturas, que são frequentemente documentadas em sites de turismo, Wikipedia, bancos de imagens e redes sociais.  
**Persistência em Search Results:** A importância de rolar e explorar profundamente os resultados de busca (scrolling), testando diferentes combinações de keywords e crops para encontrar informações específicas.  
**Ferramentas Secundárias:** Enfatizar que o pensamento analítico e a técnica de busca são mais valiosos que depender exclusivamente de ferramentas automatizadas.

- **Pergunta:** Como se chama esta estátua?  
**Resposta:** 'sl{rudolph the chrome nosed reindeer}'  
***Nota: Utilize busca reversa de imagem focando na escultura completa ou em detalhes característicos. Se a busca reversa não for conclusiva, extraia palavras-chave visuais (estilo, material, inscrições) e use Google dorking com termos como "statue", "sculpture", "monument" combinados com características observadas.***

- **Pergunta:** Quem tirou esta fotografia?  
**Resposta:** 'sl{kjersti stensrud}'  
***Nota: O fotógrafo pode ser identificado através dos metadados da imagem (se disponíveis), créditos em sites onde a imagem foi indexada, ou informações de copyright em plataformas como Flickr, Wikimedia Commons ou sites de turismo que hospedam a mesma foto.***

### 🔵 **Task 8: ...e Justiça para Todos**

Desafio de dificuldade superior, exigindo que o analista revise sua abordagem e aplique técnicas avançadas de inteligência visual para identificar não apenas uma estátua, mas todo o seu contexto urbano circundante.

Conceitos explorados:  
**Inteligência Visual Avançada:** A capacidade de perceber detalhes que passam despercebidos, mudando a perspectiva de análise (conforme destacado na palestra TED de Amy Herman, "A lesson on looking").  
**Geolocalização Contextual:** Identificar o entorno do objeto principal (como o prédio em frente) para validar a localização exata, indo além da simples identificação do monumento.  
**Resolução Iterativa de Problemas:** A necessidade de abandonar abordagens iniciais que não funcionam (ex: busca reversa genérica que retorna milhares de estátuas similares) e refinar a busca com combinações específicas de pistas visuais.  
**Análise de Ponto de Vista (POV):** Entender de onde a foto foi tirada para identificar o que está "opposto" (opposite) à estátua, utilizando mapas de rua (como Google Street View) para validar a linha de visão.

- **Pergunta:** Qual é o nome da personagem que a estátua representa?  
**Resposta:** 'sl{Lady Justice}'  
***Nota: Identifique a estátua através de busca reversa ou análise de suas características únicas (roupas, objetos que segura, estilo). O título da task ("...and justice for all") pode ser uma pista temática forte sobre o personagem.***

- **Pergunta:** Onde fica esta estátua?  
**Resposta:** 'sl{Alexandria, Virginia}'  
***Nota: Após identificar o nome da estátua, pesquise sua localização oficial (cidade, praça ou endereço específico). Valide se a aparência do local na imagem corresponde à localização encontrada.***

- **Pergunta:** Qual é o nome do edifício que fica em frente a esta estátua?  
**Resposta:** 'sl{The Westin Alexandria Old Town}'  
***Nota: Esta é a parte mais desafiadora. Use o Google Street View na localização encontrada para simular o ângulo da foto e identificar qual edifício está diretamente em frente à estátua. Pesquise também o nome histórico ou oficial desse prédio.***

### 🔵 **Task 9: A vista do meu quarto de hotelm**

O foco desta tarefa é introduzir a geolocalização de vídeos, demonstrando que um vídeo é essencialmente uma sequência de imagens (frames) que podem ser extraídas, 
analisadas individualmente e submetidas às mesmas técnicas de OSINT aplicadas em fotos estáticas.

Conceitos explorados:  
**Geolocalização de Vídeo:** Aplicação de metodologias de IMINT em arquivos de vídeo, aproveitando que um vídeo contém múltiplos frames (geralmente 24 imagens por segundo) que oferecem mais oportunidades de análise e extração de dados visuais.  
**FFmpeg:** Ferramenta de linha de comando essencial para processamento de vídeo, usada para extrair frames-chave específicos que contenham informações geográficas relevantes (placas, marcos, paisagens).  
**Extração de Frames:** Técnica de decompor um vídeo em imagens individuais para aplicar busca reversa, análise visual e Google dorking em momentos específicos onde informações importantes são visíveis.  
**Análise Temporal:** Capacidade de revisar o vídeo múltiplas vezes e em diferentes velocidades para capturar detalhes que podem passar despercebidos na reprodução normal.

- **Pergunta:** Qual é o nome do hotel onde o meu amigo ficou hospedado há alguns anos?  
**Resposta:** 'sl{NOVOTEL SINGAPORE CLARKE QUAY}'  
***Nota: Baixe o vídeo anexado e use o FFmpeg (conforme o guia do Nixintel) para extrair frames que mostrem vistas da janela, placas, logotipos ou marcos visíveis. Aplique busca reversa de imagem nos frames extraídos e use Google dorking para identificar o hotel específico com base nas pistas visuais encontradas no vídeo.***
