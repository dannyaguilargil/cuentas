# Generated by Django 4.1.4 on 2023-04-04 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0003_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitud_usuario',
            old_name='apellido',
            new_name='primerapellido',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='apellido',
            new_name='primerapellido',
        ),
    ]