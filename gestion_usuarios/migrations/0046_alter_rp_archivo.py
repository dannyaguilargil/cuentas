# Generated by Django 4.1.4 on 2023-06-22 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0045_usuario_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rp',
            name='archivo',
            field=models.FileField(default='', upload_to='pdfs/', verbose_name='archivo'),
        ),
    ]
