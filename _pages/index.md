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

O tema usado está [disponível no Github](https://github.com/maximevaillancourt/digital-garden-jekyll-template).


<strong>Recently updated notes</strong>

<ul>
  {% assign recent_notes = site.notes | sort: "last_modified_at_timestamp" | reverse %}
  {% for note in recent_notes limit: none %}
    <li>
      {{ note.last_modified_at | date: "%Y-%m-%d" }} — <a class="internal-link" href="{{ site.baseurl }}{{ note.url }}">{{ note.title }}</a>
    </li>
  {% endfor %}
</ul>

<style>
  .wrapper {
    max-width: 46em;
  }
</style>
