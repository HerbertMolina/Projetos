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

