# Generated by Django 4.1.4 on 2023-06-26 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0057_cuentacontratista_objetocontrato'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuentacontratista',
            name='pdfcontrato',
            field=models.CharField(default='pdfs/NOCARGADO', max_length=80, verbose_name='Pdf del contrato'),
        ),
    ]
