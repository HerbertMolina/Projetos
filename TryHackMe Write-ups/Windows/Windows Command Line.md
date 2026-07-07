# Windows Command Line - TryHackMe

## 📊 Info
- Dificuldade: Fácil
- Categoria: Básico
- Data: 06/07/2026

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
***Nota: ***

- **Pergunta:** Qual é o nome do serviço de escuta na porta 135?  
**Resposta:** 'RpcSs'  
***Nota: Conforme a saída do 'netstat -abon', o serviço é o 'RpcSs' rodando dentro do 'svchost.exe').***

- **Pergunta:** Qual é o nome do serviço de escuta na porta 3389?  
**Resposta:** 'TermService'  
***(Nota: A porta 3389 é a padrão do serviço de Área de Trabalho Remota no Windows).***

## 🚩 Flags
- User: THM{...}
- Root: THM{...}

## 💡 Aprendizado
[O que você aprendeu]
