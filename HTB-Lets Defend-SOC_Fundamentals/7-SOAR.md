# Relatório de Aprendizado: SOAR - Orquestração, Automação e Resposta de Segurança

> **Curso:** SOC Fundamentals — Let's Defend / Hack The Box  
**Módulo:** SOAR (Security Orchestration Automation and Response)  
**Data:** Outubro de 2026  
**Nível:** Técnico Inicial  
**Status:** Concluído  
> 

---

## Objetivo de Aprendizado

Compreender o papel do SOAR na integração de ferramentas de segurança, na automação de tarefas repetitivas e na padronização de investigações por meio de playbooks, aumentando a eficiência, a velocidade e a consistência da equipe do SOC.

---

## Conceitos-Chave Abordados

### Definição e Propósito

- **Integração e Automação:** Permite que diferentes produtos e ferramentas de segurança trabalhem em conjunto, automatizando tarefas manuais e repetitivas (como consultar automaticamente o VirusTotal para um endereço IP gerado por um alerta do SIEM).
- **Soluções de Mercado:** Exemplos citados incluem Splunk Phantom, IBM Resilient, Logsign e Demisto.

### Benefícios Principais

- **Economia de Tempo:** Automatização de fluxos de trabalho (workflows) comuns, como verificação de reputação de IP, consulta de hashes de arquivos e envio de amostras para análise em sandbox.
- **Centralização:** Funciona como uma plataforma unificada que integra diversas ferramentas (sandbox, gerenciamento de logs, APIs de terceiros), evitando a necessidade de alternar constantemente entre diferentes interfaces.
- **Playbooks:** Guias passo a passo para a investigação de diferentes cenários de alerta. Garantem que todos os analistas sigam os mesmos procedimentos padronizados (ex: obrigatoriedade de verificar a reputação de um IP), eliminando inconsistências e erros humanos na equipe.

### Aplicação no Let's Defend

- O módulo de "Gestão de Casos" (Case Management) simula a funcionalidade básica de um SOAR.
- Ao abrir um ticket de caso, um playbook é atribuído automaticamente, orientando o analista nas etapas exatas de investigação do alerta do SIEM associado.

---

## Aplicação Prática / Laboratório

> *Módulo focado na compreensão conceitual e na simulação do fluxo de "Gestão de Casos" e execução de playbooks no ambiente Let's Defend.*
> 

**Anotações pessoais:**

- A atribuição automática de playbooks a casos abertos é crucial para garantir que analistas, especialmente em cenários de alto volume de alertas, não pulem etapas críticas de validação.
- A automação de consultas básicas transforma minutos de trabalho manual em segundos, permitindo que o analista foque sua energia cognitiva na análise contextual e na tomada de decisão, em vez da coleta bruta de dados.

---

## Conexão com OSINT e Portfólio Profissional

A lógica e os benefícios do SOAR são diretamente aplicáveis à otimização de fluxos de trabalho em investigações de OSINT:

- **Automação de Coleta de Dados:** Assim como o SOAR consulta automaticamente o VirusTotal, investigações de OSINT podem ser otimizadas com scripts ou ferramentas que automatizam a busca de um indicador (IP, domínio, e-mail, nome) em múltiplas fontes abertas simultaneamente, economizando horas de trabalho manual.
- **Playbooks de Investigação:** Criar checklists ou "playbooks" pessoais para diferentes cenários de OSINT (ex: investigação de comércio físico sem presença digital, verificação de antecedentes de pessoas) garante que nenhuma fonte de dados seja esquecida. Isso assegura que a qualidade e a profundidade do relatório sejam consistentes, independentemente do volume de casos ou do cansaço do investigador.
- **Centralização de Evidências:** A ideia de uma "plataforma única" do SOAR reflete a necessidade de consolidar todas as descobertas de OSINT em um único local de análise (como um caderno digital estruturado ou ferramenta de link analysis), evitando a fragmentação de evidências e facilitando a geração do relatório final para o cliente.
