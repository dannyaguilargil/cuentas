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
    cedula = models.IntegerField(verbose_name='Cedula')
    ##hast aqui va el de usuarios registrados
    lugarexpedicion = models.CharField(max_length=40, verbose_name='Lugar de expedicion')
    dependencia = models.CharField(max_length=40, verbose_name='Dependencia')
    sexo = models.CharField(max_length=40, verbose_name='Sexo', choices=sexos, default='F')
    #usuario = models.CharField(max_length=40, verbose_name='Usuario')
    #contrasena = models.CharField(max_length=40, verbose_name='Contrasena')
    telefono = models.CharField(max_length=40, verbose_name='Telefono' ,default="")
    celular = models.CharField(max_length=40, verbose_name='Celular' ,default="")
    direccion = models.CharField(max_length=40, verbose_name='Direccion', default='')
    #######################################################################
    sede = models.CharField(max_length=80, verbose_name='Sede', default='Administrativa' , choices=sede) #choices
    fechafinalcontrato = models.CharField(max_length=40, verbose_name='Fecha final del contrato', default='')
    ############## SISTEMA DE INFORMACION REQUERIDO #########################
    tiposolicitud = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default='Consultar', choices=tiposolicitud) #choices
    apicativo = models.CharField(max_length=40, verbose_name='Aplicativo', default='kubApp', choices=aplicativo) #choices
    observaciones = models.CharField(max_length=40, verbose_name='Observaciones', default='')
    ###########5  veces los aplicativos #### para realizar varias solicitudes
    tiposolicitud1 = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default='Consultar', null=True) #choices
    aplicativo1 = models.CharField(max_length=40, verbose_name='Aplicativo', default='kubApp', choices=aplicativo, null=True) #choices
    observaciones1 = models.CharField(max_length=40, verbose_name='Observaciones', null=True, blank=True)
    tiposolicitud2 = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default='Consultar', null=True) 
    aplicativo2 = models.CharField(max_length=40, verbose_name='Aplicativo', default='kubApp', choices=aplicativo, null=True)
    observaciones2 = models.CharField(max_length=40, verbose_name='Observaciones', null=True, blank=True)
    tiposolicitud3 = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default='Consultar', null=True)
    aplicativo3 = models.CharField(max_length=40, verbose_name='Aplicativo', default='kubApp', choices=aplicativo, null=True) 
    observaciones3 = models.CharField(max_length=40, verbose_name='Observaciones', null=True, blank=True)
    tiposolicitud4 = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default='Consultar', null=True)
    aplicativo4 = models.CharField(max_length=40, verbose_name='Aplicativo', default='kubApp', choices=aplicativo, null=True)
    observaciones4 = models.CharField(max_length=40, verbose_name='Observaciones', null=True, blank=True)
    tiposolicitud5 = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default='Consultar', null=True) 
    aplicativo5 = models.CharField(max_length=40, verbose_name='Aplicativo', default='kubApp', choices=aplicativo, null=True) 
    observaciones5 = models.CharField(max_length=40, verbose_name='Observaciones', null=True, blank=True)

### se repite el proceso para que cambie de flujo de contratista a supervisor ###
class solicitudsistemasupervisor(models.Model):
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
    cedula = models.IntegerField(verbose_name='Cedula')
    ##hast aqui va el de usuarios registrados
    lugarexpedicion = models.CharField(max_length=40, verbose_name='Lugar de expedicion')
    dependencia = models.CharField(max_length=40, verbose_name='Dependencia')
    sexo = models.CharField(max_length=40, verbose_name='Sexo', choices=sexos, default='F')
    #usuario = models.CharField(max_length=40, verbose_name='Usuario')
    #contrasena = models.CharField(max_length=40, verbose_name='Contrasena')
    telefono = models.CharField(max_length=40, verbose_name='Telefono' ,default="")
    celular = models.CharField(max_length=40, verbose_name='Celular' ,default="")
    direccion = models.CharField(max_length=40, verbose_name='Direccion', default='')
    #######################################################################
    sede = models.CharField(max_length=80, verbose_name='Sede', default='Administrativa' , choices=sede) #choices
    fechafinalcontrato = models.CharField(max_length=40, verbose_name='Fecha final del contrato', default='')
    ############## SISTEMA DE INFORMACION REQUERIDO #########################
    tiposolicitud = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default='Consultar', choices=tiposolicitud) #choices
    apicativo = models.CharField(max_length=40, verbose_name='Aplicativo', default='kubApp', choices=aplicativo) #choices
    observaciones = models.CharField(max_length=200, verbose_name='Observaciones', default='')
    observacionessupervisor = models.CharField(max_length=200, verbose_name='Observaciones del supervisor', default='')


class pazysalvo(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.IntegerField(verbose_name='Cedula')
    permisos = models.BooleanField(default=False)
    rfid = models.BooleanField(default=False)

class aplicativo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, verbose_name='Nombre del aplicativo')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre


class modulo(models.Model):
    id = models.AutoField(primary_key=True)
    aplicativo=models.ForeignKey(aplicativo,null=True,blank=True,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, verbose_name='Nombre del modulo')
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)



   
  