# Windows Command Line - TryHackMe

## 📊 Info
- Dificuldade: Fácil
- Categoria: Básico
- Data: 06/07/2026
- Link: `https://tryhackme.com/room/windowscommandline`  

## 🔍 Resumo
Este laboratório atua como uma introdução prática ao prompt de comando do Windows. O foco é familiarizar o operador com o interpretador de comandos padrão, 
navegação no sistema de arquivos e execução de diretivas básicas, fundamentais para enumeração e administração de sistemas Windows.
(Nota: O PowerShell é o padrão moderno, mas o cmd.exe permanece como a base do CLI).


## 🛠️ Processo
### 🔵 **Task 1: Introdução**  

O processo pede para que seja usado o interpretador do Windows (CLI) e conectado com o serviço SSH. Além de destacar as vantagens de usar CLI.  

- **Pergunta:** Qual é o interpretador de linha de comandos predefinido no ambiente Windows?  
**Resposta:**  'cmd.exe'  
***Nota: a execução do comando 'WIN + R' , seguido do comando 'cmd.exe' na caixa de pesquisa, abrirá o interpretador.***  

### 🔵 **Task 2 : Informação do sistema e navegação**  
O foco é na coleta de informações do sistema. Aqui segue uma lista interessante que auxília nesse processo.  

  Comandos explorados:  
  **set:** Exibe as variáveis de ambiente.  
  **ver:** Exibe a versão atual do sistema operacional.    
  **systeminfo:** Mostra o relatório detalhado sobre o software e o hardware.  
  **comando | more:** "Canaliza" a saída de um comando (como driverquery) para paginar a visualização. Você usa a barra de espaço para avançar as páginas e CTRL + C para sair.  
  **help:** Exibe informações de ajuda e os parâmetros de um comando específico.  
  **cls:** Limpa a tela do prompt de comando.  

- **Pergunta:** Qual é a versão do sistema operacional da VM Windows?  
**Resposta:** 10.0.20348.2655  
***Nota: O Comando 'ver' mostra essa saída.***

- **Pergunta:** Qual é o hostname (nome da máquina) da VM Windows?  
**Resposta:** WINSRV2022-CORE  
***Nota: O comando 'systeminfo' mostra essa saída.***  

### 🔵 **Task 3: Solução de problemas de rede**  

O foco desta tarefa é utilizar a linha de comando para verificar configurações de rede, testar conectividade e investigar portas e serviços ativos no sistema.  
(É fundamental para enumeração e troubleshooting)  

  Comandos explorados:  
  **ipconfig:** Exibe o endereço IP, máscara de sub-rede e gateway padrão.  
  **ipconfig /all:** Mostra informações detalhadas, incluindo servidores DNS, status do DHCP e endereço físico (MAC).  
  **ping [alvo]:** Testar para procurar o endereço físico do servidor (endereço MAC)?  
  
- **Pergunta:** Qual comando podemos usar para procurar o endereço físico do servidor (endereço MAC)?  
**Resposta:** 'ipconfig /all'  
***Nota: O comando 'ipconfig/all mostra além dessa, outras informações de rede. *** 

- **Pergunta:** Qual é o nome do serviço de escuta na porta 135?  
**Resposta:** 'RpcSs'  
***Nota: Conforme a saída do 'netstat -abon', o serviço é o 'RpcSs' rodando dentro do 'svchost.exe').*** 

- **Pergunta:** Qual é o nome do serviço de escuta na porta 3389?  
**Resposta:** 'TermService'  
***(Nota: A porta 3389 é a padrão do serviço de Área de Trabalho Remota no Windows).***  

### 🔵 **Task 4: Gestão de arquivos e diretórios**  

O foco é navegar no sistema de arquivos, manipular diretórios e ler o conteúdo de arquivos para encontrar a flag oculta.  

  Comandos explorados:  
  **cd:** Navega entre diretórios.  
  **dir:** Lista arquivos e pastas no diretório atual.  
  **type:** Exibe o conteúdo de um arquivo de texto na tela.  

- **Pergunta:** Quais são os conteúdos do arquivo em 'C:\Treasure\Hunt'?  
**Resposta:** `THM{...}` *(Cole aqui a sua flag exata)*  
***Nota: Para chegar à resposta, o processo foi navegar até o diretório alvo com 'cd C:\Treasure\Hunt', listar os arquivos com 'dir' para identificar o nome do arquivo e, por fim, usar 'type [nome_do_arquivo]' para ler seu conteúdo.***

### 🔵 **Task 5: Gestão de tarefas e processos**  

O foco é gerenciar processos em execução via linha de comando, similar ao Gerenciador de Tarefas do Windows.  

  Comandos explorados:  
  **tasklist:** Lista todos os processos em execução.  
  **tasklist /FI "imagename eq [nome]":** Filtra processos pelo nome do executável.  
  **taskkill /PID [pid]:** Encerra um processo específico pelo seu ID.  

- **Pergunta:** Qual comando você usaria para encontrar os processos em execução relacionados ao `notepad.exe`?    
**Resposta:** 'tasklist /FI "imagename eq notepad.exe"'    
***Nota: Usa-se o parâmetro '/FI' (filter) com a condição 'imagename eq' para buscar processos com o nome exato do executável.***  

- **Pergunta:** Qual comando você pode usar para matar o processo com o PID 1516?    
**Resposta:** 'taskkill /PID 1516'  
***Nota: O comando 'taskkill' com o parâmetro '/PID' encerra o processo identificado pelo seu Process ID.***

### 🔵 **Task 6: Conclusão**  

Consolidando o aprendizado, lembrando que a linha de comando possui diversas outras utilidades (como 'chkdsk', 'driverquery' e 'sfc /scannow') e reforçando o uso do parâmetro '/?' para consultar a ajuda de qualquer comando e do 'more' para paginar saídas longas.  

  Comandos explorados:  
  **shutdown /s:** Desliga o sistema.  
  **shutdown /r:** Reinicia o sistema.  
  **shutdown /a:** Aborta um desligamento ou reinicialização agendada.  

- **Pergunta:** O comando 'shutdown /s' pode desligar um sistema. Qual é o comando que você pode usar para reiniciar um sistema?  
**Resposta:** 'shutdown /r'  
***Nota: A flag '/r' (restart) instrui o sistema a reiniciar após o encerramento dos processos.***  

- **Pergunta:** Qual comando você pode usar para abortar um desligamento do sistema agendado?  
**Resposta:** 'shutdown /a'  
***Nota: A flag '/a' (abort) cancela qualquer sequência de desligamento ou reinicialização que esteja em contagem regressiva.***
