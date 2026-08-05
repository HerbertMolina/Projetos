# Threat Hunting: Introduction

## 📊 Info  
- Dificuldade: Fácil  
- Categoria: Threat Hunting / Blue Team  
- Data: 04/08/2026  
- Link: `https://tryhackme.com/room/threathuntingintroduction`    

## 🔍 Resumo  
Conceitos fundamentais, abordagens e técnicas de Threat Hunting (Caça a Ameaças), entendendo como buscar proativamente por atividades maliciosas que possam ter evadido os sistemas de detecção tradicionais.

## 🛠️ Processo  

### 🔵 **Task 1: Introdução**  

Apresentando a definição de Threat Hunting, diferenciando-o da resposta a incidentes (que é reativa), e estabelecer os objetivos de aprendizado e pré-requisitos necessários para o módulo.

Conceitos explorados:  
**Threat Hunting (Caça a Ameaças):** A busca sistemática e proativa por atividades maliciosas em um ambiente que possam ter evadido os sistemas de detecção automatizados.  
**Diferença para Incident Response:** Enquanto a resposta a incidentes reage a alertas confirmados, os threat hunters buscam ativamente ameaças ocultas antes que causem danos significativos.  
**Objetivos de Aprendizado:** Compreender o que é threat hunting, o que os hunters procuram no ambiente, as diferentes abordagens e técnicas empregadas, e aplicar esses conceitos em cenários realistas.  
**Pré-requisitos:** Conhecimento básico de cibersegurança e do cenário de ameaças, familiaridade com Windows Event Logs e entendimento de técnicas básicas de ataque e da Cyber Kill Chain.  

### 🔵 **Task 2: O que é a deteção proativa de ameaças?**

Threat Hunting: Diferenciando-o da Resposta a Incidentes (Incident Response) e introduzindo o conceito crítico de "Dwell Time" (Tempo de Permanência), destacando por que a proatividade é essencial na segurança moderna.

Conceitos explorados:  
**Threat Hunting vs. Incident Response:** A diferença fundamental está no gatilho e na abordagem. O Threat Hunting é **proativo** e autoiniciado pelo analista sem depender de um alerta, buscando ameaças antes que o comprometimento seja óbvio. A Resposta a Incidentes é **reativa**, acionada por um alerta de segurança confirmado, focando na contenção e remediação.  
**Dwell Time (Tempo de Permanência):** O número médio de dias que um invasor permanece não detectado no ambiente após o comprometimento inicial. Dados da indústria indicam médias de 20 a 30 dias. Reduzir o dwell time é um objetivo primário do threat hunting, pois minimiza drasticamente o potencial de roubo de dados e danos operacionais.  
**Analogia da Segurança Física:** Comparação entre defesas automatizadas (câmeras, sensores, alarmes) e a caça ativa (guardas patrulhando internamente). Sistemas automatizados falham contra ataques sofisticados (zero-days, evasão), exigindo a busca humana proativa por anomalias sutis.  

- **Pergunta:** Como se denomina o número médio de dias durante os quais um invasor permanece indetetado numa rede?  
**Resposta:** 'Dwell time'  
***Nota: O texto define explicitamente "Dwell time" como o número médio de dias que um invasor permanece não detectado no ambiente após o comprometimento inicial, destacando que a indústria reporta médias de 20 a 30 dias.***

- **Pergunta:** A deteção proativa de ameaças é reativa ou proativa?  
**Resposta:** 'Proactive'  
***Nota: A distinção central da tarefa é que, ao contrário da resposta a incidentes (reativa), o threat hunting é uma busca proativa por ameaças, iniciada pelo caçador antes que qualquer alerta seja disparado.***

### 🔵 **Task 3: Estratégias de caça**

O foco desta tarefa é apresentar as três abordagens fundamentais de Threat Hunting utilizadas na indústria, explicando quando e como aplicar cada metodologia com base nas informações disponíveis e nos objetivos da investigação.

Conceitos explorados:  
**Hypothesis-Driven Hunting (Caça Orientada por Hipótese):** Inicia com uma suspeita ou pergunta específica (ex: "O departamento financeiro foi alvo de phishing recente?"). O caçador formula uma hipótese e busca evidências para prová-la ou refutá-la, sendo ideal quando há conhecimento de domínio sobre riscos específicos do ambiente.  
**Intelligence-Driven Hunting (Caça Orientada por Inteligência):** Baseia-se em inteligência de ameaças externa (Threat Intelligence). O caçador utiliza relatórios de pesquisadores, feeds de segurança e frameworks como o **MITRE ATT&CK** (que padroniza táticas e técnicas de adversários, ex: T1566.002, T1059.001) para buscar comportamentos ou IOCs associados a grupos de ataque que visam seu setor ou região.  
**Indicator-Driven Hunting (Caça Orientada por Indicadores):** Foca em artefatos concretos e objetivos, conhecidos como Indicadores de Comprometimento (IOCs), como hashes de arquivos, endereços IP, nomes de domínio ou padrões de linha de comando. É altamente escalável e facilmente automatizável.  

**Seleção Estratégica:** Caçadores experientes escolhem a abordagem com base na pergunta que precisam responder. Muitas organizações executam os três tipos em paralelo, rotacionando o foco conforme as prioridades e a inteligência recém-disponibilizada.

- **Pergunta:** Que abordagem de deteção de ameaças utilizaria se tivesse recebido informações sobre ameaças relativas a um grupo APT que tem como alvo o seu setor?  
**Resposta:** 'Intelligence-driven'  
***Nota: Quando há inteligência específica sobre um grupo de ameaças (APT) direcionando seu setor, a abordagem orientada por inteligência (Intelligence-Driven) é a ideal, pois permite mapear as TTPs (Táticas, Técnicas e Procedimentos) conhecidas do adversário no seu ambiente.***

- **Pergunta:** Qual é a abordagem de deteção de ameaças mais eficiente quando se dispõe de uma lista de hashes de ficheiros e de IOCs provenientes de um feed de ameaças?  
**Resposta:** 'Indicator-driven'  
***Nota: A caça orientada por indicadores é projetada exatamente para isso: buscar correspondências objetivas e diretas de artefatos conhecidos (IOCs).***

