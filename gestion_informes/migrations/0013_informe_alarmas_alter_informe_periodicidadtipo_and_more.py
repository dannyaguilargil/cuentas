# Generated by Django 5.0.3 on 2024-05-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_informes', '0012_alter_informe_fechaentregainicial_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='informe',
            name='alarmas',
            field=models.IntegerField(blank=True, null=True, verbose_name='Dias de anticipacion de alarma'),
        ),
        migrations.AlterField(
            model_name='informe',
            name='periodicidadtipo',
            field=models.CharField(choices=[('Dias', 'Días'), ('Meses', 'Meses')], max_length=200, verbose_name='Tipo de periodicidad'),
        ),
        migrations.AlterField(
            model_name='informe',
            name='totalentregas',
            field=models.IntegerField(blank=True, default='10000', null=True, verbose_name='Total de entregas'),
        ),
    ]
