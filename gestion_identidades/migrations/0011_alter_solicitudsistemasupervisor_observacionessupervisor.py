# Generated by Django 5.0.3 on 2024-04-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0010_rename_aplicativo_solicitudsistemasupervisor_apicativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudsistemasupervisor',
            name='observacionessupervisor',
            field=models.CharField(default='', max_length=200, verbose_name='Observaciones del supervisor'),
        ),
    ]
