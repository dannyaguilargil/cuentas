# Generated by Django 5.0.3 on 2024-10-03 22:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_informes', '0017_alter_informe_totalentregas'),
        ('gestion_supervisor', '0010_alter_supervisor_usuario'),
        ('gestion_usuarios', '0074_alter_usuario_email_alter_usuario_rol'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cargo',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='dependencia',
            field=models.ForeignKey(blank=True, max_length=40, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_informes.dependencia', verbose_name='dependencia'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, max_length=40, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='lugarexpedicion',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Lugar de expedicion'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='primerapellido',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Primer apellido'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('admin_identidadades', 'Administrador de identidades'), ('supervisor', 'Supervisor'), ('identidades', 'Usuario final de identidades'), ('informes', 'ente de control (informes)'), ('super_admin_identidades', 'Super admin de identidades'), ('admin_sara', 'Administrador de SARA')], default='identidades', max_length=40, verbose_name='Rol'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='supervisor',
            field=models.ForeignKey(blank=True, max_length=40, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisor_detail', to='gestion_supervisor.supervisor', verbose_name='supervisor'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
