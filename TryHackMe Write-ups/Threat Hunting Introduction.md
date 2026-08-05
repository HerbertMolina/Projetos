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
**Resposta:** 'Intelligence-driven hunting'  
***Nota: Quando há inteligência específica sobre um grupo de ameaças (APT) direcionando seu setor, a abordagem orientada por inteligência (Intelligence-Driven) é a ideal, pois permite mapear as TTPs (Táticas, Técnicas e Procedimentos) conhecidas do adversário no seu ambiente.***

- **Pergunta:** Qual é a abordagem de deteção de ameaças mais eficiente quando se dispõe de uma lista de hashes de ficheiros e de IOCs provenientes de um feed de ameaças?  
**Resposta:** 'Indicator-driven hunting'  
***Nota: A caça orientada por indicadores é projetada exatamente para isso: buscar correspondências objetivas e diretas de artefatos conhecidos (IOCs).***

### 🔵 **Task 4: Alvos de caça**

O foco desta tarefa é definir o "O QUÊ" (WHAT) da caça a ameaças: os tipos de evidências e artefatos que indicam atividade maliciosa, categorizando os principais alvos que um threat hunter deve procurar nos logs e sistemas.

Conceitos explorados:  
**Known Malware (Malware Conhecido):** Busca por indicadores de softwares maliciosos já catalogados e analisados por pesquisadores (ex: hashes de arquivo, padrões de linha de comando, conexões C2), frequentemente obtidos via feeds de inteligência ou plataformas como VirusTotal. O desafio é que variantes e zero-days podem evadir essa detecção baseada em assinaturas.  
**Attack Residues (Resíduos de Ataque):** Artefatos inevitavelmente deixados pelos invasores ao executar sua cadeia de ataque (ex: criação de processos incomuns, execução de ferramentas administrativas nativas como `whoami` ou `net user`, conexões de rede inesperadas, modificações no registro). São valiosos por serem independentes de malware específico, capturando comportamentos de ataque genéricos.  
**Known Vulnerabilities (Vulnerabilidades Conhecidas):** Busca por evidências de que vulnerabilidades públicas e críticas (ex: Log4Shell) foram exploradas no ambiente, analisando logs de aplicação em busca de padrões de exploit e comportamentos anômalos de processos após a tentativa de exploração.  
**Abordagem em Camadas:** A caça a ameaças mais eficaz combina esses três alvos, procurando simultaneamente por malware conhecido, resíduos de ataque comportamentais e sinais de exploração de vulnerabilidades.

- **Pergunta:** Que categoria de alvo de caça representa os artefactos deixados pelos atacantes durante o seu ataque?  
**Resposta:** 'Attack residues'  
***Nota: Conforme definido no "Target 2", os "Attack residues" são especificamente os artefatos que os invasores deixam para trás ao executar sua cadeia de ataque, como execução de comandos, criação de arquivos ou conexões de rede anômalas.***

### 🔵 **Task 5: Técnicas de caça**

O foco desta tarefa é apresentar o "COMO" (HOW) da caça a ameaças: os métodos práticos e as ferramentas que os threat hunters utilizam para procurar evidências concretas em diversas fontes de dados do ambiente.

Conceitos explorados:  
**Fontes de Dados (Data Sources):** Threat hunters buscam em múltiplas fontes, como event logs, dados de EDR (Endpoint Detection and Response), sistemas SIEM, tráfego de rede, logs de DNS, web logs e logs de aplicação. Um caçador habilidoso correlaciona evidências entre várias fontes, pois nenhuma fonte isolada conta a história completa.  

**Attack Signatures (Assinaturas de Ataque):** Padrões que indicam atividade maliciosa, como hashes de arquivos, parâmetros de linha de comando suspeitos (ex: `powershell.exe -EncodedCommand`), processos filhos incomuns (ex: `cmd.exe` spawnado por `winword.exe`) ou modificações em chaves de registro de persistência. São eficazes contra ameaças conhecidas, mas podem falhar contra variantes ou zero-days.  

**Indicators of Compromise (IOCs):** Artefatos específicos deixados por invasores (hashes, IPs, domínios, emails, URLs, chaves de registro) carregados em ferramentas para busca de correspondência exata. Produzem resultados objetivos, mas tornam-se obsoletos rapidamente conforme atacantes rotacionam sua infraestrutura.  

**Behavioral Pattern Analysis (Análise de Padrões Comportamentais):** Busca por sequências de eventos que, em conjunto, indicam atividade maliciosa, mesmo que eventos individuais pareçam benignos. Exemplos incluem cadeias de processos (Word → cmd → PowerShell → IP externo), padrões de acesso a arquivos ou sequências de movimento lateral. É poderosa por detectar ataques mesmo sem assinaturas ou IOCs conhecidos.  
**Logical Queries and Anomaly Detection (Consultas Lógicas e Detecção de Anomalias):** Uso de lógica condicional para encontrar combinações suspeitas de eventos que desviam da atividade normal do ambiente (ex: comandos de administrador às 3h da manhã, conta SYSTEM executando comandos interativos, conexões de saída em portas não padrão). Requer profundo conhecimento do que é "normal" no ambiente.  

**Integração de Métodos:** Caçadores eficazes raramente dependem de um único método. Uma caça abrangente combina múltiplas técnicas (ex: começar com IOCs, expandir para padrões comportamentais e finalizar com consultas lógicas) para maximizar a probabilidade de detectar ameaças conhecidas e desconhecidas.

- **Pergunta:** Qual é a técnica de pesquisa que utiliza hashes de ficheiros, endereços IP e nomes de domínio para procurar artefactos específicos?  
**Resposta:** 'Indicators of Compromise'  
***Nota: O texto define explicitamente IOCs como "specific artifacts left by attackers: file hashes, IP addresses, domain names, email addresses, URLs, and registry keys", sendo esta a técnica que busca correspondências exatas desses artefatos no ambiente.***

- **Pergunta:** Que técnica de pesquisa corresponde à seguinte expressão: «O Word.exe inicia o cmd.exe, que, por sua vez, inicia o powershell.exe, que se liga a um IP externo»?  
**Resposta:** 'Behavioral Pattern Analysis'  
***Nota: Esta cadeia de processos é o exemplo clássico dado no "Method 3: Behavioral Pattern Analysis", sob a categoria de "Process chains". A técnica foca em sequências de eventos que, em conjunto, revelam atividade maliciosa, mesmo que eventos individuais pareçam normais.***
