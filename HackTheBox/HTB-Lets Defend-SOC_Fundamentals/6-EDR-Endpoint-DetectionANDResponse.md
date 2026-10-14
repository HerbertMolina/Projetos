# Relatório de Aprendizado: EDR - Detecção e Resposta de Endpoints

> **Curso:** SOC Fundamentals — Let's Defend / Hack The Box  
**Módulo:** EDR - Endpoint Detection and Response 
**Data:** Outubro de 2026  
**Nível:** Técnico Inicial  
**Status:** Concluído  
> 

---

## Objetivo de Aprendizado

Compreender a função crítica das soluções de *Endpoint Detection and Response* (EDR) no monitoramento contínuo de dispositivos, na investigação profunda de atividades suspeitas e na aplicação de medidas de contenção para impedir a movimentação lateral de ameaças na rede.

---

## Conceitos-Chave Abordados

### Definição e Propósito do EDR

- Solução integrada de segurança que combina monitoramento contínuo em tempo real e coleta de dados do endpoint com recursos de resposta e análise automatizados baseados em regras.
- Ferramentas de mercado citadas: CarbonBlack, SentinelOne e FireEye HX.

### Capacidades de Investigação

- **Busca por IOC (Indicadores de Comprometimento):** Possibilidade de pesquisar um indicador específico (endereço IP, hash de arquivo, nome de processo) em todos os hosts da rede simultaneamente para identificar o escopo de um ataque.
- **Visibilidade do Dispositivo:** Acesso a informações detalhadas do endpoint, incluindo histórico do navegador, conexões de rede ativas e lista de processos em execução.
- **Investigação ao Vivo:** Capacidade de conectar-se diretamente à máquina comprometida para realizar uma análise forense ou de comportamento em tempo real.

### Contenção de Incidentes

- **Isolamento de Rede:** Ação crítica para impedir que um invasor se comunique com servidores externos ou realize movimentação lateral na rede interna.
- **Isolamento com Visibilidade:** O recurso de contenção do EDR desconecta o dispositivo das redes internas e externas, mas mantém um canal de comunicação exclusivo com o centro de gerenciamento do EDR, permitindo que a investigação e a análise continuem mesmo com a máquina isolada.

---

## Aplicação Prática / Laboratório

> *Módulo com foco na interface de "Segurança de Endpoint" do Let's Defend, praticando a busca de hosts, análise de processos e aplicação de políticas de contenção.*
> 

**Anotações pessoais:**

- A busca proativa por um hash MD5 específico em todos os hosts é uma das ações mais poderosas para determinar a extensão real de um comprometimento, indo muito além do alerta inicial que pode ter sido gerado em apenas uma máquina.
- A distinção entre isolar completamente uma máquina e isolá-la mantendo o canal com o EDR é fundamental para uma resposta a incidentes eficaz.

---

## Conexão com OSINT e Portfólio Profissional

As funcionalidades do EDR possuem paralelos metodológicos diretos com técnicas avançadas de OSINT:

- **Pivotagem de Indicadores (IOC Hunting):** A prática de pegar um hash ou IP e buscá-lo em *todos* os endpoints é idêntica à pivotagem em OSINT. Ao encontrar um dado de um alvo (ex: um número de telefone ou nome de usuário), o investigador deve buscar esse mesmo indicador em todas as bases de dados disponíveis para mapear a extensão total da presença digital ou das conexões ocultas do alvo.
- **Análise de Processos e Conexões:** A capacidade do EDR de mostrar quais processos estão se comunicando com a rede reflete a análise de metadados e infraestrutura em OSINT. Entender como um sistema operacional se comporta "por baixo do capô" ajuda a identificar anomalias, seja em um servidor corporativo ou ao analisar a infraestrutura técnica de um site ou perfil investigado.
- **Lógica de Contenção:** Compreender como as equipes de defesa isolam ativos ajuda a prever como alvos em investigações de OSINT podem reagir ou quais rastros digitais podem ser preservados ou cortados quando medidas defensivas são acionadas.
