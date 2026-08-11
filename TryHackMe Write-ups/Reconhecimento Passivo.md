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

