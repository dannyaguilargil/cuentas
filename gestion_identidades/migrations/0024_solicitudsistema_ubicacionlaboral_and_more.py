# Generated by Django 5.0.3 on 2024-09-17 14:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0023_alter_solicitudsistema_sede_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudsistema',
            name='ubicacionlaboral',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Ubicacion laboral'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='cargo',
            field=models.CharField(default=django.utils.timezone.now, max_length=40, verbose_name='Cargo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='cedula',
            field=models.IntegerField(verbose_name='Cedula'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='sede',
            field=models.CharField(blank=True, choices=[('ADMINISTRATIVA', 'Administrativa'), ('UBA PBL', 'UBA Puente barco leones'), ('UBA LIBERTAD', 'UBA Libertad'), ('UBA COMUNEROS', 'UBA Comuneros'), ('UBA AGUA CLARA', 'UBA Agua clara'), ('UBA LOMA DE BOLIVAR', 'UBA Loma de bolivar'), ('UBA POLICLINICO', 'UBA Policlinico')], default='ADMINISTRATIVA', max_length=80, null=True, verbose_name='Sede'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='tipodocumento',
            field=models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('PASAPORTE', 'Pasaporte'), ('CE', 'Cedula de extranjeria')], default='CC', max_length=40, verbose_name='Tipo de documento'),
        ),
    ]