# Generated by Django 4.1.4 on 2023-04-10 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0014_planilla'),
    ]

    operations = [
        migrations.CreateModel(
            name='actividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objeto', models.CharField(max_length=300, verbose_name='Objeto del contrato')),
                ('lugar', models.CharField(max_length=40, verbose_name='Lugar donde realizo la actividad')),
                ('fecha', models.CharField(max_length=40, verbose_name='Fecha de la cuenta')),
                ('actividades', models.CharField(max_length=600, verbose_name='Actividades a realizar ')),
                ('resultadoactvidades', models.CharField(max_length=600, verbose_name='Resultado de las actividades realizadas')),
            ],
        ),
    ]
