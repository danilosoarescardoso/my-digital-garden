---
title: "APIs para Pessoas de Negócio: uma breve introdução"
date: 2022-11-01 13:56:54
tags: [tecnologia, apis, 2022]
---

Faz um tempo que o termo APIs está em constante crescente, seja na internet, eventos presenciais ou prospectos do mercado. Uma rápida busca no [Google Trends](https://trends.google.com/trends/explore?date=all&geo=BR&q=%2Fm%2F0z5n) mostra como o assunto ganhou relevância e parece que não vai sair de moda em breve. Algumas iniciativas como o [Open Finance](https://startupi.com.br/open-finance-apis/) sendo implementado em escala globa ajudam a explicar o motivo de tantas empresas e pessoas estarem disseminando conteúdo sobre APIs.

A ideia desse artigo é simplificar a noção do que são APIs, trazendo para uma visão de negócios e não técnica os conceitos que permeiam a criação, utilidade e benefícios no uso de APIs. A ideia é que você, ao final desse texto, saiba quais assuntos são necessários estudar para se aprofundar na temática, além de ter uma ideia clara de como uma API funciona e de como ela pode o conceito pode te atender estrategicamente.

<img src="{{ site.baseurl }}/assets/meeting.jpg"/>

## Porque conhecer APIs

APIs são um assunto mega relevante para o contexto de [digitalização e transformação digital](https://www.forbes.com/sites/googlecloud/2021/08/10/digital-transformation-youre-doing-it-wrong-if-youre-not-looking-at-apis/?sh=7971a90433da) que os organizações tem vivido. Para pequenas empresas as APIs podem representar a forma como seu produto é exposto ao mercado, já que potencializam a criação de apps, sistemas e serviços [de forma rápida e padronizada](https://blogs.cisco.com/cloud/enabling-application-development-velocity-in-an-api-first-world). Para grandes empresas, as [plataformas de API](https://swagger.io/blog/api-strategy/enterprise-api-platform/) podem trazer a mesma agilidade do mercado emergente para o contexto de complexidade das grandes corporações.

Tangibilizando um pouco mais, as APIs podem ser o motor para a estratégia que papeis como CEO e CTO esperam trazer para as suas equipes. Enquanto PO e analista de negócios, as APIs podem ser um caminho mais simples de trazer informações de banco de dados para seus sistemas internos ou até mesmo se tornar um produto, dependendo da maturidade do seus times técnicos com o assunto.

## O que são APIs

Imagine que você foi a um restaurante e pediu o cardápio. Mesmo que hajam diferentes estilos, cores e formas de apresentar o conteúdo, o conceito de um cardápio não se altera. Seu objetivo é mostrar as opções de pratos que existem no restaurante, agindo como uma **interface** entre os clientes e garçons/restaurante. Em tecnologia, o termo interface é utilizado quando temos algum padrão de comunicação para dois sistemas completamente diferentes.

O termo API é um acrônimo para *application programming interface*, ou **Interface de Programação de Aplicação** em português. Isso significa que APIs servem para padronizar a comunicação entre dois sistemas diferentes. No caso do restaurante, o cardápio seria uma API. Existe ali um **padrão de comunicação** (preço, nome e composição dos pratos) fornecido pelo restaurante que ajuda o consumidor a fazer suas escolhas. O restaurante não precisa conhecer previamente os gostos do seu consumidor para construir um cardápio, basta seguir os padrões do mercado.

> APIs servem para padronizar a comunicação entre dois sistemas diferentes. 

Da mesma forma, o cliente não precisa não precisa conhecer todos os pratos antes de ir em um restaurante, já que ele sabe que o cardápio informará aquilo que ele precisa. Com isso estabelecido, precisamos trazer alguns conceitos importantes que permeiam o que caracteriza uma API e a difere de outras formas de comunicação.

### Modelo cliente-servidor 

APIs são baseadas na [protocolo de comunicação HTTP](https://rockcontent.com/br/blog/http/), base da Web 2.0. No HTTP toda comunicação é feita de um cliente a um servidor. No exemplo do restaurante, o consumidor que olha o cardápio é o **cliente** e o restaurante o **servidor**. Nesse modelo de comunicação, todo pedido de informação é chamado de requisição. Ou seja, quando você olha para os pedidos no cardápio, você está vendo os resultados de uma requisição, já que precisou acessar a API - cardápio - para ter acesso às informações.

A partir do momento que você escolher um prato e comunicar ao garçom, estará fazendo uma nova requisição, dessa vez pedindo um prato. 

### Requisições e respostas
Apesar de já fazer parte da explicação anterior, acredito que faça sentido deixar esse ponto um pouco mais específico. Como a comunicação na internet sempre tem um servidor e um solicitante, imagine que toda comunicação será síncrona. Vamos imaginar um exemplo de dois irmãos conversando. Digamos que o irmão mais novo quer saber onde está o seu controle do videogame perguntando para seu irmão mais velho. Nesse exemplo o irmão mais novo é o cliente, que precisa da informação, enquanto o irmão mais velho é o servidor, o que detém - ou não - a informação necessária.

Para que os dois se comuniquem, é necessário que o irmão mais novo faça uma pergunta. No caso de APIs chamamos isso de requisição. A resposta do irmão, independente do conteúdo, será dada ao irmão mais novo por ser uma comunicação síncrona. Podemos enriquecer esse exemplo posteriormente incluindo os verbos HTTP e os códigos de resposta para um melhor entendimento.

### APIs não guardam estado

Assim como um cardápio não armazena informações sobre o cliente, uma API não salva nenhuma informação que passa por ela, sendo considerada *stateless*. Além disso, cada requisição é fechada logo depois de ser realizada. Isso significa que cabe às partes - cliente e servidor - guardar os dados caso seja necessário, já que a API é a apenas um protocolo de comunicação. No nosso exemplo do restaurante, o garçom pode guardar o nome da pessoa para um melhor atendimento e irá guardar as informações do pedido para garantir que seja atendido conforme solicitado.

### Sistema de camadas

Por mais que o cliente queira pedir agilidade ou que seu prato tenha algo diferente, tudo isso será feito com o garçom, nunca com o cozinheiro ou dono do restaurante. No que tange APIs, isso significa que as camadas de responsabilidade de uma API são sempre bem definidas e separadas. Se é necessário uma autenticação de segurança prévia, será impossível acessar a API antes de haver a autenticação do cliente.

<img src="{{ site.baseurl }}/assets/rest.png"/>


## O que é possível fazer com APIs

Agora que já foram trazidos detalhes para entender conceitualmente o que é uma API, trarei alguns exemplos mais próximos do contexto organizacional. Como uma API é uma forma de *integrar* diferentes sistemas, podemos estabelecer alguns cenários onde as APIs são uma solução:

* **Integrar sistema de RH com sistema de onboarding.** Imagine que sua empresa possua uma plataforma de onboarding apartada do sistema de RH. Enquanto o sistema de onboarding traz as primeiras atividades que uma pessoa terá na empresa, o sistema de RH cuida da contratação, documentos e processos relacionados. Para fazer com que esses dois sistemas se falem e troquem informações, podemos usar APIs para fazer essa ponte. Uma API pode ser usada para criar um novo usuário no sistema de onboarding trazendo seus dados básicos provenientes do sistema de RH.
* **Exibir determinadas informações no frontend do seu aplicativo.** Caso sua empresa tenha um aplicativo e você queira adicionar informações na tela, para agregar valor ao usuário, APIs são uma das formas de fazer isso. Com uma API você pode trazer a informação que deseja para as telas do app, fazendo com que o usuário não precise usar outro serviço pra obter informações. Um app com estatísticas esportivas pode, por exemplo, mostrar a temperatura das próximas horas para a pessoa decidir se faz um esporte ao ar livre ou não.  
* **Criar um produto baseado no conhecimento da sua área que possa ser adquirido por empresas externas.** Imagine que você trabalha fazendo análises de risco de crédito e que criou um passo-a-passo infalível para suas análises. Com uma API, é possível *produtificar* esse conhecimento e disponibilizar ao mercado. Dessa forma você cria um produto rentável que pode ser adquirido por pessoas e empresas que precisem dessa funcionalidade. A API pode ser embarcada em sistemas já existentes (por exemplo, um CRM) ou você pode criar uma aplicação com telas para ter 100% de controle sobre a experiência do usuário.

## Alguns casos reais

### Postagens musicais no Instagram
Se você usa o Instagram com frequência, já deve ter reparado que muita gente faz de vez em quando posts analisando as músicas que escutam pelo Spotify. Alguns posts [montam lineups de festivais baseados no que a pessoa mais escuta](https://techcrunch.com/2022/09/06/lineupsupplys-app-turns-music-festival-posters-into-spotify-playlists/), outros mostram [playlists baseadas no humor](https://www.cnet.com/tech/home-entertainment/supercharge-your-music-streaming-with-these-spotify-wrapped-alikes/) da pessoa naquele dia. Mas como essas análises são feitas?

Nesse caso, o site/sistema que monta essas artes criativas possui uma inteligência para analisar os dados do Spotify  do usuário. Para ter acesso a esses dados, as APIs do Spotify são usadas. Enquanto o usuário acessa seu Spotify, coloca a senha e permite que os dados sejam usados por aquele site/sistema, as APIs do Spotify são acessadas de forma invisível ao usuário, trazendo metadados das músicas ouvidas e permitindo que o desenvolvedor do site/sistema tenha uma massa de dados para analisar de forma criativa.

<img src="{{ site.baseurl }}/assets/festival.png"/>
Exemplo criativo de posts criados usando APIs do Spotify

### Twitter do Dólar Bipolar
Existe uma conta bem interessante no Twitter chamada [Dólar Bipolar](https://twitter.com/DolarBipolar). Nesse perfil é possível saber a cada meia hora se a cotação do dólar subiu ou caiu. E como eles fazem para saber? Existe uma automacão que checa a cotação do dólar de tempos em tempos e a coleta. Essa automação valida se o dado subiu ou caiu e aciona as APIs do Twitter para fazer o post. Simples assim.

### Stripe: APIs como modelo de negócio
Trazendo para um contexto corporativo, talvez a [Stripe](https://stripe.com/blog/payment-api-design) seja o melhor caso de sucesso de uma estratégia de APIs. Em um mundo onde não haviam padrões para processamento de pagamento online, a empresa criou um sistema que era focado na experiência do desenvolvedor, ou seja, tornou o processamento de pagamento algo simples para quem integra e feito 100% com uso de APIs. Com isso a empresa viveu um boom e hoje é considerada referência para quem busca usar APIs como base do seu negócio.

O mercado de processamento de pagamentos via APIs é um negócio tão lucrativo e aberto que temos um caso de bastante sucesso no Brasil também, a [PagarMe](https://www.projetodraft.com/pedro-18-e-henrique-19-criaram-sozinhos-uma-empresa-milionaria-a-pagar-me-e-querem-muito-mais/). Hoje os fundadores da empresa tocam a Brex, startup americana focada em cash management para corporações de tecnologia. Isso vem para mostrar como uma boa estratégia no uso de APIs consegue pontecializar os negócios e trazer mais opções de atuação. 

## Como aprofundar no assunto
Minha expectativa é poder trazer mais textos, exemplos e vídeos que te ajudem a entender cada vez mais para que APIs servem, mas enquanto esses conteúdos não saem, vou deixar algumas dicas abaixo:

1. **Entenda os contratos REST.** Acredito que o primeiro passo num aprofundamento do que são APIs é entender o famoso contrato de uma API. Ele é uma descrição dos campos que compõe a API, de como um desenvolvedor pode usa-la e sobre quais formas de autenticação existem para ela. A partir do contrato haverão vários desdobramentos para entender melhor os conceitos de APIs.
2. **Conheça os verbos HTTP.** Para uma API ser operacional, existem verbos que definem ações para cada operação feita na API. Na hora de obter um dado usamos um GET, e na hora de criar um novo dado usamos um POST. Apesar de ser intuitivo, vale a pena [conhecer os principais verbos HTTP](https://www.devmedia.com.br/servicos-restful-verbos-http/37103) para ter uma ideia do que pode ser feito com uma API. 
3. **Autenticação e autorização.** APIs são seguras? Sim! Existem diferentes formas de autenticar e autorizar usuários e acessos. Como é um assunto um pouco complexo, acredito que valha a pena ler algum artigo introdutório que mostre alguns [meios de autorizar usuários](https://www.bry.com.br/blog/seguranca-de-api/), apenas para entender quas mecanismos de segurança existem.