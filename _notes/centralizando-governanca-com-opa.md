---
title: "Centralizando governança de políticas com Open Policy Agent"
date: 2022-11-28 21:27:54
---

No contexto de sistemas distribuídos, precisamos de regras para uma infinidade de casos:

* Controlar acessos a uma **API**
* Permitir a criação de **recursos de infra** em cloud
* Executar **deploys** em ambientes produtivos e de homologação
* Gerir **acesso de rede** à instâncias de determinada aplicação
* etc

Para a definição dessas regras costumamos usar o termo políticas. Cada ferramenta possui suas políticas e definições próprias. No caso de controlar acessos de uma API, podemos colocar políticas no API Gateway ou no *microsserviço* que implementa os *endpoints*. Para controlar acessos de rede podemos configurar políticas no *load balancer* ou *firewall* e por aí vai.

<img src="{{ site.baseurl }}/assets/stop.jpeg"/>


Um problema que surge com o enorme conjunto de tecnologias e conceitos que existem hoje é que fica difícil **gerenciar de forma unificada** as diferentes políticas implementadas por uma determinada área. Imagine o trabalho que um time de segurança possui ao ter que catalogar todas as diferentes validações de segurança feitas nos diferentes sistemas que uma empresa pode ter. Governar aspectos de sistemas distribuídos demanda soluções que permitam descentralizar a governança, mas sempre mantendo o controle acessível a quem é responsável.

Uma solução para esse tipo de problema é o [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/). O OPA, como também é conhecido, é uma ferramenta *open source* que visa unificar a definição de políticas em apenas uma *engine*. Através de uma linguagem de alto nível, é possível estabelecer políticas para diferentes tipos de tecnologia, unificando a forma como elas são escritas e diminuindo o processamento dos outros serviços. Com isso é possível não apenas segregar políticas das regras de negócio como também aumentar a segurança, criando uma camada adicional de validações.

## Como funciona na prática

Para que o OPA funcione, existem algumas características do seu funcionamento que precisam ser pontuadas:

1. Toda política de um sistema é armazenada como objetos JSON. Por exemplo, as características de um grupo de servidores podem ser definidas pela seguinte sintaxe:

``` 
{
    "servers": [
        {"id": "app", "protocols": ["https", "ssh"], "ports": ["p1", "p2", "p3"]},
        {"id": "db", "protocols": ["mysql"], "ports": ["p3"]},
        {"id": "cache", "protocols": ["memcache"], "ports": ["p3"]},
        {"id": "ci", "protocols": ["http"], "ports": ["p1", "p2"]},
        {"id": "busybox", "protocols": ["telnet"], "ports": ["p1"]}
    ],
    "networks": [
        {"id": "net1", "public": false},
        {"id": "net2", "public": false},
        {"id": "net3", "public": true},
        {"id": "net4", "public": true}
    ],
    "ports": [
        {"id": "p1", "network": "net1"},
        {"id": "p2", "network": "net3"},
        {"id": "p3", "network": "net2"}
    ]
}
```

Na sintaxe acima, extraída de um exemplo da [documentação oficial](https://www.openpolicyagent.org/docs/latest/), é possível ver que existem informações sobre três servidores diferentes, incluindo as portas e redes usadas. É nesse arquivo que são definidas as políticas para seus ativos digitais.

<img src="{{ site.baseurl }}/assets/opa-arch.svg"/>

Figura 1 - Arquitetura de uma política no Open Policy Agent   
 
2. cada requisição / acesso feito a uma ferramenta que possui políticas é validado por uma instância do OPA. Para isso, é necessário fazer uma *avaliação de política*, que nada mais é do que fazer uma *query* validando se aquela política foi violada ou não. Por exemplo: você pode executar a seguinte *query* para validar se uma conexão sem HTTPS é aceita no servidor:

```
input.servers[0].protocols[0] == "http"
```
Se o retorno for falso, isso significa que uma conexão insegura não é aceita, ou seja, uma política foi violada. Dessa forma é possível barrar a comunicação antes de chegar no servidor desejado. Existe também a possibilidade de rodar uma *query* que valide todas as políticas existentes de uma única vez. Se alguma falhar, o acesso é barrado. 

3. Quando uma política é criada em JSON, existe um *bind* que é feito para uma [linguagem de alto nível chamada Rego](https://www.styra.com/blog/how-to-write-your-first-rules-in-rego-the-policy-language-for-opa/). Todas políticas são armazenadas com essa sintaxe. As *queries* para avaliação de políticas também devem ser escritas em Rego.

4. É possível executar avaliações de política usando APIs REST ou CLI, para facilitar automações e comunicações M2M. 

5. A ferramenta [faz parte do Cloud Native Computing Foundation](https://www.cncf.io/projects/open-policy-agent-opa/) desde 2018. 

## Casos de Uso
Por ser uma ferramenta com alguns anos de bagagem, já existem casos de uso bem bacanas com ela. Seguem algumas aplicações que podem ser feitas no dia-a-dia:

### Kubernetes
Para controlar cada chamada feita nas APIs do Kubernetes existem os *Admission Controllers*, ferramentas do próprio K8's. Como as *requests* são interceptadas, é possível fazer diferentes validações e modificações que sejam necessárias. Uma das formas de fazer isso é com o *Open Policy Agent*.

Colocar o OPA como um *Admission Controller* faz com que seja possível checar *labels* nos recursos manipulados, validar conflitos com *Ingress* já existentes, sendo possível também modificar os objetos alvo de validação. 

### APIs
É possível criar políticas que impeçam o acesso a determinados *endpoints* apenas para pessoas que possuam determinado token, escopo ou variável pré-determinada. Apesar desse não ser o caso de uso mais comum, já que o API Gateway tende a ser a peça responsável por esse tipo de validação, é interessante perceber como é possível centralizar a governança desse tipo de validação em uma ferramenta como o OPA. 

Com OPA é possível fazer o *parse* de JWTs e validar o conteúdo deles, diminuindo a necessidade de validações no API Gateway e até no serviço que gerencia as regras de negócio. 

## Trade-offs
Apesar de ser uma ferramenta versátil e muito útil no contexto de aplicações em cloud, vale ressaltar que ela não é uma bala de prata. Existem alguns passos a considerar ao adotá-la:

### Maturidade técnica
Uma ferramenta que centraliza a governança de políticas precisa de um contexto muito maduro e consciente das capacidades que existem no uso dessa tecnologia. Criar políticas para toda e qualquer validação vai gerar gargalos, débitos técnicos e aumentar a carga cognitiva dos times, que precisarão entender diferentes camadas de regras existentes no OPA. É necessário definir uma gestão por processos de forma clara, separando responsabilidades e papeis de forma objetiva.  

### Gestão por processos
Para uma ferramenta desse tipo fazer sentido, é necessário que as responsabilidades sejam bem definidas. Quando houver clareza sobre quem pode criar, modificar e excluir regras, além de um comitê que gerencia todas as políticas, aí todos poderão usar a ferramenta extraindo máximo valor. Vale a pena ter um [*board* de arquitetura](https://www.youtube.com/watch?v=dNrF1tZf4Lk) pensando na melhor forma de aplicar a ferramenta. Além disso, é válido trazer uma [visão de produtos e plataforma](https://www.youtube.com/watch?v=5f1Ioxef__o) para adoção da ferramenta. Um [time de plataforma](https://www.thoughtworks.com/en-br/radar/techniques/platform-engineering-product-teams) tocando essa ferramenta é uma ideia que parece fazer sentido, por exemplo. 

### Pode não valer a pena em alguns casos
Por mais que governar todas as políticas a partir de um único ponto seja uma ideia interessante, pode ser que não faça sentido para seu contexto usa-la em todas as ferramentas. A melhor forma de avaliar se vale a pena ou não usar o OPA em cada contexto é rodar MVPs, tendo sempre em mente a questão dos processos e maturidade técnica. Havendo viabilidade técnica para uma determinada ferramenta, como o Terraform, aí deve-se pensar nos processos e próximos passos. 

tags: [[tecnologia]], [[arquitetura]]