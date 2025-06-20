---
title: "API Design First: definindo as capacidades digitais"
date: 2023-05-22 14:06:56
tags: [api first, api design first, apis, 2023, tecnologia, desenvolvimento]
---

Quando abordamos a visão de **API como Produto**, trazemos alguns conceitos que nos permitam focar em atender as dores do usuário. O primeiro passo nesse caminho, de acordo com a [literatura de James Higginbotham](https://www.amazon.com.br/Principles-Web-Design-James-Higginbotham/dp/0137355637), é o de definir quais são as capacidades digitais esperadas para esse produto. 

## Resumo

* Para melhor entendimento deste texto, garanta que você conhece os termos citados nos **Pré-Requisitos**
* **Capacidades digitais** são os recursos tecnológicos que entregarão os outcomes - resultados - esperados pela pessoa cliente de sua API
* **Outcomes** são os resultados que o cliente espera receber ao usar sua API ou produto digital
* **Job Stories** é uma metodologia usada para descobrir quais são as capacidades digitais que seu produto precisa ter através das necessidades da pessoa cliente. 

### Resumo das etapas
* Defina os **outcomes** desejados pelo seu cliente
* Com os **outcomes**, escreva **job stories**
* Com os **job stories**, temos definidas as **capacidades digitais** esperadas para nossa API relacionadas com os respectivos **outcomes**
* **Armazene** seus job stories de uma forma que o time de desenvolvimento consiga entender porque aquelas capacidades foram definidas anteriormente

## Pré-requisitos

Para entender o conceito de API First e tirar máximo proveito, indicamos que alguns conhecimentos sejam estabelecidos previamente:

* Métodos HTTP
* Verbos HTTP
* Princípios básicos do Protocolo HTTP

> Para aprender estes e outros termos, leia o texto: [APIs para Pessoas de Negócio: Termos técnicos essenciais](https://danilocardoso.dev/blog/apis-pessoas-negocio-termos-tecnicos/)

<img src="{{ site.baseurl }}/assets/capacidades-digitais.png"/>

## O que são capacidades digitais

As **capacidades digitais** são recursos que entregam *outcomes* (resultados esperados) através de automação. É uma forma dos clientes interagirem com sua organização através de um meio digital. Para o usuário final, não importa o que será feito para alcançar os ***outcomes***. Por baixo dos passos, inúmeras tecnologias e técnicas podem ser utilizadas para que o *outcome* seja alcançado. 

Abaixo temos um exemplo do que poderiam ser capacidades digitais para um sistema de apostas online:

|  Capacidade digital | Endpoint REST  |
|---|---|
| Executar uma aposta online| POST /apostas  |
| Checar o resultado de uma aposta  | GET /apostas/{idAposta}  |
| Checar apostas em um determinado time  | GET /apostas/times/{nomeTime}  | 


No exemplo acima temos três capacidades que um produto digital relacionado a apostas se propõe a ter. Essas capacidades podem ser estabelecidas utilizando uma API REST, que pode entregar tecnologicamente o *outcome* para as capacidades. 

Agora que você sabe o que são capacidades digitais, podemos entender de que forma elas podem ser identificadas. Para isso, a estratégia recomendada por James é a de usarmos **Job Stories**, baseada na metodologia ***Jobs do Be Done (JTBD)***.

## Entendendo Job Stories

*Job Stories* é uma técnica que visa traduzir a necessidade do cliente em capacidades digitais. Essa técnica toma como base o conceito de "Jobs to be Done", criado por Clayton Christensen. Nela, procuramos entender quais serão as jornadas - ou jobs to be done - que o usuário executará em nosso produto. 

No caso de APIs, a proposta feita por James é de criarmos job stories descrevendo essas jornadas. Dessa forma conseguiremos traduzir cada um dos JTBD em requisitos funcionais para a API. 

### Estrutura de uma Job Story

Uma job story possui três divisões: "Quando, eu quero, então poderei." Elas servem para:

* **Quando**: o **evento** que irá desencadear o *outcome* esperado pela pessoa usuária. São indicadores-chave de quando a API será usada.
* **Eu quero**: A **capacidade** identificada pela pessoa cliente como **ação a ser tomada**. Essa informação será usada para entender quais operações serão realizadas pela API.
* **Então poderei**: O outcome esperado pela pessoa cliente. É o campo que definirá o critério de aceitação para a API desenhada. 

Na minha concepção, o conceito fica mais claro se adotarmos a seguinte nomenclatura tropicalizada:

|  Termo original | Versão tropicalizada  |
|---|---|
| Quando | necessidade  |
| Eu quero  | capacidade  |
| Então poderei  | resultado  | 

### Exemplo de um job story

Pedi pro ChatGPT montar um exemplo de *job story*. O resultado foi o seguinte:

> Claro! Vamos pensar em uma aplicação para pedir comida online. Uma "job story" para essa situação pode ser:

> - Quando __(eu chego tarde do trabalho)__,
- Eu quero __(pedir uma refeição através de um aplicativo)__,
- Então poderei __(ter uma refeição pronta quando eu chegar em casa)__.

> Essa job story ajuda a **equipe de desenvolvimento** a entender um cenário de uso realista, podendo se concentrar em facilitar esse processo para seus usuários. Eles podem trabalhar para garantir que o aplicativo permita pedidos antecipados e forneça uma estimativa precisa do tempo de entrega, por exemplo.

### Como obter e armazenar jobs stories

James Higginbotham dá algumas dicas legais de como obter job stories para seu projeto de API. Das que ele cita em seu livro, a que acho mais interessante é a de guardar as jobs stories em arquivos markdown.

Dessa forma é possível guardar um histórico das mudanças que uma API teve junto do seu repositório de código-fonte, permitindo que o desenvolvedor entenda o caminho que foi percorrido até aquela API ser feita. 

Para obtenção das job stories, acredito que um simples arquivo de texto ou formulário já resolvam, já que o mais importante é ter esses dados para os próximos passos do design de sua API. 

## O próximo passo

Depois de as **capacidades digitais** e **job stories** da sua API, chega a hora de definirmos as **Atividades e Passos**. O texto será disponibilizado em breve.


