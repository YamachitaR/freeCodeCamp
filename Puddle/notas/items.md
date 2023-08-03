# Items


##  Criando e habilitando app item
No terminal, vamos criar nosso aplicação denotado de item 

~~~bash 
python3 manage.py startapp item 
~~~


Agora vamos habilitar, para isso vamos no settings.py e colocamos nome da aplicação na ultima linha conforme a linha abaixo 

~~~ python 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'item',
]
~~~

## models

Dentro do item/models.py

~~~ python 
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

~~~

depois 

~~~ bash 
 python manage.py makemigrations
 ~~~

e depois 

~~~ bash 
python manage.py migrate 
~~~


para criamos um banco de dados 


## Create Super User

Para cria basta

~~~bash 
python manage.py createsuperuser
~~~

## Habilitando que ADM consiga ter acesso ao banco de dado que foi criado 

no arquivo: item/admin.py
~~~ python 
from django.contrib import admin

# Register your models here.
from .models import Category

admin.site.register(Category)
~~~