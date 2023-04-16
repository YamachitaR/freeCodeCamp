# First App

Vamos criar a nosso primeiro aplicação.

## Criando APP
O nome da nossa aplicaçãos será core
~~~ bash 
python3 manage.py startapp core
~~~

## Habilitando core

Não sei se a palavra melhor é essa mas ...

Dentro do diretório puddle no arquivo settings.py na lista INSTALLED_APPS vamos adicionar um elemento denotado de core, como é demonstrado abaixo 

~~~python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core'
]
~~~

## Criando nosso primeiro ..

No views.py  do direotrio core, vamos criar função chamado index, que vai servir para rendelizar a nossa pagina 

~~ python
def index(request):
    return render(request, 'core/index.html')
~~~

Repare que o path sera core/index.html , vamos criar nosso index.html

## Criando index.html

Vamos criar um diretorio chamado templates que vai esta localizando dentro do diretório core, dentro do templates vai esta outro diretorio denotado core e dentro dele vai ter o arquivo index.html

Observação: na nossa função index nos colocamos o path como sendo core/index.html, sendo não necessário dizer que esta dentro diretorio templates.

~~~ html
<!doctype hmtl>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script src="https://cdn.tailwindcss.com"></script>
        <title>Puddle</title>
    </head>
    <body>
        <div class="px-6 py-6" >
            <h1>The front page</h1>
        </div>
    </body>
</html> 
~~~

## Adcionando o caminho 

No arquivo urls.py do diretorio puddle 
vamos fazer 

~~~ python 
from core.views import index 

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
]
~~~

Precismaos colocar a biblioteca que importa a nossa função 