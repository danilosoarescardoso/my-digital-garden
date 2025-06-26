---
title: Estudando contratos de API com ChatGPT
date: 2023-03-15 09:37:05
---

Estava estudando melhores práticas para documentações de APIs hoje quando me surgiu uma ideia: 

> e se eu pedisse pro ChatGPT criar uma API pra mim seguindo algumas premissas passadas para ele?

Fiz o teste e o resultado ficou legal e prático para exemplificar os principais conceitos. Acredito que nada substitua o bom e velho livro na estante, mas é um recurso a mais para agilizar testes no dia-a-dia.

## O comando enviado

Para gerar o Swagger, enviei os seguintes parâmetros: 

* Crie uma API usando o padrão OAS 3.0. 
* Essa API servirá para cadastrar e retornar receitas a partir de ingredientes que eu tenha em casa.
* Os ingredientes deverão ser passados via POST em formato de lista dentro do body.
* A API deverá ter um endpoint que retorne uma receita específica a partir do seu ID.
* A API deverá ter um endpoint que retorne quais receitas posso fazer a partir de um determinado ingrediente enviado por query parameter.
* A API deverá usar o termo "receitas" como recurso.
* Todos os endpoints deverão ter retornos 400 e 500 configurados e respeitar as melhores práticas na escrita de recursos, endpoints e respostas.

## O resultado

```yaml
openapi: 3.0.0
info:
  title: Receitas API
  description: API para cadastro e consulta de receitas a partir de ingredientes disponíveis.
  version: 1.0.0

servers:
  - url: https://api.example.com/v1

paths:
  /receitas:
    post:
      summary: Cadastrar receita
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                nome:
                  type: string
                  description: Nome da receita
                ingredientes:
                  type: array
                  description: Lista de ingredientes necessários para a receita
                  items:
                    type: string
      responses:
        '201':
          description: Receita cadastrada com sucesso
        '400':
          description: Requisição inválida
        '500':
          description: Erro interno do servidor

  /receitas/{id}:
    get:
      summary: Consultar receita pelo ID
      parameters:
        - name: id
          in: path
          required: true
          description: ID da receita a ser consultada
          schema:
            type: integer
            minimum: 1
      responses:
        '200':
          description: Receita encontrada
        '400':
          description: Requisição inválida
        '404':
          description: Receita não encontrada
        '500':
          description: Erro interno do servidor

  /receitas/disponiveis:
    get:
      summary: Consultar receitas a partir de ingredientes disponíveis
      parameters:
        - name: ingredientes
          in: query
          required: true
          description: Lista de ingredientes disponíveis separados por vírgula
          schema:
            type: array
            items:
              type: string
      responses:
        '200':
          description: Receitas encontradas
        '400':
          description: Requisição inválida
        '500':
          description: Erro interno do servidor

components:
  schemas:
    Receita:
      type: object
      properties:
        id:
          type: integer
          description: ID da receita
        nome:
          type: string
          description: Nome da receita
        ingredientes:
          type: array
          description: Lista de ingredientes necessários para a receita
          items:
            type: string

```

## Explicando o resultado

Usando o [Editor do Swagger](https://editor.swagger.io), foi possível ver o contrato de maneira gráfica e inferir alguns outputs:


### Padrão OAS 3.0
Quando pedimos para o padrão da API ser o OAS 3.0 (*Open API Specification*), estamos nos referindo a [essa documentação](https://swagger.io/specification/). Ela é a definição padrão que o mercado tem usado para validar como o contrato de uma API é escrito.

Algumas das definições que existem nesse padrão são:

* como os campos de uma API devem ser descritos
* de que forma a autenticação e autorização deve ser descrita
* Como utilizar parâmetros na query (query parameters)
* entre outros...

### API para cadastro e retorno de receitas a partir de ingredientes
Quando enviei esse comando, quis dizer que minha API precisaria ter, pelo menos, dois endpoints. Um que servisse para cadastro das receitas e outro que retornasse as receitas cadastradas. Além disso, o endpoint de cadastro precisa enviar os ingredientes necessários para a receita ser feita. 

Com isso temos o seguinte resultado:

<img src="{{ site.baseurl }}/assets/endpoints.png"/>
imagem 1 - Endpoints solicitados

<img src="{{ site.baseurl }}/assets/ingredientes.png"/>
imagem 2 - Ingredientes


### Retorno de receita pelo seu ID
Para esse item, o endpoint criado foi o demonstrado abaixo. Ele recebe um ID na requisição e retorna uma receita específica:

<img src="{{ site.baseurl }}/assets/receita.png"/>
imagem 3 - Receita

### Receita a partir de ingredientes
Essa premissa tem como objetivo receber uma lista de ingredientes e retornar uma receita que inclua todos eles. Para isso temos o seguinte endpoint criado:

<img src="{{ site.baseurl }}/assets/receita-por-itens.png"/>
imagem 4 - Receita por itens

### Receitas como "*collection*"
Para garantir certa organização na API, pedi que fosse criada a *collection* "receitas". Assim atingimos a boa prática de usar substantivos para caracterizar os objetos manuseados pela API.

<img src="{{ site.baseurl }}/assets/collections.png"/>
<img src="{{ site.baseurl }}/assets/schemas.png"/>

imagem 5 e 6 - onde ficam as *collections*



### Retornos 400 e 500 configurados 
Como último item, pedi que todos os endpoints tivessem erros 400 e 500 configurados. Isso significa que em caso de erro, o desenvolvedor que utilizará a API precisa saber previamente quais respostas ele terá, para poder preparar seu sistema consumidor/cliente e utilizar o erro da melhor forma possível.

<img src="{{ site.baseurl }}/assets/erros-respostas.png"/>
imagem 7 - erros 400 e 500 minimamente configurados

## Trade-offs

Como falei, nem tudo são flores. Existem alguns problemas não só nesse contrato mas até mesmo com o próprio ChatGPT, a saber:

* Tive que rodar minha solicitação muitas vezes na versão gratuita do ChatGPT até conseguir que o contrato ficasse pronto
* Não foi feito tagueamento correto dos endpoints
* Não foi especificado um formato de resposta para os erros
* O path para obter receitas a partir de determinados ingredientes não está dentro das melhores práticas de design de API

Esses são apenas alguns exemplos que mostram que precisamos conhecer um assunto antes de usar o ChatGPT para nos apoiar. Se eu não conhecesse como contratos de API devem ser feitos, poderia divulgar uma informação errada. Além disso, apesar de a ferramenta ser generativa, ele funciona de acordo com nossos inputs. Se não especificarmos o que queremos, ela vai gerar outputs com erros.

Mesmo assim, acredito que o ChatGPT continua sendo uma ótima ferramenta para auxiliar nos estudos de como um bom contrato de API deve ser escrito. 

tags: [[inteligência artificial]], [[arquitetura]], [[APIs]]