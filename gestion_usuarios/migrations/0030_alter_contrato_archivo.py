# Generated by Django 4.1.4 on 2023-04-28 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0029_alter_contrato_archivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='archivo',
            field=models.FileField(default='1', upload_to='pdfs/', verbose_name='Pdf del contrato'),
        ),
    ]