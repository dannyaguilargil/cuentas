# Generated by Django 4.1.4 on 2023-06-25 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0052_remove_cuentacontratista_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentacontratista',
            name='archivo',
            field=models.FileField(default='pdfs/NOCARGADO', upload_to='pdfs/', verbose_name='archivo'),
        ),
    ]
