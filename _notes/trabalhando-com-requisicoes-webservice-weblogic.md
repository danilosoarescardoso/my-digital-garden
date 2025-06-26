---
title: Testando requisições a Webservices SOAP no Weblogic
date: 2020-04-26 02:02:27
---

Sempre que trabalho com uma tecnologia, gosto de ler mais sobre ela e fazer experimentos. Quando trabalhamos com desenvolvimento, isso acaba sendo muito comum, aprender com a prática e o dia-a-dia. Um dos exemplos desse aprendizado que adquiri nos últimos meses foi trabalhando com algumas tecnologias novas na carreira.

Na área que sou responsável na TCS, uma das aplicações que cuidamos é feita em Java e roda no [Weblogic](https://www.oracle.com/br/middleware/technologies/weblogic.html), servidor mantido pela Oracle para sistemas Java EE. Algo muito interessante que tenho me aprofundado nos últimos meses mexendo com Weblogic é no teste de web services que ele traz como padrão, chamado Web Services Test Client. 

Essa ferramenta é muito útil porque permite que testes sejam feitos de maneira rápida, sem ter que criar mocks no SoapUI, por exemplo. Segundo a documentação oficial, o Web Services Test Client serve para:

* testar funcionalidades básicas para testar a operação correta do webservice 'deployado'
* testes básicos de segurança para autenticação
* visualizar o WSDL do web service
* testes avançados, como transações atômicas, envio de mensagens SOAP, políticas de segurança Oracle Web Service Manager (OWSM), entre outros

Se você tem um web service implementado em um servidor Weblogic, é bem fácil acessar o Web Services Test Cliente, basta apenas acessar a URL http://host:port/ws_utc do seu projeto. O host deverá ser substituído pelo servidor Weblogic que está sendo utilizado e a porta deverá ser a utilizada pelo seu Weblogic (geralmente usa-se a porta 7001 como default).

## Exemplificando

Vou mostrar abaixo alguns prints de como o cenário de testes pode ser montado. Para o exemplo, utilizei [este repositório](https://github.com/AKSarav/SampleWebService) disponível no Github. Após subir o ambiente, basta acessar a URL do projeto seguindo padrão mencionado acima, e o que aparecerá será a tela abaixo:


<img src="{{ site.baseurl }}/assets/primeira.png"/>

Imagem 1 - Endpoints registrados na aplicação

Na tela acima podemos ver os dois endpoints criados nesse projeto, "GetRhymingWorld" e "Hello". Ao clicar no primeiro, temos a tela abaixo apresentada, listando os parâmetros recebidos e opções de autenticação, endereçamento, entre outros. Para nosso exemplo, utilizaremos apenas a função de passar parâmetro, para verificar como os testes de API funcionam nesse cenário. 


<img src="{{ site.baseurl }}/assets/segunda.png"/>

Imagem 2 - Parâmetro do primeiro endpoint

O endpoint dessa aplicação foi criado para receber uma palavra e retornar as rimas dela a partir do site [Datamuse](https://www.datamuse.com/api/). Fiz o teste pesquisando pela palavra 'Java'. Ao clicar em 'Invoke', o Weblogic enviará uma requisição para a API, trazendo os resultados no formato xml.

Abaixo vemos o xml que foi retornado com os sinônimos em inglês para a palavra 'Java'. Podemos ver também que existem alguns dados em JSON, mas isso ocorreu porque essa é a forma que a API do Datamuse retorna seus resultados. Nada que um simples parse na aplicação não resolva. 


<img src="{{ site.baseurl }}/assets/terceira.png"/>

Imagem 3 - Retorno do endpoint

Vale ressaltar que existem outras aplicações que trazem o mesmo tipo de funcionalidade, como o SoapUI. A diferença é que com essa ferramenta você ganha um pouco mais de agilidade por já ser um recurso implementado no Weblogic, além de ter mais uma opção para as horas em que múltiplos testes são necessários.

Caso tenha alguma sugestão ou dúvida, só me enviar nos comentários ou por mensagem! 

tags: [[arquitetura]], [[tecnologia]]
