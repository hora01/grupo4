# Generated by Django 4.2.1 on 2023-06-22 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articulos', '0004_alter_clase_contenido_alter_clase_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoalumno',
            name='dni',
            field=models.IntegerField(null=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='descripccion',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='fecha_de_entrega',
            field=models.DateField(null=True, verbose_name='Fecha de entrega'),
        ),
    ]
