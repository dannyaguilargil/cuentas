# Generated by Django 4.1.4 on 2023-04-05 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0004_rename_apellido_solicitud_usuario_primerapellido_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='prueba',
            fields=[
                ('nombre', models.CharField(max_length=40)),
                ('cedula', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]