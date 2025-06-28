---
title: "API Para Pessoas de Negócio: Códigos HTTP"
date: 2024-10-21 00:04:51
tags: [apis, 2024]
---

Nesse texto reúno algumas dicas importantes sobre Códigos de Resposta HTTP, essenciais para o bom funcionamento de uma API e/ou produto digital.

## O que são Códigos de Resposta HTTP
Na comunicação HTTP, temos sempre dois atores: um **cliente** e um **servidor**. O cliente pede informações ou ações e o servidor interpreta e envia respostas, sempre de forma síncrona. Para que o cliente saiba o que aconteceu durante a solicitação feita ao servidor, as respostas do servidor possuem um código de resposta, para auxiliar no entendimento.

Dados podem ser enviados quando necessário pelo servidor, mas os códigos de resposta garantem que o cliente possa entender qual comportamento ocorreu..

## Famílias de código HTTP (1XX, 2XX, 3XX, 4XX e 5XX)

Para facilitar a interpretação pelo cliente, os códigos de resposta HTTP são classificados em diferentes "famílias", com base no primeiro dígito, e cada uma delas indica um tipo de situação ou resposta que o servidor está fornecendo ao cliente.

**1XX (Informacional**): Essas respostas são raramente vistas pelo usuário, pois indicam que o servidor recebeu a solicitação e que o cliente pode continuar o processo. 
**Exemplo: 100 Continue** significa que o cliente pode continuar enviando o corpo da solicitação, já que os cabeçalhos foram aceitos.

**2XX (Sucesso)**: Essa família indica que a solicitação foi recebida, compreendida e processada corretamente. O código mais comum é o **200 OK**, que informa que a operação foi concluída com sucesso. Outros exemplos incluem o **201 Created**, utilizado quando um novo recurso é criado, como ao cadastrar um novo usuário.

**3XX (Redirecionamento)**: Esses códigos informam que o cliente precisa tomar outra ação para completar a solicitação. O **301 Moved Permanently** indica que o recurso foi movido permanentemente para uma nova URL, enquanto o **302 Found** indica um redirecionamento temporário.

**4XX (Erros do Cliente)**: Esta categoria cobre situações em que houve um problema com a solicitação feita pelo cliente. O **404 Not Found** é um dos mais conhecidos e indica que o recurso solicitado não foi encontrado. Outro exemplo é o **400 Bad Request**, que indica que a solicitação não pôde ser processada devido a uma sintaxe incorreta.

**5XX (Erros do Servidor)**: Esses códigos indicam que o servidor encontrou um erro ao tentar processar a solicitação. O **500 Internal Server Error** é o mais comum e indica uma falha genérica no servidor. Outro exemplo é o **503 Service Unavailable**, que indica que o servidor está temporariamente incapaz de atender a solicitação, geralmente devido a manutenção ou sobrecarga.

## Dicas importantes

### Não precisamos usar todos os códigos HTTP

Os códigos de status HTTP são padronizados para facilitar a comunicação entre servidores e clientes (navegadores ou outras aplicações), mas não é obrigatório que todos eles sejam utilizados em uma aplicação. Na prática, muitas APIs e sistemas utilizam apenas um subconjunto desses códigos, especialmente os mais comuns, como o **200 OK**, **404 Not Found**, e **500 Internal Server Error**. O uso de muitos códigos pode complicar a manutenção ou a consistência das respostas em alguns sistemas, e é comum simplificar utilizando apenas os mais relevantes para o contexto da aplicação.

Isso não compromete o funcionamento da comunicação, desde que os códigos escolhidos sejam usados corretamente e correspondam ao comportamento esperado pelo cliente. O importante é **garantir que o cliente saiba** se a solicitação foi bem-sucedida ou se ocorreu um erro, e como lidar com as situações apresentadas. O uso consciente e simplificado dos códigos mais comuns garante clareza e eficiência nas respostas.


### Faça benchmarks
Empresas líderes em suas áreas, como Stripe e GitHub, são exemplos de excelência no uso de códigos HTTP, oferecendo APIs robustas, com respostas claras e padronizadas. Fazer bench dessas empresas permite adotar boas práticas já validadas por elas além de evitar cenários já passados pelas mesmas. Temos dois exemplos muito bons que são:

**Exemplo no Mercado Financeiro: Stripe**
A Stripe, uma das principais plataformas de pagamento online, é referência no uso de APIs bem documentadas e na aplicação criteriosa de códigos HTTP. No contexto de serviços financeiros, onde precisão e confiança são fundamentais, a Stripe define claramente o comportamento de sua API usando os códigos HTTP de forma consistente e previsível. Por exemplo:

**200 OK**: Usado para confirmações de sucesso em transações e operações com dados sensíveis.

**201 Created:** Utilizado quando um novo recurso é criado, como uma nova cobrança ou cliente, com a URL do novo recurso sendo retornada.

**400 Bad Request**: Quando uma solicitação falha devido a um erro do cliente, como falta de parâmetros obrigatórios ao criar uma cobrança.

**402 Payment Required**: Um código relativamente raro, mas usado pela Stripe para indicar que há um problema com o pagamento, como um cartão de crédito recusado.

A Stripe também oferece um excelente exemplo de como usar detalhadamente os códigos 4XX e 5XX para comunicar erros relacionados ao processamento de pagamentos, fornecendo mensagens detalhadas de erro e orientações claras de correção.

**Exemplo em Outras Áreas: GitHub (Tecnologia)**
No setor de tecnologia, o GitHub é uma referência para APIs usadas por desenvolvedores de software. Ele oferece uma API pública que permite interagir com repositórios, issues, pull requests, entre outras funcionalidades. O GitHub também adota um uso eficiente dos códigos HTTP:

**202 Accepted:** Usado quando uma ação foi aceita, mas ainda está em processamento, como a criação de uma build ou uma operação de merge.

**403 Forbidden:** Comumente retornado quando um usuário tenta acessar um repositório privado ou fazer ações para as quais não tem permissões.

**409 Conflict:** Utilizado para indicar conflitos, como quando um merge não pode ser concluído devido a alterações conflitantes.

Além disso, o GitHub faz um excelente uso do rate limiting (limitação de taxa) e retorna 429 Too Many Requests quando o cliente ultrapassa o limite de solicitações permitidas, incentivando o uso responsável da API.

### Códigos HTTP Mais Usados em APIs com Casos de Uso

Quando desenvolvemos APIs REST, o uso correto dos códigos de status HTTP é essencial para fornecer respostas claras e padronizadas aos clientes. Cada código transmite informações importantes sobre o sucesso ou falha de uma operação e ajuda os consumidores da API a entenderem como lidar com as respostas.

Abaixo estão os códigos HTTP mais comuns em APIs REST, junto com exemplos de casos de uso específicos:

##### 2XX (sucesso)

**200 OK**  
  **Uso:** A solicitação foi processada com sucesso e a resposta contém os dados solicitados ou a confirmação da operação.  
  **Caso:** Retornar uma lista de recursos ou os detalhes de um recurso específico após um `GET`. Também usado para confirmar sucesso em atualizações via `PUT` ou `PATCH`.

**201 Created**  
  **Uso:** Indica que um novo recurso foi criado com sucesso.  
  **Caso:** Após uma requisição `POST`, como ao registrar um novo usuário ou criar um item. A resposta deve incluir o cabeçalho `Location` com a URL do novo recurso criado.

**204 No Content**  
  **Uso:** A solicitação foi bem-sucedida, mas não há conteúdo para retornar.  
  **Caso:** Usado para operações como `DELETE`, quando o recurso foi removido com sucesso, ou para `PUT`/`PATCH`, quando uma atualização é realizada sem a necessidade de retornar dados.

##### 3XX (redirecionamento)

**301 Moved Permanently**  
  **Uso:** Indica que o recurso foi movido permanentemente para uma nova URL.  
  **Caso:** Ao mudar a estrutura da API e redirecionar clientes de uma rota antiga para uma nova, garantindo compatibilidade com versões anteriores.

**304 Not Modified**  
  **Uso:** Informa que o recurso não foi modificado desde a última solicitação, permitindo que o cliente use a versão em cache.  
  **Caso:** Em endpoints de `GET`, quando o cliente já possui uma cópia do recurso (com base no `ETag` ou `Last-Modified`), evitando o tráfego desnecessário de dados.

##### 4XX (erros do cliente)

**400 Bad Request**  
  **Uso:** A solicitação é inválida ou malformada, como erros de sintaxe ou parâmetros incorretos.  
  **Caso:** O cliente envia um corpo JSON malformado ou parâmetros de consulta inválidos, como ao tentar criar um recurso com dados faltantes ou incorretos.

**401 Unauthorized**  
  **Uso:** O cliente não forneceu credenciais de autenticação ou as credenciais são inválidas.  
  **Caso:** Tentativa de acessar um endpoint protegido sem token de autenticação ou com um token expirado.

**403 Forbidden**  
  **Uso:** O cliente está autenticado, mas não tem permissão para acessar o recurso.  
  **Caso:** Um usuário autenticado tenta acessar um recurso ou realizar uma ação para a qual não possui as permissões adequadas, como tentar deletar um recurso de outro usuário.

**404 Not Found**  
  **Uso:** O recurso solicitado não foi encontrado.  
  **Caso:** Tentativa de acessar um recurso que não existe ou que foi removido, como buscar por um ID inexistente em uma coleção de usuários.

**405 Method Not Allowed**  
  **Uso:** O método HTTP utilizado não é suportado para o recurso solicitado.  
  **Caso:** Tentar usar `POST` em um endpoint que só aceita `GET`, ou `DELETE` em um recurso que não permite exclusão.

**422 Unprocessable Entity**  
  **Uso:** A solicitação é bem formada, mas não pode ser processada devido a erros de validação nos dados.  
  **Caso:** Ao enviar um `POST` ou `PUT` com dados que falham em passar regras de validação, como um campo de e-mail ausente ou formato incorreto.

##### 5XX (erros do servidor)

**500 Internal Server Error**  
  **Uso:** Ocorreu um erro inesperado no servidor ao processar a solicitação.  
  **Caso:** Erros genéricos que não foram tratados adequadamente pelo servidor, como exceções não capturadas ou falhas no código.

**502 Bad Gateway**  
  **Uso:** O servidor, atuando como gateway ou proxy, recebeu uma resposta inválida de outro servidor upstream.  
  **Caso:** Em arquiteturas de microserviços, quando um serviço não consegue se comunicar corretamente com outro serviço de backend.

**503 Service Unavailable**  
  **Uso:** O servidor está temporariamente indisponível, geralmente por causa de manutenção ou sobrecarga.  
  **Caso:** Quando o serviço está em manutenção ou o servidor está com excesso de carga e não consegue processar novas solicitações.

**504 Gateway Timeout**  
  **Uso:** Um servidor, atuando como gateway ou proxy, não recebeu uma resposta a tempo de outro servidor upstream.  
  **Caso:** Quando um microserviço demora mais do que o esperado para responder, resultando em um timeout na comunicação entre serviços.

