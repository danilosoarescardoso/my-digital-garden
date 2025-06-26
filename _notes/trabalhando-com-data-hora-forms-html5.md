---
title: Trabalhando com campo de data e hora em forms com HTML5
date: 2020-06-26 18:52:01
---

**tl;dr:** a forma mais fácil de trabalhar com campos de data/hora em forms é através de bibliotecas de datepicker. O suporte do HTML5 a campos de data não permite uma rápida implementação cross-browser.

Trabalhar com forms é algo comum na hora de desenvolver telas e recursos para sistemas, e um dos campos que pode dar bastante dor de cabeça são inputs e seus diferentes tipos. Recentemente atuei em um projeto onde era necessário utilizar um campo de data e hora. Na hora de criar o form, usei a [tag datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/datetime-local), que é o novo padrão no HTML5 ao invés do antigo datetime.

Até aí tudo bem. O problema foi na hora de testar essa solução em dispositivos móveis. A falha ocorreu devido a forma como browsers móveis preenchem o campo data do datetime-local. Ao invés de utilizarem o padrão do HTML5, tanto Chrome como Safari, os [dois browsers mais utilizados em smartphones](https://gs.statcounter.com/browser-market-share/mobile/worldwide) preenchem o campo como texto. Por exemplo, se você selecionar uma data como a de criação deste post, 26 de julho de 2020, ao invés do campo ser preenchido no padrão que você passar, será necessário processar a data recebida para que seja manipulada da maneira correta no backend.

Mas se você quiser resolver isso no front, o jeito vai ser utilizar uma biblioteca de datepicker. No próprio site de [documentação da Mozilla](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/datetime-local) - uma das principais referências em documentação sobre padrões web - existe uma solução paliativa com Vanilla JS, mas acredito que ela seja muito verbosa caso sua necessidade seja apenas um campo de data/hora.

Como o projeto tinha o framework Vue implementado, a solução foi encontrar uma biblioteca de datepicker que fosse interessante. No meu caso optei pelo [vue-datetime](https://github.com/mariomka/vue-datetime), excelente solução feita pelo [Mario Juaréz](https://www.linkedin.com/in/mariojuarez).

A implementação dela é bem simples, como campos de data e hora deveriam ser. Precisei apenas importar o componente e instanciá-lo com algumas poucas parametrizações. Segue como ficou o resultado abaixo:

<img src="{{ site.baseurl }}/assets/0.png"/>

Figura 1 - Datepicker com vue-datetime

tags: [[tecnologia]]