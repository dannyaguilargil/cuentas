# Generated by Django 4.1.4 on 2023-06-25 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0049_cuentacontratista'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuentacontratista',
            name='actividades',
        ),
        migrations.AddField(
            model_name='cuentacontratista',
            name='archivo',
            field=models.FileField(default='NO CARGADO', upload_to='pdfs/', verbose_name='archivo'),
        ),
    ]
