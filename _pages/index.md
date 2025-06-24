---
layout: page
title: Home
id: home
permalink: /
---

# Seja bem-vindo(a)! 🌱 

<p style="padding: 3em 1em; background: #f5f7ff; border-radius: 4px;">
  Criei esse blog para falar dos assuntos que tenho interesse, como música, tecnologia, economia e outros tópicos em geral. Caso queira entrar em contato comigo, use minhas redes sociais listadas na página <a class="internal-link" href="{{ site.baseurl }}/about">Sobre</a>.
</p>

---

<strong>Tópicos</strong>
<p> 
  {% assign subject_pages = site.notes | where: "layout", "subject" %}
  {% for note in subject_pages %}
    <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>{% unless forloop.last %}, {% endunless %}
  {% endfor %}
</p><br>

---

<strong>Anotações</strong>

<ul style="list-style-type:none" class="lista-de-posts">
  {% assign recent_notes = site.notes | where_exp: "note", "note.layout != 'subject'" | sort: "created_at_timestamp" | reverse %}
  {% for note in recent_notes limit: none %}
    <li>
      <span class="data">{{ note.date | date: "%m · %Y" }}</span > <a class="internal-link titulo" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>


O tema usado está [disponível no Github](https://github.com/maximevaillancourt/digital-garden-jekyll-template).


<style>
  .wrapper {
    max-width: 46em;
  }
</style>
