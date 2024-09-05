# Generated by Django 5.0.3 on 2024-08-29 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0018_alter_solicitudsistema_supervisor'),
        ('gestion_usuarios', '0068_alter_usolicitudes_supervisor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pazysalvo',
            name='cedula',
        ),
        migrations.AddField(
            model_name='pazysalvo',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.usuario'),
        ),
    ]