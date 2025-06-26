---
title: "APIs para Pessoas de Negócio: o que é necessário para construir APIs"
date: 2022-11-22 15:04:17
---

Recentemente fiz [[APIs para Pessoas de Negócio: uma breve introdução|um texto introdutório]] sobre como APIs podem ser entendidas por pessoas de negócio. No texto de hoje a ideia é trazer o que uma pessoa, equipe e empresa precisam ter para poderem criar suas primeiras APIs. Vale ressaltar que as ideias que trarei aqui são baseadas na experiência que tive em diferentes empresas e na literatura técnica e organizacional que tenho consumido nos últimos anos. Detalhes adicionais ou casos de uso diferentes precisam ser analisados com tempo e dedicação.

<img src="{{ site.baseurl }}/assets/lego.png"/>
Figura 1 - Quais peças são necessárias para montar uma API?

## Estratégia Corporativa de APIs
Apesar de não ser estritamente necessário ter uma estratégia de APIs definida a nível corporativo para conseguir utiliza-las, é extremamente válido que sua empresa tenha uma [estratégia clara e definida para APIs](https://br.sensedia.com/post/como-a-estrategia-api-first-beneficia-negocios-de-solucoes-digitais). Isso porque APIs podem se tornar um problema quando são mal construídas, quando não possuem seu comportamento observado ao longo do tempo ou quando não são subaproveitadas.

APIs são vistas como algo inovador atualmente, devido à certa facilidade que elas trazem no compartilhamento de informações. Mas não podemos esquecer que **todo código implementado é legado**. Quando falamos de sistemas legados, estamos nos referindo a sistemas que necessitam de atenção especial. Por isso ter uma estratégia corporativa de APIs garante que suas entregas não serão apenas potencializadas através do seu uso, mas que se manterão relevantes para a organização. 

Além disso, precisamos lembrar que APIs necessitam de contratação de pessoas, softwares e infraestrutura. Ter uma estratégia definida garante que todas as tarefas gerenciais necessárias sejam realizadas. 

## Time técnico especializado
Quando for necessário definir uma squad para tocar seu projeto ou saber quais são os papéis envolvidos na criação de uma API, são esses conhecimentos e perfis que costumam ser necessários:

### Pessoa Desenvolvedora Backend
É a pessoa responsável por escrever o código da API. Geralmente - mas não mandatório - a pessoa implementa um *microsserviço*¹, que é uma pequena porção de código com uma responsabilidade única. Imagine um caso de um app de delivery; pode ser necessário para o negócio criar uma API que liste todos os estabelecimentos a partir de filtros específicos. Para isso, o código que for implementado pela pessoa desenvolvedora criará *endpoints*² que irão expor essa regra de negócio. 

### Pessoa Arquiteta de Soluções
A [arquitetura de soluções](https://santodigital.com.br/arquitetura-de-solucoes/) é a espinha dorsal de uma API. É a área que costuma ser responsável por definir a linguagem de programação que será utilizada, os padrões de escrita de código, onde ele será executado e quais tecnologias serão envolvidas. 

Ainda utilizando o exemplo do app de delivery: para implementar a API de listar todos os estabelecimentos, a pessoa arquiteta de soluções pode definir que será utilizado o framework NodeJS para escrita do código, o padrão REST para desenho da API e que será usado um banco de dados MySQL. Tudo vai depender das necessidades que o negócio possui. 

### Pessoa Engenheira DevOps
Para uma API ser exposta para o usuário final, é necessário que o processo seja automatizado em algum momento. A exposição até pode ser feita de forma manual, mas imagine que esse processo é repetitivo e pode ser feito por diferentes pessoas. Pra evitar retrabalho e perda de tempo/recursos, o melhor caminho é automatizar os *deploys*³. Para isso a engenheira DevOps é a pessoa responsável por construir uma *pipeline*⁴ que a entrega de código nos ambientes produtivos.

Quando uma *pipeline* é construída, ela faz uma série de validações no código que foi implementado pela pessoa desenvolvedora backend, checando se a qualidade está satisfatória e permite que testes sejam feitos em ambientes preparados para tal, antes de levar aquela API para o usuário final. 

### Pessoa Engenheira de Confiabilidade (SRE)
É a responsável por assegurar que, uma vez que a API foi disponibilizada, ela será monitorada para garantir sua operação conforme o esperado em termos técnicos. Essa pessoa cria visualizações (dashboards) para que indicadores da API sejam acompanhados e traz melhorias para que a experiência final do cliente possa ser sempre garantida da melhor forma possível.  

### Pessoa Engenheira de Qualidade (QA)
A pessoa Engenheira de Qualidade garante que o objetivo inicial do negócio esteja garantido. É a pessoa que efetua testes nos *endpoints* para validar os dados que são recebidos a cada requisição, checando se há alguma inconsistência. Caso algum ajuste seja necessário, a pessoa desenvolvedora backend terá que fazer alterações no código até que o resultado final seja obtido. 

## Recursos de Infraestrutura  
Existem duas formas de expor uma API: interna e externamente. APIs internas são usadas pelos sistemas da sua própria empresa. Um sistema de logística se comunica com o sistema de vendas, por exemplo. Já APIs externas são usadas para integrar produtos a parceiros. Uma transportadora pode, por exemplo, fornecer uma API que entregue o custo médio de um frete a partir de dois pontos geográficos, usando sua inteligência de mercado. Essa API pode ser *monetizada*⁵ de forma que a transportadora ganhe dinheiro e os parceiros consigam agregar valor aos seus produtos.

Para que tudo isso seja feito, são necessários alguns itens de infraestrutura. São eles:


### Servidores
Para uma API ser exposta, interna ou externamente, é necessário prover um servidor. Um servidor, a grosso modo, é [uma máquina onde o código é executado](https://developer.mozilla.org/pt-BR/docs/Learn/Common_questions/What_is_a_web_server). Com o advento da computação em nuvem a maioria das empresas criam seus servidores em serviços como Azure, AWS e Google Cloud. Além de poderem criar servidores "clássicos", esses provedores de computação em nuvem fornecem alguns [aceleradores para que APIs sejam criadas com pouco código](https://learn.microsoft.com/en-us/azure/api-management/mock-api-responses?tabs=azure-portal), facilitando algumas estratégias de negócio e testes rápidos.

### Bancos de dados
Uma API expõe e recebe dados. Dependendo da sua estratégia, ela vai precisar de um banco de dados próprio para seus dados serem armazenados. Se sua ideia for apenas expor um dado que já existe em algum sistema da sua empresa, existem mecanismos que permitem fazer a exposição sem ter de re-armazenar essas informações. A melhor estratégia técnica será definida pela Pessoa Arquiteta de Soluções.

### API Gateway 
Quando o código de uma API fica pronto e ela está no ar, é possível integrar com ela diretamente ou usar um API Gateway para padronizar a conexão. Um API Gateway é um produto que permite [criar uma camada adicional de acesso a suas APIs](https://www.redhat.com/pt-br/topics/api/what-does-an-api-gateway-do), para que todo consumo seja feito a partir de um único ponto de entrada. Com um API Gateway é possível definir padrões de URL, validações adicionais de segurança, monitoramento das conexões feitas pelos parceiros, além de facilitar a monetização dependendo de qual API Gateway for utilizado. 

Apesar de não ser um item obrigatório em pequenas e médias empresas, um API Gateway contribui na organização das APIs que existem em um determinado departamento, área ou instituição, além de prover mais segurança e observabilidade. A Pessoa Arquiteta de Soluções poderá te ajudar a entender melhor esse conceito e validar se é necessário no seu contexto. 


## Concluindo...
Apesar de não ser uma receita infalível, costumeiramente as iniciativas de API que existem no mercado utilizam uma estrutura similar a que foi descrita aqui. Acredito que com esse texto fique um pouco mais nítido quais são as atribuições, estruturas e papeis que costumam existir em um time ou empresa que faz uso de APIs. Sugiro aprofundamento nos tópicos citados, tendo em vista que o assunto tem ganho cada vez mais popularidade no mercado. Bons estudos!

---

¹ *Microsserviços* são uma abordagem arquitetônica e organizacional do desenvolvimento de software na qual o software consiste em pequenos serviços independentes que se comunicam usando APIs bem definidas. Esses serviços pertencem a pequenas equipes autossuficientes. Referência: [O que são microsserviços?](https://aws.amazon.com/pt/microservices/)


² *Endpoints* são URLs onde seu serviço pode ser acessado por uma aplicação cliente. Referência: [Qual a diferença entre endpoint e API?](https://pt.stackoverflow.com/questions/86399/qual-a-diferença-entre-endpoint-e-api)

³ *Deploy* consiste no processo de colocar no ar uma aplicação já concluída. Ele pode ocorrer durante várias fases do projeto, bem como após a sua conclusão. Referência: [O que é deploy?](https://coodesh.com/blog/dicionario/o-que-e-deploy/)

⁴ Um *pipeline* de DevOps é um conjunto de processos e ferramentas automatizados que permite que desenvolvedores e profissionais de operações colaborem na criação e implementação de código em um ambiente de produção. Referência: [Pipeline de DevOps](https://www.atlassian.com/br/devops/devops-tools/devops-pipeline)

⁵ A *monetização* de uma API ocorre quando as empresas geram lucro com suas interfaces de programação de aplicações (APIs). As APIs são a base do que é considerado atualmente como a mais avançada iteração do desenvolvimento de negócios. Referência: [O que é monetização de APIs?](https://www.redhat.com/pt-br/topics/api/what-is-api-monetization)


tags: [[tecnologia]], [[arquitetura]], [[APIs]]

