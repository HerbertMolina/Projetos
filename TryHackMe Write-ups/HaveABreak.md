# Have a Break

## 📊 Info  
- Dificuldade: Média  
- Categoria: OSINT / Investigation  
- Data: 11/08/2026  
- Link: `https://tryhackme.com/room/haveabreak`    

## 🔍 Resumo  
O objetivo é investigar o roubo de um carregamento de mais de 400.000 unidades de KitKat que desapareceu em trânsito entre a Itália e a Polônia em março de 2026. Utilizando técnicas de OSINT, análise de metadados de e-mail, geolocalização de imagens e análise de logs corporativos, o investigador deve identificar o vazador interno e desvendar a conspiração.

## 🛠️ Processo  

### 🔵 **Task 1: Investigation**

O foco desta tarefa é conduzir uma investigação completa de uma ameaça interna.

Conceitos:  
**Análise de Headers de E-mail:** Leitura cronológica inversa (de baixo para cima) dos campos `Received` para identificar o IP de origem real da mensagem. Neste caso, o IP aponta para a infraestrutura da **Mullvad VPN**, usada pelo denunciante para mascarar sua identidade.  
**Geolocalização e IMINT:** Uso de imagens de dashcam (Exhibit B) e pistas contextuais do memorando (como a cidade de **Hulín**) para localizar com precisão um posto de gasolina **Orlen** específico através do Google Maps, evitando buscas cegas em toda a rodovia.  
**Análise de Logs Corporativos:** Filtragem de arquivos CSV (`access_log.csv`) para identificar ações anômalas fora do horário comercial. A ação crítica foi um `EXPORT` do arquivo de rota sensível (`ROUTE_IT_PL_Q1_2026.pdf`).  
**Correlação de Dados e Desanonimização (OSINT):** Cruzamento de IDs de funcionários, tentativas de autenticação falhas com e-mails pessoais e o uso de ferramentas de busca reversa de e-mail (como Epieos) para vincular uma conta corporativa comprometida a uma identidade real no Google Maps.

- **Pergunta:** Que serviço de VPN foi utilizado para enviar o e-mail anónimo a partir do ficheiro .eml?  
**Resposta:** 'Mullvad'  
***Nota: A análise do header do e-mail revela o IP de origem `193.32.249.132`, que pertence ao ASN AS39351 (31173 Services AB), provedor que hospeda os nós de saída da rede Mullvad VPN.***

- **Pergunta:** Qual é a morada completa do posto de abastecimento onde o veículo desaparecido foi visto pela última vez?  
**Resposta:** 'Kroměřížská 1281, 768 24 Hulín, Czechia'  
***Nota: A imagem da dashcam mostra um posto Orlen. O memorando informa que a câmera foi recuperada perto de Hulín. Uma busca no Google Maps por "Orlen Hulín" retorna este endereço exato, que corresponde visualmente à imagem.***

- **Pergunta:** A que horas ocorreu a ação suspeita no sistema de planeamento de percursos, no dia 25 de março de 2026? (Formato: HH:MM:SS)  
**Resposta:** '22:14:09'  
***Nota: Ao filtrar o `access_log.csv` pela data de 25 de março de 2026, destaca-se uma única ação de `EXPORT` do arquivo de rota sensível fora do horário comercial, registrada exatamente neste timestamp.***

- **Pergunta:** Qual é o número de identificação do funcionário que enviou o e-mail anónimo?  
**Resposta:** 'BR-0312'  
***Nota: O denunciante afirmou estar trabalhando tarde e ter visto a atividade suspeita. O log de acesso mostra que o funcionário BR-0312 estava editando a planilha de horários dos motoristas (`DRIVER_SCHEDULE_WK13.xlsx`) às 23:41, confirmando sua presença no sistema naquela noite.***

- **Pergunta:** Qual é o número de identificação do funcionário responsável pela divulgação dos detalhes da remessa?  
**Resposta:** 'BR-0291'  
***Nota: Este é o ID vinculado à ação de `EXPORT` suspeita às 22:14:09. Além disso, logs anteriores mostram tentativas falhas de autenticação deste ID usando um endereço de e-mail pessoal, indicando a intenção de exfiltrar dados.***

- **Pergunta:** Qual é o nome completo da pessoa que divulgou a informação?  
**Resposta:** 'Radovan Blšťák'  
***Nota: O e-mail pessoal tentado pelo funcionário BR-0291 (`kraliknovak09@gmail.com`) foi submetido a uma busca reversa de OSINT (ex: Epieos). Isso revelou o perfil do Google associado, identificando o nome real como Radovan Blšťák, que inclusive deixou uma avaliação no Google Maps no posto de gasolina onde o caminhão foi visto.***
