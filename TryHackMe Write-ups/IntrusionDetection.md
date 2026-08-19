# Intrusion Detection

## 📊 Info  
- Dificuldade: Média  
- Categoria: Network Security / Intrusion Detection / Evasion  
- Data: 11/08/2026  
- Link: `https://tryhackme.com/room/idsevasion`    

## 🔍 Resumo  
O objetivo é introduzir o mundo dos Sistemas de Detecção de Intrusão (IDS) e técnicas de evasão cibernética, desafiando o aluno a orquestrar uma tomada de controle total do sistema enquanto experimenta técnicas de evasão em todas as etapas da Cyber Kill Chain, 
utilizando um sistema de pontuação de CTF interativo que avalia alertas de IDS.

## 🛠️ Processo  

### 🔵 **Task 1: Introdução**  

O foco desta tarefa é apresentar o conceito da sala, explicando que o objetivo vai além de apenas completar um CTF: é entender se e como as ações seriam detectadas por um Sistema de Detecção de Intrusão (IDS) e aprender a aplicar técnicas de evasão.

Conceitos explorados:  
**Intrusion Detection Systems (IDS):** Sistemas projetados para monitorar o tráfego de rede ou as atividades do sistema em busca de atividades maliciosas ou violações de políticas.  
**Cyber Evasion Techniques:** Métodos utilizados por atacantes para modificar seu tráfego ou comportamento a fim de evitar a detecção por sistemas de segurança, como IDS ou firewalls.  
**Cyber Kill Chain:** Modelo que descreve as fases de um ataque cibernético. A sala incentiva a experimentação de técnicas de evasão em *todas* as etapas desta cadeia.  

### 🔵 **Task 2: Noções básicas sobre deteção de intrusões**

O foco desta tarefa é introduzir os conceitos fundamentais dos Sistemas de Detecção de Intrusão (IDS), diferenciando suas metodologias de detecção e apresentando as ferramentas específicas que serão utilizadas na sala.

Conceitos explorados:  
**Intrusion Detection Systems (IDS):** Ferramentas de defesa de rede que automatizam a detecção de atividades suspeitas. Diferente de firewalls ou antivírus (que previnem/bloqueiam), o IDS monitora a atividade não restrita e classifica o que é malicioso ou benigno.  
**Metodologias de Detecção:**  
- **Signature-based (Baseada em Assinatura/Regras):** Aplica um grande conjunto de regras (rule sets) para buscar atividades suspeitas em uma ou mais fontes de dados.  
- **Anomaly-based (Baseada em Anomalia):** Estabelece uma linha de base (baseline) do que é considerado atividade normal e gera alertas quando uma atividade que não se encaixa nesse padrão é detectada.  
**Fluxo de Alertas:** Ao detectar um incidente, o IDS gera um alerta e o encaminha para plataformas de agregação de logs ou visualização de dados, como Graylog ou ELK Stack. Alguns podem ter capacidades de prevenção (IPS) e responder automaticamente.  
**Ferramentas da Sala:**  
- **Suricata:** Um IDS baseado em rede (NIDS - Network-based IDS).  
- **OSSEC:** Um IDS baseado em host (HIDS - Host-based IDS).  
Ambos implementam a metodologia de detecção por assinatura, mas seus comportamentos e os tipos de ataques que detectam diferem significativamente.

- **Pergunta:** Que metodologia de deteção de IDS se baseia em conjuntos de regras??  
**Resposta:** 'Signature-based detection'  
***Nota: O texto define explicitamente que os IDS "Signature (or rule) based" aplicam um grande conjunto de regras (rule set) para buscar atividades suspeitas, em contraste com os baseados em anomalia que usam linhas de base comportamentais.***

### 🔵 **Task 3: IDS Baseado em internet (NIDS)**  

O foco desta tarefa é introduzir os Sistemas de Detecção de Intrusão Baseados em Rede (NIDS), explicando como eles monitoram o tráfego de pacotes, seus pontos fortes, limitações e o impacto de tecnologias modernas de segurança neles.

Conceitos explorados:  
**Monitoramento de Rede:** NIDS inspeciona pacotes de rede em busca de atividades hostis ou indesejadas, como comando e controle (C2) de malware, ferramentas de exploração, varreduras (scanning), exfiltração de dados, contato com sites de phishing e violações de políticas corporativas.  
**Vantagens e Desafios:** Uma única instalação pode monitorar toda a rede, facilitando o deployment. No entanto, NIDS são mais propensos a falsos positivos devido ao alto volume de tráfego e à dificuldade de criar regras flexíveis que diferenciem tráfego malicioso de aplicações legítimas.  
**Deployment e Prevenção:** Geralmente implantados no lado LAN do firewall. Podem incluir funcionalidade de Prevenção de Intrusão (IPS) para bloquear nós automaticamente, embora isso seja frequentemente desativado devido à alta taxa de falsos positivos.  
**Impacto da Criptografia:** A confiabilidade do NIDS é adversamente afetada pela adoção generalizada de criptografia em trânsito, pois o sistema não consegue inspecionar o conteúdo de pacotes criptografados sem as chaves adequadas.  
**Ferramenta em Uso:** O nó de destino nesta sala é protegido pelo NIDS de código aberto **Suricata**, com o modo IPS desativado para permitir testes livres de ataques e observação dos alertas gerados.

- **Pergunta:** Que protocolo amplamente implementado tem um efeito negativo na fiabilidade dos NIDS?  
**Resposta:** 'TLS'  
***Nota: O texto destaca que os NIDS dependem do acesso a toda a comunicação entre os nós e, portanto, são afetados pela adoção generalizada de criptografia em trânsito. O protocolo TLS (Transport Layer Security) é o padrão amplamente implementado que criptografa esse tráfego,
impedindo a inspeção profunda de pacotes pelo NIDS.***   


