---
title: "APIs para Pessoas de Negócio: Termos técnicos essenciais"
date: 2023-01-26 11:21:43
tags: [2023, apis, produtos digitais, tecnologia]
categories:
- [gallery]
---

Continuando a série de posts sobre APIs, trago hoje uma lista de termos mais usados e necessários para conhecer ao trabalhar com APIs. Vamos lá!


**Leia também**: 
1. [APIs para Pessoas de Negócio: uma breve introdução](https://danilocardoso.dev/blog/apis-pessoas-negocio-breve-introducao/)
2. [O que é necessário para construir APIs](https://danilocardoso.dev/blog/o-que-usar-pra-criar-apis/)

<img src="{{ site.baseurl }}/assets/dict.jpeg"/>


### REST
O padrão REST é um estilo de arquitetura de software para sistemas distribuídos, que define uma série de regras para a construção de APIs. Ele foi proposto pela primeira vez em 2000 por Roy Fielding, um dos principais autores do protocolo HTTP.

As principais características do REST são:

* Uso de **recursos** identificados por URIs 
* Uso dos **métodos** HTTP: GET, POST, PUT, DELETE, etc.
* Uso de representações de **recursos** em formatos como JSON ou XML
* Uso de **protocolos** padrão da web, como HTTP e URIs

O objetivo do padrão é proporcionar uma forma consistente e simples de acessar recursos em sistemas distribuídos, usando os protocolos e padrões já estabelecidos na web. Isso permite que diferentes aplicativos e plataformas possam se comunicar de forma fácil e eficiente.

### API REST
API é um padrão de arquitetura para construir aplicações baseadas na web. Ele descreve como a comunicação entre sistemas deve ser feita, permitindo que diferentes sistemas se comuniquem de forma simples e eficiente. As APIs REST usam os métodos HTTP - como GET, POST, PUT e DELETE - para manipular dados - também chamados de **recursos** - em um servidor. Em geral, as APIs REST são implementadas usando o protocolo HTTP e são acessadas por meio de URLs.

### Protocolo HTTP
O HTTP é um protocolo de rede usado para transmitir informações na internet. Ele é usado para comunicar informações entre servidores e clientes, como navegadores web, aplicativos móveis e outros sistemas.

Ele funciona com base em solicitações e respostas. Quando um cliente envia uma solicitação para um servidor usando o HTTP, o servidor responde com uma resposta. As solicitações geralmente incluem um método HTTP, como GET, POST, PUT ou DELETE, e uma URL que identifica o recurso que o cliente deseja acessar. As respostas geralmente incluem um código de status HTTP, que indica se a solicitação foi bem-sucedida, e dados, como HTML, JSON ou XML.

É um protocolo sem estado, o que significa que as solicitações são independentes e não precisam de informações sobre solicitações anteriores para serem processadas. No entanto, para manter a conexão entre o cliente e o servidor, o protocolo pode ser usado juntamente com o protocolo HTTPS (HTTP Seguro) que usa o protocolo SSL ou TLS para criptografar as informações transmitidas.

O HTTP é amplamente usado na internet para acessar páginas web, transferir arquivos, acessar recursos de APIs e realizar outras tarefas. Ele é uma parte fundamental da arquitetura da web e é suportado por praticamente todos os navegadores e sistemas operacionais.

### Recurso
Os **recursos** são objetos ou entidades que são **expostos** pela API para serem acessados, criados, atualizados ou excluídos. Eles podem desde dados - como usuários, produtos, etc. - até operações - como login, upload de arquivos, etc. 

### Endpoint
*Endpoints* são os pontos finais de uma API onde os clientes podem acessar os recursos (como dados) fornecidos pela API. Eles são especificados por uma URL e geralmente são acessados ​​usando métodos HTTP. Cada *endpoint* geralmente representa um **recurso** específico, como um conjunto de dados ou uma operação que pode ser realizada. Por exemplo, uma API de gerenciamento de usuários pode ter um *endpoint* para criar um novo usuário, outro para atualizar um usuário existente e outro para recuperar informações sobre um usuário específico.

### Cliente HTTP
Um cliente HTTP é um programa ou aplicativo que faz **requisições** HTTP para um servidor e lida com as **respostas**. Ele pode ser desde um navegador web até um aplicativo móvel ou uma biblioteca de software usada por outro programa.

### Métodos HTTP
Os métodos HTTP - também conhecidos como **verbos** HTTP - são usados ​​para indicar a ação desejada a ser realizada em um recurso específico pela API REST. Os métodos HTTP mais comuns são:

* **GET**: recupera informações sobre um recurso específico.
* **POST**: cria um novo recurso.
* **PUT**: atualiza um recurso existente.
* **DELETE**: exclui um recurso existente.
* **PATCH**: atualiza parcialmente um recurso existente.
* **OPTIONS**: obtém informações sobre as opções de comunicação disponíveis para um recurso específico.

Cada método HTTP é projetado para realizar uma ação específica e é usado em conjunto com um endpoint específico de uma API REST.

### Request - ou requisição
Em uma API, uma *request* é um **pedido feito por um cliente** - como um aplicativo ou usuário - para acessar ou manipular recursos expostos pela API. Uma solicitação inclui o método HTTP, a URL do recurso e, opcionalmente, o corpo da solicitação, que contém os dados enviados para a API.

Exemplo de uma request GET: https://gorest.co.in/public/v2/users

Quando você entra nesse link acima está fazendo uma request. O JSON que aparece é a resposta.

### Response - ou resposta
Uma *response* é a resposta retornada pela API em resposta a uma solicitação. Ele geralmente inclui informações como o status HTTP (como 200 OK, 404 Not Found, etc.), o corpo da resposta, que contém os dados retornados pela API, e os cabeçalhos, que contêm informações adicionais sobre a resposta.

### Status HTTP
É um código numérico retornado pelo **servidor** em uma resposta HTTP que indica o resultado da solicitação feita pelo cliente. Ele é composto por um código de três dígitos, onde o primeiro dígito indica a categoria do status.

As categorias dos status HTTP são: 

* 1xx (Informational): a solicitação foi recebida pelo servidor e está sendo processada.
* 2xx (Successful): a solicitação foi processada com sucesso pelo servidor. Exemplos: 200 OK, 201 Created.
* 3xx (Redirection): a solicitação foi processada, mas o cliente precisa tomar outra ação para continuar. Exemplos: 301 Moved Permanently, 302 Found.
* 4xx (Client Error): a solicitação não pôde ser processada devido a um erro no lado do cliente. Exemplos: 400 Bad Request, 401 Unauthorized.
5xx (Server Error): a solicitação não pôde ser processada devido a um erro no lado do servidor. Exemplos: 500 Internal Server Error, 503 Service Unavailable.

Os códigos de status HTTP são importantes porque eles ajudam a entender o que aconteceu com a solicitação e o que é necessário fazer a seguir. Por exemplo, se o cliente receber um código de status 200 OK, ele sabe que a solicitação foi processada com sucesso e os dados podem ser lidos na resposta. Se o cliente receber um código de status 401 Unauthorized, ele sabe que precisa fornecer credenciais válidas antes de continuar.

### Query Parameters
São parâmetros adicionais que são incluídos na URL de uma requisição HTTP para fornecer informações adicionais para o servidor. Eles são usados para filtrar, classificar ou paginar dados retornados por uma API.

Exemplo:

```bash
GET /users?limit=10&offset=20&sort=name
```

Neste exemplo, a requisição GET está solicitando a lista de usuários com limite de 10, offset de 20 e ordenado pelo nome.

Os query parameters são usados ​​em requisições GET, pois elas são usadas para recuperar dados e não têm efeitos colaterais. No entanto, eles também podem ser usados ​​em outros tipos de requisições, como DELETE ou PUT, para fornecer informações adicionais.

### Paginação
A paginação de API é um mecanismo usado para dividir uma grande quantidade de dados em "páginas" menores, para que possam ser lidos e processados ​​de forma mais eficiente. Isso é útil pois algumas APIs lidam com grandes quantidades de dados e podem ser acessadas por vários clientes ao mesmo tempo.

Existem várias maneiras de implementar a paginação de uma API, mas as mais comuns são:

* **Limit-Offset**: são enviados os parâmetros "limit" e "offset" nos *query parameters*, onde *limit* é a quantidade de itens por página e *offset* é a partir de qual item começa a paginação;
* **Cursor**: é enviado um cursor como parâmetro, e ele representa a posição atual na lista de dados.

Além disso, é comum que a resposta da API contenha informações sobre a paginação, como o total de itens, o total de páginas, a página atual, a possibilidade de acessar a próxima e anterior página, etc.

A paginação é uma boa prática para evitar problemas de desempenho e melhorar a experiência do usuário, pois permite que os clientes acessem e processem dados de forma mais eficiente.

### API Gateway
API Gateways são componentes de **arquitetura** que servem como um ponto único de entrada para uma ou mais APIs. Eles geralmente são usados ​​para fornecer uma camada de segurança, gerenciamento de tráfego, autenticação, autorização e outras funcionalidades para as APIs.

Algumas das principais funcionalidades de um API Gateway incluem:

* **Roteamento de chamadas**: encaminhar chamadas para o back-end correto, baseado em regras configuráveis.
* **Autenticação e autorização**: autenticar e autorizar usuários que acessam as APIs, geralmente usando tokens JWT (JSON Web Token) ou OAuth.
* **Caching**: armazenar em cache respostas de API para melhorar o desempenho.
* **Rate limiting**: limitar o número de chamadas que um usuário ou aplicativo pode fazer em um período de tempo específico.
* **Transformação de mensagem**: transformar o formato de mensagem de entrada e saída para tornar as APIs mais flexíveis e fáceis de usar.

Além disso, os API Gateways também fornecem ferramentas de monitoramento e gerenciamento de APIs, como log de chamadas, estatísticas de uso e alertas de erros.

### Backend
Backend é a parte de uma aplicação que cuida das operações e lógicas que não são visíveis para o usuário final. Ele geralmente inclui componentes como bancos de dados, serviços de autenticação e autorização, lógica de negócios e outros componentes que são necessários para o funcionamento da aplicação.

A comunicação entre backend e front-end é feita através de chamadas de API, onde o front-end envia **requisições** e o backend retorna as **respostas**. O backend é responsável por lidar com a lógica de negócios, validação de dados, autenticação, autorização, e outras tarefas que são necessárias para o funcionamento da aplicação.

### Token
Um token é um objeto que contém informações de autenticação e autorização que são usadas para garantir que somente usuários autorizados possam acessar recursos protegidos em uma API. Ele é gerado pelo sistema de autenticação do backend e é enviado para o cliente HTTP como parte da resposta de uma chamada de login bem-sucedida.

Os tokens são codificados com informações de autenticação, como o ID do usuário e as permissões do usuário, e são assinados digitalmente para garantir que eles não possam ser alterados. Existem vários tipos de tokens, como JWT (JSON Web Token) e OAuth tokens, e eles são geralmente enviados no cabeçalho de autorização das chamadas de API subsequentes.

O servidor de API, ao receber uma requisição, verifica se o token é válido e se o usuário tem acesso ao recurso solicitado. Se o token é inválido ou o usuário não tem acesso, o servidor retorna um status HTTP de erro. O token é geralmente armazenado no cliente, e é enviado em todas as requisições subsequentes, para que o servidor possa identificar o usuário e garantir que ele tenha acesso aos recursos permitidos.

### JWT
JWT (JSON Web Token) é um formato de token de autenticação que é usado para transmitir informações de autenticação de forma segura entre sistemas. Ele é composto por três partes: um cabeçalho, um corpo e uma assinatura.

* O **cabeçalho** contém informações sobre o tipo do token e o algoritmo usado para assinar o token.
* O **corpo (ou payload)** contém as informações de autenticação, como o ID e as permissões do usuário. Essas informações são codificadas como um objeto JSON.
* A **assinatura** é gerada usando o algoritmo especificado no cabeçalho e uma chave secreta, e é usada para garantir que o token não possa ser alterado.

JWTs podem ser assinados usando vários algoritmos, como HMAC ou RSA. Eles são geralmente enviados no cabeçalho de autorização das chamadas de API, como "Authorization: Bearer [JWT]" para que o servidor possa verificar a validade do token e as informações de autenticação contidas nele.

JWT é amplamente utilizado em sistemas de autenticação distribuídos, onde diferentes sistemas precisam compartilhar informações de autenticação de forma segura. Ele é usado em conjunto com protocolos como OAuth 2.0 e OpenID Connect, visando fornecer autenticação e autorização para aplicativos e usuários.

### Autenticação 
Autenticação é o processo de **verificar a identidade** de um usuário ou aplicativo que está tentando acessar uma API. Isso envolve o usuário fornecendo credenciais, como nome de usuário e senha, e o sistema de autenticação verificando essas credenciais em um banco de dados de usuários. Se as credenciais são válidas, o sistema emite um token de autenticação, como um JWT, que é usado para autorizar acesso a recursos protegidos.

### Autorização
Autorização é o processo de determinar se um usuário ou aplicativo autenticado tem acesso a um recurso específico. Isso envolve o servidor de API verificando as informações de autenticação contidas no token de autenticação e comparando-as com as regras de acesso configuradas. Por exemplo, se o usuário tem permissão para acessar o recurso ou se o aplicativo tem acesso à funcionalidade específica. Se o usuário ou aplicativo não tem acesso, o servidor retorna um status HTTP de erro.

### JSON
O JSON (*JavaScript Object Notation*) é um formato de texto leve e fácil de ler que é usado para transmitir dados estruturados entre sistemas. Ele foi criado a partir do formato JavaScript, mas é independente de qualquer linguagem de programação.

O formato JSON é baseado em um conjunto simples de regras para representar dados estruturados, como objetos (que são coleções de pares nome-valor) e *arrays* (que são coleções de valores). Ele suporta diferentes tipos de dados, incluindo números, strings, booleanos e objetos aninhados.

Alguns exemplos de dados em JSON:

```json
{
    "nome": "João das Neves",
    "idade": 35,
    "endereco": {
        "rua": "Rua Muros",
        "cidade": "Westeros",
        "estado": "MG",
        "cep": "34999999"
    },
    "telefones": [
        {
            "tipo": "residencial",
            "numero": "3312345678"
        },
        {
            "trabalho": "trabalho",
            "numero": "3312345678"
        }
    ]
}	
```

```json
[
   {
      "id":1,
      "nome":"Produto 1",
      "preco":19.99
   },
   {
      "id":2,
      "nome":"Produto 2",
      "preco":29.99
   }
]
```

### CI/CD

CI/CD é uma metodologia de desenvolvimento de software que visa **automatizar** o processo de integração, construção, testes e implantação de códigos. Ele é composto por dois principais processos: *Continuous Integration* (CI) e *Continuous Deployment* (CD).

*Continuous Integration* (CI) é o processo de integrar o código de diferentes desenvolvedores em um repositório central de forma contínua. Isso é feito usando ferramentas como Jenkins, Travis CI ou CircleCI, que automatizam o processo de construção, testes e validação de código.

*Continuous Deployment* (CD) é o processo de automatizar a implantação de código em ambientes de produção. Isso é feito usando ferramentas como Jenkins, Ansible, ou Terraform. Ele permite que as novas funcionalidades e correções de bugs sejam disponibilizadas rapidamente para os usuários finais.

O processo CI/CD é considerado essencial para o desenvolvimento de software de forma ágil, pois ajuda a detectar e corrigir problemas rapidamente, aumenta a qualidade do código e ajuda a entregar novas funcionalidades de forma rápida e confiável para os usuários.

### Webhook 
Um webhook é uma forma de permitir que um sistema externo seja **notificado** sobre eventos ocorridos em outro sistema. Ele é basicamente uma URL que é chamada pelo sistema "emissor" sempre que um determinado evento ocorre. O sistema "receptor" pode então usar essa informação para atualizar seus próprios dados ou realizar outras ações.

Exemplo: imagine que você tem um sistema de gerenciamento de tarefas e deseja ser notificado sempre que uma nova tarefa é criada em outro sistema. Você pode configurar um *webhook* no outro sistema para chamar uma URL específica em seu próprio sistema sempre que uma nova tarefa é criada. Seu sistema pode, dessa forma, usar a informação para atualizar sua própria lista de tarefas.

Webhooks são muito úteis para **integrar sistemas** e automatizar fluxos de trabalho. Eles são simples de configurar e usar e não requerem que você mantenha uma conexão constante com outro sistema, o que pode economizar recursos e melhorar a escalabilidade.


### CRUD
CRUD é um acrônimo para as quatro operações básicas de **persistência de dados**: Create, Read, Update e Delete. Essas operações são usadas para gerenciar e manipular dados em um banco de dados ou outro sistema de armazenamento de dados.

* Create (Criação): permite adicionar novos dados ao sistema de armazenamento.
* Read (Leitura): permite ler ou recuperar dados do sistema de armazenamento.
* Update (Atualização): permite atualizar os dados existentes no sistema de armazenamento.
* Delete (Exclusão): permite excluir dados do sistema de armazenamento.

Sendo assim, CRUD se torna uma abordagem simples e amplamente utilizada para gerenciar dados em aplicativos e sistemas. Ele é muito usado em conjunto com APIs REST para fornecer operações CRUD através da web.
