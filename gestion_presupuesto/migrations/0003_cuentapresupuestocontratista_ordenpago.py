# Generated by Django 4.1.4 on 2023-06-28 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_presupuesto', '0002_cuentapresupuestocontratista'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuentapresupuestocontratista',
            name='ordenpago',
            field=models.CharField(default='No', max_length=200, verbose_name='Orden de pago'),
        ),
    ]