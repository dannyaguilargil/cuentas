# Generated by Django 4.1.4 on 2023-04-17 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0023_actainicio_usuario_actapago_usuario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='cuentausuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, verbose_name='Primer nombre')),
                ('segundonombre', models.CharField(max_length=40, verbose_name='Segundo nombre')),
                ('primerapellido', models.CharField(max_length=40, verbose_name='Primer apellido')),
                ('segundoapellido', models.CharField(max_length=40, verbose_name='Segundo apellido')),
                ('email', models.CharField(max_length=40, verbose_name='Email')),
                ('supervisor', models.CharField(max_length=40, verbose_name='Supervisor')),
                ('tipodocumento', models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('PASAPORTE', 'Pasaporte'), ('CE', 'Cedula de extranjeria')], default='CC', max_length=40, verbose_name='Tipo de documento')),
                ('cedula', models.IntegerField(verbose_name='Cedula')),
                ('dependencia', models.CharField(max_length=40, verbose_name='Dependencia')),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=40, verbose_name='Sexo')),
                ('numero', models.IntegerField(verbose_name='Numero del contrato')),
                ('objeto', models.CharField(max_length=300, verbose_name='Objeto')),
                ('fechaperfeccionamiento', models.CharField(max_length=300, verbose_name='Fecha de perfeccionamiento')),
                ('valor', models.CharField(max_length=300, verbose_name='Valor del contrato')),
                ('fechacontrato', models.CharField(max_length=40, verbose_name='Fecha del contrato')),
                ('fechaterminacion', models.CharField(max_length=40, verbose_name='Fecha final del contrato')),
                ('duracion', models.CharField(max_length=40, verbose_name='Duracion del contrato')),
                ('numerorp', models.IntegerField(verbose_name='Numero del rp')),
                ('fecharp', models.CharField(max_length=40, verbose_name='Fecha del rp')),
                ('numeroactainicio', models.IntegerField(verbose_name='Numero del proceso del acta de inicio')),
                ('fechaactainicio', models.CharField(max_length=300, verbose_name='Fecha de acta de inicio')),
            ],
        ),
        migrations.AlterField(
            model_name='usolicitudes',
            name='tipodocumento',
            field=models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('PASAPORTE', 'Pasaporte'), ('CE', 'Cedula de extranjeria')], default='CC', max_length=40, verbose_name='Tipo de documento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('CONTRATISTA', 'Contratista'), ('SUPERVISOR', 'Supervisor'), ('GESCON', 'Gescon'), ('PRESUPUESTO', 'Presupuesto'), ('TESORERIA', 'Tesoreria'), ('ADMINISTRADOR', 'Administrador')], default='CONTRATISTA', max_length=40, verbose_name='Rol'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipodocumento',
            field=models.CharField(choices=[('CC', 'Cedula de ciudadania'), ('PASAPORTE', 'Pasaporte'), ('CE', 'Cedula de extranjeria')], default='CC', max_length=40, verbose_name='Tipo de documento'),
        ),
    ]