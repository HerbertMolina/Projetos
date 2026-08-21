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

### 🔵 **Task 4: Noções básicas de reconhecimento e evasão**

O foco desta tarefa é aplicar técnicas básicas de evasão durante a fase de reconhecimento (Reconnaissance) da Cyber Kill Chain, demonstrando como modificar o comportamento de ferramentas como o Nmap para reduzir a geração de alertas em um NIDS (Suricata) e HIDS (Wazuh).

Conceitos explorados:  
**Detecção Padrão do Nmap:** Comandos como `nmap -sV` executam ações predefinidas (como solicitar caminhos longos para gerar erros 404 e obter versões de serviço) que são facilmente detectadas por IDS devido a assinaturas conhecidas, como o User-Agent padrão do Nmap.  
**Evasão Parcial via User-Agent:** A alteração do User-Agent HTTP usando o argumento `--script-args http.useragent="<AGENT_AQUI>"` pode enganar regras básicas de assinatura, mas não impede a detecção baseada no comportamento agressivo da varredura.  
**Trade-off entre Evasão e Informação:** Técnicas de evasão mais furtivas, como o SYN scan (`-sS`), evitam a detecção de versão de serviço e reduzem drasticamente a quantidade de informações coletadas. É um equilíbrio semelhante ao uso de sonar ativo vs. passivo em guerra naval.  
**Contexto do Alvo:** A necessidade de evasão depende da posição do ativo. Ativos públicos podem estar sob ataque constante de botnets (enterrando seu tráfego no ruído), enquanto ativos internos críticos gerarão alarmes imediatos com um único alerta.  
**Definição de Evasão:** Pode ser **completa** (nenhum alerta gerado) ou **parcial** (alerta gerado, mas com severidade reduzida, sendo menos provável de ser investigado). O sistema de pontuação da sala reflete isso, penalizando menos alertas de baixa severidade.

- **Pergunta:** Que escala é utilizada para medir a gravidade dos alertas no Suricata? (*-*)  
**Resposta:** '1-3'  
***Nota: O Suricata utiliza uma escala de severidade de 1 a 3 para classificar a criticidade dos alertas gerados, onde 1 é baixa e 3 é alta.***
  
- **Pergunta:** Quantos serviços o nmap consegue identificar na totalidade quando se realiza a análise de serviços (-sV)?  
**Resposta:** '3'  
***Nota: Ao executar a varredura de versão de serviço (`-sV`) contra o alvo específico desta sala, o Nmap consegue identificar completamente 3 serviços rodando nas portas abertas.*** 

### 🔵 **Task 5: Mais manobras de evasão e reconhecimento**

O foco desta tarefa é explorar técnicas avançadas de evasão utilizando o scanner web Nikto, demonstrando como ajustar parâmetros de varredura (tuning) e opções de evasão para equilibrar a coleta de informações com a redução (ou, paradoxalmente, o aumento) de alertas no IDS.

Conceitos explorados:  
**Agressividade do Nikto:** O Nikto é inerentemente mais agressivo que o Nmap, gerando milhares de alertas (ex: ~7000) se executado com configurações padrão em múltiplas portas.  
**Scan Tuning (-T):** A capacidade de refinar a varredura para categorias específicas (ex: `-T 1 2 3` para arquivos interessantes, má configuração e divulgação de informações), evitando testes contraproducentes em um CTF, como vetores de Negação de Serviço (DoS).  
**Evasão no Nikto:** Alteração do User-Agent e uso de flags de evasão (`-e`), como codificação aleatória de URL e variação de caixa (casing).  
**O Paradoxo da Evasão:** Técnicas de evasão avançadas (como modificar o espaçamento de requisições ou codificação aleatória) podem, na verdade, *aumentar* a detectabilidade, pois IDS modernos (como o Suricata) identificam cabeçalhos inválidos ou caracteres inesperados como anomalias, somando-se às assinaturas de exploit conhecidas.  
**Evasão em Escala:** Estratégias teóricas de evasão incluem sobrecarregar o IDS com tráfego de botnets (DDoS no sensor), embora limitadores de throughput (rate-limiting) mitiguem isso na prática.

- **Pergunta:** Nikto, Se for encontrada uma rota interessante quando for realizada a primeira análise, como é que isso se chama?  
**Resposta:** '/login'  
***Nota: Ao executar a varredura inicial do Nikto nas portas 80 e 3000, o scanner identifica o caminho `/login` como um arquivo/diretório de interesse, indicando a presença de uma aplicação web interativa na porta 3000.*** 

- **Pergunta:** Que valor é utilizado para ativar ou desativar os vetores de negação de serviço quando se utiliza a opção de ajuste de varredura (-T) no Nikto?  
**Resposta:** '6'  
***Nota: Na documentação de tuning do Nikto, o valor `6` corresponde à categoria de testes de Negação de Serviço (DoS), que deve ser evitada em varreduras de CTF ou ambientes de produção para não causar indisponibilidade.*** 

- **Pergunta:** Que opções são utilizadas para alterar o espaçamento dos pedidos no Nikto? Utilize vírgulas para separar as opções na sua resposta.  
**Resposta:** '6,A,B'  
***Nota: As flags `6`, `A` e `B` (ou `6,a,b` em minúsculas) são utilizadas no Nikto para modificar o espaçamento e o tempo entre as requisições, tentando contornar limitações de taxa ou detecção baseada em volume de tráfego.***  

