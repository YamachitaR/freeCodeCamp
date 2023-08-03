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

## Cabeçalho

No arquivo base.html

vamos adiciona o seguinte trecho logo apos abertura da tag body.

~~~html
<nav class="py-6 px-6 flex justify-between items-center border-b border-gray-200">
    <a href="/" class="text-xl font-semibold">Puddle</a>

        <div class="space-x-6">
            <a href="#" class="text-lg font-semibold hover:text-gray-500">New item</a>
            <a href="#" class="text-lg font-semibold hover:text-gray-500">Browse</a>
            <a href="#" class="px-6 py-3 text-lg font-semibold bg-teal-500 text-white rounded-xl hover:bg-teal-700">Sign up</a>
            <a href="#" class="px-6 py-3 text-lg font-semibold bg-gray-500 text-white rounded-xl hover:bg-gray-700">Log in</a>
        </div>
</nav>
~~~


## Rodapé 

Adicione esse trexo, olhando de baixo para cima, encontre o fechamento da tag body e primeiro fechamento da tag div, no arquivo base.html

~~~ html

        <footer class="py-6 px-6 flex justify-between bg-gray-800">
            <div class="w-2/3 pr-10">
                <h3 class="mb-5 font-semibold text-gray-400">About</h3>

                <p class="text-lg text-gray-500">Lorem ipsum bla bla bla. Lorem ipsum bla bla bla. Lorem ipsum bla bla bla.</p>
            </div>

            <div class="w-1/3">
                <h3 class="mb-5 font-semibold text-gray-400">Menu</h3>

                <ul class="space-y-2">
                    <li><a href="#" class="text-lg text-teal-500 hover:text-teal-700">About</a></li>
                    <li><a href="{% url 'contact' %}" class="text-lg text-teal-500 hover:text-teal-700">Contact</a></li>
                    <li><a href="#" class="text-lg text-teal-500 hover:text-teal-700">Privacy policy</a></li>
                    <li><a href="#" class="text-lg text-teal-500 hover:text-teal-700">Term of use</a></li>
                </ul>
            </div>
        </footer>
~~~

