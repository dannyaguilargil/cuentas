# Generated by Django 5.0.3 on 2024-04-10 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0008_alter_solicitudsistema_observaciones1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='solicitudsistemasupervisor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, verbose_name='Primer nombre')),
                ('segundonombre', models.CharField(max_length=40, verbose_name='Segundo nombre')),
                ('primerapellido', models.CharField(max_length=40, verbose_name='Primer apellido')),
                ('segundoapellido', models.CharField(max_length=40, verbose_name='Segundo apellido')),
                ('cargo', models.CharField(max_length=40, verbose_name='Cargo')),
                ('email', models.CharField(max_length=40, verbose_name='Email')),
                ('supervisor', models.CharField(default='', max_length=40, verbose_name='Supervisor')),
                ('tipodocumento', models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('PASAPORTE', 'Pasaporte'), ('CE', 'Cedula de extranjeria')], default='CC', max_length=40, verbose_name='Tipo de documento')),
                ('cedula', models.IntegerField(verbose_name='Cedula')),
                ('lugarexpedicion', models.CharField(max_length=40, verbose_name='Lugar de expedicion')),
                ('dependencia', models.CharField(max_length=40, verbose_name='Dependencia')),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=40, verbose_name='Sexo')),
                ('telefono', models.CharField(default='', max_length=40, verbose_name='Telefono')),
                ('celular', models.CharField(default='', max_length=40, verbose_name='Celular')),
                ('direccion', models.CharField(default='', max_length=40, verbose_name='Direccion')),
                ('sede', models.CharField(choices=[('ADMINISTRATIVA', 'Sede administrativa'), ('UBA PBL', 'UBA Puente barco leones'), ('UBA LIBERTAD', 'UBA Libertad'), ('UBA COMUNEROS', 'UBA Comuneros'), ('UBA AGUA CLARA', 'UBA Agua clara'), ('UBA LOMA DE BOLIVAR', 'UBA Loma de bolivar'), ('UBA POLICLINICO', 'UBA Policlinico')], default='Administrativa', max_length=80, verbose_name='Sede')),
                ('fechafinalcontrato', models.CharField(default='', max_length=40, verbose_name='Fecha final del contrato')),
                ('tiposolicitud', models.CharField(choices=[('CREAR', 'Crear'), ('ACTUALIZAR', 'Actualizar'), ('ELIMINAR', 'Eliminar'), ('CONSULTAS', 'Consultas')], default='Consultar', max_length=40, verbose_name='Tipo de solicitud')),
                ('aplicativo', models.CharField(choices=[('KUBAPP', 'kubApp'), ('TNS', 'TNS'), ('ALMERA', 'Almera'), ('HICKCENTRAL', 'Hickcentral')], default='kubApp', max_length=40, verbose_name='Aplicativo')),
                ('observaciones', models.CharField(default='', max_length=200, verbose_name='Observaciones')),
                ('observacionessupervisor', models.CharField(default='', max_length=200, verbose_name='Observaciones')),
            ],
        ),
    ]
