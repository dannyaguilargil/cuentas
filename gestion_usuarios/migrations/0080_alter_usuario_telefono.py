# Generated by Django 5.0.3 on 2024-10-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0079_usuario_fechafinalcontrato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telefono fijo'),
        ),
    ]