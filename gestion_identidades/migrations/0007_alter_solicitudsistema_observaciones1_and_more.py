# Generated by Django 5.0.3 on 2024-03-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0006_alter_solicitudsistema_aplicativo1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudsistema',
            name='observaciones1',
            field=models.CharField(max_length=40, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='observaciones2',
            field=models.CharField(max_length=40, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='observaciones3',
            field=models.CharField(max_length=40, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='observaciones4',
            field=models.CharField(max_length=40, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='observaciones5',
            field=models.CharField(max_length=40, null=True, verbose_name='Observaciones'),
        ),
    ]