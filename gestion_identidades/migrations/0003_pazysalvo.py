# Generated by Django 5.0.3 on 2024-03-20 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0002_alter_solicitudsistema_apicativo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='pazysalvo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cedula', models.IntegerField(verbose_name='Cedula')),
                ('permisos', models.BooleanField(default=False)),
                ('rfid', models.BooleanField(default=False)),
            ],
        ),
    ]
