# Generated by Django 5.0.3 on 2024-09-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0028_alter_solicitudsistemasupervisor_cargo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudsistemasupervisor',
            name='fechafinalcontrato',
            field=models.CharField(blank=True, max_length=90, null=True, verbose_name='Fecha final del contrato'),
        ),
    ]