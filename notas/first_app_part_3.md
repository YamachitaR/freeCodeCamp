# First_app_part_3.md 

## Objetivo 

 -  Criar rodapé e cabeçalho da nossa págiga
 -  Ciar página de  contact 

 ## Crianto contact 

###  Criando urls 
Vamos cria a nossa rota para o contact, para isso vamos no arquivo 

~~~python
from core.views import index, contact

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
]

~~~
Repare que foi acrescentando **contact** no `from core.views import index, contact` e  `path('contact/', contact, name='contact')`  

### Criando "fução contact"
ver como se chama o nome correto,

~~~ python
def contact(request):
    return render(request, 'core/contact.html')
~~~

Parecido que foi criado para index

### contact html

Vamos adicionar um arquivo junto com os demais html que foi criado  denotado contact.html

~~~ html
{% extends 'core/base.html' %}

{% block title %} Welcome {% endblock %}

{% block content %}
    <h1>The front page</h1>
{% endblock %}
~~~

Bem parecido que foi feito com index.html 

