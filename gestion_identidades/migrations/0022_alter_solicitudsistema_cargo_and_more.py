# Generated by Django 5.0.3 on 2024-09-16 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0021_alter_solicitudsistema_dependencia'),
        ('gestion_informes', '0017_alter_informe_totalentregas'),
        ('gestion_supervisor', '0010_alter_supervisor_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudsistema',
            name='cargo',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='cedula',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cedula'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='celular',
            field=models.CharField(blank=True, default='', max_length=40, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='dependencia',
            field=models.ForeignKey(blank=True, max_length=40, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_informes.dependencia', verbose_name='dependencia'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='direccion',
            field=models.CharField(blank=True, default='', max_length=40, null=True, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='email',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='lugarexpedicion',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Lugar de expedicion'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='observaciones',
            field=models.CharField(blank=True, default='', max_length=40, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='sexo',
            field=models.CharField(blank=True, choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=40, null=True, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_supervisor.supervisor'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='telefono',
            field=models.CharField(blank=True, default='', max_length=40, null=True, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='solicitudsistemasupervisor',
            name='telefono',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Telefono'),
        ),
    ]
