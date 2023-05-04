from django.db import models

# Create your models here.
class Entrada(models.Model):  
    nombre = models.CharField(max_length=60)
    contenido = models.TextField(max_length=600)
    #si quiero puedo poner menos caracteres
    imagen = models.URLField()
    autor = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    nombre = models.CharField(max_length=90)
    comentario = models.TextField(max_length=500)

    def __str__(self):
        return self.nombre

        