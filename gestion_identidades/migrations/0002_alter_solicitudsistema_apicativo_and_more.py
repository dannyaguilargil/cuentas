# Generated by Django 5.0.3 on 2024-03-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudsistema',
            name='apicativo',
            field=models.CharField(choices=[('KUBAPP', 'kubApp'), ('TNS', 'TNS'), ('ALMERA', 'Almera'), ('HICKCENTRAL', 'Hickcentral')], default='kubApp', max_length=40, verbose_name='Aplicativo'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='cedula',
            field=models.IntegerField(verbose_name='Cedula'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='sede',
            field=models.CharField(choices=[('ADMINISTRATIVA', 'Sede administrativa'), ('UBA PBL', 'UBA Puente barco leones'), ('UBA LIBERTAD', 'UBA Libertad'), ('UBA COMUNEROS', 'UBA Comuneros'), ('UBA AGUA CLARA', 'UBA Agua clara'), ('UBA LOMA DE BOLIVAR', 'UBA Loma de bolivar'), ('UBA POLICLINICO', 'UBA Policlinico')], default='Administrativa', max_length=80, verbose_name='Sede'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='tiposolicitud',
            field=models.CharField(choices=[('CREAR', 'Crear'), ('ACTUALIZAR', 'Actualizar'), ('ELIMINAR', 'Eliminar'), ('CONSULTAS', 'Consultas')], default='Consultar', max_length=40, verbose_name='Tipo de solicitud'),
        ),
    ]
