---
title: Aumentando a segurança de APIs com JWT - Conceitos
date: 2021-07-15 17:25:14
tags: [segurança, apis, oauth, jwt]
---

## Introdução

Segurança é um assunto que está sempre em alta, seja quando usamos um aplicativo de lazer como Instagram ou acessando nossos dados bancários no computador e celular. Com o advento da [Lei Geral de Proteção de Dados (LGPD)](https://www.serpro.gov.br/lgpd/menu/a-lgpd/o-que-muda-com-a-lgpd), a forma como sistemas lidam com informações de usuários se tornou uma questão altamente crítica, não importando o tamanho da empresa.

Com isso, muitas empresas passaram a dispender mais dinheiro e recursos para que os dados de seus clientes estejam seguros. Isso é uma proteção não só para o usuário final como para as instituições, prevenindo uma série de impactos em sua reputação, finanças e etc.

Como lidei bastante com assuntos de segurança de APIs nos últimos tempos, resolvi criar algumas publicações mostrando ferramentas e técnicas de criptografia que permitem uma melhor segurança para APIs e como elas podem ser implementadas no dia-a-dia.


## Conceitos

O primeiro passo para proteger uma API é conhecer as técnicas que existem. Apesar de haver formas mais simples como o [Basic Auth](https://datatracker.ietf.org/doc/html/rfc7617), vou partir do princípio de que precisamos de algo mais seguro, seguindo os padrões mais modernos da *Internet Engineering Task Force*. Por ser um assunto denso, darei um breve resumo sobre tópicos que considero importantes e como são usados, mas vale ressaltar: tem muito mais coisa pra conhecer e estudar.

### Comunicação cliente - servidor

Sempre que falamos de autenticação com os padrões OAuth, estamos falando de uma comunicação baseada na arquitetura cliente - servidor, isto é, um cliente solicitando informações para um servidor. Por mais complexas que as estruturas sejam, elas sempre vão se basear nesse tipo de arquitetura. Existe uma opção usada em sistemas legados e soluções empresariais que é o SAML, mas vou focar nas soluções baseadas em HTTP.

<img src="{{ site.baseurl }}/assets/client-server.png"/>


### OAuth 2.0

O protocolo [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749), lançado em 2006, é uma evolução do OAuth. Ele é definido como um padrão aberto de autorização. Seu foco é a delegação de acesso à APIs. Dentro do framework OAuth 2.0 existem quatro atores principais:

● **Resource Owner:** entidade capaz de dar acesso à um recurso protegido (pode ser o usuário final).

● **Resource Server:** servidor que armazena os recursos protegidos. O acesso a ele é feito através de tokens.

● **Client:** uma aplicação que solicita recursos protegidos, através da autorização do dono.

● **Authorization Server:** servidor que emite tokens de acesso ao *client*, depois da autenticação e obtenção da autorização.

Vale ressaltar que a comunicação no OAuth 2.0 é feita utilizando JSONs. Quando uma API é protegida com esse protocolo, as requisições precisam de um header do tipo *Authorization* com um JWT como valor.

**[OIDC 1.0](https://www.linkedin.com/pulse/aspnet-core-jwt-bearer-token-claims-roles-policies-alex-tochetto/)**

O OpenID Connect 1.0 é uma camada de identificação que fica no topo do protocolo OAuth 2.0. Ela permite validar um usuário através de autenticação em um servidor de autorização OAuth 2.0, bem como obter informações básicas de perfil desse usuário através de endpoints REST. Também permite que seja possível autenticar diferentes usando tipos de *clients* (web, mobile, etc). Para isso, existe uma série de especificações que definem alguns processos de como o OIDC deve ser implementado e funcionar, sendo alguns deles:

1. **[Dynamic Client Registration (DCR)](https://openid.net/specs/openid-connect-registration-1_0.html)**: define padrões de como um client pode ser cadastrado via endpoints REST;
2. **[Core](https://openid.net/specs/openid-connect-core-1_0.html)**: Define o funcionamento do OIDC e como a autenticação deve ser feita.
3. **[Discovery](https://openid.net/specs/openid-connect-discovery-1_0.html)**: descreve como clientes podem descobrir informações sobre provedores OpenID de forma dinâmica.

<img src="{{ site.baseurl }}/assets/oidc.png"/>

### JWT

Os [JSON Web Tokens](https://datatracker.ietf.org/doc/html/rfc7519) - ou JWTs - são um meio de representação de autoridade que podem ser trafegados entre duas partes. São URL *safe*, o que significa que podem ser trafegados em URLs sem que haja problemas de *encoding*. As autoridades (*claims*) dentro do JWT são codificadas em um objeto JSON que é usado como *payload.* Esse payload pode ser assinado digitalmente (JWS) ou encriptado (JWE). Com isso é possível assinar digitalmente o payload, evitando que ele seja lido por qualquer um.

## Grant Types

São os tipos de autenticação possíveis de serem feitos. Cada tipo de autorização possui passos para que a autoridade de consumo seja consentida. Os tipos mais conhecidos são:

**1. Authorization Code**

Esse fluxo é utilizado por clientes públicos e privados, no qual eles precisam trocar um código de autorização (*authorization code*) em troca de um código de acesso (access token).

Esse *authorization code* é obtido através de um redirecionamento feito para o serviço de autenticação, onde o usuário se loga. Nesse redirecionamento é passado um *callback*, que será chamado quando a autenticação for efetuada com sucesso. 

Ao retornar para o serviço que solicitou o *authorization code*, ele poderá chamar o servidor de autorização novamente, dessa vez solicitando um *access token*. Esse *access token*, conforme já falamos mais acima, é quem permitirá o acesso ao recurso desejado.

<img src="{{ site.baseurl }}/assets/auth_code.png"/>


**2. Client Credentials**

Enquanto o fluxo de *authorization code* é feito para autorizar usuários, existe uma forma de autenticar aplicações, fluxo que alguns chamam de *machine to machine* (M2M). Esse método é usado quando não precisamos de um usuário específico. Para isso, é necessário que o cliente tenha sido cadastrado anteriormente no servidor de autorização. No momento do cadastro será gerado um *client_id* e um *client_secret*, parâmetros que serão usados para solicitar1 um *access token* diretamente, sem tantos redirecionamentos. 

<img src="{{ site.baseurl }}/assets/client_credentials.png"/>


**3. [JWT Bearer](https://datatracker.ietf.org/doc/html/rfc7523)**

Esse não é o método de autorização mais conhecido ou usado - tanto que é difícil achar exemplos de implementação dele na internet - mas como utilizei em algumas implementações que fiz, achei válido falar dele. 

Esse fluxo é utilizado quando não se deseja trafegar dados sensíveis dos usuários por meio de *requests*. Dessa forma, a identificação do usuário é feita por meio de um JWT assinado que é enviado ao servidor de autorização informando os dados da pessoa que será autenticada. Esse token geralmente é assinado com uma chave privada, sendo que seu conteúdo só poderá ser acessado caso quem deseje lê-lo tenha a chave pública que faz par com a privada. 

Para que o servidor de autorização consiga validar o JWT assinado, é necessário que a chave pública que faz par com a chave privada durante a assinatura esteja cadastrada no servidor de autorização. Existe algumas especificidades na hora de manipular esse token que mostrarei na hora de apresentar as implementações no código.


<img src="{{ site.baseurl }}/assets/jwt-bearer.png"/>

---

### Para finalizar

Acredito que esses sejam bons conteúdos para começar a entender como podemos aplicar segurança em APIs utilizando JWTs, OAuth 2.0 e outros protocolos. No próximo post farei algumas implementações para mostrar como isso pode ser feito utilizando Java e outras tecnologias.

Deixo para estudo alguns links muito importantes que me ajudaram a produzir esse artigo. Boa leitura!

[OpenID Connect 1.0 - Identity & Authentication](https://developer.orange.com/tech_guide/openid-connect-1-0/)

[Componentes do JWT (JWS, JWE, JWA, JWK, JWKS)](https://www.brunobrito.net.br/jose-jwt-jws-jwe-jwa-jwk-jwks/)

[OpenID.net](https://openid.net/)

[ASP.NET Core - JWT Bearer Token - Claims, Roles and Policies](https://www.linkedin.com/pulse/aspnet-core-jwt-bearer-token-claims-roles-policies-alex-tochetto/)