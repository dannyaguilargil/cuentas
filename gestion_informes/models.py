from django.db import models
from gestion_usuarios.choices import periodicidadtipo

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
    #slug = models.SlugField(max_length=200, verbose_name='Slug del informe', unique=True)
    entecontrol=models.ForeignKey(entecontrol,null=True,blank=True,on_delete=models.CASCADE) ##ente de control
    normativa = models.FileField(upload_to='pdfs/', default=obtener_archivo_predeterminado, verbose_name='Normativa')
    dependencia=models.ForeignKey(dependencia,null=True,blank=True,on_delete=models.CASCADE) ##dependencia
    descripcion = models.CharField(max_length=1000, verbose_name='Descripcion del informe', blank=True, null=True)
    ## por ahora la fecha lo hare con varchar pero la modificare##
    fechaentregainicial = models.DateField(verbose_name='Fecha inicial de entrega', null=True,blank=True)##debe ser obligatorio
    fechaentregapendiente = models.DateField(verbose_name='Fecha pendiente de entrega',null=True,blank=True)
    ######## agregarle periodicidad dias y meses ############
    periodicidad = models.IntegerField(verbose_name='Periodicidad cantidad', null=True,blank=True) #debe ser obligatorio
    periodicidadtipo = models.CharField(max_length=200, verbose_name='Tipo de periodicidad', choices=periodicidadtipo) #dias y meses
    totalentregas = models.IntegerField(verbose_name='Total de entregas', null=True,blank=True, default="10000")#debe ser obligatorio
    alarmas = models.IntegerField(verbose_name='Dias de anticipacion de alarma', null=True,blank=True) #ejemplo con una debo permtir por ahi tres
    alarmas2 = models.IntegerField(verbose_name='Segunda alarma', null=True,blank=True)
    alarmas3 = models.IntegerField(verbose_name='Tercera alarma', null=True,blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre


class alarma(models.Model):
    id = models.AutoField(primary_key=True)
    informe=models.ForeignKey(informe,null=True,blank=True,on_delete=models.CASCADE) ##informe
    dias = models.IntegerField(verbose_name='Dias de anticipacion alarma')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)


class entrega(models.Model):
    id = models.AutoField(primary_key=True)
    informe=models.ForeignKey(informe,null=True,blank=True,on_delete=models.CASCADE) ##informe
    fecha = models.DateField(verbose_name='Fecha de entrega', null=True,blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self): ##falta hacer validacion cuando no hay entrega
        return f"{self.informe.nombre} / {self.fecha}"


class evidencia(models.Model):
    id = models.AutoField(primary_key=True)
    entrega=models.ForeignKey(entrega,null=True,blank=True,on_delete=models.CASCADE) ##informe
    nombre = models.CharField(max_length=200, verbose_name='Nombre', null=True,blank=True)##lo tomare como observaciones
    archivo = models.FileField(upload_to='pdfs/', default=obtener_archivo_predeterminado, verbose_name='Archivo de evidencia')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

