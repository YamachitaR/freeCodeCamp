from django.db import models

# Create your models here.

# estamos criando para ser um banco de dado de categoria
class Category(models.Model):
    name = models.CharField(max_length=255) # nome da categoria,  aquantidade de caracter <=255

    class Meta:
        ordering = ('name', ) # Faz com que apareça em ordem 
        #verbose_name_plural = 'tipos'
        verbose_name_plural = 'Categories' # Mudar o nome 

    #Faz com que o nome seja aparecido corretamente
    # caso contrario aparece como obj 
    def __str__(self):
        return self.name 