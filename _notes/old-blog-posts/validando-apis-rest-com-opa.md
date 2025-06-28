---
title: Validando APIs REST com Open Policy Agent
date: 2022-12-20 17:21:27
---

O Open Policy Agent, que [citei no blog há algumas semanas atrás](https://danilocardoso.dev/blog/centralizando-governanca-com-opa/), é uma ferramenta que permite a criação de políticas de forma centralizada, afim de gerenciar e validar diferentes aspectos de segurança das suas aplicações, seja de infra como arquitetura. Uma das validações que o OPA permite realizar é a de **contratos de API**.

Validar contratos é um aspecto muito importante em uma estratégia de APIs porque garante que os critérios definidos pelo time de arquitetura e negócio estão sendo seguidos pelas pessoas desenvolvedoras. Uma API fora do padrão traz inúmeros problemas para instituições, como por exemplo:

* **Alta carga cognitiva para stakeholders.** Padrões existem para tornar a comunicação mais efetiva, definindo **símbolos comuns** que pessoas de diferentes contextos possam entender. Uma API fora dos padrões exige reuniões com quem desenhou o contrato e explicações técnicas para que os stakeholders possam entender porque foi feito daquela forma. Definir regras para contratos e valida-las a cada deploy é uma forma de **diminuir a carga cognitiva** para as pessoas envolvidas.
* **Débito técnico constante.** Uma API que já começa sem padrão tende a se tornar uma dor de cabeça para as equipes, já que inúmeros problemas podem ocorrer. Performance, disponibilidade e confiabilidade são apenas alguns exemplos de **[*ilities*](http://www.softwarearchitecturenotes.com/architecturerequirements.html)** que são impactados com APIs fora de um padrão técnico pré-estabelecido.  
* **Problemas para integrar.** Os padrões de desenho para API existem para que qualquer empresa consiga integrar seus produtos através de um determinado padrão, entre tantos outros casos de uso. Quando os padrões de mercado não são seguidos, toda e qualquer integração vai exigir documentações adicionais, reuniões e refinamento de requisitos, já que aquela API pode ter sido desenhada e implementada de qualquer jeito possível. E acredite, existem muitas formas de escrever uma API quando não existe um padrão de mercado balizando as entregas. 

<img src="{{ site.baseurl }}/assets/path3.jpeg"/>

## Opções ao validar APIs

Existem várias formas de validar o contrato de uma API. Uma das mais famosas é com o [Spectral](https://stoplight.io/open-source/spectral), ferramenta *open source* que permite definir uma série de políticas para suas APIs. O que vou mostrar nesse texto é como usar o OPA para validar os contratos de duas formas diferentes, mas é bom deixar claro que existem N outras alternativas no mercado.

### Validando com OPA

Para usar OPA diretamente, é necessário instalar a ferramenta, o que pode ser feito com esse comando:

```bash
curl -L -o opa https://github.com/open-policy-agent/opa/releases/download/v0.11.0/opa_linux_amd64
```

Após isso, é necessário tornar o arquivo executável:

```bash
chmod 755 ./opa
```

A partir desse momento basta executar o arquivo passando alguns parâmetros, a saber:

* ***bundle***: são *sets* de políticas que podem estar em diferentes diretórios ou URLs e podem ser usados pelo OPA *on-the-fly*, sem que seja necessário reiniciar seu serviço
* ***format***: definir o valor desse campo como *pretty* permite que a validação retorne em um formato de melhor leitura humana, para fins de debug. Sem esse parâmetro o retorno trará algumas informações a mais. Ambos retornos são em JSON
* ***input:*** aqui é onde o contrato que será validado deve ser atribuído. Nesse caso estamos usando um arquivo em JSON no [padrão OpenAPI](https://www.openapis.org). 

Dessa forma, o comando executado fica assim:

```bash
opa eval \
  --bundle ./spego/src \
  --format pretty \
  --input ./spego/example/inputs/openapi.json \
  "data.openapi.main.results"
```

Nesse exemplo estamos usando um *bundle* de políticas que está disponível [nesse diretório](https://github.com/kevinswiber/spego), chamado Spego. Com esse *bundle* é possível utilizar algumas validações feitas pelo *Spectral*, para aumentar a rigidez dos padrões adotados para APIs, indo além do padrão OpenAPI. 

Para executar esse exemplo peguei o arquivo Swagger do PetStore para validar, tendo o seguinte resultado:

```json
[
  {
    "code": "duplicated-entry-in-enum",
    "status": "success"
  },
  {
    "code": "info-contact",
    "status": "success"
  },
  {
    "code": "info-description",
    "status": "success"
  },
  {
    "code": "no-eval-in-markdown",
    "status": "success"
  },
  {
    "code": "no-script-tags-in-markdown",
    "status": "success"
  },
  {
    "code": "openapi-tags-uniqueness",
    "status": "success"
  },
  {
    "code": "operation-description",
    "status": "success"
  },
  {
    "code": "operation-operationId",
    "status": "success"
  },
  {
    "code": "operation-operationId-unique",
    "status": "success"
  },
  {
    "code": "operation-operationId-valid-in-url",
    "status": "success"
  },
  {
    "code": "operation-parameters",
    "status": "success"
  },
  {
    "code": "operation-success-response",
    "message": "Operation must have at least one \"2xx\" or \"3xx\" response.",
    "path": [
      "paths",
      "/pet/{petId}",
      "delete",
      "responses"
    ],
    "severity": "warn",
    "status": "failure"
  },
  {
    "code": "operation-success-response",
    "message": "Operation must have at least one \"2xx\" or \"3xx\" response.",
    "path": [
      "paths",
      "/pet/{petId}",
      "post",
      "responses"
    ],
    "severity": "warn",
    "status": "failure"
  },
  {
    "code": "operation-success-response",
    "message": "Operation must have at least one \"2xx\" or \"3xx\" response.",
    "path": [
      "paths",
      "/store/order/{orderId}",
      "delete",
      "responses"
    ],
    "severity": "warn",
    "status": "failure"
  },
  {
    "code": "operation-success-response",
    "message": "Operation must have at least one \"2xx\" or \"3xx\" response.",
    "path": [
      "paths",
      "/user",
      "post",
      "responses"
    ],
    "severity": "warn",
    "status": "failure"
  },
  {
    "code": "operation-success-response",
    "message": "Operation must have at least one \"2xx\" or \"3xx\" response.",
    "path": [
      "paths",
      "/user/logout",
      "get",
      "responses"
    ],
    "severity": "warn",
    "status": "failure"
  },
  {
    "code": "operation-success-response",
    "message": "Operation must have at least one \"2xx\" or \"3xx\" response.",
    "path": [
      "paths",
      "/user/{username}",
      "delete",
      "responses"
    ],
    "severity": "warn",
    "status": "failure"
  },
  {
    "code": "operation-success-response",
    "message": "Operation must have at least one \"2xx\" or \"3xx\" response.",
    "path": [
      "paths",
      "/user/{username}",
      "put",
      "responses"
    ],
    "severity": "warn",
    "status": "failure"
  },
  {
    "code": "operation-tag-defined",
    "status": "success"
  },
  {
    "code": "operation-tags",
    "status": "success"
  },
  {
    "code": "path-declarations-must-exist",
    "status": "success"
  },
  {
    "code": "path-keys-no-trailing-slash",
    "status": "success"
  },
  {
    "code": "path-not-include-query",
    "status": "success"
  },
  {
    "code": "path-params",
    "message": "Operation must define parameter \"{orderId}\" as expected by path \"/store/order/{orderId}\".",
    "path": [
      "paths",
      "/store/order/{orderId}",
      "delete"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Operation must define parameter \"{orderId}\" as expected by path \"/store/order/{orderId}\".",
    "path": [
      "paths",
      "/store/order/{orderId}",
      "get"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Operation must define parameter \"{petId}\" as expected by path \"/pet/{petId}\".",
    "path": [
      "paths",
      "/pet/{petId}",
      "delete"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Operation must define parameter \"{petId}\" as expected by path \"/pet/{petId}\".",
    "path": [
      "paths",
      "/pet/{petId}",
      "get"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Operation must define parameter \"{petId}\" as expected by path \"/pet/{petId}\".",
    "path": [
      "paths",
      "/pet/{petId}",
      "post"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Operation must define parameter \"{petId}\" as expected by path \"/pet/{petId}/uploadImage\".",
    "path": [
      "paths",
      "/pet/{petId}/uploadImage",
      "post"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Operation must define parameter \"{username}\" as expected by path \"/user/{username}\".",
    "path": [
      "paths",
      "/user/{username}",
      "delete"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Operation must define parameter \"{username}\" as expected by path \"/user/{username}\".",
    "path": [
      "paths",
      "/user/{username}",
      "get"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Operation must define parameter \"{username}\" as expected by path \"/user/{username}\".",
    "path": [
      "paths",
      "/user/{username}",
      "put"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Parameter \"orderId\" must be used in path \"/store/order/{orderId}\".",
    "path": [
      "paths",
      "/store/order/{orderId}",
      "delete",
      "parameters",
      "0"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Parameter \"orderId\" must be used in path \"/store/order/{orderId}\".",
    "path": [
      "paths",
      "/store/order/{orderId}",
      "get",
      "parameters",
      "0"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Parameter \"petId\" must be used in path \"/pet/{petId}\".",
    "path": [
      "paths",
      "/pet/{petId}",
      "delete",
      "parameters",
      "1"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Parameter \"petId\" must be used in path \"/pet/{petId}\".",
    "path": [
      "paths",
      "/pet/{petId}",
      "get",
      "parameters",
      "0"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Parameter \"petId\" must be used in path \"/pet/{petId}\".",
    "path": [
      "paths",
      "/pet/{petId}",
      "post",
      "parameters",
      "0"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Parameter \"petId\" must be used in path \"/pet/{petId}/uploadImage\".",
    "path": [
      "paths",
      "/pet/{petId}/uploadImage",
      "post",
      "parameters",
      "0"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Parameter \"username\" must be used in path \"/user/{username}\".",
    "path": [
      "paths",
      "/user/{username}",
      "delete",
      "parameters",
      "0"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Parameter \"username\" must be used in path \"/user/{username}\".",
    "path": [
      "paths",
      "/user/{username}",
      "get",
      "parameters",
      "0"
    ],
    "severity": "error",
    "status": "failure"
  },
  {
    "code": "path-params",
    "message": "Parameter \"username\" must be used in path \"/user/{username}\".",
    "path": [
      "paths",
      "/user/{username}",
      "put",
      "parameters",
      "0"
    ],
    "severity": "error",
    "status": "failure"
  }
]
```

Como podemos ver o resultado um compilado de todos os resultados em JSON, mostrando tantos as políticas que foram atendidas e quais falharam. 

### Validando com conftest

Uma outra forma de validar contratos de APIs REST com OPA é através do [conftest](https://conftest.dev), que é uma ferramenta para escrita de testes de arquivos de configuração. Com ela podemos criar scripts que validam arquivos de configuração, tendo um resultado em formato textual, exibido na linha de comando.

Para instalar a ferramenta basta executar os comandos abaixo:

```bash
LATEST_VERSION=$(wget -O - "https://api.github.com/repos/open-policy-agent/conftest/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/' | cut -c 2-)
wget "https://github.com/open-policy-agent/conftest/releases/download/v${LATEST_VERSION}/conftest_${LATEST_VERSION}_Linux_x86_64.tar.gz"
tar xzf conftest_${LATEST_VERSION}_Linux_x86_64.tar.gz
sudo mv conftest /usr/local/bin
``` 

Vamos usar o mesmo arquivo Swagger para validar as regras. O comando para que isso seja feito é esse:

```bash
conftest test -n "openapi.main" ./openapi.json
```
Como podemos ver na sintaxe, o primeiro parâmetro passado são as regras que devem ser usadas - usamos o mesmo bundle, Spego - e como segundo parâmetro passamos o arquivo Swagger. O resultado obtido rodando a feramenta foi:

```bash
WARN - ./openapi.json - openapi.main - operation-success-response - Operation must have at least one "2xx" or "3xx" response. [paths/~1pet~1{petId}/delete/responses]
WARN - ./openapi.json - openapi.main - operation-success-response - Operation must have at least one "2xx" or "3xx" response. [paths/~1pet~1{petId}/post/responses]
WARN - ./openapi.json - openapi.main - operation-success-response - Operation must have at least one "2xx" or "3xx" response. [paths/~1store~1order~1{orderId}/delete/responses]
WARN - ./openapi.json - openapi.main - operation-success-response - Operation must have at least one "2xx" or "3xx" response. [paths/~1user/post/responses]
WARN - ./openapi.json - openapi.main - operation-success-response - Operation must have at least one "2xx" or "3xx" response. [paths/~1user~1logout/get/responses]
WARN - ./openapi.json - openapi.main - operation-success-response - Operation must have at least one "2xx" or "3xx" response. [paths/~1user~1{username}/delete/responses]
WARN - ./openapi.json - openapi.main - operation-success-response - Operation must have at least one "2xx" or "3xx" response. [paths/~1user~1{username}/put/responses]
FAIL - ./openapi.json - openapi.main - path-params - Operation must define parameter "{petId}" as expected by path "/pet/{petId}". [paths/~1pet~1{petId}/delete]
FAIL - ./openapi.json - openapi.main - path-params - Parameter "petId" must be used in path "/pet/{petId}". [paths/~1pet~1{petId}/delete/parameters/1]
FAIL - ./openapi.json - openapi.main - path-params - Operation must define parameter "{petId}" as expected by path "/pet/{petId}". [paths/~1pet~1{petId}/get]
FAIL - ./openapi.json - openapi.main - path-params - Parameter "petId" must be used in path "/pet/{petId}". [paths/~1pet~1{petId}/get/parameters/0]
FAIL - ./openapi.json - openapi.main - path-params - Operation must define parameter "{petId}" as expected by path "/pet/{petId}". [paths/~1pet~1{petId}/post]
FAIL - ./openapi.json - openapi.main - path-params - Parameter "petId" must be used in path "/pet/{petId}". [paths/~1pet~1{petId}/post/parameters/0]
FAIL - ./openapi.json - openapi.main - path-params - Operation must define parameter "{petId}" as expected by path "/pet/{petId}/uploadImage". [paths/~1pet~1{petId}~1uploadImage/post]
FAIL - ./openapi.json - openapi.main - path-params - Parameter "petId" must be used in path "/pet/{petId}/uploadImage". [paths/~1pet~1{petId}~1uploadImage/post/parameters/0]
FAIL - ./openapi.json - openapi.main - path-params - Operation must define parameter "{orderId}" as expected by path "/store/order/{orderId}". [paths/~1store~1order~1{orderId}/delete]
FAIL - ./openapi.json - openapi.main - path-params - Parameter "orderId" must be used in path "/store/order/{orderId}". [paths/~1store~1order~1{orderId}/delete/parameters/0]
FAIL - ./openapi.json - openapi.main - path-params - Operation must define parameter "{orderId}" as expected by path "/store/order/{orderId}". [paths/~1store~1order~1{orderId}/get]
FAIL - ./openapi.json - openapi.main - path-params - Parameter "orderId" must be used in path "/store/order/{orderId}". [paths/~1store~1order~1{orderId}/get/parameters/0]
FAIL - ./openapi.json - openapi.main - path-params - Operation must define parameter "{username}" as expected by path "/user/{username}". [paths/~1user~1{username}/delete]
FAIL - ./openapi.json - openapi.main - path-params - Parameter "username" must be used in path "/user/{username}". [paths/~1user~1{username}/delete/parameters/0]
FAIL - ./openapi.json - openapi.main - path-params - Operation must define parameter "{username}" as expected by path "/user/{username}". [paths/~1user~1{username}/get]
FAIL - ./openapi.json - openapi.main - path-params - Parameter "username" must be used in path "/user/{username}". [paths/~1user~1{username}/get/parameters/0]
FAIL - ./openapi.json - openapi.main - path-params - Operation must define parameter "{username}" as expected by path "/user/{username}". [paths/~1user~1{username}/put]
FAIL - ./openapi.json - openapi.main - path-params - Parameter "username" must be used in path "/user/{username}". [paths/~1user~1{username}/put/parameters/0]

25 tests, 0 passed, 7 warnings, 18 failures, 0 exceptions
```

## Trade-offs envolvidos
Como podemos ver, quando usamos o conftest temos um resultado diferente do OPA. Como o conftest é uma ferramenta de teste, a ideia é que ela possa ser usada em uma *pipeline*, por exemplo, já que será possível validar se há ou não alguma falha através de uma interface de linha de comando. No caso do Open Policy Agent *puro* temos um resultado programático, que pode ser exibido em dashboards ou lido de diferentes formas.

Um ponto que vale a pena ressaltar é que o Open Policy Agent é uma plataforma para gestão de políticas. Com ela é possível fazer muito mais do que simplesmente validar arquivos Swagger. Você deve ir por esse caminho se estiver pensando em uma plataforma que centralize a gestão de políticas de diferentes ferramentas de infra-estrutura, por exemplo.

Já no caso do conftest estamos falando de uma ferramenta que, construída em cima do OPA, permite a validação de arquivos de configuração. Nesse caso, se você quer algo focado em validações de políticas específicas, como arquivos Terraform ou Swagger, a opção a ser escolhida deve ser o conftest. Você não terá uma plataforma de gestão de políticas centralizadas, mas validará os arquivos que necessitar.

Vale a pena citar também que ambas ferramentas usam a linguagem de alto nível Rego para escrita das políticas. Será necessário estudar - ou conhecer - essa linguagem para tirar máximo proveito da ferramenta escolhida. 


---


Espero que tenha gostado desse artigo e caso tenha alguma dúvida, entre em contato comigo pelos links que aparecem aqui no blog. Abraços!


tags: [[tecnologia]], [[arquitetura]]