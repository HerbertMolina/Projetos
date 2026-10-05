# Relatório de Aprendizado: Analista de SOC e suas Responsabilidades

> **Curso:** SOC Fundamentals — Let's Defend / Hack The Box
> **Módulo:** SOC Analyst and Their Responsibilities
> **Data:** Outubro de 2026
> **Nível:** Fundacional
> **Status:** Concluído

---

## Objetivo de Aprendizado

Compreender o papel central do Analista de SOC como primeira linha de defesa, sua rotina diária de triagem e as três habilidades técnicas fundamentais necessárias para investigar alertas com eficácia: 
Sistemas Operacionais, Redes e Análise de Malware.

---

## Conceitos-Chave Abordados

### O Papel do Analista
*   **Primeira Linha de Investigação:** O analista é o primeiro a investigar ameaças ao sistema.
*   **Triagem e Escalonamento:** Responsável por determinar a veracidade da ameaça e, se necessário, escalar o incidente para supervisores ou equipes de resposta para mitigação.
*   **Dinamismo da Função:** A variedade constante de vetores de ataque e malware torna o trabalho menos monótono, exigindo adaptação e aprendizado contínuo.

### Rotina Diária
*   Análise contínua de alertas gerados pelo **SIEM**.
*   Validação de ameaças reais utilizando ferramentas complementares como **EDR** (Endpoint Detection and Response), **Gerenciamento de Logs** e **SOAR**.

### Habilidades Técnicas Fundamentais
| Área de Conhecimento | Aplicação na Prática do Analista |
|---|---|
| **Sistemas Operacionais** | Conhecer profundamente o comportamento "normal" do Windows e Linux para identificar com precisão atividades anormais ou serviços suspeitos. |
| **Redes de Computadores** | Rastrear IPs e URLs maliciosos, verificar se há dispositivos internos tentando se conectar a eles e identificar potenciais vazamentos de dados na rede. |
| **Análise de Malware** | Determinar o propósito real do código malicioso, identificar táticas de evasão e, crucialmente, detectar comunicação com servidores de Comando e Controle (C2). |

---

## Aplicação Prática / Laboratório

> *Módulo teórico focado no mapeamento de competências. Estabelece a base de conhecimento prévio necessária antes de operar as ferramentas técnicas (como o SIEM) nos próximos laboratórios.*

**Anotações pessoais:**
*   A premissa "para saber o que é anormal, primeiro é preciso saber o que é normal" é a regra de ouro tanto para o SOC quanto para investigações externas.  

---

## Conexão com OSINT e Portfólio Profissional

As responsabilidades descritas para o Analista de SOC possuem paralelos diretos e valiosos com a prática de OSINT:

*   **Linha de Base de Normalidade:** Assim como o analista precisa saber o que é um serviço normal do Windows, no OSINT preciso saber o que é um padrão normal de atividade digital para um comércio físico ou perfil pessoal, permitindo que anomalias (como contas falsas ou movimentações suspeitas) saltem aos olhos.
*   **Investigação de Redes (IPs e URLs):** A capacidade de rastrear conexões maliciosas é o cerne da inteligência de fontes abertas. Entender como um SOC correlaciona um alerta de firewall a um endpoint interno me ajuda a construir investigações de infraestrutura digital mais robustas.
*   **Identificação de Comando e Controle (C2):** A lógica de encontrar o "cérebro" por trás de um malware é a mesma usada para identificar a fonte real ou os beneficiários ocultos por trás de uma rede de perfis falsos ou empresas de fachada.

---

do a ponte com seus objetivos de OSINT e investigação.
*   Você salva no seu portfólio.
