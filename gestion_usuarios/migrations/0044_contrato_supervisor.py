# Generated by Django 4.1.4 on 2023-06-12 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0043_alter_usuario_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='supervisor',
            field=models.CharField(default='', max_length=40, verbose_name='Supervisor'),
        ),
    ]
