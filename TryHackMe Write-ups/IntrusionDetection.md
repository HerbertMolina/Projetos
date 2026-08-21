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

O foco desta tarefa é aplicar técnicas básicas de evasão durante a fase de reconhecimento (Reconnaissance) da Cyber Kill Chain

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

Explorando técnicas avançadas de evasão utilizando o scanner web Nikto, demonstrando como ajustar parâmetros de varredura (tuning) e opções de evasão para equilibrar a coleta de informações com a redução (ou, paradoxalmente, o aumento) de alertas no IDS.

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

### 🔵 **Task 6: Inteligência de fontes abertas**

Demonstrar como a Inteligência de Fontes Abertas (OSINT) atua como um "sonar passivo", coletando informações valiosas sem enviar sondagens ativas que possam acionar alertas no IDS, explorando dados que o alvo ou terceiros já divulgaram publicamente.

Conceitos explorados:  
**OSINT como Evasão Passiva:** Diferente de scanners ativos (Nmap, Nikto), o OSINT é praticamente indetectável por IDS, pois depende de informações já expostas ou adquiridas de fontes desconectadas do alvo direto.  
**Fontes de Terceiros:** Ferramentas como Shodan (para serviços ativos), mecanismos de busca com operadores avançados, scanners de subdomínios (recon-ng) e consultas WHOIS/ASN podem revelar infraestrutura sem tocar no alvo.  
**Fontes do Próprio Alvo:** Páginas de erro, extensões de arquivo, páginas de debug, cabeçalhos de servidor (Server tag) e até listagens de vagas de emprego podem vazar detalhes sobre a stack tecnológica utilizada.  
**Limitações do OSINT:** Depende da disposição do alvo em divulgar dados. Protocolos como WireGuard, que não respondem a consultas não autenticadas, são invisíveis a scanners de terceiros como o Shodan.

- **Pergunta:** Que versão do Grafana está a ser executada no servidor?  
**Resposta:** '8.2.5'  
***Nota: Ao inspecionar o site público ou utilizar técnicas de OSINT (como verificar o cabeçalho do servidor ou páginas de erro), é possível identificar que a instância do Grafana em execução está na versão 8.2.5.*** 

- **Pergunta:** Qual é o ID da vulnerabilidade CVE grave que afeta esta versão do Grafana?  
**Resposta:** 'CVE-2021-43798'  
***Nota: A versão 8.2.5 do Grafana é vulnerável à falha crítica de divulgação de arquivos (Directory Traversal) identificada como CVE-2021-43798, também conhecida como "Grafana 8.x Authentication Bypass".***  

- **Pergunta:** Se este servidor estivesse disponível ao público, que site poderia já ter informações sobre os seus serviços?  
**Resposta:** 'shodan'  
***Nota: O Shodan é o motor de busca especializado em dispositivos conectados à internet, sendo a principal fonte de informação passiva sobre serviços, portas e banners expostos publicamente antes mesmo de qualquer varredura direta.*** [[14]]

- **Pergunta:** Como poderíamos procurar ficheiros PDF no site «example.com», utilizando os parâmetros de pesquisa avançada do Google?  
**Resposta:** 'site:example.com filetype:pdf'  
***Nota: A combinação dos operadores de busca avançada `site:` (para restringir ao domínio) e `filetype:` (para filtrar pela extensão do arquivo) é a técnica padrão de Google Dorking para este cenário.***

### 🔵 **Task 7: Conjuntos de regras**

Importância e as limitações dos conjuntos de regras (rulesets) em IDS baseados em assinatura, explorando uma vulnerabilidade crítica conhecida (CVE-2021-43798 no Grafana) para observar se o IDS consegue detectá-la ou se a evasão é bem-sucedida devido a lacunas na cobertura das regras.

Conceitos explorados:  
**Qualidade do Ruleset:** A eficácia de um IDS baseado em assinatura depende totalmente da qualidade, atualização e precisão de suas regras. Regras imprecisas geram falsos positivos ou falsos negativos, comprometendo a segurança.  
**Exploração de Vulnerabilidade Conhecida:** Uso de um script de exploit público (ex: `GrafanaDirInclusion`) para abusar de uma falha de inclusão de diretório, permitindo a leitura de arquivos do sistema com os privilégios do usuário que executa o serviço.  
**Análise de Detecção:** Após a exploração, a verificação do histórico de alertas do IDS revela se a ação foi detectada. Em alguns casos, como a leitura de arquivos sensíveis (`/etc/shadow`), o NIDS (Suricata) pode gerar um alerta, enquanto em outros cenários a exploração pode passar despercebida, destacando a necessidade de defesa em camadas (como um HIDS).

- **Pergunta:** Qual é a palavra-passe da conta grafana-admin?  
**Resposta:** 'GraphingTheWorld32'  
***Nota: Ao explorar a vulnerabilidade de inclusão de diretório no Grafana, é possível ler arquivos de configuração ou banco de dados que revelam a senha do administrador, que neste cenário é "GraphingTheWorld32".*** 

- **Pergunta:** É possível obter acesso direto ao servidor agora que se sabe a palavra-passe do grafana-admin? (sim/não)  
**Resposta:** 'yay'  
***Nota: Com as credenciais de administrador do Grafana comprometidas, é possível obter acesso direto e interativo ao painel de controle do servidor, escalando o nível de comprometimento.*** 

- **Pergunta:** Algum dos IDS em anexo é capaz de detetar o ataque caso o ficheiro /etc/shadow seja solicitado através da exploração? Se sim, qual dos IDS o detetou?  
**Resposta:** 'suricata'  
***Nota: Ao solicitar um arquivo altamente sensível como `/etc/shadow` através do exploit, o NIDS Suricata é capaz de detectar a assinatura da tentativa de acesso ou o padrão de tráfego malicioso, gerando um alerta, enquanto o HIDS (Wazuh) pode ou não capturar dependendo da configuração específica da regra de integridade de arquivos.***

