---
title: "Integrando sistemas com Kafka: uma breve introdução"
date: 2023-10-02 14:31:37
tags: [kafka, 2023]
---

Quando falamos sobre integração de sistemas, existem diferentes tecnologias e padrões que podem ser adotados. Isso vale tanto para sistemas pequenos, como aqueles pessoais e de startups, até em casos de arquiteturas empresariais, com milhões de requisições por segundo. De forma muito simplificada, existem dois principais mecanismos para integrações serem feitas: síncronas, por meio de APIs, ou assíncronas, por meio de mensagens e eventos. Existem outros modelos, mas estes dois são os mais difundidos.

Quando falamos de eventos e mensagens, precisamos nos aprofundar melhor para entender o que define um evento e uma mensagem. Vale a pena ter um texto apenas para falar disso. Mas de forma resumida:

> um evento é **qualquer acontecimento** em um sistema. Pode ser desde um item sendo adicionado em um carrinho de compras até um erro que aconteceu em um determinado ponto do sistema;

> Uma mensagem é uma **forma de integrar** diferentes sistemas, enviando a informação de um ponto a outro. 

Vale ressaltar que a mensageria tem um fluxo diferente de APIs. Quando uma API fornece um dado, ele somente é entregue quando solicitado, de forma síncrona. Já uma mensagem é enviada de forma assíncrona, ou seja, ela será armazenada em um determinado local onde será consumida quando o consumidor necessitar. Nesse ponto existem diferentes formas de gerar e armazenar mensagens, e é onde entra o Kafka, assunto principal do texto de hoje.

## O que é o Kafka

Existem várias ferramentas que podem ser usadas na hora de trabalhar com mensageria. Hoje falarei do Kakfa. Ele é uma aplicação criada pelo LinkedIn e que se tornou open source com o passar dos anos. Algumas pesquisas indicam que 80% das empresas na Fortune 100 usam a ferramenta de alguma forma.

Para desenvolvedores e arquitetos e desenvolvedores é interessante estudar Kafka por vários motivos técnicos, entre eles:

*  habilidade de publicar e assinar streaming de eventos
*  processar streaming de eventos em tempo real
*  manter uma lista ordenada de eventos de acordo com sua ocorrência


<img src="{{ site.baseurl }}/assets/before-and-after-kafka-1.png"/>
*Figura 1 - Sistemas antes e depois de usarem o Kafka. Fonte: Freecodecamp*

## Alguns casos de uso

Abaixo temos alguns exemplos de como o Kafka pode ser usado:

* **Netflix**: Usa o Kafka para [manter sincronizada toda a sua gigantesca rede de microsserviços](https://www.confluent.io/blog/how-kafka-is-used-by-netflix/)
* **Spotify**: No Spotify o Kafka é utilizado para [coleta de dados de streaming de músicas e podcasts, além de qualquer ação do usuário](https://engineering.atspotify.com/2016/03/spotifys-event-delivery-the-road-to-the-cloud-part-ii/). Com tais dados é possível fazer recomendações otimizadas
*  **Banco ING**: O banco holândes usa o Kafka, entre outros casos de uso, para [mandar notificações em tempo real](https://www.youtube.com/watch?v=mAVSrb7Xrm8) sobre mudanças no valor de ações no mercado

## O que vem por aí

Ainda não tenho nenhum conteúdo planejado, mas quero continuar escrevendo sobre os principais tópicos de Kafka conforme for estudando sobre e utilizando nos projetos em que estou envolvido. Fiquem ligados! 😉

## Links de referência

Seguem abaixo alguns links para auxiliar no entendimento de como o Kafka pode te ajudar em suas soluções digitais.

* [The Apache Kafka Handbook – How to Get Started Using Kafka. FreeCodeCamp](https://www.freecodecamp.org/news/apache-kafka-handbook/)
* [O que é o Apache Kafka no Azure HDInsight. Microsoft](https://learn.microsoft.com/pt-br/azure/hdinsight/kafka/apache-kafka-introduction)
* [Apache Kafka® Quick Start, Confluent Developer](https://developer.confluent.io/quickstart/kafka-on-confluent-cloud/)
