# Generated by Django 5.0.3 on 2024-09-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0022_alter_solicitudsistema_cargo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudsistema',
            name='sede',
            field=models.CharField(blank=True, choices=[('ADMINISTRATIVA', 'Administrativa'), ('UBA PBL', 'UBA Puente barco leones'), ('UBA LIBERTAD', 'UBA Libertad'), ('UBA COMUNEROS', 'UBA Comuneros'), ('UBA AGUA CLARA', 'UBA Agua clara'), ('UBA LOMA DE BOLIVAR', 'UBA Loma de bolivar'), ('UBA POLICLINICO', 'UBA Policlinico')], default='Administrativa', max_length=80, null=True, verbose_name='Sede'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='tipodocumento',
            field=models.CharField(blank=True, choices=[('CC', 'Cedula de ciudadania'), ('PASAPORTE', 'Pasaporte'), ('CE', 'Cedula de extranjeria')], default='CC', max_length=40, null=True, verbose_name='Tipo de documento'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='tiposolicitud',
            field=models.CharField(blank=True, choices=[('CREAR', 'Crear'), ('ACTUALIZAR', 'Actualizar'), ('ELIMINAR', 'Eliminar'), ('CONSULTAS', 'Consultas')], default='Consultar', max_length=40, null=True, verbose_name='Tipo de solicitud'),
        ),
    ]
