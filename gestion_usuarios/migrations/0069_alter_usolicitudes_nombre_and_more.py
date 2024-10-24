# Generated by Django 5.0.3 on 2024-09-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0068_alter_usolicitudes_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usolicitudes',
            name='nombre',
            field=models.CharField(max_length=40, verbose_name='Primer nombre'),
        ),
        migrations.AlterField(
            model_name='usolicitudes',
            name='segundoapellido',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Segundo apellido'),
        ),
        migrations.AlterField(
            model_name='usolicitudes',
            name='segundonombre',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Segundo nombre'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='segundoapellido',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Segundo apellido'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='segundonombre',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Segundo nombre'),
        ),
    ]