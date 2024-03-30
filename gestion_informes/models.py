from django.db import models

# Create your models here.
class entecontrol(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name='Nombre ente de control')
    descripcion = models.CharField(max_length=40, verbose_name='Descripcion ente de control', blank=True, null=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    ## agregando esto para mostrarlo por nombre en el panel de admin
    def __str__(self):
        return self.nombre

class dependencia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name='Nombre dependencia')
    responsable = models.CharField(max_length=200, verbose_name='Nombre del responsable')
    correoresponsable = models.CharField(max_length=200, verbose_name='Correo del responsable')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
    
###informes ###

def obtener_archivo_predeterminado():
    return 'pdfs/'


class informe(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name='Nombre del informe')
    slug = models.SlugField(max_length=200, verbose_name='Slug del informe', unique=True)
    entecontrol=models.ForeignKey(entecontrol,null=True,blank=True,on_delete=models.CASCADE) ##ente de control
    normativa = models.FileField(upload_to='pdfs/', default=obtener_archivo_predeterminado, verbose_name='Normativa')
    dependencia=models.ForeignKey(dependencia,null=True,blank=True,on_delete=models.CASCADE) ##dependencia
    ## por ahora la fecha lo hare con varchar pero la modificare##
    fechaentregainicial = models.CharField(max_length=200, verbose_name='Fecha inicial de entrega')
    fechaentregapendiente = models.CharField(max_length=200, verbose_name='Fecha pendiente de entrega')
    ######## agregarle periodicidad dias y meses ############
    periodicidad = models.CharField(max_length=200, verbose_name='Periodicidad cantidad')
    periodicidadtipo = models.CharField(max_length=200, verbose_name='Tipo de periodicidad') #dias y meses
    totalentregas = models.IntegerField(verbose_name='Total de entregas')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    descripcion = models.CharField(max_length=1000, verbose_name='Descripcion del informe', blank=True, null=True)
