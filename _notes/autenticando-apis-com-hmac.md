---
title: Autenticando APIs com HMAC
date: 2023-08-06 19:10:53

---

Recentemente estava estudando sobre como funciona a autenticação de APIs usando HMAC e resolvi fazer um texto explicando sobre como esse modelo de segurança para APIs opera, trazendo seus prós, contras e indicações de uso.

## O que é HMAC

Dentro da área de segurança da informação, um MAC é considerado um ** código autenticador de mensagem** - o termo significa *message authentication code* em inglês. Geralmente um algoritmo de criptografia MAC recebe uma chave secreta - que pode ser qualquer série de caracteres - e uma mensagem que será autenticada. O resultado do processamento da mensagem com a chave secreta é uma *string* única que será enviada para o consumidor dessa mensagem, junto com a mensagem original. 

Para que o consumidor valide a integridade da mensagem recebida, ele deverá receber previamente a chave secreta e qual algoritmo de criptografia que foi utilizado para gerar o hash.

## HMAC em APIs

No mundo de APIs, esse processo de gerar uma *string* e enviar para os consumidores é conhecido como HMAC, ou *Hash-based message authentication code* em inglês - **código de autenticação de mensagem baseado em Hash** em português. Sabe quando você precisa de um token pra usar uma API? Então, existem várias formas de obter e gerar tokens. Na autenticação HMAC, o token a ser utilizado para validar a autenticidade da mensagem e do seu emissor é feito utilizando essa string. Agora vamos ver como essa validação é feita.

## Como funciona a validação no HMAC

Com HMAC, ao invés de você enviar um token OAuth, com escopos, permissões e informações do remetente, o token enviado é a hash que expliquei anteriormente. A ideia desse token não é a de garantir a autenticidade do remetente, mas sim garantir que a mensagem recebida está consistente com o que foi enviado pelo remetente. Até existem casos de uso onde OAuth e HMAC são combinados, mas não existe uma obrigatoriedade. 

Como dito anteriormente, a hash é enviada junto com a mensagem para validação. Quando a mensagem é recebida, o destinatário já deve ter a chave secreta em mãos para cifrar a mensagem. Com isso ele vai gerar uma nova hash e compará-la com a hash recebida na requisição. Se as duas forem iguais, ele aceita a mensagem. Se não, a descarta.

Na imagem abaixo o fluxo é descrito de forma visual para facilitar o entendimento:

<img src="{{ site.baseurl }}/assets/hmac-auth.drawio.png"/>

## Considerações sobre a autenticação HMAC

Apesar de ser uma alternativa à autenticação OAuth, tenho algumas considerações a serem feitas na hora de usar algo como HMAC:

* **Gestão de chaves**. Para que haja uma boa governança do processo de autenticação HMAC, é necessário gerenciar de maneira eficiente as diferentes chaves a serem compartilhadas com seus parceiros. Diferente de uma autenticação OAuth 2.0 que possui um ator somente para fazer isso - o servidor de autenticação - trabalhar com HMAC demanda a gestão dessas chaves por conta própria. Pelo menos não encontrei nos meus estudos uma ferramenta de autenticação que faça a gestão das chaves por default.
* **Não possui confidencialidade**. Diferente de OAuth onde podemos usar métodos de autenticação como o jwt-bearer, que encripta o payload para evitar vazamento de informações confidenciais, por exemplo, no HMAC a mensagem vai do jeito que ela foi escrita. A ideia do HMAC não é aumentar a confidencialidade, mas sim garantir a integridade da mensagem escrita pelo remetente. 
* **Sobrecarga de desempenho**. Trabalhar com algoritmos de criptografia, apesar de aumentar a segurança de suas aplicações, gera maior necessidade de processamento computacional. Em transanções em tempo real (RT) ou quase em tempo real (NRT) isso pode ser um baita problema. É necessário levar esse ponto em consideração.
* **Não garante a autenticidade do remetente**. Apesar de haver uma chave secreta compartilhada apenas entre remetente e destinatário, não é possível garantir que o remetente é realmente quem esperamos que ele seja no HMAC. Isso porque qualquer atacante pode tomar conta de uma chave secreta e se passar pelo remetente. Nesse caso autenticações com certificado digital ou fluxo de *client credentials* ajudam a aumentar a segurança de suas APIs, garantindo que o remetente é realmente quem ele diz ser.

Apesar desses pontos, existem algumas características quem podem fazer o HMAC ser útil na sua estratégia de APIs em determinados casos de uso, como por exemplo:

* **Camada adicional contra ataques DDoS**. Uma das formas de implementar HMAC é incluindo o timestamp do momento da requisição. Com isso, apenas uma requisição será aceita pelo servidor caso todas as informações estejam certas, já que as subsequentes requisições em DDoS terão timestamps diferentes.
* **Garantia de integridade do payload**. Podem haver casos de uso específicos onde garantir a não alteração do payload durante a sua transmissão seja importante. No meu ponto de vista, isso pode ser adicionado como camada adicional de segurança em um fluxo OAuth 2.0 desde que haja o conhecido risco de um payload ser modificado.


tags: [[arquitetura]], [[tecnologia]]