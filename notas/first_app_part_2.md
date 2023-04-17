# Fisrt App - 2

## Objetivo 

Vamos refatorar o código index.html


## base.hml

Vamos cria ´base.html´ no mesmo local do ´index.html´

~~~ html
<!doctype hmtl>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
        <title>{% block title %}   {% endblock %} | Puddle</title>
    </head>
    <body>
        <div class="px-6 py-6" >
            {% block content %}
            {% endblock %}
        </div>
    </body>
</html> 
~~~

##  Refazendo index.html

Logo temos que ficara 

~~~ html
{% extends 'core/base.html' %}


{% block title %} Welcome {% endblock %}

{% block content %}
    <h1>The front page</h1>
{% endblock %}
~~~

## Observação 

- 'base.html´ aonde vai ficar nossa parte comuns de todo site, no proximo passo vai ser criação do cabeçalho e rodape;

- `index.html` sera a nosso pagina inicial;

-  `{% extends 'core/base.html' %}` vai funcionar como fosse uma biblioteca, esta "extentendo" da base.html

-  Repare na plavra 'block' nos dois arquivo, como estivessemos colocando os blocos do index.html em base.html 