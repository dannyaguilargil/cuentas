# Generated by Django 5.0.3 on 2024-03-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_identidades', '0005_solicitudsistema_aplicativo1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudsistema',
            name='aplicativo1',
            field=models.CharField(choices=[('KUBAPP', 'kubApp'), ('TNS', 'TNS'), ('ALMERA', 'Almera'), ('HICKCENTRAL', 'Hickcentral')], default='kubApp', max_length=40, null=True, verbose_name='Aplicativo'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='aplicativo2',
            field=models.CharField(choices=[('KUBAPP', 'kubApp'), ('TNS', 'TNS'), ('ALMERA', 'Almera'), ('HICKCENTRAL', 'Hickcentral')], default='kubApp', max_length=40, null=True, verbose_name='Aplicativo'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='aplicativo3',
            field=models.CharField(choices=[('KUBAPP', 'kubApp'), ('TNS', 'TNS'), ('ALMERA', 'Almera'), ('HICKCENTRAL', 'Hickcentral')], default='kubApp', max_length=40, null=True, verbose_name='Aplicativo'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='aplicativo4',
            field=models.CharField(choices=[('KUBAPP', 'kubApp'), ('TNS', 'TNS'), ('ALMERA', 'Almera'), ('HICKCENTRAL', 'Hickcentral')], default='kubApp', max_length=40, null=True, verbose_name='Aplicativo'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='aplicativo5',
            field=models.CharField(choices=[('KUBAPP', 'kubApp'), ('TNS', 'TNS'), ('ALMERA', 'Almera'), ('HICKCENTRAL', 'Hickcentral')], default='kubApp', max_length=40, null=True, verbose_name='Aplicativo'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='observaciones1',
            field=models.CharField(default='', max_length=40, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='observaciones2',
            field=models.CharField(default='', max_length=40, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='observaciones3',
            field=models.CharField(default='', max_length=40, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='observaciones4',
            field=models.CharField(default='', max_length=40, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='observaciones5',
            field=models.CharField(default='', max_length=40, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='tiposolicitud1',
            field=models.CharField(default='Consultar', max_length=40, null=True, verbose_name='Tipo de solicitud'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='tiposolicitud2',
            field=models.CharField(default='Consultar', max_length=40, null=True, verbose_name='Tipo de solicitud'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='tiposolicitud3',
            field=models.CharField(default='Consultar', max_length=40, null=True, verbose_name='Tipo de solicitud'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='tiposolicitud4',
            field=models.CharField(default='Consultar', max_length=40, null=True, verbose_name='Tipo de solicitud'),
        ),
        migrations.AlterField(
            model_name='solicitudsistema',
            name='tiposolicitud5',
            field=models.CharField(default='Consultar', max_length=40, null=True, verbose_name='Tipo de solicitud'),
        ),
    ]
