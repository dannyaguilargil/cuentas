# Generated by Django 5.0.3 on 2024-03-21 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0003_pazysalvo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudsistema',
            name='contrasena',
        ),
        migrations.RemoveField(
            model_name='solicitudsistema',
            name='usuario',
        ),
        migrations.AddField(
            model_name='solicitudsistema',
            name='celular',
            field=models.CharField(default='', max_length=40, verbose_name='Celular'),
        ),
    ]
