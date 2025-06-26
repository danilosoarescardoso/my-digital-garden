---
title: Quando usar cache em suas APIs
date: 2023-04-13 11:49:29
---

De forma simplificada, **cache** é um recurso que diminui a necessidade de processamento computacional ao deixar informações estáticas **mais perto** dos consumidores. Imagine, por exemplo, que você tem uma loja online. Seu site utiliza API de terceiros para obter informações sobre os produtos, como descrições, preços e avaliações. Os clientes que visitam o seu site precisam ter acesso rápido e preciso a essas informações para tomar decisões de compra.

Neste cenário, o uso de cache pode ser extremamente útil para melhorar a experiência do usuário e reduzir a carga no servidor da API de terceiros. Com uma carga reduzida, os custos de consumo de uma API de terceiros também será menor.

## Benefícios de cache em APIs

Usando cache você tem alguns benefícios, como:

* **Tempo de carregamento da página mais rápido**: Armazenar em cache as informações do produto frequentemente acessadas pode acelerar o tempo de carregamento das páginas do seu site. Isso significa que os clientes podem navegar pelos produtos mais rapidamente e ter uma experiência de usuário mais satisfatória.

* **Menor latência**: Se a API de terceiros estiver localizada geograficamente longe do seu servidor ou dos usuários finais, a latência pode ser um problema. Ao utilizar cache, as informações do produto podem ser armazenadas mais próximas aos usuários finais, reduzindo a latência e melhorando a velocidade de acesso às informações.

* **Tolerância a falhas**: Se a API de terceiros enfrentar problemas temporários ou ficar indisponível, o cache pode servir como uma camada adicional de resiliência. Os dados armazenados em cache ainda estarão disponíveis para os clientes, permitindo que seu site continue funcionando até que a API retorne à normalidade.

* **Escalabilidade**: À medida que seu negócio cresce e atrai mais visitantes, a demanda por informações do produto aumenta. O uso de cache permite que seu site escale de maneira eficiente, pois reduz a carga nos servidores da API e no seu próprio sistema.

## Cenários para uso de cache

Existem alguns cenários onde utilizar cache em APIs é indicado, como por exemplo:

* **Consultas frequentes e repetitivas**: Se a API é consultada frequentemente com os mesmos parâmetros, o cache pode armazenar temporariamente os resultados, economizando recursos de processamento e tempo de resposta.

* **Dados estáticos ou pouco voláteis**: Se os dados retornados pela API não mudam com frequência ou são estáticos, o cache é uma boa opção para armazenar essas informações e reduzir a quantidade de requisições ao servidor.

* **Limitação de taxa (rate limiting)**: Se a API possui limitações de taxa de requisições, o uso de cache pode ajudar a evitar exceder esses limites, armazenando os resultados das requisições anteriores e reduzindo o número de chamadas à API.

tags: [[APIs]], [[arquitetura]]