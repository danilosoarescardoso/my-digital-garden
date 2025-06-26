---
title: "Usando Cache em APIs: Exemplo Prático"
date: 2023-04-18 12:18:24
---

Recentemente fiz dois posts sobre [quando usar](https://danilocardoso.dev/blog/quando-usar-cache-apis/) e [quando não usar](https://danilocardoso.dev/blog/quando-nao-usar-cache-apis/) cache em APIs. No texto de hoje mostro de forma simples como o cache pode ser usado em uma API. O link para o repositório pode ser [encontrado aqui](https://github.com/danilosoarescardoso/cache-python-example).

Vamos lá!

## Premissas da API
Para o exemplo,criei uma API em Python utilizando a biblioteca Flask, que permite a criação de endpoints de forma bastante simples. A API tem duas rotas principais, uma para obter todos os produtos e outra para obter um produto específico com base em seu ID.

## Dependências
Utilizei as seguintes bibliotecas:

* **Flask**: framework web em Python usado para criar aplicativos web e APIs RESTful.
* **jsonify**: é uma função do Flask que transforma objetos Python em JSON para que possam ser retornados como uma resposta HTTP.
* **Flask-Caching**: é uma extensão Flask que fornece recursos de armazenamento em cache para o aplicativo Flask.
* **time**: é um módulo Python que fornece funções relacionadas ao tempo, como sleep, que é usada neste exemplo para simular um acesso a um banco de dados adicionando um atraso em algumas das funções.

## Utilizando o cache nos endpoints
No endpoint que lista produtos por ID inclui um cache de 10 segundos. Isso significa que quando uma chamada é feita, a informação será buscada no banco de dados. Nas próximas chamadas que ocorrerem dentro de 10 segundos, a resposta enviada será aquela armazenada em cache, logo não haverá o processamento da função que vai até o banco de dados.

```python
# Return a product by id
@app.route('/products/<int:id>')
@cache.cached(timeout=10)  # 10 seconds of cache
def get_product(id):
    return jsonify(find_product(id))
```

Para simplificar o teste, a função que retorna o produto não possui acesso a um banco de dados real, mas sim um atraso de 5 segundos para simular esse acesso, buscando os dados em um *array*. 

```python
# find product by id
def find_product(id):
    
    # Adding a simple delay to simulate an access to a database
    time.sleep(5)
    
    for product in products:
        if product['id'] == id:
            return product
    return None
```

Logo, a primeira chamada vai demorar mais de 5 segundos e as demais serão mais rápidas, dentro dos 10 segundos de cache.

### Configuração do cache

Para usar o cache na aplicação, utilizei os seguintes parâmetros de inicialização:

```python
app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://localhost:6379'})
```

Nas parametrizações acima, estou utilizando o Redis como banco de dados de cache. Para instalar o Redis, basta seguir as instruções [deste link](https://redis.io/topics/quickstart) e subir a sua instância. Em **CACHE_TYPE** é definido o tipo de cache que será utilizado pela aplicação. Os modos disponíveis são estes:

* **simple**: cache simples em memória para aplicações de processo único. Não recomendado para uso em produção ou ambientes com vários processos.
* **filesystem**: cache que armazena dados no sistema de arquivos local. Adequado para implantações de servidor único, onde o cache não precisa ser compartilhado entre vários processos ou servidores.
* **redis**: Um cache que usa o Redis como backend. Adequado para implantações mais complexas ou quando você precisa de um cache distribuído que pode ser compartilhado entre vários processos ou servidores.
* **memcached**: Um cache que usa o Memcached como backend. Adequado para cache distribuído em vários servidores.
* **saslmemcached**: Um cache Memcached que suporta o mecanismo de autenticação SASL (Simple Authentication and Security Layer).
* **gaememcached**: Um cache que usa o serviço Memcached do Google App Engine. Adequado para aplicativos em execução no Google App Engine.
* **uwsgi**: Um cache que usa o framework de cache do uWSGI. Adequado para implantações usando uWSGI como servidor de aplicativos.

No caso deixei como Redis por ser a configuração *default* da biblioteca.

## Testando a API e resultados
Utilizando o Postman, fiz algumas chamadas sem o cache e posteriormente com o cache. Podemos ver, no primeiro resultado, que a resposta demorou 5 segundos para ser retornada. Nas próximas chamadas, a resposta foi retornada em menos de 1 segundo, pois o cache foi utilizado.

<img src="{{ site.baseurl }}/assets/request-without-cache.png"/>

Imagem 1 - Resposta sem cache

---

<img src="{{ site.baseurl }}/assets/request-with-cache.png"/>

Imagem 2 - Resposta com cache

---

Fiz o mesmo teste com o endpoint que retorna todos os produtos, obtendo os seguintes resultados:

<img src="{{ site.baseurl }}/assets/request-without-cache-2.png"/>

Imagem 3 - Resposta sem cache

---

<img src="{{ site.baseurl }}/assets/request-with-cache-2.png"/>

Imagem 4 - Resposta com cache

## Considerações

Esse foi um exemplo bem simples de como cache pode ser usado em APIs. Em sistemas distribuídos, onde há uma maior complexidade técnica, pode ser necessário utilizar camadas adicionais de cache ou outras técnicas. Por isso vale a pena estudar a fundo as ferramentas que existem além do Redis e entender, no caso do Redis, como se aplicam os diferentes tipos de cache que ele implementa.

tags: [[APIs]], [[arquitetura]]