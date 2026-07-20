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

.

