# SOC Fundamentals - Let's Defend / Hack The Box
**Link do Treinamento -** https://app.letsdefend.io/training/lessons/soc-fundamentals

> Documentação estruturada do percurso de aprendizado no curso SOC Fundamentals, com foco na aplicação prática de conceitos de Blue Team e operações de Security Operations Center (SOC) em investigações de Inteligência de Fontes Abertas (OSINT).

---

## Sobre o Projeto

Este repositório contém uma série de relatórios técnicos e reflexivos desenvolvidos durante a conclusão do curso SOC Fundamentals da plataforma Let's Defend (Hack The Box). 

O objetivo principal desta documentação é dupla:
1. Consolidar o conhecimento técnico sobre as operações, ferramentas e fluxos de trabalho de um SOC moderno.
2. Estabelecer pontes metodológicas claras entre a análise defensiva de segurança e a prática de investigações OSINT, especialmente voltadas para comércio físico sem presença digital e investigação de pessoas.

---

## Módulos Documentados

A seguir, a relação dos relatórios individuais que compõem esta trilha de aprendizado:

* **Introdução ao SOC:** Estrutura, operação e ecossistema de ferramentas.
* **SOC Types and Roles:** Modelos de operação (In-house, Virtual, Co-Managed, Command) e funções da equipe.
* **Analista de SOC e suas Responsabilidades:** Rotina de triagem e habilidades fundamentais (SO, Redes, Malware).
* **Relação entre SIEM e Analista:** Fluxo de trabalho, gestão de alertas e otimização de regras.
* **Gerenciamento de Log:** Centralização de dados, busca unificada e validação de incidentes.
* **EDR - Detecção e Resposta de Endpoints:** Visibilidade de processos, investigação ao vivo e contenção de hosts.
* **SOAR - Orquestração, Automação e Resposta:** Playbooks, automação de tarefas e centralização de fluxos de trabalho.
* **Feed de Inteligência de Ameaças:** Validação de IOCs, limitações de ferramentas automatizadas e contexto temporal.
* **Erros Comuns Cometidos por Analistas de SOC:** Armadilhas analíticas, falsos negativos e a importância do pensamento crítico.

---

## Competências Desenvolvidas

* **Análise de Artefatos:** Capacidade de extrair e correlacionar indicadores de comprometimento (IPs, hashes, domínios) a partir de alertas brutos.
* **Metodologia de Investigação:** Aplicação de fluxos padronizados (playbooks) para garantir consistência, rastreabilidade e ausência de viés na análise.
* **Pensamento Crítico sobre Dados:** Compreensão das limitações de ferramentas automatizadas (como VirusTotal e sandboxes) e a necessidade vital de validação cruzada e análise contextual.
* **Visão Sistêmica de Segurança:** Entendimento de como as ações de um atacante são registradas em diferentes camadas (Endpoint, Rede, Proxy) e como defender esses perímetros.

---

## A Interseção com OSINT e Portfólio Profissional

A principal proposta de valor desta documentação é a tradução de conceitos de SOC para a prática de OSINT. As competências adquiridas neste curso impactam diretamente a qualidade das investigações de campo:

* **Pivotagem de Indicadores:** A técnica de buscar um hash ou IP em todos os logs do SOC é idêntica à pivotagem em OSINT. Encontrar um dado de um alvo exige a busca desse mesmo indicador em todas as bases de dados disponíveis para mapear a extensão total de suas conexões.
* **Consciência de Rastros Digitais:** Entender como um SOC monitora e armazena logs ajuda o investigador de OSINT a saber quais ações deixam rastros definitivos, refinando as técnicas de coleta de inteligência e a avaliação de risco do alvo.
* **Validação e Temporalidade:** A armadilha do cache em feeds de ameaças espelha o risco de usar dados desatualizados em OSINT (ex: domínios ou números de telefone reatribuídos). A disciplina de verificar carimbos de data e hora (timestamps) e forçar consultas atualizadas é aplicada em ambos os campos.
* **Padronização de Relatórios:** A rigidez dos processos de um SOC (como os playbooks do SOAR) inspira a criação de checklists e fluxos de trabalho próprios para investigações de OSINT, garantindo que nenhum detalhe seja negligenciado, mesmo em cenários de alto volume de trabalho.

---

<div align="center">

*Portfólio de Cibersegurança — Blue Team & OSINT*  
*Documentação gerada em Outubro de 2026*

</div>
