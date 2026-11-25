### **Relatório de Análise de Segurança: Comprometimento via Serviço Telnet com Credenciais Padrão**  
  

---

### **Contexto e Objetivo da Investigação**  
Este documento formaliza a avaliação de segurança realizada na máquina "Meow", classificada como um exercício introdutório (Tier 0) na plataforma Hack The Box. O objetivo central foi demonstrar as fases fundamentais de um teste de intrusão em rede, desde a enumeração de serviços expostos até a exploração de configurações inseguras de autenticação.  

A investigação simula um cenário onde um serviço legado de acesso remoto é exposto à rede sem mecanismos adequados de proteção, permitindo a validação de credenciais padrão ou ausentes. Este exercício serve como base para a compreensão de vetores de ataque triviais, porém críticos, frequentemente encontrados em ambientes de produção mal configurados.

---

### **Artefatos e Ferramentas de Análise**  
- **Conexão de Rede (OpenVPN)**: Estabelecimento de túnel seguro para acesso à rede isolada do laboratório.  
- **Nmap (Network Mapper)**: Utilizado para varredura de portas e identificação de serviços (fingerprinting) no alvo.  
- **ICMP Echo Request (Ping)**: Ferramenta básica para validação de conectividade e presença do host na rede.  
- **Cliente Telnet**: Protocolo e ferramenta de linha de comando utilizados para interagir com o serviço exposto na porta 23/TCP e executar a autenticação.  

---

### **Metodologia de Investigação**  
A abordagem seguiu um fluxo estruturado de avaliação de segurança, alinhado às práticas padrão de reconhecimento e exploração:  

- **Validação de Conectividade**: Verificação inicial da reachability do alvo utilizando requisições ICMP, observando o TTL (Time To Live) para inferir o sistema operacional subjacente.  
- **Enumeração de Superfície de Ataque**: Varredura de portas TCP para identificar serviços ativos. A análise focou na detecção de portas não padrão ou serviços legacy expostos.  
- **Análise de Serviço e Fingerprinting**: Identificação da versão e do sistema operacional associado ao serviço descoberto, utilizando técnicas de banner grabbing e detecção de versão do Nmap.  
- **Exploração de Falha de Configuração**: Tentativa de autenticação no serviço identificado utilizando credenciais padrão da indústria (ex: `root`, `admin`) combinadas com ausência de senha (blank password), explorando a falta de políticas de senha obrigatórias.  
- **Pós-Exploração e Coleta de Evidência**: Navegação no sistema de arquivos com privilégios máximos obtidos para localizar e extrair o artefato de validação (flag).  

---

### **Linha do Tempo da Operação (Timeline)**  
O diagrama abaixo ilustra a sequência cronológica de eventos durante a avaliação, destacando a rapidez com que uma superfície de ataque mal configurada pode ser totalmente comprometida.  

<img width="3006" height="2229" alt="MEOW1" src="https://github.com/user-attachments/assets/9d60960e-798a-4493-9798-ae65f9598cdb" />

---

### **Tabela de Evidências e Conclusões Investigativas**  
A tabela a seguir documenta as descobertas técnicas, vinculando cada etapa da investigação à ferramenta utilizada, à lógica de execução e à conclusão obtida.  

| Etapa Investigativa | Ferramenta / Artefato | Lógica de Execução / Comando Aplicado | Conclusão Técnica (Evidência) |
| :--- | :--- | :--- | :--- |
| **Validação de Conectividade** | `ping` | Envio de requisições ICMP para o IP do alvo. | Host ativo, TTL=63 (indutivo de sistema Linux roteado). |
| **Enumeração de Portas** | `nmap` | Varredura TCP padrão (`nmap -v <IP>`). | Porta 23/TCP identificada como aberta. |
| **Fingerprinting de Serviço** | `nmap` | Detecção de versão (`nmap -sV <IP>`). | Serviço identificado como `Linux telnetd`. |
| **Validação de Autenticação** | `telnet` | Tentativa de login com usuário `root` e campo de senha vazio. | Sucesso na autenticação sem necessidade de senha. |
| **Aquisição de Privilégios** | Shell do Sistema | Verificação do prompt de comando após login. | Acesso concedido diretamente como usuário `root`. |
| **Coleta de Evidência (Flag)** | `cat` | Leitura do arquivo `flag.txt` no diretório home do root. | Artefato obtido: `b40abdfe23665f766f9c61ecba8a4c19` |

---

### **Esquema Resumido do Processo de Análise**  
Para demonstrar a reprodutibilidade e a estrutura lógica do trabalho em um ambiente de avaliação de segurança, o fluxo de análise é representado no esquema abaixo.  

<img width="800" height="6024" alt="MEOW2" src="https://github.com/user-attachments/assets/dc54c0c5-ac24-468c-bd2e-f1936ca2cf55" />

---

### **Considerações Profissionais e Recomendações de Mitigação**  
Embora este cenário seja um exercício introdutório, ele ilustra uma falha crítica frequentemente encontrada em ambientes reais: a exposição de serviços de acesso remoto legados sem controles de autenticação adequados. O protocolo Telnet, por sua natureza, transmite todos os dados, incluindo credenciais, em texto claro, tornando-o suscetível a ataques de interceptação (sniffing).  

**Recomendações de Hardening derivadas desta análise:**  
- **Desativação de Serviços Legados**: Substituir imediatamente o uso de Telnet por protocolos criptografados, como SSH (Secure Shell), que garantem a confidencialidade e integridade dos dados em trânsito.  
- **Gestão de Credenciais**: Implementar políticas rigorosas que proíbam o uso de contas padrão (como `root` ou `admin`) com senhas em branco ou previsíveis. A autenticação deve exigir complexidade mínima e, idealmente, ser complementada por Autenticação Multifator (MFA).  
- **Segmentação de Rede e Filtragem**: Restringir o acesso a serviços de administração apenas a endereços IP de confiança, utilizando firewalls de rede ou listas de controle de acesso (ACLs) para reduzir a superfície de ataque exposta.  

Esta prática reforça competências fundamentais para operações de **SOC Fundamentals** e testes de intrusão iniciais, demonstrando a capacidade de identificar e explorar configurações inseguras básicas.  
