# Generated by Django 5.0.3 on 2024-04-25 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_informes', '0011_alter_informe_fechaentregainicial_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informe',
            name='fechaentregainicial',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha inicial de entrega'),
        ),
        migrations.AlterField(
            model_name='informe',
            name='periodicidad',
            field=models.IntegerField(blank=True, null=True, verbose_name='Periodicidad cantidad'),
        ),
        migrations.AlterField(
            model_name='informe',
            name='totalentregas',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total de entregas'),
        ),
    ]