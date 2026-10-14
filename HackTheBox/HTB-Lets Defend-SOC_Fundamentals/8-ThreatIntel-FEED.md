# Relatório de Aprendizado: Feed de Inteligência de Ameaças

> **Curso:** SOC Fundamentals — Let's Defend / Hack The Box  
**Módulo:** Threat Intelligence Feed  
**Data:** Outubro de 2026  
**Nível:** Técnico Inicial  
**Status:** Concluído  
> 

---

## Objetivo de Aprendizado

Compreender o papel dos feeds de Inteligência de Ameaças (Threat Intelligence) na validação de indicadores de comprometimento (IOCs), a importância de consultar fontes externas durante uma investigação e, crucialmente, as limitações dessas ferramentas, como falsos negativos e a reatribuição histórica de endereços IP.

---

## Conceitos-Chave Abordados

### Definição e Propósito

- **O que são:** Conjuntos de dados (como hashes de malware, endereços IP ou domínios de servidores de Comando e Controle) fornecidos por empresas terceirizadas ou comunidades de segurança.
- **Função no SOC:** Orientar as investigações, permitindo que o analista verifique rapidamente se um artefato em mãos (ex: um hash de arquivo) já foi associado a atividades maliciosas conhecidas no passado.

### Fontes de Consulta

- Exemplos de fontes gratuitas e amplamente utilizadas na indústria: VirusTotal e Talos Intelligence.

### Limitações Críticas e Armadilhas Comuns

- **Ausência de Evidência não é Evidência de Ausência:** Se um hash de arquivo não retorna resultados maliciosos no VirusTotal, o analista não deve assumir automaticamente que o arquivo é seguro. É um erro grave. A análise estática e dinâmica do arquivo ainda é obrigatória.
- **Reatribuição de Endereços IP:** Um endereço IP listado como malicioso no passado (ex: usado como C2 na AWS) pode ter sido desligado e realocado meses depois para um uso legítimo (ex: um blog pessoal). O histórico malicioso de um IP não garante que ele seja uma ameaça no momento presente. O contexto temporal é fundamental.

---

## Aplicação Prática / Laboratório

> *Módulo com foco na consulta prática de IPs e hashes na página de "Threat Intel" do Let's Defend, aplicando o pensamento crítico sobre os resultados obtidos.*
> 

**Anotações pessoais:**

- A lição reforça que a inteligência de ameaças é um ponto de partida para a investigação, não a conclusão definitiva.
- A verificação cruzada é essencial: um único feed não conta a história completa, e a interpretação do analista sobre o contexto do artefato é insubstituível.

---

## Conexão com OSINT e Portfólio Profissional

A utilização de feeds de inteligência de ameaças possui paralelos metodológicos diretos e valiosos com a prática de OSINT:

- **Validação Cruzada de Indicadores:** Assim como o analista de SOC consulta um hash ou IP no VirusTotal, o investigador de OSINT deve cruzar um indicador (nome de usuário, e-mail, telefone, domínio) em múltiplas plataformas e bases de dados para construir um perfil confiável e evitar conclusões baseadas em uma única fonte.
- **Contexto Temporal e Reatribuição:** A armadilha da reatribuição de IPs no SOC é idêntica à reatribuição de nomes de domínio, números de telefone ou nomes de usuário no OSINT. Um perfil ou domínio que foi malicioso ou pertenceu a uma pessoa no passado pode hoje ser legítimo ou pertencer a outra pessoa. A data da informação é tão crítica quanto a informação em si.
- **Gerenciamento de Falsos Negativos:** No OSINT, assim como no SOC, a ausência de resultados em uma busca inicial não significa que o alvo não exista ou não tenha rastros. Significa apenas que a abordagem atual ou a fonte consultada não foi suficiente, exigindo a aplicação de técnicas alternativas, como análise de metadados, busca por variações do nome ou investigação de conexões indiretas.
