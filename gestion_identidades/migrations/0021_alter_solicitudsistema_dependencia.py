# Generated by Django 5.0.3 on 2024-09-10 22:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0020_alter_pazysalvo_rfid_and_more'),
        ('gestion_informes', '0017_alter_informe_totalentregas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudsistema',
            name='dependencia',
            field=models.ForeignKey(max_length=40, on_delete=django.db.models.deletion.CASCADE, to='gestion_informes.dependencia', verbose_name='dependencia'),
        ),
    ]
