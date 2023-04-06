from django.db import models


# Create your models here.
#class solicitud_usuario(models.Model):
#    nombre = models.CharField(max_length=40)
#    segundonombre = models.CharField(max_length=40)
#    primerapellido = models.CharField(max_length=40)
#    segundoapellido = models.CharField(max_length=40)
#    cargo = models.CharField(max_length=40)
#    email = models.CharField(max_length=40)
#    supervisor = models.CharField(max_length=40)
#    tipodocumento = models.CharField(max_length=40)
#    cedula = models.IntegerField(primary_key=True)
       
#    class Meta:
#        db_table = 'usolicitud'   
       
#    def __str__(self):
#        return 'SOLICITUD DE USUARIO: ' + self.nombre + ' ' + self.primerapellido
      
       
#QUIERO HACER LA PARTE PRIMERO DE MOSTRAR LOS USUARIOS REGISTRADOS Y INCLUIR USUARIOS REGISTRADOS EN EL ADMIN
class usuario(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre')
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido')
    cargo = models.CharField(max_length=40, verbose_name='Cargo')
    email = models.CharField(max_length=40, verbose_name='Email')
    supervisor = models.CharField(max_length=40, verbose_name='Supervisor')
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento')
    cedula = models.IntegerField(primary_key=True, verbose_name='Cedula')
    ##hast aqui va el de usuarios registrados
    lugarexpedicion = models.CharField(max_length=40, verbose_name='Lugar de expedicion')
    dependencia = models.CharField(max_length=40, verbose_name='Dependencia')
    sexo = models.CharField(max_length=40, verbose_name='Sexo')
    usuario = models.CharField(max_length=40, verbose_name='Usuario')
    contrasena = models.CharField(max_length=40, verbose_name='Contrasena')
    rol = models.CharField(max_length=40, verbose_name='Rol')
    

    def __str__(self):
        return 'USUARIO: ' + self.nombre + ' ' + self.primerapellido
    
    
class prueba(models.Model):
    nombre = models.CharField(max_length=40)
    cedula = models.IntegerField(primary_key=True)
    
    
class usolicitudes(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre')
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido')
    cargo = models.CharField(max_length=40, verbose_name='Cargo')
    email = models.CharField(max_length=40, verbose_name='Email')
    supervisor = models.CharField(max_length=40, verbose_name='Supervisor')
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento')
    cedula = models.IntegerField(primary_key=True, verbose_name='Cedula')

       
    def __str__(self):
        return 'SOLICITUD DE USUARIO: ' + self.nombre + ' ' + self.primerapellido
    
#por ahora solo quiero hacer registros pero debo referenciarlo con llave foranea
class contrato(models.Model):
    numero = models.IntegerField(primary_key=True, verbose_name='Numero')
    numeroproceso = models.IntegerField(verbose_name='Numero de proceso')
    objeto = models.CharField(max_length=300, verbose_name='Objeto')
    #fechasuscripcion = models.CharField(max_length=300, verbose_name='Fecha de suscripcion')
    fechaperfeccionamiento = models.CharField(max_length=300, verbose_name='Fecha de perfeccionamiento')
    valor = models.CharField(max_length=300, verbose_name='Valor del contrato')
    fechacontrato = models.CharField(max_length=300, verbose_name='Fecha del contrato')
    fechaterminacion = models.CharField(max_length=300, verbose_name='Fecha final del contrato')
    duracion = models.CharField(max_length=40, verbose_name='Duracion del contrato')
    #pendiente asignar llave foranea aqui
    def __str__(self):
        return 'CONTRATO: '+self.objeto
    
class rp(models.Model):
    numero = models.IntegerField(primary_key=True, verbose_name='Numero del rp')
    fecha = models.CharField(max_length=300, verbose_name='Fecha del rp')
    duracion = models.CharField(max_length=40, verbose_name='Duracion del contrato')
    valor = models.CharField(max_length=300, verbose_name='Valor del contrato')
    #pendiente asignar llave foranea aqui
    def __str__(self):
        return 'REGISTRO PRESUPUESTAL: '+self.fecha