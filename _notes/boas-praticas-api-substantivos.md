---
title: "Boas práticas no design de APIs: use substantivos em vez de verbos"
date: 2022-02-08 16:56:34
tags: [open apis, apis, api first]
---

Um dos grandes trunfos do padrão REST é permitir grande flexibilidade na hora de implementar uma API. Logo, é necessário definir padrões e boas práticas para que diferentes desenvolvedores possam trabalhar em uma mesma API e entender o que está acontecendo. Não só o time técnico, mas até para pessoas leigas fica claro o que está feito quando adotamos essas práticas. Pensando nisso, seguem algumas ideias para que APIs sejam mais claras:

### URLs devem ser simples

A primeira dica é também a mais importante: **deixe URLs base o mais simples e intuitivas possível**. Uma URL clara faz o consumo ser facilitado e lógico. Para isso podermos usar um conceito de design chamado *Affordance*. Ele define que um elemento deve dar dicas ou explicar como ser usado visualmente, sem a necessidade de um manual. Um exemplo clássico são maçanetas e asas de xícara. Subtende-se apenas ao olhar que devemos pegar esses objetos, pois entendemos a mensagem de que aquilo foi feito para ser manuseado.

Assim como nesses casos, APIs devem ter *affordance* aplicado. Pra isso Brian Mulloy cita que devemos ter, no máximo, duas URLs base para cada recurso. Para dar um exemplo, imagine uma API onde os recursos são clubes de futebol. Ela pode ter o seguinte desenho:

* /clubes
* /clubes/palmeiras

Dessa forma nossa API lista uma coleção (primeira opção) e um clube específico (segunda opção) sendo legível para desenvolvedores e pessoas não-técnicas. Assim conseguimos também deixar os endpoints mais claros, sem a necessidade de verbos, que já citamos serem ruins. 

### Nada de verbos em URLs base

Desenvolvedores costumam escrever endpoints usando termos que facilitem seu entendimento, como *listAllClubs*. Outro motivo é manter certa coesão com os métodos que realizam o que aquele endpoint cita.

O problema dessa abordagem é que ela foca apenas no objeto, que em nosso exemplo é um clube de futebol. Como faríamos para relacionar os jogadores, comissão técnica, patrocinadores, partidas e afins? Teríamos que ter, provavelmente, uma lista de endpoints assim:

* /listAllPlayers
* /listNextMatches
* /getAllPartners

Pode parecer fazer sentido, mas se o projeto crescer e comportar mais esportes e domínios, logo será impossível entender os endpoints, a não ser que seja gasto um tempo lendo a documentação e se aprofundando no que a API entrega.

### Use verbos HTTP de forma intuitiva

Quando cortamos os verbos comuns, dependemos de um bom uso dos verbos HTTP. Pensando em um sistema CRUD, vamos ter endpoints para criar, editar, deletar e atualizar registros. Utilizando o mesmo exemplo citado mais acima, temos duas URLs base, uma para trabalhar com clubes em geral e outra para clubes específicos.

Juntando os verbos HTTP que trazem a funcionalidade de CRUD com as duas URLs base, temos 8 endpoints que permitem a criação de uma API rica em funcionalidades. Com isso teríamos os seguintes endpoints:

| Recurso  |  POST | GET  | PUT  | DELETE  |
|---|---|---|---|---|
| /clubes/  |  criar um novo clube | listar clubes   | atualizar lista de clubes   | deletar todos os clubes   |
| /clubes/palmeiras  | Erro  | mostrar dados do clube Palmeiras   | caso o clube Palmeiras exista, o atualiza  | apagar clube Palmeiras   |



