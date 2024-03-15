from django.db import models
from gestion_usuarios.choices import sexos, rol, tipodocumento,sede,tiposolicitud,aplicativo

# Create your models here.
class solicitudsistema(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre')
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido')
    cargo = models.CharField(max_length=40, verbose_name='Cargo') #cargo o numero de contrato
    email = models.CharField(max_length=40, verbose_name='Email')
    supervisor = models.CharField(max_length=40, verbose_name='Supervisor', default='')
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento',choices=tipodocumento, default='CC')
    ####################################################
    cedula = models.IntegerField(max_length=40, verbose_name='Cedula')
    ##hast aqui va el de usuarios registrados
    lugarexpedicion = models.CharField(max_length=40, verbose_name='Lugar de expedicion')
    dependencia = models.CharField(max_length=40, verbose_name='Dependencia')
    sexo = models.CharField(max_length=40, verbose_name='Sexo', choices=sexos, default='F')
    usuario = models.CharField(max_length=40, verbose_name='Usuario')
    contrasena = models.CharField(max_length=40, verbose_name='Contrasena')
    telefono = models.CharField(max_length=40, verbose_name='Telefono' ,default="")
    direccion = models.CharField(max_length=40, verbose_name='Direccion', default='')
    #######################################################################
    sede = models.CharField(max_length=40, verbose_name='Sede', default='Administrativa') #choices
    fechafinalcontrato = models.CharField(max_length=40, verbose_name='Fecha final del contrato', default='')
    ############## SISTEMA DE INFORMACION REQUERIDO #########################
    tiposolicitud = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default='Consultar') #choices
    apicativo = models.CharField(max_length=40, verbose_name='Aplicativo', default='kubApp') #choices
    observaciones = models.CharField(max_length=40, verbose_name='Observaciones', default='')

   
  