# Wi-Fi Fundamentals and Reconnaissance

## 📊 Info  
- Dificuldade: Fácil  
- Categoria: Network Security / Wi-Fi Hacking  
- Data: 11/08/2026  
- Link: `https://tryhackme.com/room/wififundamentalsandrecon`    

## 🔍 Resumo  
O objetivo é aprender os fundamentos de como as redes Wi-Fi operam e realizar a fase inicial de reconhecimento em auditorias de segurança sem fio.  

## 🛠️ Processo  

### 🔵 **Task 1: Introdução**

Apresentação do escopo do módulo de Hacking Wi-Fi, destacando a importância de incluir redes sem fio nos testes de penetração e preparar o ambiente de laboratório para as atividades práticas.

Conceitos explorados:  
**Superfície de Ataque Wireless:** Redes sem fio estendem a infraestrutura de uma organização além das barreiras de segurança física, irradiando sinais para ruas e estacionamentos.  
**Fundamentos de Operação:** Compreensão de Access Points (APs), estações (clients), BSSIDs, ESSIDs, canais e bandas de frequência (2.4 GHz e 5 GHz).  
**Frames 802.11:** Importância dos frames de *beacon* (anúncio da rede) e *probe request* (solicitação de conexão por clientes) para um atacante.  
**Modo Monitor:** Capacidade de colocar uma interface sem fio em modo de escuta passiva para capturar todo o tráfego no ar, essencial para ferramentas da suite `aircrack-ng`.  

### 🔵 **Task 2: Como funciona o Wi-Fi**

Estabelecendo os fundamentos teóricos do padrão IEEE 802.11, explicando como as redes sem fio operam, como os dispositivos se identificam e como o espectro de radiofrequência é organizado, 
o que é essencial para entender as vulnerabilidades exploradas nos ataques subsequentes.

Conceitos explorados:  
**Access Points (AP) e Stations (STA):** O AP cria a rede e faz a ponte entre os clientes sem fio e a rede cabeada. A STA é qualquer dispositivo cliente (laptop, smartphone, IoT) que se conecta ao AP. Um AP junto com todas as suas STAs associadas forma um Basic Service Set (BSS).  
**Identificadores de Rede (BSSID vs. ESSID vs. SSID):**  
- **BSSID:** O endereço MAC do rádio do AP, que identifica unicamente um único ponto de acesso.  
- **ESSID:** O nome legível por humanos da rede sem fio, exibido na lista de redes do dispositivo.  
- **SSID:** O campo de nome em si. Na prática, "SSID" e "ESSID" são frequentemente usados de forma intercambiável, mas a distinção é importante: uma rede (ESSID) pode ser anunciada por vários APs (múltiplos BSSIDs) para cobrir um prédio inteiro.  
**Canais e Bandas de Frequência:** O espectro Wi-Fi é dividido em bandas (2.4 GHz, 5 GHz e 6 GHz). A banda de 2.4 GHz tem maior alcance, mas é congestionada (apenas os canais 1, 6 e 11 não se sobrepõem). A banda de 5 GHz oferece maior throughput e mais canais não sobrepostos, sendo o padrão para implantações corporativas.  
**Impacto no Reconhecimento:** Uma interface em modo monitor só pode escutar um canal por vez. Portanto, ferramentas de varredura precisam "pular" (hop) entre os canais. Varreduras padrão que focam apenas em 2.4 GHz perderão completamente as redes corporativas que operam em 5 GHz.

- **Pergunta:** Qual é o termo utilizado para designar o endereço MAC que identifica de forma única um único ponto de acesso?  
**Resposta:** 'BSSID'  
Qual é a opção do wpa_supplicant que faz com que o cliente procure uma rede pelo nome, em vez de aguardar os seus sinais de beacon?***Nota: Conforme a tabela de termos, o BSSID é o endereço MAC do rádio do AP, servindo como o identificador único de hardware para aquele ponto de acesso específico.***

- **Pergunta:** Que termo descreve o nome legível por pessoas de uma rede sem fios?  
**Resposta:** 'ESSID'  
***Nota: A tabela define explicitamente o ESSID como "The human-readable network name shown in a device's list of networks". (Nota: "SSID" também é frequentemente aceito, pois o texto menciona que são usados de forma intercambiável).***

### 🔵 **Task 3: 802.11 Quadros**

Detalhando os tipos de frames (quadros) do padrão IEEE 802.11, explicando como diferenciá-los transforma uma captura de tráfego bruto em um relato legível da atividade da rede.

Conceitos explorados:  
**As Três Classes de Frames:**  
- **Management (Gerenciamento):** Estabelecem e mantêm a relação entre estações e pontos de acesso. Em padrões mais antigos, trafegam em texto claro e sem autenticação, permitindo que qualquer dispositivo os leia ou forje (base para muitos ataques).  
- **Control (Controle):** Mensagens curtas que coordenam o acesso ao meio compartilhado para evitar transmissões simultâneas (ex: RTS, CTS, ACK).  
- **Data (Dados):** Carregam o payload real da rede. Mesmo em redes criptografadas, o cabeçalho que envolve o payload permanece desprotegido e útil para um atacante.  
**Beacon Frames:** O ponto de acesso transmite esses frames periodicamente (cerca de 10 vezes por segundo) para anunciar sua presença, incluindo BSSID, ESSID (a menos que oculto), canal, taxas de dados e configuração de segurança. É a base do escaneamento passivo.  
**Probe Requests:** Frames de gerenciamento que um cliente transmite quando procura ativamente por uma rede. Dispositivos frequentemente "proclamam" os nomes das redes às quais se conectaram anteriormente, revelando sua lista de redes confiáveis a qualquer receptor no alcance.  
**Authentication, Association e Deauthentication:** O processo de conexão é uma troca de dois estágios (autenticação e associação). A desconexão requer apenas um único frame (deauthentication), que no WPA2 não é autenticado, permitindo que um atacante forje o endereço do AP e desconecte um cliente à vontade (usado para capturar handshakes).

- **Pergunta:** Que tipo de quadro 802.11 é que um ponto de acesso transmite periodicamente para anunciar a sua presença?  
**Resposta:** 'Beacon'  
***Nota: O texto afirma explicitamente: "An access point advertises its presence by broadcasting beacon frames, typically around ten times per second."***

- **Pergunta:** Que quadro de gestão é que um cliente envia para procurar ativamente uma rede pelo nome?  
**Resposta:** 'Probe request'  
***Nota: Conforme descrito na seção "Probe Requests", este é o frame de gerenciamento que um cliente transmite quando procura ativamente por uma rede, muitas vezes revelando os nomes das redes às quais já se conectou no passado.***

### 🔵 **Task 4: Modo Monitor**

Explicando como reconfigurar uma interface sem fio para observar redes às quais ela não está conectada, detalhando a diferença entre os modos de operação e o processo para habilitar o modo de monitoração (monitor mode) usando a suite `aircrack-ng`.

Conceitos explorados:  
**Managed Mode vs. Monitor Mode:** No modo gerenciado (padrão), o rádio age como um cliente comum, descartando frames não endereçados a ele. O modo monitor remove esse filtro, capturando passivamente todos os frames 802.11 no canal atual, essencial para reconhecimento e ataques.  
**Interferência de Processos:** Serviços como `NetworkManager`, `wpa_supplicant`, `avahi-daemon` e `dhclient` gerenciam a conexão de rede e podem alterar canais ou modos automaticamente, corrompendo capturas. O comando `sudo airmon-ng check kill` identifica e interrompe esses processos conflitantes.  
**Habilitando o Modo Monitor:** O comando `sudo airmon-ng start <interface>` (ex: `wlan0`) desativa o modo gerenciado e cria uma nova interface virtual dedicada à monitoração, geralmente com o sufixo `mon` (ex: `wlan0mon`).  
**Verificação:** O utilitário `sudo iw dev` pode ser usado para confirmar se o campo `type` da interface foi alterado para `monitor`.

- **Pergunta:** Depois de executar o comando `sudo airmon-ng start wlan0`, qual é o nome da interface em modo de monitorização que é criada?  
**Resposta:** 'wlan0mon'  
***Nota: A saída do comando `airmon-ng start` exibe explicitamente a criação de uma "monitor mode vif" (virtual interface) nomeada `wlan0mon` associada ao dispositivo físico `wlan0`.***

### 🔵 **Task 5: Analisar as ondas de rádio com o airodump-ng**

O foco desta tarefa é demonstrar como utilizar o `airodump-ng`, a ferramenta de enumeração da suite `aircrack-ng`, para capturar e analisar o tráfego de redes sem fio, identificando redes, clientes, canais e configurações de segurança.

Conceitos explorados:  
**Execução do airodump-ng:** A ferramenta varre os canais (por padrão, a banda de 2.4 GHz com `--band bg`) para capturar frames de beacon e probe. Uma varredura completa deve durar de 30 a 60 segundos para permitir múltiplas passagens por cada canal.  
**Análise da Seção de Access Points (APs):** A tabela superior lista os APs, com colunas cruciais como `BSSID` (endereço MAC), `PWR` (força do sinal), `CH` (canal), `ENC` (criptografia), `AUTH` (método de autenticação) e `ESSID` (nome da rede). Redes ocultas aparecem como `<length: N>`.  
**Análise da Seção de Stations (Clientes):** A tabela inferior lista os dispositivos clientes. Clientes não associados (`not associated`) revelam os nomes das redes que procuram na coluna `Probes`, o que é fundamental para ataques de Rogue Access Point (AP Falso).  
**Varredura na Banda de 5 GHz:** Redes corporativas de alto valor frequentemente operam na banda de 5 GHz. Para capturá-las, é necessário travar o rádio em um canal específico (ex: `-c 44`) e usar a banda `a` (`--band a`).  
**Filtragem e Captura Direcionada:** Uma vez identificado o alvo, o escaneamento pode ser restrito a um canal e BSSID específicos (`-c` e `--bssid`), salvando os dados em um arquivo (`-w`) para análise posterior, como a captura de handshakes.

- **Pergunta:** Que valor aparece na coluna AUTH numa rede empresarial (802.1X)?  
**Resposta:** 'MGT'  
***Nota: A tabela de referência "ENC, CIPHER and AUTH at a Glance" e a saída do scan de 5 GHz mostram claramente que o valor `MGT` na coluna `AUTH` indica autenticação Enterprise / 802.1X.***

- **Pergunta:** Em que canal funcionam as redes empresariais?  
**Resposta:** '44'  
***Nota: O texto afirma explicitamente: "The lab's enterprise networks... all operate on the 5 GHz band on channel 44." A saída do comando `airodump-ng --band a -c 44` confirma que todas as redes com AUTH MGT estão no canal 44.***

- **Pergunta:** Quantos pontos de acesso estão a transmitir o ESSID CorpNet?  
**Resposta:** '2'  
***Nota: A saída do scan de 5 GHz lista dois BSSIDs distintos (`F0:9F:C2:71:22:15` e `F0:9F:C2:71:22:1A`) que compartilham o mesmo ESSID `CorpNet`, ilustrando a distinção entre BSSID e ESSID mencionada na Task 2.***

### 🔵 **Task 6: Descobrir redes ocultas**

O foco desta tarefa é demonstrar como contornar a técnica de "ocultação de SSID" (SSID cloaking), provando que esconder o nome da rede não é uma medida de segurança eficaz, e como se conectar a essa rede para acessar recursos internos.

Conceitos explorados:  
**SSID Cloaking (Ocultação de SSID):** Administradores podem configurar o AP para omitir o ESSID nos frames de beacon. No entanto, o nome ainda é transmitido em texto claro quando um cliente legítimo se conecta (em frames de probe request ou association request).  
**Identificação no airodump-ng:** Uma rede oculta aparece com o campo ESSID vazio, mas o `airodump-ng` ainda consegue ler o comprimento real do nome, exibindo algo como `<length: 9>`.  
**Revelação Ativa com mdk4:** Quando não há clientes conectados para forçar uma reconexão (abordagem passiva), pode-se usar o `mdk4` no modo de probing (`p`) para enviar um dicionário de nomes candidatos. O AP só responde com um "Probe Response" se o nome enviado corresponder exatamente ao seu ESSID real e ao comprimento correto.  
**Conexão com wpa_supplicant:** Para que um cliente se conecte a uma rede oculta, ele deve ser configurado para procurar ativamente pelo nome, usando a diretiva `scan_ssid=1` no arquivo de configuração, em vez de apenas ouvir beacons.  
**Acesso ao Gateway:** Após obter o IP via `dhclient`, é possível acessar o painel de administração do roteador (geralmente no `.1` da sub-rede) usando credenciais padrão para recuperar a flag.

- **Pergunta:** Qual é o SSID da rede oculta que descobriu?  
**Resposta:** 'Staff-Net'  
***Nota: O `mdk4` recebe uma resposta de probe do AP alvo apenas quando o nome candidato "Staff-Net" é enviado, confirmando que este é o ESSID real da rede oculta.***

- **Pergunta:** Em que canal funciona a rede oculta?  
**Resposta:** '11'  
***Nota: A saída do `airodump-ng` mostra claramente que o BSSID da rede oculta (`F0:9F:C2:6A:88:26`) está operando no canal 11 da banda de 2.4 GHz.***

- **Pergunta:** No airodump-ng, o campo ESSID de uma rede oculta apresenta um nome em branco e um comprimento na forma <comprimento: N>. O que significa N neste caso?  
**Resposta:** '9'  
***Nota: O texto destaca que, mesmo com o nome oculto, o comprimento do SSID é vazado no frame de beacon. No caso de "Staff-Net", o comprimento é 9 caracteres, exibido como `<length: 9>`.***

- **Pergunta:** Qual é a opção do wpa_supplicant que faz com que o cliente procure uma rede pelo nome, em vez de aguardar os seus sinais de beacon?  
**Resposta:** 'scan_ssid=1'  
***Nota: A diretiva `scan_ssid=1` no arquivo de configuração do `wpa_supplicant` instrui o cliente a enviar probe requests direcionados com o nome da rede, contornando a falta de beacons da rede oculta.***

- **Pergunta:** Ligue-se à rede que descobriu e leia o painel no seu gateway. Que flag é que este devolve?  
**Resposta:** 'THM{0e6521916c3adf08e5b6830f6675351e4eebec92}'  
***Nota: Após se conectar à rede "Staff-Net" e obter um IP via DHCP, o acesso ao painel do gateway (192.168.16.1) com as credenciais padrão (admin/admin) revela a flag na página inicial.***

### 🔵 **Task 7: Organizar o seu reconhecimento**

Explicando como salvar e organizar os dados coletados durante o reconhecimento sem fio, garantindo que as informações possam ser utilizadas em ataques subsequentes, já que a saída padrão do terminal é descartada ao fechar a janela.

Conceitos explorados:  
**Salvamento de Capturas (`-w`):** O uso da flag `-w` (write) no `airodump-ng` para salvar todo o tráfego capturado em um conjunto de arquivos com um prefixo definido. É recomendado travar o rádio em um canal específico (`-c`) e, idealmente, em um BSSID específico (`--bssid`) para manter o arquivo pequeno e focado no alvo.  
**Formatos de Arquivo Gerados:** Uma captura com `-w` gera múltiplos arquivos numerados (ex: `-01`):  
- **`.cap`**: A captura bruta de pacotes. É o arquivo mais importante, contendo todos os frames (beacons, handshakes, etc.) e é o arquivo passado para ferramentas como `aircrack-ng`.  
- **`.csv`**: Um resumo em texto puro de todos os APs e clientes observados, fácil de filtrar com `grep`.  
- **`.kismet.csv` / `.kismet.netxml`**: Resumos nos formatos CSV e XML do Kismet, para compatibilidade com outras ferramentas.  
- **`.log.csv`**: Um log contínuo de atividade, incluindo dados de GPS se um receptor estiver conectado.  
**Otimização de Saída:** A flag `--output-format csv` pode ser usada para gerar *apenas* o arquivo de resumo `.csv`, evitando a criação dos arquivos de captura de pacotes e logs do Kismet quando apenas o inventário é necessário.  
**Inventário de Alvos:** A importância de manter um registro separado dos alvos valiosos, incluindo ESSID, BSSID, canal, banda, configuração de segurança e clientes associados (crucial para ataques que exigem a presença de um cliente, como a captura de handshake WPA2).

- **Pergunta:** Qual é a opção do airodump-ng que grava os dados capturados em ficheiros?  
**Resposta:** '-w'  
***Nota: O texto afirma explicitamente: "The -w flag instructs airodump-ng to write everything it receives to a set of files named after a given prefix."***

### 🔵 **Task 8: Conclusão**
Consolidando todo o fluxo de trabalho de reconhecimento sem fio realizado na sala, resumindo as etapas desde a preparação da interface até a descoberta de redes ocultas, e introduzindo os tópicos que serão abordados nas próximas salas do módulo de Wi-Fi Hacking.

Conceitos explorados:  
**Resumo do Fluxo de Trabalho:**  
1. **Preparação da Interface:** Uso de `airmon-ng check kill` e `airmon-ng start` para habilitar o modo monitor (`wlan0mon`), confirmado via `iw dev`.  
2. **Varredura das Bandas:** Uso do `airodump-ng` para mapear redes em 2.4 GHz (`--band bg`) e, separadamente, em 5 GHz (`--band a -c 44`) para alcançar redes corporativas.  
3. **Classificação de Redes:** Análise das colunas `ENC`, `CIPHER` e `AUTH` para identificar configurações como OPN (Aberta), WEP, WPA2-PSK, WPA3-SAE, MGT (Enterprise) e OWE.  
4. **Análise de Estações:** Identificação de clientes associados e, crucialmente, clientes não associados (`not associated`) sondando redes que não estão sendo transmitidas ativamente no ambiente.  
5. **Revelação de SSID Oculto:** Uso do `mdk4` para sondar ativamente uma rede oculta (cujo comprimento era conhecido) até que ela respondesse, seguido pela conexão via `wpa_supplicant` com a diretiva `scan_ssid=1`.  
**Propriedades do 802.11 Exploradas:** O reconhecimento passivo é altamente eficaz porque os APs anunciam sua presença continuamente via beacons, e os frames de gerenciamento trafegam em texto claro sem autenticação, permitindo que até redes que tentam se esconder sejam desmascaradas.  
