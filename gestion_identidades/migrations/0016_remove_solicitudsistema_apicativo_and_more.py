# Generated by Django 5.0.3 on 2024-08-26 23:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0015_remove_solicitudsistema_aplicativo3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudsistema',
            name='apicativo',
        ),
        migrations.RemoveField(
            model_name='solicitudsistema',
            name='tiposolicitud1',
        ),
        migrations.RemoveField(
            model_name='solicitudsistema',
            name='tiposolicitud2',
        ),
        migrations.AddField(
            model_name='solicitudsistema',
            name='aplicativo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_identidades.aplicativo'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='aplicativo1',
            field=models.CharField(blank=True, choices=[('KUBAPP', 'kubApp'), ('TNS', 'TNS'), ('ALMERA', 'Almera'), ('HICKCENTRAL', 'Hickcentral'), ('SARA', 'SARA'), ('ANNARLAB', 'ANNARLAB'), ('GLPI', 'Mesa de ayuda GLPI'), ('ORTHANC', 'ORTHANC'), ('NUBE', 'Nube'), ('ZIMBRA', 'email Zimbra')], default='kubApp', max_length=40, null=True, verbose_name='Aplicativo 2'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='aplicativo2',
            field=models.CharField(blank=True, choices=[('KUBAPP', 'kubApp'), ('TNS', 'TNS'), ('ALMERA', 'Almera'), ('HICKCENTRAL', 'Hickcentral'), ('SARA', 'SARA'), ('ANNARLAB', 'ANNARLAB'), ('GLPI', 'Mesa de ayuda GLPI'), ('ORTHANC', 'ORTHANC'), ('NUBE', 'Nube'), ('ZIMBRA', 'email Zimbra')], default='kubApp', max_length=40, null=True, verbose_name='Aplicativo 3'),
        ),
        migrations.AlterField(
            model_name='solicitudsistemasupervisor',
            name='apicativo',
            field=models.CharField(choices=[('KUBAPP', 'kubApp'), ('TNS', 'TNS'), ('ALMERA', 'Almera'), ('HICKCENTRAL', 'Hickcentral'), ('SARA', 'SARA'), ('ANNARLAB', 'ANNARLAB'), ('GLPI', 'Mesa de ayuda GLPI'), ('ORTHANC', 'ORTHANC'), ('NUBE', 'Nube'), ('ZIMBRA', 'email Zimbra')], default='kubApp', max_length=40, verbose_name='Aplicativo'),
        ),
    ]