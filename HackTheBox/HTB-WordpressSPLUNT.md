## **Relatório de Análise Forense Digital: Comprometimento de Servidor WordPress via Web Shell**  
Link - https://app.hackthebox.com/sherlocks/WordpressWebForensics  
*Desafio: WordpressWebForensics (Hack The Box Sherlocks)*  

---

### **Contexto e Objetivo da Investigação**  
Este documento formaliza a investigação de um incidente de segurança cibernética simulado, envolvendo o comprometimento de um servidor web corporativo hospedando uma instância do WordPress. O objetivo central foi reconstruir a cadeia de ataque (Cyber Kill Chain), desde a fase inicial de reconhecimento até o estabelecimento de persistência via web shell, utilizando técnicas de análise de logs de acesso do Apache2.  

A investigação demonstra a aplicação prática de competências de DFIR (Digital Forensics and Incident Response) e operações de SOC, focando na identificação de Indicadores de Comprometimento (IoCs), correlação temporal de eventos e mapeamento tático do adversário.

---

### **Artefatos e Ferramentas de Análise**  
- **`access.log`**: Registro completo de requisições HTTP recebidas pelo servidor Apache2, contendo endereços IP de origem, timestamps, métodos HTTP, URIs solicitadas, códigos de status e User-Agents.  
- **Plataforma de Análise (Splunk)**: Utilizada para ingestão, indexação, filtragem avançada (SPL - Search Processing Language) e ordenação cronológica dos eventos, permitindo a identificação eficiente de padrões anômalos em grandes volumes de dados.

---

### **Metodologia de Investigação**  
A análise foi conduzida seguindo um fluxo estruturado de inteligência de logs, priorizando a evidência sobre a suposição:  

- **Detecção de Reconhecimento**: Filtragem de logs por User-Agents conhecidos de ferramentas de varredura de segurança (ex: WPScan) para isolar o tráfego malicioso do tráfego legítimo.  
- **Análise de Exploração**: Correlação de requisições direcionadas ao endpoint de autenticação (`wp-login.php`), analisando a transição de códigos de status HTTP (de `200 OK` para falhas repetidas, culminando em `302 Found` para redirecionamento de sucesso).  
- **Rastreamento de Pós-Exploração e Persistência**: Investigação de requisições a diretórios administrativos (`wp-admin/theme-editor.php`) e subsequente monitoramento de tráfego direcionado a arquivos PHP incomuns dentro da estrutura de temas do WordPress, indicativo de execução remota de comandos (web shell).  
- **Validação de Comportamento**: Análise da frequência e do padrão de requisições (ex: intervalos de poucos segundos entre requisições POST) para confirmar a interação automatizada ou manual com o artefato malicioso.

---

### **Linha do Tempo do Ataque (Timeline)**  
O diagrama abaixo ilustra a sequência cronológica de eventos reconstruída a partir da análise dos logs, destacando a velocidade e a progressão do ataque.  

<img width="5211" height="2073" alt="htb-wpscan1" src="https://github.com/user-attachments/assets/7c2d33c9-1a78-4808-b08d-7791119c4f95" />


---

### **Tabela de Evidências e Conclusões Investigativas**  
A tabela a seguir documenta as descobertas técnicas, vinculando cada questão investigativa à fonte de dados, à lógica de busca aplicada e à conclusão forense.  

| Questão Investigativa | Fonte e Lógica de Busca | Trecho ou Padrão Identificado no Log | Conclusão Técnica (IoC / Evidência) |
| :--- | :--- | :--- | :--- |
| **IP de origem do reconhecimento** | `access.log` / Filtragem por keyword "wpscan" | `"WPScan v3.8.25 (https://wpscan.com/wordpress-security-scanner)"` | `203.101.190.116` |
| **Início da atividade de reconhecimento** | `access.log` / Ordenação cronológica (`sort _time`) | Primeira requisição HEAD ao diretório raiz do WordPress | `2024-08-28 03:15:23` |
| **Versão da ferramenta de ataque** | `access.log` / Extração do campo User-Agent | `WPScan v3.8.25` | `WPScan v3.8.25` |
| **Duração do ataque de força bruta** | `access.log` / Filtragem por `uri_path="*wp-login.php"` e análise de delta temporal | Primeira tentativa (03:50:33) até o sucesso com status 302 (03:50:40) | `7 segundos` |
| **Tema WordPress comprometido** | `access.log` / Filtragem por requisições a `*themes*` e `theme-editor.php` | Acesso e modificação no diretório do tema padrão recente | `twentytwentyfour` |
| **Arquivo PHP utilizado como web shell** | `access.log` / Filtragem por `*twentytwentyfour*` e análise de novos arquivos | Requisições a um arquivo de padrão 404 modificado | `hidden-404.php` |
| **Primeira execução de comando via web shell** | `access.log` / Filtragem por `method="POST"` e `uri="*hidden-404.php*"` | Primeira requisição POST ao arquivo malicioso após sua criação | `2024-08-28 04:03:51` |
| **User-Agent da sessão de pós-exploração** | `access.log` / Extração do campo User-Agent nas requisições ao web shell | Navegador desktop padrão, distinto do User-Agent do WPScan | `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0` |

---

### **Esquema Resumido do Processo de Análise**  
Para demonstrar a reprodutibilidade e a estrutura lógica do trabalho em um ambiente de SOC, o fluxo de análise é representado no esquema abaixo.  

<img width="824" height="5551" alt="htb-wpscan2" src="https://github.com/user-attachments/assets/2a184135-915c-4a4e-89b1-7a41f9327e4f" />


---

Esta investigação destaca a eficácia de ataques automatizados contra superfícies de exposição mal configuradas. A janela entre o reconhecimento e a obtenção de acesso válido foi de apenas minutos, e a persistência foi estabelecida explorando funcionalidades legítimas, porém perigosas, do WordPress (edição de arquivos via painel administrativo).  

**Recomendações de Hardening derivadas desta análise:**  
- Desabilitar a edição de temas e plugins diretamente pelo painel administrativo, definindo `define('DISALLOW_FILE_EDIT', true);` no arquivo `wp-config.php`.  
- Implementar mecanismos de proteção contra força bruta no endpoint `wp-login.php`, como limitação de taxa (rate limiting), autenticação multifator (MFA) ou plugins de segurança que bloqueiem IPs após falhas consecutivas.  
- Configurar monitoramento contínuo no SIEM para alertar sobre requisições POST a arquivos PHP dentro de diretórios de temas que não correspondam a atualizações legítimas.  

---  
*Documento gerado com foco em padrões profissionais de DFIR, priorizando clareza técnica, rastreabilidade das evidências e formatação executiva.*
