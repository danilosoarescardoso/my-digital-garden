---
title: "API Design First: passo-a-passo"
date: 2023-05-17 17:41:45
tags: [apis, 2023, tecnologia, desenvolvimento]
---

"**API Design First**" é uma abordagem de desenvolvimento de software onde o design da API (Interface de Programação de Aplicativos) é feito antes da implementação do código.

Em outras palavras, a primeira etapa é **definir e projetar** a interface da API - como as diferentes partes do software se comunicarão entre si - usando uma linguagem de descrição de API como OpenAPI ou RAML. Somente após a API ser projetada e aprovada, a equipe começa a escrever o código que implementa essa interface.

A vantagem dessa abordagem é que ela incentiva a pensar cuidadosamente sobre como a API será usada e como ela deve ser estruturada antes de começar a codificar. Isso pode levar a APIs mais bem projetadas, com melhor usabilidade e menos necessidade de refatoração posterior. Além disso, permite que as equipes de front-end e back-end trabalhem em paralelo, uma vez que o contrato da API já foi acordado.

Para conseguirmos chegar a um contrato que atenda todas as partes, podemos seguir esse passo-a-passo:

## Processo ADDR

<img src="{{ site.baseurl }}/assets/addr.png"/>
ADDR é um acrônimo que se refere a um processo comum na escrita e design de APIs. Ele é composto pelas seguintes etapas:

* **Alinhar**: Garante o alinhamento entre os diferentes escopos envolvidos, como negócio, produto e tecnologia, fechando um entendimento de quais são os resultados esperados para o projeto.

* **Definir**: Fase onde são mapeados os requisitos do cliente em capacidades digitais que definirão a necessidade de uma ou mais APIs para entregar os resultados esperados.

* **Desenhar**:  Aqui o design da API é feito, procurando o melhor API Style para os resultados esperados pelas partes envolvidas

* **Refinar**: Nessa fase é coletado o feedback dos desenvolvedores através de testes, prototipações e escrita de documentação

## Fases para escrever um contrato de API

Existem 7 fases, segundo James Higginbotham, para que o contrato de uma API seja feito:

1. [**Identificar capacidades digitais.**](https://danilocardoso.dev/blog/api-design-first-definindo-capacidades-digitais/) identificar as necessidades do cliente e resultados esperados, incluindo as respectivas capacidades digitais. 
2. **Definir atividades.** expandir capacidades digitais para incluir um entendimento único e claro das atividades necessárias para atingir os resultados esperados usando sessões colaborativas de design. 
3. **Identificar fronteiras da API.** validar se já não existe alguma API que pode ser reutilizada e, no caso de necessidade de novas APIs, quais deverão ser criadas.
4. **Modelar Perfis de API.** definir através de sessões colaborativas de design qual o melhor perfil de API a ser utilizado, incluindo recursos e operações.
5. **Design de Alto nível da API.** Escolher um ou mais Perfis de API que serão usados e documentar os elementos de design de alto nível envolvidos.
6. **Refino do Design.** Incluir feedback dos consumidores da API usando técnicas que busquem a melhor experiência para o desenvolvedor.
7. **Documentar a API.** finalizar a documentação da API, incluindo materiais para onboarding, testes e formas de acelerar a integração.

Nos próximos textos aprofundarei em cada uma das etapas listadas acima.

