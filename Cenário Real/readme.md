# Cenários Reais | OSINT, Investigação e Attack Surface Management

> **Enxergar o que está oculto. Proteger o que importa.**

Este espaço reúne investigações técnicas, análises de exposição digital, mapeamento de superfície de ataque (ASM), reconhecimento e avaliações de segurança realizadas em cenários reais autorizados e ambientes controlados.

O objetivo não é apenas identificar informações ou executar ferramentas, mas compreender o que cada descoberta representa, verificar sua relevância e estabelecer correlações entre diferentes fontes de informação.

A metodologia prioriza a investigação técnica, a validação manual e a interpretação dos resultados pelo profissional.

---

## Objetivo

Demonstrar a aplicação prática de técnicas de OSINT, reconhecimento, análise de infraestrutura e avaliação de exposição digital.

As atividades buscam identificar:

- Ativos digitais associados a um domínio ou organização.
- Informações públicas que possam revelar exposição desnecessária.
- Serviços e tecnologias acessíveis externamente.
- Registros DNS e informações relacionadas à infraestrutura.
- Subdomínios, certificados e possíveis relações entre ativos.
- Portas, serviços e versões que mereçam investigação.
- Configurações potencialmente inadequadas.
- Indícios de vulnerabilidades e possíveis pontos de risco.

Cada descoberta é analisada individualmente, considerando contexto, evidências, relevância e limitações técnicas.

---

## Metodologia de trabalho

### Reconhecimento e coleta de informações

A investigação começa pela identificação do alvo e pela coleta de informações disponíveis em fontes públicas.

São utilizados serviços online, mecanismos de pesquisa, bases de dados e ferramentas especializadas para reunir informações que possam contribuir para o entendimento da presença digital do ativo investigado.

Exemplos:

- WHOIS e RDAP.
- ViewDNS.
- crt.sh.
- Shodan.
- Censys.
- Netlas.
- OSINT Framework.
- theHarvester.
- Mecanismos de pesquisa e fontes públicas.

### Verificação individual dos serviços

**A investigação não se resume a executar um scanner e aceitar automaticamente tudo o que ele apresenta.**

Sempre que aplicável, os serviços e informações identificados são examinados separadamente.

São realizadas consultas específicas para compreender o comportamento de cada serviço, validar informações coletadas e identificar possíveis inconsistências.

Essa abordagem permite aprofundar a análise e evitar que resultados genéricos sejam tratados como descobertas confirmadas.

### Análise técnica e correlação

Os resultados obtidos por ferramentas locais e serviços online passam por avaliação manual.

Nesta etapa, são examinadas as relações entre as informações coletadas.

Exemplos:

- Correlação entre domínio, DNS e endereços IP.
- Comparação entre registros DNS atuais e históricos.
- Identificação de possíveis relações entre subdomínios e infraestrutura.
- Verificação de serviços expostos e tecnologias identificadas.
- Análise de informações obtidas em diferentes fontes.
- Investigação de possíveis divergências entre os resultados.

Uma informação isolada pode não representar um risco. Entretanto, quando correlacionada com outras evidências, pode revelar uma exposição relevante.

### Validação das descobertas

Antes de considerar qualquer informação como uma descoberta técnica, são avaliados:

- Confiabilidade da fonte.
- Atualidade da informação.
- Possibilidade de falso positivo.
- Evidências que sustentam a descoberta.
- Contexto de exposição.
- Impacto potencial.
- Necessidade de verificações adicionais.

Os resultados são classificados de acordo com o nível de confirmação, distinguindo fatos observados, indícios e hipóteses investigativas.

### Documentação e relatório técnico

Após a investigação, as informações relevantes são organizadas e interpretadas.

Os resultados passam por uma revisão técnica antes de serem incorporados ao relatório final.

A documentação pode incluir:

- Objetivo e escopo.
- Metodologia utilizada.
- Ferramentas e fontes consultadas.
- Evidências coletadas.
- Análise técnica.
- Descobertas e possíveis impactos.
- Limitações da investigação.
- Recomendações de segurança.

---

## Ferramentas e serviços

As ferramentas são selecionadas conforme a necessidade de cada investigação. Não existe dependência de uma única plataforma ou solução automatizada.

**OSINT e inteligência de fontes abertas**
- ViewDNS
- Shodan
- Censys
- Netlas
- crt.sh
- theHarvester
- OSINT Framework

**Reconhecimento e infraestrutura**
- Nmap
- Amass
- Subfinder
- httpx
- Wappalyzer
- DNS e WHOIS/RDAP

**Avaliação de segurança**
- Burp Suite
- Nuclei
- Nessus
- ffuf
- Gobuster
- Pentest-Tool

**Análise e documentação**
- Linux / Kali Linux
- Python
- Bash
- Git / GitHub

*As ferramentas são utilizadas conforme o escopo, a finalidade e o nível de autorização de cada atividade. A presença de uma ferramenta nesta lista não significa que ela seja utilizada em todos os cenários.*

---

## Princípios da investigação

- **Análise humana:** ferramentas auxiliam na coleta, mas a interpretação técnica é responsabilidade do profissional.
- **Validação:** resultados não são considerados verdadeiros apenas porque foram apresentados por uma ferramenta.
- **Correlação:** informações de diferentes fontes são comparadas para construir um contexto mais consistente.
- **Precisão:** evitar conclusões precipitadas e classificações sem evidências suficientes.
- **Rastreabilidade:** preservar referências, registros e evidências que sustentem as descobertas.
- **Contextualização:** compreender o ambiente antes de atribuir risco a um serviço ou tecnologia.
- **Responsabilidade:** respeitar escopo, autorização, privacidade e limites legais.


---

Nem toda informação encontrada representa uma vulnerabilidade.

Um serviço acessível, uma tecnologia identificada ou uma porta aberta não configuram automaticamente uma falha de segurança.

A relevância de cada descoberta depende do contexto, da configuração, da exposição e das evidências disponíveis.

Por isso, o trabalho não consiste apenas em encontrar informações, mas em investigar o que elas significam.

---

## ⚠️ Aviso e responsabilidade

As investigações publicadas possuem finalidade educacional, pesquisa e demonstração de competências técnicas.

Atividades envolvendo ativos de terceiros são realizadas somente mediante autorização e dentro dos limites estabelecidos para cada avaliação.

Informações sensíveis, credenciais, dados pessoais e detalhes que possam comprometer a segurança de terceiros são omitidos ou substituídos por dados fictícios quando necessário.

---

**Herbert Molina | Cibersegurança**

*Investigação • OSINT • Attack Surface Management • Reconhecimento • Análise de Exposição Digital*

<img width="1220" height="1289" alt="redesociais" src="https://github.com/user-attachments/assets/d45f05ea-cd76-4ba2-934d-0571036fa533" />
