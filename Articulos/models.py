from django.db import models

# Create your models here.
class Autor(models.Model):
   desarrollador = models.CharField(max_length=100, verbose_name="Desarrollador")
 

class Entrada(models.Model):  
    nombre = models.CharField(max_length=60)
    contenido = models.TextField(max_length=600) #si quiero puedo poner menos caracteres
    imagen = models.URLField()
    autor = models.OneToOneField(Autor, on_delete=models.CASCADE, primary_key=True) # Uno a uno (Un autor para cada tecnología)
     
class Comentario(models.Model):
    fecha = models.DateField(null=True, verbose_name="Fecha")
    email = models.EmailField(max_length=90, null=True, verbose_name="Email")
    nombre = models.CharField(max_length=90, verbose_name="Nombre")
    mensaje = models.TextField(max_length=500, verbose_name="Mensaje")

class Visitante(models.Model):
    cometo=models.BooleanField(verbose_name="Ha comentado")
    comentario= models.ForeignKey(Comentario, on_delete=models.CASCADE) # Muchos a uno (un visitante hace uno o mas de un comentarios)

class Tecnologia(models.Model):
    nombre = models.CharField(max_length=60)
    autor = models.OneToOneField(Autor, on_delete=models.CASCADE, primary_key=True)

#Falta le relación muchos a muchos

        