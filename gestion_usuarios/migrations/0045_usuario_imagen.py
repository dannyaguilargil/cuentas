# Generated by Django 4.1.4 on 2023-06-22 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0044_contrato_supervisor'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(default='imgs/sinfoto.jpeg', upload_to='imgs/'),
        ),
    ]
