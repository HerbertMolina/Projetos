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
