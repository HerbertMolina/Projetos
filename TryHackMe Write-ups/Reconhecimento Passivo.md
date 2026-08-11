# Passive Reconnaissance

## 📊 Info  
- Dificuldade: Fácil  
- Categoria: Network Security / Reconnaissance  
- Data: 11/08/2026  
- Link: `https://tryhackme.com/room/passiverecon`    

## 🔍 Resumo  
O objetivo é aprender a utilizar ferramentas essenciais de reconhecimento passivo (como `whois`, `nslookup`, `dig`, DNSDumpster e Shodan.io) para coletar inteligência de fontes públicas sem interagir diretamente com o alvo.

## 🛠️ Processo  

### 🔵 **Task 1: Introdução**  

Conceitos fundamentais de reconhecimento passivo, diferenciando-o do reconhecimento ativo e estabelecendo os objetivos de aprendizado e os pré-requisitos da sala.

Conceitos explorados:  
**Passive vs. Active Reconnaissance:** O reconhecimento passivo coleta inteligência de fontes públicas sem entrar em contato direto com o alvo (baixo risco de detecção). Em contraste, o reconhecimento ativo interage diretamente com o sistema alvo, o que pode gerar logs e alertar defensores.  
**Fontes de Dados Públicos:** Mesmo com leis de privacidade mais rigorosas (GDPR, CCPA), grandes quantidades de dados úteis continuam publicamente expostas através de WHOIS, registros DNS, logs de certificados, mecanismos de busca e plataformas de censo de dispositivos.  
**Objetivos de Aprendizado:** Uso de `whois` para detalhes de registro de domínio, uso de `dig` e `nslookup` para consultas DNS, descoberta de subdomínios via DNSDumpster e logs de Certificate Transparency (CT), e coleta de inteligência sobre serviços expostos usando Shodan.io.  
**Pré-requisitos:** Conhecimento básico de networking e familiaridade com o terminal. A sala recomenda concluir previamente os módulos de Networking e Fundamentals se necessário.  
**Aviso sobre o AttackBox:** Usuários não assinantes do TryHackMe precisam se conectar via OpenVPN para obter acesso à Internet e utilizar ferramentas que dependem de consultas web (DNSDumpster, Shodan, crt.sh). Não é necessário realizar o deploy de uma máquina alvo (VM), pois todas as queries são feitas contra domínios públicos relacionados ao TryHackMe.

### 🔵 **Task 2: Passivo vs Ativo**

Distinção fundamental entre reconhecimento passivo e ativo, destacando os riscos, as metodologias e os exemplos práticos de cada abordagem no contexto de segurança cibernética.

Conceitos explorados:  
**Reconnaissance (Recon):** A fase preliminar de coleta de informações sobre um alvo, sendo o primeiro passo em frameworks de ataque modernos como a Cyber Kill Chain e a Unified Kill Chain.  
**Passive Reconnaissance (Reconhecimento Passivo):** Coleta de inteligência baseada exclusivamente em informações publicamente disponíveis, sem enviar pacotes ao alvo ou interagir diretamente com ele. Exemplos: consultar registros DNS públicos, logs de transparência de certificados (crt.sh), vagas de emprego, Shodan, Censys e repositórios públicos no GitHub.  
**Active Reconnaissance (Reconhecimento Ativo):** Envolvimento direto com o alvo, onde as sondagens podem ser registradas, detectadas ou bloqueadas. Exemplos: pings ICMP, varredura de portas (Nmap, masscan), fuzzing de endpoints, engenharia social e abordagens físicas.  
**Interação Humana:** Qualquer interação direta com uma pessoa afiliada ao alvo (como perguntar sobre a infraestrutura em um evento social) é classificada como reconhecimento ativo, mesmo que nenhum pacote de rede seja enviado.  
**Dica para Defensores:** Organizações devem monitorar continuamente sua própria pegada passiva (usando alertas do Shodan, watchers de logs de CT) para minimizar o que os atacantes podem descobrir sem tocar na rede.

- **Pergunta:** Visita a página do Facebook da empresa-alvo, na esperança de obter alguns nomes dos seus funcionários. Que tipo de atividade de reconhecimento é esta? (A para ativa, P para passiva)  
**Resposta:** 'P'  
***Nota: Acessar uma página pública do Facebook para coletar nomes de funcionários é uma forma de reconhecimento passivo.***

- **Pergunta:** Fazes um ping ao endereço IP do servidor web da empresa para verificar se o tráfego ICMP está bloqueado. Que tipo de atividade de reconhecimento é esta? (A para ativa, P para passiva)  
**Resposta:** 'A'  
***Nota: Enviar um ping (pacote ICMP) diretamente ao servidor web do alvo constitui uma interação direta com a infraestrutura.***

- **Pergunta:** Por acaso, encontras o administrador de TI da empresa-alvo numa festa. Tentas recorrer à engenharia social para obter mais informações sobre os sistemas e a infraestrutura de rede da empresa. Que tipo de atividade de reconhecimento é esta? (A para ativa, P para passiva)  
**Resposta:** 'A'  
***Nota: Conforme destacado no texto, qualquer interação direta com uma pessoa afiliada ao alvo conta como reconhecimento ativo, mesmo que não envolva o envio de pacotes de rede, pois há um engajamento direto com a organização alvo.***

### 🔵 **Task 3: WHOIS**

O foco desta tarefa é introduzir o protocolo WHOIS e seu sucessor moderno, o RDAP, demonstrando como consultar detalhes de registro de domínios para coletar inteligência passiva valiosa sobre um alvo.

Conceitos explorados:  
**Protocolo WHOIS:** Protocolo de consulta/resposta (porta 43) que fornece detalhes de registro de nomes de domínio, mantidos pelo registrador. Informações típicas incluem: registrador, dados de contato do registrante (frequentemente ofuscados por serviços de privacidade), datas de criação/atualização/expiração, name servers e códigos de status (ex: `clientTransferProhibited`).  
**RDAP (Registration Data Access Protocol):** O sucessor moderno e oficial do WHOIS para domínios gTLD. Utiliza HTTPS (seguro), retorna dados estruturados em JSON (legível por máquinas), suporta internacionalização e oferece melhores controles de privacidade, alinhando-se às regras atuais de proteção de dados.  
**Análise de Dados WHOIS/RDAP:** Ataques focam em datas (para estimar a idade da empresa ou planejar phishing em períodos de renovação), no registrador (para padrões de phishing), nos name servers (potenciais pontos fracos) e em mudanças históricas de infraestrutura.  
**Ferramentas:** Uso do cliente de linha de comando `whois` ou consultas via `curl` para endpoints RDAP (formatando a saída com `jq`), além de alternativas online como whois.icann.org ou whoxy.com para dados históricos.

- **Pergunta:** Quando é que o TryHackMe.com foi registado?  
**Resposta:** '20180705'  
***Nota: A saída do comando `whois` ou da consulta RDAP exibe claramente o campo "Creation Date" (ou "registration" event) como 2018-07-05, indicando a data de registro inicial do domínio.***

- **Pergunta:** Qual é o registrador do TryHackMe.com?  
**Resposta:** 'NAMECHEAP.com'  
***Nota: O campo "Registrar" na saída da consulta identifica a empresa responsável pelo registro do domínio, que neste caso é a NAMECHEAP INC.***

- **Pergunta:** Que empresa é que o TryHackMe.com utiliza para os servidores de nomes?  
**Resposta:** 'cloudflare.com'  
***Nota: Ao analisar os registros de name servers (ou consultando o domínio via ferramentas como `dig` ou `whois`), verifica-se que a infraestrutura de DNS do TryHackMe é gerenciada pela Cloudflare.***

### 🔵 **Task 4: nslookup & dig**

Utilizando ferramentas como `nslookup` e `dig` para traduzir nomes de domínio em endereços IP, encontrar servidores de e-mail e revelar registros TXT, sem interagir diretamente com os servidores do alvo.

Conceitos explorados:  
**Consultas DNS Passivas:** As consultas são enviadas a resolvedores públicos ou abertos (como 1.1.1.1 ou 8.8.8.8), e não diretamente aos servidores autoritativos do alvo, mantendo a natureza passiva da operação.  
**nslookup:** Ferramenta mais antiga, ainda útil para compatibilidade (especialmente em sistemas Windows), mas com saída menos detalhada. Sintaxe comum: `nslookup -type=TIPO DOMINIO [SERVIDOR]`.  
**dig (Domain Information Groper):** A ferramenta moderna e preferida para consultas DNS. Fornece uma saída mais limpa, exibe valores de TTL (Time To Live) por padrão e é mais confiável para consultas complexas e scripts. Sintaxe: `dig [@SERVIDOR] DOMINIO [TIPO]`.  
**Tipos Comuns de Registros DNS:**  
- **A / AAAA:** Endereços IPv4 e IPv6.  
- **CNAME:** Nome Canônico (alias que aponta um domínio para outro).  
- **MX:** Servidores de e-mail (Mail Exchanger), onde valores menores indicam maior prioridade.  
- **SOA:** Start of Authority (servidor de nomes primário, e-mail do admin e número de série da zona).  
- **TXT:** Registros de texto, frequentemente usados para SPF, DKIM, DMARC, verificação de domínio ou, em CTFs, para esconder flags.  
**Privacidade e Defesa:** O uso de resolvedores públicos que suportam DoH/DoT (como 1.1.1.1) ajuda a evitar que o ISP registre as consultas. Defensores devem monitorar mudanças inesperadas em registros DNS (novos MX ou TXT maliciosos), que podem indicar subdomain takeover ou erros de configuração.

- **Pergunta:** Verifica os registos TXT do thmlabs.com. Qual é o indicador que lá aparece?  
**Resposta:** 'THM{a5b83929888ed36acb0272971e438d78}'  
***Nota: Ao executar o comando `dig txt thmlabs.com` (ou `nslookup -type=txt thmlabs.com`), o registro TXT retorna a string contendo a flag do desafio.***

### 🔵 **Task 5: DNSDumpster & Certificados**

Como descobrir subdomínios não anunciados de forma totalmente passiva, utilizando fontes de OSINT como o DNSDumpster e os logs de Transparência de Certificados (CT Logs), expandindo a superfície de ataque conhecida sem enviar tráfego direto ao alvo.

Conceitos explorados:  
**Importância dos Subdomínios:** Subdomínios (ex: `dev.internal.company.com`, `blog.tryhackme.com`) frequentemente expõem serviços esquecidos, vulneráveis ou mal configurados (shadow IT), aumentando a superfície de ataque com APIs ou portais administrativos expostos.  
**DNSDumpster:** Ferramenta gratuita que agrega dados DNS públicos de caches de mecanismos de busca, bancos de dados de transferência de zona e registros de certificados. Ela não realiza enumeração por força bruta, mantendo a operação 100% passiva, e fornece mapas visuais das relações entre subdomínios, IPs e servidores de e-mail.  
**Certificate Transparency (CT) Logs (crt.sh):** Atualmente o método mais eficaz de descoberta passiva de subdomínios. É um framework de registro público (obrigatório desde ~2015) que registra todos os certificados SSL/TLS emitidos. O campo *Subject Alternative Name* (SAN) lista os domínios e subdomínios cobertos, permitindo a descoberta em tempo real usando curingas (ex: `%.tryhackme.com`).  
**Outras Ferramentas:** SecurityTrails (buscas limitadas gratuitas) e ferramentas de linha de comando como `Subfinder`, que agregam múltiplas fontes passivas.  
**Perspectiva do Defensor:** Organizações devem monitorar logs de CT e listas de subdomínios para detectar registros órfãos (dangling records), que apresentam risco de *subdomain takeover*, ou subdomínios não autorizados.

- **Pergunta:** Pesquise tryhackme.com no DNSDumpster. Na secção Serviços / Banners, qual deles tem o número mais elevado?  
**Resposta:** 'cloudflare'  
***Nota: Ao consultar o domínio no DNSDumpster, a seção "Services / Banners" agrega os provedores de serviços detectados. No caso do TryHackMe, a Cloudflare aparece com a maior contagem, refletindo seu uso extensivo como CDN e provedor de DNS/segurança para o domínio.***



