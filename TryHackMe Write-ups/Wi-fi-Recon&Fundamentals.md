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

O foco desta tarefa é estabelecer os fundamentos teóricos do padrão IEEE 802.11, explicando como as redes sem fio operam, como os dispositivos se identificam e como o espectro de radiofrequência é organizado, 
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
***Nota: Conforme a tabela de termos, o BSSID é o endereço MAC do rádio do AP, servindo como o identificador único de hardware para aquele ponto de acesso específico.***

- **Pergunta:** Que termo descreve o nome legível por pessoas de uma rede sem fios?  
**Resposta:** 'ESSID'  
***Nota: A tabela define explicitamente o ESSID como "The human-readable network name shown in a device's list of networks". (Nota: "SSID" também é frequentemente aceito, pois o texto menciona que são usados de forma intercambiável).***

### 🔵 **Task 3: 802.11 Quadros**

O foco desta tarefa é detalhar os tipos de frames (quadros) do padrão IEEE 802.11, explicando como diferenciá-los transforma uma captura de tráfego bruto em um relato legível da atividade da rede.

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

O foco desta tarefa é explicar como reconfigurar uma interface sem fio para observar redes às quais ela não está conectada, detalhando a diferença entre os modos de operação e o processo para habilitar o modo de monitoração (monitor mode) usando a suite `aircrack-ng`.

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

