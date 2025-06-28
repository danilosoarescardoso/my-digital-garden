---
title: Documentando decisões de arquitetura com ADRs
date: 2022-01-18 10:57:54

---

Dentro da área de tecnologia a **informação textual** é um recurso muito importante. É com ela que transferimos conhecimento entre os times, seja no aspecto técnico ou de negócios. Saber os padrões de projeto utilizados pela equipe ou os requisitos funcionais que o time de negócios levantou para certa funcionalidade são casos de uso em que documentos de texto são essenciais para uma comunicação efetiva.

Quando falamos de projetos ágeis, podemos definir que nenhum consegue ter todos seus detalhes fixados antes de começar. Ao mesmo tempo, agilidade envolve mudanças que acontecem no meio do caminho. Uma forma de capturar essas mudanças dentro da arquitetura de sistemas é através dos **Registros de Decisão de Arquitetura** - ou **Architecture Decision Record** (ADR) em inglês. Esses documentos permitem o acompanhamento de mudanças que acontecem na arquitetura de um sistema, de forma a sintetizar o que levou a tal decisão.


## Motivações 

A necessidade de haver esse tipo de iniciativa é a dificuldade de lidar com projetos em andamento, independente do tamanho da empresa. Um exemplo é o tamanho que documentações costumam ter. Segundo Michael Nygard, ninguém lê documentações extensas. Por mais que nos esforcemos por desenvolver uma cultura de documentação técnica, a realidade é que elas acabam ficando de lado em grande parte das ocasiões.

Outra motivação é a falta de um padrão para acompanhamento das mudanças que ocorrem durante o andamento de um projeto técnico. 

>Porquê mudaram o tipo de banco de dados? De onde surgiu aquele endpoint? 

Existem duas escolhas a serem feitas quando uma pessoa que não estava envolvida na decisão toma conhecimento dela:

* **Aceitar cegamente.** Geralmente essa opção pode funcionar, mas se o projeto passa por muitas mudanças durante sua evolução, a tendência é que o time de desenvolvedores não se sinta a vontade de propor alterações, afetando diretamente a qualidade do que está sendo implementado.
* **Alterar a decisão cegamente.** Não entender os motivos pode levar a alterações drátiscas no projeto, podendo colocar tudo a perder.

## Consequências

Ao utilizar ADRs, espera-se que todo o time envolvido - desde os pares de negócios até os técnicos e de suporte - tenha noção da jornada que o projeto percorreu, sendo possível entender o estado atual da aplicação, mesmo que haja alguma complexidade na implementação. Com isso é possível garantir compreensão técnica mesmo quando o time sofre com *turnover*, por exemplo. 

A ideia principal dos ADRs é evitar esforço para entender o código e tudo o que já foi feito. E quando alterações sejam necessárias, será muito mais fácil compreender os impactos e históricos do que já foi decidido anteriormente. E claro, deve-se criar um novo documento com as mudanças que serão decididas para manter o padrão.

## Onde se aprofundar

Caso queira conhecer mais sobre o conhecimento, recomendo alguns conteúdos que me ajudaram a entender melhor a ideia e perceber o quão ela é importante. Tem alguns exemplos de como escrever ADRs - fiz esse texto seguindo parte da estrutura - e alguns casos reais, como o da Conta Azul. Bons estudos!

* [Lesson 55 - Architecture Decision Records, Mark Richards](https://www.youtube.com/watch?v=LMBqGPLvonU)
* [Homepage of the ADR GitHub organization](https://adr.github.io)
* [Architectural Decision Records na Conta Azul](https://engineering.contaazul.com/architectural-decision-records-na-conta-azul-cfbb0f71e8ab)
* [Documenting Architecture Decisions, Michael Nygard](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions) 
*  [Architecture Decision Records in Action, Michael Keeling](https://resources.sei.cmu.edu/asset_files/Presentation/2017_017_001_497746.pdf)

tags: [[arquitetura]], [[tecnologia]]