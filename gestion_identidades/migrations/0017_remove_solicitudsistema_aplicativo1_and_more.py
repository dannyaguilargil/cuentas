# Generated by Django 5.0.3 on 2024-08-27 13:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0016_remove_solicitudsistema_apicativo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudsistema',
            name='aplicativo1',
        ),
        migrations.RemoveField(
            model_name='solicitudsistema',
            name='aplicativo2',
        ),
        migrations.RemoveField(
            model_name='solicitudsistema',
            name='observaciones1',
        ),
        migrations.RemoveField(
            model_name='solicitudsistema',
            name='observaciones2',
        ),
        migrations.AddField(
            model_name='pazysalvo',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='pazysalvo',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitudsistema',
            name='modulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_identidades.modulo'),
        ),
    ]