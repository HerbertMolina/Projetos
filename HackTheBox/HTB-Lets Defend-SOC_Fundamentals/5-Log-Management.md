# Relatório de Aprendizado: Gerenciamento de Log  

> **Curso:** SOC Fundamentals — Let's Defend / Hack The Box  
**Módulo:** Log Management  
**Data:** Outubro de 2026  
**Nível:** Técnico Inicial  
**Status:** Concluído  
> 

---

## Objetivo de Aprendizado

Compreender a função central do Gerenciamento de Logs na consolidação de dados de segurança, sua aplicação prática na validação de incidentes e na caça a ameaças, e a importância de saber o que procurar e onde procurar em diferentes fontes de log.

---

## Conceitos-Chave Abordados

### Definição e Centralização

- O Gerenciamento de Logs fornece acesso unificado a todos os registros de um ambiente (logs da Web, sistema operacional, firewall, proxy, EDR, etc.) em um único local.
- Essa centralização aumenta drasticamente a eficiência da investigação e reduz a margem de erro, eliminando a necessidade de consultar dispositivos ou sistemas individualmente.

### Propósito na Investigação de Incidentes

- **Validação de Comunicação com C2:** Ao identificar um malware, o analista utiliza o gerenciamento de logs para pesquisar o endereço de Comando e Controle (ex: "letsdefend.io") e verificar se algum dispositivo da rede tentou se comunicar com ele.
- **Caça a Ameaças Não Detectadas (Threat Hunting):** Quando um alerta do SIEM indica um vazamento de dados de um host específico para um IP suspeito, isolar o host não é suficiente. O analista deve pesquisar esse IP suspeito em *todos* os logs para garantir que nenhum outro dispositivo da rede foi comprometido ou tentou a mesma comunicação, cobrindo possíveis falhas de detecção do sistema.

### Tipos de Fontes de Log

- Exemplos práticos no ambiente Let's Defend incluem logs de **Proxy**, **Exchange** e **Firewall**, que podem ser consultados simultaneamente através de uma única busca unificada.

---

## Aplicação Prática / Laboratório

> *Módulo com exercícios práticos de busca básica em logs no ambiente Let's Defend.*
> 

**Anotações pessoais:**

- Exercício de busca reversa: Identificar o endereço IP de origem que acessou uma URL específica (ex: repositório público no GitHub).
- Exercício de identificação de fonte: Determinar o tipo de log (logtype) com base em atributos de rede específicos, como porta de destino e endereço IP de origem.
- A prática reforça que a investigação não termina no alerta inicial do SIEM, mas se aprofunda nos logs brutos para garantir a contenção total do incidente.

---

## Conexão com OSINT e Portfólio Profissional

A metodologia de Gerenciamento de Logs tem paralelos diretos e valiosos com a coleta e correlação de dados em investigações de OSINT:

- **Agregação de Fontes:** Assim como o SOC centraliza logs de firewall, proxy e EDR, uma investigação de OSINT eficaz agrega dados de múltiplas fontes abertas (WHOIS, registros DNS, metadados, redes sociais) para evitar a visão limitada de consultar apenas uma plataforma.
- **Expansão da Investigação (Pivotagem):** A prática de buscar um IOC (Indicador de Comprometimento) em *todos* os logs após isolar um único host é idêntica à técnica de OSINT de pivotagem. Ao encontrar um ativo de um alvo (ex: um e-mail, telefone ou IP), o investigador deve buscar esse mesmo indicador em todas as outras bases de dados disponíveis para descobrir conexões ocultas ou ativos adicionais que a busca inicial não revelou.
- **Precisão na Consulta:** Saber "o que procurar e onde procurar" em logs é a mesma habilidade necessária para construir *dorks* avançadas e filtros precisos no OSINT, eliminando ruído e encontrando o dado exato necessário para a tomada de decisão.

---

**Pergunta**

Qual endereço IP de origem digitou o URL 'https:// github .com/apache/flink/compare'?

'*172.16.17.54*'

Qual é o tipo de log que tem um número de porta de destino de 52567 e um endereço IP de origem de 8.8.8.8?

'*dns*'
