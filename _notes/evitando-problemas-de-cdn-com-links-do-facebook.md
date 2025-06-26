---
title: Evitando problemas de CDN com links do Facebook
date: 2018-11-24 21:07:42

---


Você já ouviu falar em CDNs? Elas são um recurso de infra-estrutura utilizado para otimizar o tráfego da internet. Para isso, ao invés do usuário bater diretamente no seu servidor, ele consulta um serviço na nuvem, que contém cópias do seu site. Assim o tráfego direto diminui e o tempo que o usuário leva para acessar seu site diminui, já que o conteúdo é servir otimizadamente.

As CDNs funcionam, assim, como um cache do seu site através da nuvem. Daí vem o seu nome, Rede de Distribuição de Conteúdo, ou **Content Delivery Network**. A imagem abaixo representa bem como elas funcionam:

<img src="{{ site.baseurl }}/assets/cdn.jpg"/>


Esse recurso é muito utilizado por empresas que possuem um grande fluxo de acessos. Onde trabalho, enfrentamos recentemente um problema com isso. Utilizamos CDN mas um certo link estava tendo acessos diretos, sem passar pelo serviço. Depurando o caso, observamos que isso ocorria devido a uma nova política de links do Facebook.

De uns tempos para cá a rede social passou a colocar um ID em cada link clicado a partir do seu site. Por exemplo: quando clica em um link de outro no site no seu Facebook, o destino é aquele link com um parâmetro fbclid no final. 

O problema dessa atualização do Facebook é que ela força o usuário a bater no servidor e não na CDN. É como se a CDN não tivesse aquela página pronta em seu serviço, mostrando ao usuário a página que está no servidor.

Existem uma série de métodos para se livrar desse problema. Algumas passam por configurações na CDN e outros em adaptações do seu .htacess, caso use Apache. A solução para esse problema vai depender do seu time de infra-estrutura. O importante é evitar que esses acessos continuem vindo diretamente ao seu servidor, visto que isso pode sobrecarregar sua aplicação. 

tags: [[tecnologia]]