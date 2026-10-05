# Relatório de Aprendizado: SOC Types and Roles

> **Curso:** SOC Fundamentals — Let's Defend / Hack The Box
> **Módulo:** SOC Types and Roles
> **Data:** Outubro de 2026
> **Nível:** Fundacional
> **Status:** Concluído

---

## Objetivo de Aprendizado

Compreender as diferentes estruturas organizacionais de um *Security Operations Center* (SOC), os três pilares fundamentais de sua operação (Pessoas, Processos e Tecnologia) e as responsabilidades específicas de cada função dentro da equipe de segurança.

---

## Conceitos-Chave Abordados

### Definição de SOC
Uma facility (física ou virtual) onde a equipe de segurança da informação monitora e analisa continuamente a segurança de uma organização, com o propósito principal de detectar, analisar e responder a incidentes cibernéticos.

### Modelos de SOC
| Modelo | Descrição |
|---|---|
| **In-house SOC** | Equipe interna construída e mantida pela própria organização. Requer orçamento dedicado para sua continuidade. |
| **Virtual SOC** | Equipe sem instalação física permanente, operando de forma remota e distribuída em várias localidades. |
| **Co-Managed SOC** | Modelo híbrido onde a equipe interna de SOC trabalha em coordenação com um provedor externo de serviços gerenciados de segurança (MSSP). |
| **Command SOC** | Equipe de alto nível que supervisiona SOCs menores em uma grande região (comum em provedores de telecomunicações e agências de defesa). |

### Os Três Pilares: Pessoas, Processos e Tecnologia
*   **Pessoas:** Profissionais altamente treinados, capazes de se adaptar a novos cenários de ataque e dispostos a pesquisar continuamente.
*   **Processos:** Ações extremamente padronizadas, alinhadas a frameworks e requisitos de segurança como *NIST, PCI e HIPAA*, garantindo que nenhuma etapa seja negligenciada.
*   **Tecnologia:** Ferramentas de detecção, prevenção e análise. A escolha deve considerar o orçamento e a realidade da organização, não apenas o produto "mais famoso" do mercado.

### Funções (Roles) no SOC
| Função | Responsabilidade Principal |
|---|---|
| **SOC Analyst (L1, L2, L3)** | Classifica alertas, investiga a causa raiz e aconselha sobre a remediação. |
| **Incident Responder** | Responsável pela detecção de ameaças e realiza a avaliação inicial de violações de segurança. |
| **Threat Hunter** | Profissional que busca *proativamente* ameaças e vulnerabilidades (como APTs) que podem ter evadido as medidas de segurança tradicionais. |
| **Security Engineer** | Mantém a infraestrutura de segurança, como a integração e manutenção de soluções SIEM e SOAR. |
| **SOC Manager** | Responsável por orçamento, estratégia, gestão de equipe e coordenação operacional (foco gerencial, não técnico). |

---

## Aplicação Prática / Laboratório

> *Módulo teórico focado no mapeamento do ecossistema de segurança corporativa. Estabelece o vocabulário e a estrutura organizacional necessários antes da operação técnica nas ferramentas.*

**Anotações pessoais:**
- A distinção entre *Incident Responder* (reativo/inicial) e *Threat Hunter* (proativo) é crucial para entender o fluxo de trabalho de uma equipe madura.
- O pilar "Processos" reforça que a tecnologia sozinha não resolve problemas; a padronização (ex: NIST) é o que garante a repetibilidade e a qualidade da resposta.

---

## Conexão com OSINT e Portfólio Profissional

Este módulo tem aplicação direta na estruturação dos meus próprios serviços de OSINT:

1. **Alinhamento com Processos:** Assim como um SOC segue frameworks (NIST, PCI), minhas investigações de OSINT (seja para comércio físico ou pessoas) devem seguir um fluxo padronizado e documentado, garantindo confiabilidade e rastreabilidade das fontes.
2. **Mentalidade de Threat Hunting:** A função de *Threat Hunter* é essencialmente uma investigação proativa. Isso se alinha perfeitamente com a investigação de pessoas ou comércios sem presença digital, onde é necessário "caçar" indicadores e conexões ocultas antes que se tornem um problema ou para validar uma oportunidade.
3. **Conhecimento do Público-Alvo:** Entender as dores de um *SOC Manager* ou *Security Engineer* me ajuda a formatar relatórios de OSINT que sejam diretamente acionáveis e valiosos para equipes de defesa corporativa.

---
