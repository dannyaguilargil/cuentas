# Generated by Django 4.1.4 on 2023-04-14 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0018_alter_certificadoseguimiento_fechasuscripcion_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usolicitudes',
            options={'verbose_name': 'Solicitud de usuario', 'verbose_name_plural': 'Solicitudes de usuarios'},
        ),
        migrations.AlterModelTable(
            name='usolicitudes',
            table='Solicitudes de usuarios',
        ),
    ]
