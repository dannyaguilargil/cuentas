from django.db import models
from gestion_usuarios.choices import sexos, rol, tipodocumento
from django.contrib.auth.models import User

class cuentasupervisor(models.Model):
    ############REVISAR QUE TENGAN LOS MISMOS DATOS QUE EL ANTERIOR##############################
    nombre = models.CharField(max_length=40, verbose_name='Primer nombre', default="No asignado")
    #segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre')
    #primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    #segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido')
    #email = models.CharField(max_length=40, verbose_name='Email')
    #supervisor = models.CharField(max_length=40, verbose_name='Supervisor')
    #tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento',choices=tipodocumento, default='CC')
    #cedula = models.IntegerField(verbose_name='Cedula')#llevarlo por id de cuenta y relacionarlo con usuario
    #dependencia = models.CharField(max_length=40, verbose_name='Dependencia')
    #sexo = models.CharField(max_length=40, verbose_name='Sexo', choices=sexos, default='F')
    #gestion de contratacion, tener en cuenta el pdf
    #numero = models.IntegerField(verbose_name='Numero del contrato')
    #objeto = models.CharField(max_length=300, verbose_name='Objeto') # este objeto de contrato debe remplazar al cargo en usuario
    #fechaperfeccionamiento = models.CharField(max_length=300, verbose_name='Fecha de perfeccionamiento')
    #valor = models.CharField(max_length=300, verbose_name='Valor del contrato')
    #fechacontrato = models.CharField(max_length=40, verbose_name='Fecha del contrato')
    #fechaterminacion = models.CharField(max_length=40, verbose_name='Fecha final del contrato')
    #duracion = models.CharField(max_length=40, verbose_name='Duracion del contrato')
    #gestion de contratacion, tener en cuenta el pdf
    #gestion de rp, tener en cuenta el pdf
    #numerorp = models.IntegerField(verbose_name='Numero del rp')
    #fecharp = models.CharField(max_length=40, verbose_name='Fecha del rp')
    #gestion de rp, tener en cuenta el pdf
    #gestion de acta de inicio, tener en cuenta el pdf
    #numeroactainicio = models.IntegerField(verbose_name='Numero proceso del acta de inicio')
    #fechaactainicio = models.CharField(max_length=300, verbose_name='Fecha de acta de inicio')
    #gestiones del supervisor
    #radicado = models.CharField(max_length=40, verbose_name='Radicado')
    #validacionsupervisor = models.CharField(max_length=40, verbose_name='Validacion de la cuenta')
    #observacionessupervisor = models.CharField(max_length=40, verbose_name='Observaciones de la cuenta')
    #gestiones del supervisor
    
class cuentasupervisorcontratista(models.Model):
    nombrecompleto = models.CharField(max_length=80, verbose_name='Nombre completo', default='No asignado')
    cedula = models.IntegerField(verbose_name='Cedula', default=1)
    objetocontrato = models.CharField(max_length=200, verbose_name='Objeto del contrato', default='No asignado')
    #radicado = models.CharField(max_length=80, verbose_name='Radicado', default='No asignado')
    ##POR AHORA TOMARE EL ID PERO QUEDA PENDIENTE EL RADICADO
    archivo = models.CharField(max_length=200, verbose_name='Pdf del formato de actividades', default='pdfs/NOCARGADO') #ESTE ES EL PDF DE ACTIVIDADES
    pdfplanilla = models.CharField(max_length=200, verbose_name='Pdf de la planilla', default='pdfs/NOCARGADO')
    
class supervisor(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario', default=2)
    cedula = models.IntegerField(primary_key=True, verbose_name='Cédula')
    cargo = models.CharField(max_length=120, verbose_name='Cargo', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usuario.get_full_name()  # Muestra el nombre completo del usuario