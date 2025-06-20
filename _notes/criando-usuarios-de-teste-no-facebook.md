---
title: Criando usuários de teste no Facebook
date: 2018-11-17 21:06:32
tags: [redes sociais, facebook, login]
---

<img src="{{ site.baseurl }}/assets/facebook-login-1521224093933_615x300.jpg"/>

Sistemas de login utilizando redes sociais são muito comuns. Se a aplicação precisa de uma área privada e com informações pessoais, essa é a melhor forma de isolar os dados. Entretanto, [usuários costumam não gostar de criar contas](https://conversionxl.com/blog/social-login/) em sites. Além de levar tempo, eles ficam na dúvida sobre qual será a utilização de seus dados.

Para evitar isso, surgiram os logins sociais. Com eles, é possível automatizar o processo de login através de uma conta de rede social. Nesse caso, você tem menos informações do usuário, mas consegue retê-lo, deixando para pegar o restante de dados importantes (como determinados documentos ou endereço).

Existem muitas [formas de implementar o login social](https://canaltech.com.br/software/aprenda-a-adicionar-o-login-com-facebook-no-seu-site-usando-javascript-ou-php/), seja do Facebook, Twitter ou outras redes. Hoje vou apresentar não como implementar esses recursos, mas como utilizar a função de criar contas de teste através da API do Facebook.

Recentemente trabalhei em uma atividade para implementar um novo formato de login pelo Facebook onde trabalho. Na hora de testar, me deparei com a seguinte dificuldade: como testar com meu usuário caso ele já tenha os registros no banco? Precisava entrar sempre no BD para apagar meu registro e testar novamente.

Foi aí que, lendo a documentação do Facebook, encontrei uma função que permite [criar usuários de teste](https://developers.facebook.com/docs/apps/test-users/?locale=pt_BR). Com eles, você pode definir permissões específicas para cada aplicação e realizar o fluxo de login normalmente, podendo testar o comportamento do usuário após entrar no sistema.

Esse recurso me ajudou muito, inclusive a encontrar inconsistências no que eu havia implementado. Existem algumas limitações, como:

* Somente admins de aplicativos e desenvolvedores podem ter acesso a usuários de teste;
* apenas 2 mil usuários de teste podem ser criados;
* suas interações são permitidas apenas entre usuários de teste

Apesar disso, creio que a ferramenta seja ótima para testes unitários de acesso. Enfim, se quiser saber mais sobre isso, [veja a seguinte documentação](https://developers.facebook.com/docs/apps/test-users/?locale=pt_BR). Boa sorte!

