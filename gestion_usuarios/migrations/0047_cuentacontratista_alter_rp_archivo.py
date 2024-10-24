# Generated by Django 4.1.4 on 2023-06-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_usuarios', '0046_alter_rp_archivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='cuentacontratista',
            fields=[
                ('numeroplanilla', models.IntegerField(primary_key=True, serialize=False, verbose_name='Numero de planilla')),
                ('actividades', models.FileField(default='No', upload_to='pdfs/', verbose_name='actividades')),
            ],
        ),
        migrations.AlterField(
            model_name='rp',
            name='archivo',
            field=models.FileField(default='No cargado', upload_to='pdfs/', verbose_name='archivo'),
        ),
    ]
