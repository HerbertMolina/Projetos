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
**Resposta:** `cmd.exe`

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
**Resposta:** 10.0.17763.1821 (ou 10.0.17763 conforme exibido no systeminfo).

- **Pergunta:** Qual é o hostname (nome da máquina) da VM Windows?
**Resposta:** WIN-SRV-2019


## 🚩 Flags
- User: THM{...}
- Root: THM{...}

## 💡 Aprendizado
[O que você aprendeu]
