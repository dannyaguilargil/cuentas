# Generated by Django 4.1.4 on 2023-04-17 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0019_alter_usolicitudes_options_alter_usolicitudes_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_usuarios.usuario'),
        ),
    ]