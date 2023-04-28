# Generated by Django 4.1.4 on 2023-04-14 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0017_certificadoseguimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificadoseguimiento',
            name='fechasuscripcion',
            field=models.CharField(max_length=40, verbose_name='Fecha de suscripcion del contrato'),
        ),
        migrations.AlterField(
            model_name='certificadoseguimiento',
            name='fechaterminacion',
            field=models.CharField(max_length=40, verbose_name='Fecha terminacion del contrato'),
        ),
        migrations.AlterField(
            model_name='usolicitudes',
            name='supervisor',
            field=models.CharField(max_length=40, verbose_name='supervisor'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=40, verbose_name='Sexo'),
        ),
    ]