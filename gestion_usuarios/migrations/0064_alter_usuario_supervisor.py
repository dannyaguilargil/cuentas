# Generated by Django 4.1.4 on 2023-07-04 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_supervisor', '0006_rename_supervisore_supervisor'),
        ('gestion_usuarios', '0063_cuentacontratista_flujo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_supervisor.supervisor'),
        ),
    ]
