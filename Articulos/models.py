from django.db import models

# Create your models here.
class Comentario(models.Model):
    fecha = models.DateField(null=True, verbose_name="Fecha")
    email = models.EmailField(max_length=90, null=True, verbose_name="Email")
    nombre = models.CharField(max_length=90, verbose_name="Nombre")
    mensaje = models.TextField(max_length=500, verbose_name="Mensaje")

class Visitante(models.Model):
    cometo=models.BooleanField(verbose_name="Ha comentado")
    comentario= models.ForeignKey(Comentario, on_delete=models.CASCADE) # Muchos a uno (un visitante hace uno o mas de un comentarios)

class Persona( models.Model):
    nombre_apellido = models.CharField(max_length=100, verbose_name="Nombre y apellido")
    email = models.EmailField(max_length=100, verbose_name="Email")
    teléfono = models.CharField(max_length=256, verbose_name="Teléfono de contacto")

    class Meta: 
        abstract = True #modelo abstracto para la base de datos. Clase padre para Profesor y Alumno.
    
    def __str__(self):
        return f"{self.nombre_apellido}" #para ubicar los nombres en el admin


class Profesor(Persona):
    profesión = models.BooleanField(verbose_name="Titulo profesional")
    entrevistas = models.BooleanField(verbose_name="Entrevistas aprobadas")

class Alumno(Persona):
    informacion_detallada_de_alumno = models.CharField(max_length=500, verbose_name="Información detallada del alumno", null=True)

class InfoAlumno(models.Model):
    dni = models.IntegerField(verbose_name="DNI", null=True)
    dirección = models.CharField(max_length=200, verbose_name="Dirección")
    fecha_ingreso = models.DateField(verbose_name="Fecha de ingreso", default='1900-01-01')
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE, primary_key=True) # Uno a uno (una lista de informacion para un alumno) 

class Clase(models.Model):
    nombre = models.CharField(max_length=60)
    contenido = models.TextField(max_length=600) #si quiero puedo poner menos caracteres
    imagen = models.URLField()
    profesor= models.ForeignKey(Profesor, on_delete=models.CASCADE) # Muchos a uno (un profesor con muchas clases)
    número_comisión = models.IntegerField(verbose_name="Número de comisión")
    alumnos = models.ManyToManyField(Alumno) # Muchos a muchos (muchos alumnos en muchas clases)

    def __str__(self):
        return f"comisión: {self.nombre}"
    
class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    nombre_clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    descripccion = models.TextField(max_length=500)
    fecha_de_entrega = models.DateField(null=True, verbose_name="Fecha de entrega")
    def __str__(self):
        return f"nombre: {self.nombre}"

    