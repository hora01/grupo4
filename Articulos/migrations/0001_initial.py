# Generated by Django 4.2.1 on 2023-05-23 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desarrollador', models.CharField(max_length=100, verbose_name='Desarrollador')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(null=True, verbose_name='Fecha')),
                ('email', models.EmailField(max_length=90, null=True, verbose_name='Email')),
                ('nombre', models.CharField(max_length=90, verbose_name='Nombre')),
                ('mensaje', models.TextField(max_length=500, verbose_name='Mensaje')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('nombre', models.CharField(max_length=60)),
                ('contenido', models.TextField(max_length=600)),
                ('imagen', models.URLField()),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Articulos.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('nombre', models.CharField(max_length=60)),
                ('autor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Articulos.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cometo', models.BooleanField(verbose_name='Ha comentado')),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articulos.comentario')),
            ],
        ),
    ]
