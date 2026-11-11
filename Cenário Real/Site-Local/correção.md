# RELATÓRIO DE CORREÇÃO E MITIGAÇÃO PRÁTICA
**Projeto:** Mapeamento e Blindagem de Superfície de Ataque - Ambiente Web (WordPress)  
**Autor:** Herbert Molina  
**Data:** 04 de Novembro de 2026  
**Classificação:** Confidencial (Uso Interno e Tomada de Decisão)  

---

## COMO UTILIZAR ESTE DOCUMENTO

Este relatório foi desenvolvido para traduzir vulnerabilidades técnicas complexas em planos de ação de negócios. O objetivo não é apenas apontar falhas, mas fornecer um manual executivo e técnico para que a instituição saiba exatamente o que fazer, por que fazer e como fazer.

Cada item de correção segue uma estrutura padronizada:
- **O Problema:** Explicação da falha em linguagem clara, sem jargões excessivos.
- **Cenário de Ataque Simplificado:** Narrativa realista de como um invasor exploraria essa falha, baseada em modelagem de ameaças.
- **A Solução Recomendada:** A estratégia de defesa a ser adotada.
- **Passo a Passo Prático:** Instruções objetivas para a aplicação da correção.
- **Perfil de Execução:** Nível de conhecimento necessário para realizar a tarefa.

---

## VULNERABILIDADES CRÍTICAS (Ação Imediata: 0 a 7 dias)
*Estes itens representam risco iminente de comprometimento total do site, vazamento de dados de clientes (LGPD) e destruição da reputação local do negócio.*

### VULNERABILIDADE: Banco de Dados MariaDB Exposto na Internet (Porta 3306)
**O Problema:** O serviço de banco de dados que armazena todas as informações do site (usuários, senhas, dados de clientes, configurações) está configurado para aceitar conexões vindas de qualquer lugar da internet, não apenas do próprio servidor.

**Cenário de Ataque Simplificado:** Um invasor utiliza ferramentas automatizadas que varrem a internet procurando pela porta 3306 aberta. Ao encontrar o servidor, ele inicia um ataque de força bruta contra o usuário "root" ou "admin" do banco de dados. Se a senha for fraca ou padrão, ele obtém acesso total. A partir daí, ele pode baixar uma cópia completa do banco de dados (violando a LGPD) ou criar um novo usuário administrador no WordPress, assumindo o controle do site sem precisar da senha original.

**A Solução Recomendada:** Bloquear imediatamente o acesso externo à porta do banco de dados, restringindo as conexões apenas ao próprio servidor (localhost).

**Passo a Passo Prático:**
- Acessar o painel de controle do servidor (cPanel, Plesk ou firewall dedicado).
- Localizar a configuração de "Remote MySQL" ou regras de firewall de rede.
- Remover qualquer entrada que permita acesso a partir de "%" (qualquer host) ou endereços IP externos.
- Garantir que a única conexão permitida seja a partir de "127.0.0.1" ou "localhost".

**Perfil de Execução:** Administrador de Sistemas ou Suporte da Hospedagem (Nível: Intermediário).

---

### VULNERABILIDADE: Enumeração de Usuários via API REST do WordPress
**O Problema:** O WordPress possui uma funcionalidade padrão (API REST) que, quando acessada por um endereço específico, revela publicamente uma lista com os nomes de usuário (slugs), IDs e avatares de todos os administradores e editores do site.

**Cenário de Ataque Simplificado:** O invasor não precisa adivinhar o nome de login do administrador. Ele acessa o endpoint público da API e obtém o nome exato (por exemplo, "joao.silva"). Com essa informação, ele direciona um ataque de força bruta apenas para esse usuário específico, aumentando drasticamente as chances de sucesso. Alternativamente, ele usa esse nome para enviar um e-mail de phishing altamente personalizado (Spear Phishing), fingindo ser o suporte do site, fazendo com que o próprio administrador entregue sua senha voluntariamente.

**A Solução Recomendada:** Desabilitar a listagem pública de usuários na API REST para visitantes não autenticados.

**Passo a Passo Prático:**
- Instalar e ativar um plugin de segurança consolidado (como Wordfence, iThemes Security ou Solid Security).
- Nas configurações do plugin, localizar a opção relacionada à "API REST" ou "Proteção de Usuários".
- Ativar a configuração que desabilita a descoberta de usuários (frequentemente chamada de "Disable REST API for non-logged-in users" ou "Ocultar nomes de usuário").
- Alternativamente, adicionar um filtro específico no arquivo `functions.php` do tema ativo para bloquear esse endpoint.

**Perfil de Execução:** Desenvolvedor WordPress ou Webmaster (Nível: Básico a Intermediário).

---

### VULNERABILIDADE: Divulgação de Erros de Banco de Dados e Risco de Injeção SQL
**O Problema:** O site está configurado para exibir mensagens de erro detalhadas do banco de dados quando uma entrada inválida é processada (como no campo de busca), revelando a estrutura interna do sistema.

**Cenário de Ataque Simplificado:** O invasor insere um caractere especial (como uma aspa simples) no campo de busca do site. O site "quebra" e exibe um erro técnico. Usando ferramentas automatizadas (como sqlmap), o invasor explora essa falha de "Injeção SQL às Cegas" (Blind SQLi). Mesmo sem ver os dados na tela, a ferramenta faz perguntas ao banco de dados (verdadeiro/falso) e, pouco a pouco, extrai informações confidenciais, como hashes de senhas e dados de clientes, sem nunca precisar fazer login.

**A Solução Recomendada:** Desativar a exibição de erros de depuração em ambiente de produção e garantir que o código do site sanitize todas as entradas de dados.

**Passo a Passo Prático:**
- Acessar os arquivos do site via Gerenciador de Arquivos ou FTP.
- Abrir o arquivo `wp-config.php` na raiz do site.
- Localizar as linhas `define('WP_DEBUG', true);` e `define('WP_DEBUG_DISPLAY', true);`.
- Alterar ambos os valores para `false`.
- Solicitar ao desenvolvedor do tema ou plugin de busca que revise o código, garantindo o uso de funções de preparação de consultas do WordPress (como `$wpdb->prepare`) para evitar a injeção de código.

**Perfil de Execução:** Desenvolvedor WordPress (Nível: Intermediário).

---

## VULNERABILIDADES ALTAS (Ação em Curto Prazo: 7 a 30 dias)
*Estes itens facilitam a escalada de um ataque ou expõem vetores de entrada secundários que devem ser fechados.*

### VULNERABILIDADE: Painéis Administrativos Padrão e FTP Expostos sem MFA
**O Problema:** As interfaces de gerenciamento da hospedagem (cPanel, Webmail, Webdisk) e o serviço de transferência de arquivos (FTP, porta 21) estão acessíveis publicamente na internet, sem proteção adicional além de uma senha simples.

**Cenário de Ataque Simplificado:** O invasor foca no acesso FTP ou cPanel. Como muitos usuários reutilizam senhas ou usam senhas fracas, o invasor consegue acesso. Uma vez dentro do cPanel, ele não precisa hackear o WordPress. Ele simplesmente faz o upload de um arquivo malicioso (webshell) ou edita o arquivo `index.php` do site. O resultado imediato é que todos os visitantes do site são redirecionados para páginas de phishing ou anúncios maliciosos, destruindo a reputação do negócio local e fazendo com que o Google blackliste o domínio.

**A Solução Recomendada:** Restringir o acesso a esses painéis por endereço IP de confiança e implementar Autenticação de Múltiplos Fatores (MFA/2FA) obrigatória.

**Passo a Passo Prático:**
- No cPanel, acessar a ferramenta "Gerenciador de IPs" ou "Bloqueio de IP".
- Configurar o sistema para permitir acesso às portas do cPanel e Webmail apenas a partir do endereço IP fixo do escritório ou da equipe de TI.
- Na seção de Segurança do cPanel, localizar a opção "Autenticação de Dois Fatores" (Two-Factor Authentication) e ativá-la, vinculando-a a um aplicativo autenticador no celular.
- Desativar o acesso FTP se o Gerenciador de Arquivos do cPanel ou SFTP (mais seguro) forem suficientes para a operação.

**Perfil de Execução:** Administrador de Sistemas ou Webmaster (Nível: Básico).

---

## VULNERABILIDADES MÉDIAS E BAIXAS (Ação em Médio Prazo: 30 a 90 dias)
*Itens que, isoladamente, representam risco menor, mas que em conjunto degradam a postura de segurança e facilitam ataques automatizados.*

### VULNERABILIDADE: Ausência de Headers de Segurança HTTP
**O Problema:** O servidor web não envia instruções de segurança aos navegadores dos visitantes, deixando o site vulnerável a manipulações do lado do cliente.

**Cenário de Ataque Simplificado:** Um invasor convence um visitante a acessar o site através de um link manipulado. Como não há uma política de segurança de conteúdo (CSP) ou proteção contra clickjacking (X-Frame-Options), o navegador do visitante carrega o site dentro de um quadro invisível (iframe) controlado pelo invasor. Quando o visitante clica para interagir com o site, ele está, na verdade, clicando em botões controlados pelo invasor, podendo autorizar transações ou instalar extensões maliciosas sem perceber.

**A Solução Recomendada:** Configurar o servidor web para enviar cabeçalhos de segurança HTTP modernos em todas as respostas.

**Passo a Passo Prático:**
- Acessar o arquivo `.htaccess` na raiz do site WordPress.
- Adicionar as diretivas de cabeçalho recomendadas pelo OWASP no final do arquivo (incluindo Strict-Transport-Security, X-Content-Type-Options, X-Frame-Options e Content-Security-Policy).
- Testar a configuração em ferramentas como o Mozilla Observatory para garantir que não haja erros de sintaxe que derrubem o site.

**Perfil de Execução:** Desenvolvedor Web ou Administrador de Sistemas (Nível: Intermediário).

---

### VULNERABILIDADE: Exposição de Metadados de Plugins e Configuração do robots.txt
**O Problema:** Ferramentas de identificação revelam versões específicas de plugins (como Elementor e JetEngine), e o arquivo `robots.txt` expõe caminhos administrativos desnecessários.

**Cenário de Ataque Simplificado:** O invasor identifica que o site usa uma versão específica do Elementor. Ele consulta bancos de dados públicos de vulnerabilidades e descobre uma falha conhecida nessa versão exata. O arquivo `robots.txt`, que deveria apenas orientar motores de busca, acaba servindo como um "mapa" para o invasor, confirmando a existência de arquivos AJAX administrativos que ele pode tentar explorar automaticamente.

**A Solução Recomendada:** Manter o ambiente rigorosamente atualizado e limpar configurações que expõem a estrutura interna do site.

**Passo a Passo Prático:**
- Acessar o painel do WordPress e atualizar o núcleo (core), o tema e todos os plugins para as versões mais recentes.
- Remover e desinstalar completamente qualquer plugin ou tema que não esteja em uso ativo.
- Editar o arquivo `robots.txt` na raiz do site, removendo linhas `Allow` que apontam para `/wp-admin/` ou `/wp-includes/`, mantendo apenas as regras essenciais para indexação de conteúdo público.

**Perfil de Execução:** Webmaster ou Administrador do Site (Nível: Básico).

---

## PRÓXIMOS PASSOS E PROPOSTA DE VALOR

Para um negócio que depende da confiança local e da disponibilidade contínua do seu canal digital, a segurança não pode ser tratada como um detalhe técnico. As falhas identificadas são de configuração, o que significa que podem ser resolvidas rapidamente sem a necessidade de reescrever o site.

Apresentamos dois caminhos para a resolução:

**Opção A: Execução Interna Supervisionada**
A equipe interna ou o prestador de hospedagem atual utiliza este relatório como um roteiro de tarefas. Nossa consultoria fica disponível para validar as configurações aplicadas e realizar uma varredura de validação (re-teste) após a implementação para emitir o "Certificado de Conformidade".

**Opção B: Consultoria de Correção e Blindagem (Recomendada)**
Nossa equipe assume a execução técnica das configurações de firewall, restrição de acesso à API REST, aplicação de headers de segurança e hardening do ambiente WordPress.
Ao final, entregamos:
1. Relatório de Conformidade Técnica atestando o fechamento das brechas.
2. Documentação das novas regras de segurança aplicadas.
3. Sessão de treinamento de 1 hora para a equipe do negócio sobre boas práticas de senhas e identificação de phishing, mitigando o fator humano.

Este relatório serve como base formal para a tomada de decisão, demonstrando a devida diligência na proteção dos dados dos clientes e na continuidade das operações, em conformidade com os princípios da LGPD.

---

**Fim do Relatório**

**Contato do Autor:** Herbert Molina  
**Email:** herbertluizmolinaperfil@gmail.com  
**LinkedIn:** linkedin.com/in/herbert-molina  
