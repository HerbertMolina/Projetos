# Metasploitable 2 sob a Ótica Moderna

- **Atividade:** Análise de Impacto e Vetores de Ataque com Táticas, Técnicas e Procedimentos (TTPs) Modernos
- **Alvo:** Metasploitable 2 
- **Framework de Referência:** MITRE ATT&CK®
- **Data da Documentação:** 08/10/2026
- **Status:** Análise de Post-Exploitation e Impacto no Negócio

---

## Introdução:
Embora o Metasploitable 2 seja uma máquina virtual lançada há mais de uma década, ela representa perfeitamente o **"Tech Debt" (Dívida Técnica)** e sistemas legados que ainda permeiam redes corporativas reais (servidores não atualizados, bancos de dados antigos, protocolos deprecados). 

A diferença entre um ataque "de ontem" (script kiddie rodando exploits manuais) e um ataque "de hoje" (Ransomware as a Service, APTs, Pentest profissional) está na **automação, no pós-exploração (Post-Exploitation) e no movimento lateral**. Abaixo, detalhamos como um atacante moderno operaria e, crucialmente, **o que exatamente poderia ser roubado ou comprometido** neste ambiente.

---

## Acesso Inicial
Hoje, um atacante ou pentester não perde tempo digitando comandos manuais de Telnet ou FTP. A abordagem moderna envolve:

1. **Reconhecimento Acelerado:** Uso de ferramentas como `Masscan` ou `RustScan` para identificar portas abertas em segundos, seguidas por scripts NSE (Nmap Scripting Engine) para fingerprinting de versões.
2. **Automação de Exploração:** Uso de frameworks de C2 (Command and Control) modernos como **Sliver**, **Havoc** ou **Mythic C2**, ou o clássico **Metasploit**, para executar exploits de forma a gerar uma sessão reversa (Reverse Shell) estável e ofuscada, burlando IDS/IPS básicos.
3. **Vetores:**
   - **vsftpd 2.3.4 (Backdoor):** Explorado para gerar shell imediata.
   - **distccd (RCE):** Uso de payloads Python compilados para execução remota.
   - **UnrealIRCd:** Exploração via módulo Metasploit gerando payload Meterpreter.
   - **Samba/NFS:** Acesso direto a arquivos sensíveis sem sequer precisar de shell, apenas montando o share.

---

## O Que Pode Ser Obtido?
Uma vez que o atacante tem execução de código (geralmente como `root` devido à facilidade dos exploits no MS2), inicia-se a fase de **Coleta de Dados e Pós-Exploração**. Em um ambiente real com falhas equivalentes, o atacante obteria:

### Credenciais e Chaves Criptográficas
Com acesso root, o atacante não precisa quebrar senhas; ele as extrai para usar em outros sistemas (Movimento Lateral).
*   **Hashes de Senhas (Linux):** Extração de `/etc/shadow`. Com as ferramentas modernas (ex: `Hashcat` em GPUs na nuvem), hashes fracos (como os do MS2) são quebrados em minutos.
*   **Chaves SSH Privadas:** Leitura de `~/.ssh/id_rsa` de todos os usuários. Se o administrador usou a mesma chave em outros servidores, o atacante ganha acesso a toda a infraestrutura sem disparar alertas de firewall.
*   **Senhas em Memória/Disco:** Uso de ferramentas modernas como **`Mimipenguin`** (o equivalente ao Mimikatz para Linux) para extrair senhas em texto claro da memória RAM, ou **`LaZagne for Linux`** para buscar senhas salvas no navegador ou clientes de banco de dados.
*   **Credenciais de Bancos de Dados:** Leitura de arquivos de configuração (ex: `wp-config.php` no Mutillidae, arquivos `.conf` do PostgreSQL/MySQL) revelando senhas de banco de dados que podem dar acesso a servidores de produção isolados.

### Dados Sensíveis do Negócio (Exfiltração)
*   **Bases de Dados de Clientes:** O MS2 possui bancos de dados MySQL e PostgreSQL. Um atacante moderno executaria um dump completo (`.sql`) e o exfiltraria silenciosamente via DNS tunneling ou HTTPS para um servidor externo (Técnica de *Exfiltration Over C2 Channel*).
*   **Histórico de Comandos (Bash History):** O arquivo `~/.bash_history` é uma mina de ouro. Administradores frequentemente digitam senhas por engano na linha de comando ou deixam tokens de API, chaves AWS/Azure e URLs internas expostas.
*   **Dados de Aplicações Web:** O MS2 roda **DVWA** e **Mutillidae**. Em um cenário real, isso representa acesso a dados de PII (Informações de Identificação Pessoal), cartões de crédito (PCI-DSS) e registros médicos (HIPAA), levando a multas milionárias e processos por violação de dados.

### Topologia de Rede e Movimento Lateral (Pivoting)
O servidor comprometido raramente é o alvo final; ele é o **Ponto de Pivô**.
*   **Tabelas ARP e Roteamento:** Comandos como `arp -a` e `ip route` revelam outras sub-redes internas que o atacante não conseguia ver da internet.
*   **Tunneling e Pivoting:** O atacante instalaria ferramentas modernas como **Ligolo-ng**, **Chisel** ou **Proxychains** para criar um túnel SOCKS5. Isso permite que a máquina do atacante "veja" e ataque a rede interna corporativa através do servidor comprometido, burlando firewalls de perímetro.

### Persistência Silenciosa (Living off the Land - LoL)
Para garantir que não percam o acesso caso a vulnerabilidade inicial (ex: vsftpd) seja corrigida:
*   **Criação de Backdoors de SSH:** Modificação do `~/.ssh/authorized_keys` do root para permitir acesso com a chave pública do atacante.
*   **Cron Jobs Maliciosos:** Criação de tarefas agendadas que baixam e executam o agente C2 a cada 5 minutos.
*   **Rootkits de Kernel:** Instalação de rootkits modernos (ex: Diamorphine) para esconder processos maliciosos, portas abertas e arquivos do administrador do sistema.

---

## O Que Fariam os Atores de Ameaça Hoje?

Se o Metasploitable 2 fosse um servidor de produção real exposto na internet hoje, o destino do sistema dependeria do perfil do atacante:

| Perfil do Ator | Ação Imediata no MS2 | Impacto Final no Negócio |
| :--- | :--- | :--- |
| **Ransomware (ex: LockBit, BlackCat)** | 1. Exfiltrar dados do MySQL/PostgreSQL.<br>2. Criptografar arquivos e apagar backups.<br>3. Deixar nota de resgate. | **Dupla Extorsão:** Vazamento de dados de clientes na Dark Web + Paralisação total das operações (RTO de semanas). |
| **Cryptojackers (ex: TeamTNT)** | 1. Instalar minerador oculto (XMRig).<br>2. Desabilitar ferramentas de monitoramento (Sysmon, auditd).<br>3. Usar a máquina para minerar Monero. | **Degradação de Performance:** Servidor lento, contas de nuvem (AWS/GCP) com custos astronômicos no fim do mês. |
| **APT / Espionagem (Nation-State)** | 1. Mapear a rede interna (Pivoting).<br>2. Roubar credenciais de AD (Active Directory) via Kerberoasting se houver integração.<br>3. Manter acesso stealth por meses. | **Roubo de Propriedade Intelectual:** Vazamento de segredos industriais, espionagem corporativa de longo prazo. |
| **Hacktivistas / DDoS Botnets** | 1. Instalar scripts de ataque (ex: LOIC, Mirai).<br>2. Alistar a máquina em botnet. | **Ataques de Negação de Serviço:** O servidor é usado para derrubar sites de terceiros, manchando a reputação do IP da empresa. |

---

A análise do Metasploitable 2 sob a ótica moderna demonstra que **a exploração é apenas a porta de entrada**. O verdadeiro risco reside no que o atacante faz *depois* de entrar. 

Em ambientes corporativos atuais, a presença de falhas legadas (como as encontradas no MS2) é inaceitável porque:
1. **Não há como defender o indefensável:** Sistemas sem suporte (EOL) não recebem patches de segurança.
2. **A superfície de ataque é vasta:** Protocolos antigos (como `rlogin`, `telnet`, FTP sem TLS) transmitem credenciais em texto claro, facilitando a interceptação (Sniffing) por atores internos ou em trânsito.
3. **O tempo de residência (Dwell Time) é alto:** Ferramentas modernas de EDR (Endpoint Detection and Response) detectariam o comportamento anômalo (ex: execução de `nmap` interno, dumping de `/etc/shadow`, tunelamento de rede), mas em sistemas legados, muitas vezes não há agentes de segurança instalados.

### Mapeamento Rápido MITRE ATT&CK
*   **Initial Access:** T1190 (Exploit Public-Facing Application)
*   **Execution:** T1059 (Command and Scripting Interpreter)
*   **Credential Access:** T1003 (OS Credential Dumping)
*   **Discovery:** T1082 (System Information Discovery), T1049 (System Network Connections Discovery)
*   **Lateral Movement:** T1021 (Remote Services - SSH)
*   **Exfiltration:** T1041 (Exfiltration Over C2 Channel)

---

*Este relatório demonstra a transição do pensamento puramente técnico (como executar o exploit) para o pensamento analítico de negócios e risco (qual o impacto da exploração), habilidade altamente valorizada em cargos de SOC Analyst, Threat Hunter e Pentester.*
