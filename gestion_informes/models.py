from django.db import models

# Create your models here.
class entecontrol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name='Nombre ente de control')
    descripcion = models.CharField(max_length=40, verbose_name='Descripcion ente de control', blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

class dependencia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name='Nombre dependencia')
    responsable = models.CharField(max_length=200, verbose_name='Nombre del responsable')
    correoresponsable = models.CharField(max_length=200, verbose_name='Correo del responsable')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    