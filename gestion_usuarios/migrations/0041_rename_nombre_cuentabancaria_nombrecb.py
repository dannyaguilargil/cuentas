# Generated by Django 4.1.4 on 2023-06-11 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0040_cuentabancaria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuentabancaria',
            old_name='nombre',
            new_name='nombrecb',
        ),
    ]