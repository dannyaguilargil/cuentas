from django.db import models
from gestion_usuarios.choices import sexos, rol, tipodocumento,sede,tiposolicitud,aplicativos
###voy a probar si se puede agregar una llave foranea desde otro modulo
from gestion_supervisor.models import supervisor
from gestion_usuarios.models import usuario
###voy a probar si se puede agregar una llave foranea desde otro modulo


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
    apicativo = models.CharField(max_length=40, verbose_name='Aplicativo', default='kubApp', choices=aplicativos) #choices
    observaciones = models.CharField(max_length=200, verbose_name='Observaciones', default='')
    observacionessupervisor = models.CharField(max_length=200, verbose_name='Observaciones del supervisor', default='')

### el paz y salvo debe ser una llave foranea de un un usuario registrado
class pazysalvo(models.Model):
    id = models.AutoField(primary_key=True)
    usuario=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)
    permisos = models.BooleanField(default=False)
    rfid = models.BooleanField(default=False, verbose_name='Tarjeta control de acceso')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.usuario.nombre

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
    def __str__(self):
        return self.nombre


# Create your models here.
class solicitudsistema(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre', null=True,blank=True)
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido', null=True,blank=True)
    cargo = models.CharField(max_length=40, verbose_name='Cargo') #cargo o numero de contrato
    email = models.CharField(max_length=40, verbose_name='Email')
    supervisor = models.ForeignKey(supervisor,null=False,blank=False,on_delete=models.CASCADE)
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
    fechafinalcontrato = models.DateField(verbose_name='Fecha final del contrato', null=True,blank=True)
    ############## SISTEMA DE INFORMACION REQUERIDO #########################
    tiposolicitud = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default='Consultar', choices=tiposolicitud)
    #apicativo = models.CharField(max_length=40, verbose_name='Aplicativo', default='kubApp', choices=aplicativos) #choices
    ###################################################
    aplicativo=models.ForeignKey(aplicativo,null=True,blank=True,on_delete=models.CASCADE)
    modulo=models.ForeignKey(modulo,null=True,blank=True,on_delete=models.CASCADE)
    ########################################
    observaciones = models.CharField(max_length=40, verbose_name='Observaciones', default='')
    ###########5  veces los aplicativos #### para realizar varias solicitudes
    #tiposolicitud1 = models.CharField(max_length=40, verbose_name='Tipo de solicitud 2', null=True, blank=True, choices=tiposolicitud, default='Consultar') #choices
    #aplicativo1=models.ForeignKey(aplicativo,null=True,blank=True,on_delete=models.CASCADE)
    #observaciones1 = models.CharField(max_length=40, verbose_name='Observaciones 2', null=True, blank=True)
    #tiposolicitud2 = models.CharField(max_length=40, verbose_name='Tipo de solicitud 3', null=True, blank=True, choices=tiposolicitud, default='Consultar') 
    #aplicativo2 = models.CharField(max_length=40, verbose_name='Aplicativo 3', default='kubApp', choices=aplicativos, null=True, blank=True) #choices
    #observaciones2 = models.CharField(max_length=40, verbose_name='Observaciones', null=True, blank=True)
    #tiposolicitud3 = models.CharField(max_length=40, verbose_name='Tipo de solicitud 4', default='Consultar', null=True)
    #aplicativo3 = models.CharField(max_length=40, verbose_name='Aplicativo', default='kubApp', choices=aplicativo, null=True) 
    #observaciones3 = models.CharField(max_length=40, verbose_name='Observaciones', null=True, blank=True)
    #tiposolicitud4 = models.CharField(max_length=40, verbose_name='Tipo de solicitud 5', default='Consultar', null=True)
    #aplicativo4 = models.CharField(max_length=40, verbose_name='Aplicativo', default='kubApp', choices=aplicativo, null=True)
    #observaciones4 = models.CharField(max_length=40, verbose_name='Observaciones', null=True, blank=True)




   
  