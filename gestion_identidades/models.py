from django.db import models
from gestion_usuarios.choices import sexos, rol, tipodocumento,sede,tiposolicitud,aplicativos
###voy a probar si se puede agregar una llave foranea desde otro modulo
from gestion_supervisor.models import supervisor
from gestion_usuarios.models import usuario
from gestion_informes.models import dependencia
###voy a probar si se puede agregar una llave foranea desde otro modulo




### el paz y salvo debe ser una llave foranea de un un usuario registrado
class pazysalvo(models.Model):
    id = models.AutoField(primary_key=True)
    usuario=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)
    permisos = models.BooleanField(default=False)
    rfid = models.BooleanField(default=False, verbose_name='Tarjeta control de acceso')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.usuario.nombre if self.usuario else "Sin usuario"

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
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido', )
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido', null=True,blank=True)
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento',choices=tipodocumento, default='CC')
    cedula = models.IntegerField(verbose_name='Cedula')
    lugarexpedicion = models.CharField(max_length=40, verbose_name='Lugar de expedicion', null=True,blank=True)
    sexo = models.CharField(max_length=40, verbose_name='Sexo', choices=sexos, default='F', null=True,blank=True)

    ####################################################
    telefono = models.CharField(max_length=40, verbose_name='Telefono' ,default="", null=True,blank=True)
    celular = models.CharField(max_length=40, verbose_name='Celular' ,default="", null=True,blank=True)
    direccion = models.CharField(max_length=40, verbose_name='Direccion', default='', null=True,blank=True)
    cargo = models.CharField(max_length=40, verbose_name='Cargo') #cargo o numero de contrato
    ##############################################################
    #######REVISAR
    email = models.CharField(max_length=40, verbose_name='Email')
    supervisor = models.ForeignKey(supervisor,on_delete=models.CASCADE, default=1)
    dependencia = models.ForeignKey(dependencia,max_length=40, verbose_name='dependencia',on_delete=models.CASCADE, default=1)
    sede = models.CharField(max_length=80, verbose_name='Sede', default=1 , choices=sede) #choices
    #######################################################################
    ubicacionlaboral = models.CharField(max_length=60, verbose_name='Ubicacion laboral', null=True,blank=True)
    fechafinalcontrato = models.DateField(verbose_name='Fecha final del contrato', null=True,blank=True)
    tarjetapf = models.CharField(max_length=60, verbose_name='Tarjeta profesional', null=True,blank=True)

    ############## SISTEMA DE INFORMACION REQUERIDO #########################
    tiposolicitud = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default=1, choices=tiposolicitud)
    aplicativo=models.ForeignKey(aplicativo, on_delete=models.CASCADE,default=1)
    modulo=models.ForeignKey(modulo,null=True,blank=True,on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=200, verbose_name='Observaciones', null=True,blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
   

### se repite el proceso para que cambie de flujo de contratista a supervisor ###
class solicitudsistemasupervisor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre', null=True,blank=True)
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido', null=True,blank=True )
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido', null=True,blank=True)
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento',choices=tipodocumento, default='CC', null=True,blank=True)
    cedula = models.IntegerField(verbose_name='Cedula', null=True,blank=True)
    lugarexpedicion = models.CharField(max_length=40, verbose_name='Lugar de expedicion', null=True,blank=True)
    sexo = models.CharField(max_length=40, verbose_name='Sexo', choices=sexos, default='F', null=True,blank=True)
    ####################################################
    telefono = models.CharField(max_length=40, verbose_name='Telefono' ,default="", null=True,blank=True)
    celular = models.CharField(max_length=40, verbose_name='Celular' ,default="", null=True,blank=True)
    direccion = models.CharField(max_length=40, verbose_name='Direccion', default='', null=True,blank=True)
    cargo = models.CharField(max_length=40, verbose_name='Cargo', null=True,blank=True) #cargo o numero de contrato
    ##############################################################
    #######REVISAR
    email = models.CharField(max_length=40, verbose_name='Email', null=True,blank=True)
    supervisor = models.ForeignKey(supervisor,on_delete=models.CASCADE, null=True,blank=True)
    dependencia = models.ForeignKey(dependencia,max_length=40, verbose_name='dependencia',on_delete=models.CASCADE, null=True,blank=True)
    sede = models.CharField(max_length=80, verbose_name='Sede', default='ADMINISTRATIVA' , choices=sede, null=True,blank=True) #choices
    #######################################################################
    ubicacionlaboral = models.CharField(max_length=60, verbose_name='Ubicacion laboral', null=True,blank=True)
    fechafinalcontrato = models.CharField(max_length=90,verbose_name='Fecha final del contrato', null=True,blank=True)
    tarjetapf = models.CharField(max_length=60, verbose_name='Tarjeta profesional', null=True,blank=True)
    ############## SISTEMA DE INFORMACION REQUERIDO #########################
    tiposolicitud = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default='Consultar', choices=tiposolicitud,null=True,blank=True)
    aplicativo=models.ForeignKey(aplicativo,null=True,blank=True,on_delete=models.CASCADE)
    modulo=models.ForeignKey(modulo,null=True,blank=True,on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=200, verbose_name='Observaciones', null=True,blank=True)
    observacionessup = models.CharField(max_length=200, verbose_name='Observaciones del supervisor', null=True,blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

class solicitudsistemaadmin(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre', null=True,blank=True)
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido', null=True,blank=True )
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido', null=True,blank=True)
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento',choices=tipodocumento, default='CC', null=True,blank=True)
    cedula = models.IntegerField(verbose_name='Cedula', null=True,blank=True)
    lugarexpedicion = models.CharField(max_length=40, verbose_name='Lugar de expedicion', null=True,blank=True)
    sexo = models.CharField(max_length=40, verbose_name='Sexo', choices=sexos, default='F', null=True,blank=True)
    ####################################################
    telefono = models.CharField(max_length=40, verbose_name='Telefono' ,default="", null=True,blank=True)
    celular = models.CharField(max_length=40, verbose_name='Celular' ,default="", null=True,blank=True)
    direccion = models.CharField(max_length=40, verbose_name='Direccion', default='', null=True,blank=True)
    cargo = models.CharField(max_length=40, verbose_name='Cargo', null=True,blank=True) #cargo o numero de contrato
    ##############################################################
    #######REVISAR
    email = models.CharField(max_length=40, verbose_name='Email', null=True,blank=True)
    supervisor = models.ForeignKey(supervisor,on_delete=models.CASCADE, null=True,blank=True)
    dependencia = models.ForeignKey(dependencia,max_length=40, verbose_name='dependencia',on_delete=models.CASCADE, null=True,blank=True)
    sede = models.CharField(max_length=80, verbose_name='Sede', default='ADMINISTRATIVA' , choices=sede, null=True,blank=True) #choices
    #######################################################################
    ubicacionlaboral = models.CharField(max_length=60, verbose_name='Ubicacion laboral', null=True,blank=True)
    fechafinalcontrato = models.CharField(max_length=90,verbose_name='Fecha final del contrato', null=True,blank=True)
    tarjetapf = models.CharField(max_length=60, verbose_name='Tarjeta profesional', null=True,blank=True)
    ############## SISTEMA DE INFORMACION REQUERIDO #########################
    tiposolicitud = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default='Consultar', choices=tiposolicitud,null=True,blank=True)
    aplicativo=models.ForeignKey(aplicativo,null=True,blank=True,on_delete=models.CASCADE)
    modulo=models.ForeignKey(modulo,null=True,blank=True,on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=200, verbose_name='Observaciones', null=True,blank=True)
    observacionessup = models.CharField(max_length=200, verbose_name='Observaciones del supervisor', null=True,blank=True)
    usuario = models.CharField(max_length=100, verbose_name='Usuario', null=True,blank=True)
    contrasena = models.CharField(max_length=100, verbose_name='Contraseña', null=True,blank=True)
    observacionesadm = models.CharField(max_length=200, verbose_name='Observaciones del administrador', null=True,blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

### se repite el proceso para que cambie de flujo de contratista a supervisor ###
class solicitudsistemarechazado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre', null=True,blank=True)
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido', null=True,blank=True )
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido', null=True,blank=True)
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento',choices=tipodocumento, default='CC', null=True,blank=True)
    cedula = models.IntegerField(verbose_name='Cedula', null=True,blank=True)
    lugarexpedicion = models.CharField(max_length=40, verbose_name='Lugar de expedicion', null=True,blank=True)
    sexo = models.CharField(max_length=40, verbose_name='Sexo', choices=sexos, default='F', null=True,blank=True)
    ####################################################
    telefono = models.CharField(max_length=40, verbose_name='Telefono' ,default="", null=True,blank=True)
    celular = models.CharField(max_length=40, verbose_name='Celular' ,default="", null=True,blank=True)
    direccion = models.CharField(max_length=40, verbose_name='Direccion', default='', null=True,blank=True)
    cargo = models.CharField(max_length=40, verbose_name='Cargo', null=True,blank=True) #cargo o numero de contrato
    ##############################################################
    #######REVISAR
    email = models.CharField(max_length=40, verbose_name='Email', null=True,blank=True)
    supervisor = models.ForeignKey(supervisor,on_delete=models.CASCADE, null=True,blank=True)
    dependencia = models.ForeignKey(dependencia,max_length=40, verbose_name='dependencia',on_delete=models.CASCADE, null=True,blank=True)
    sede = models.CharField(max_length=80, verbose_name='Sede', default='ADMINISTRATIVA' , choices=sede, null=True,blank=True) #choices
    #######################################################################
    ubicacionlaboral = models.CharField(max_length=60, verbose_name='Ubicacion laboral', null=True,blank=True)
    fechafinalcontrato = models.CharField(max_length=90,verbose_name='Fecha final del contrato', null=True,blank=True)
    tarjetapf = models.CharField(max_length=60, verbose_name='Tarjeta profesional', null=True,blank=True)
    ############## SISTEMA DE INFORMACION REQUERIDO #########################
    tiposolicitud = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default='Consultar', choices=tiposolicitud,null=True,blank=True)
    aplicativo=models.ForeignKey(aplicativo,null=True,blank=True,on_delete=models.CASCADE)
    modulo=models.ForeignKey(modulo,null=True,blank=True,on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=200, verbose_name='Observaciones', null=True,blank=True)
    observacionessup = models.CharField(max_length=200, verbose_name='Observaciones del supervisor', null=True,blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

class solicitudsistemarechazadoadm(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre', null=True,blank=True)
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido', null=True,blank=True )
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido', null=True,blank=True)
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento',choices=tipodocumento, default='CC', null=True,blank=True)
    cedula = models.IntegerField(verbose_name='Cedula', null=True,blank=True)
    lugarexpedicion = models.CharField(max_length=40, verbose_name='Lugar de expedicion', null=True,blank=True)
    sexo = models.CharField(max_length=40, verbose_name='Sexo', choices=sexos, default='F', null=True,blank=True)
    ####################################################
    telefono = models.CharField(max_length=40, verbose_name='Telefono' ,default="", null=True,blank=True)
    celular = models.CharField(max_length=40, verbose_name='Celular' ,default="", null=True,blank=True)
    direccion = models.CharField(max_length=40, verbose_name='Direccion', default='', null=True,blank=True)
    cargo = models.CharField(max_length=40, verbose_name='Cargo', null=True,blank=True) #cargo o numero de contrato
    ##############################################################
    #######REVISAR
    email = models.CharField(max_length=40, verbose_name='Email', null=True,blank=True)
    supervisor = models.ForeignKey(supervisor,on_delete=models.CASCADE, null=True,blank=True)
    dependencia = models.ForeignKey(dependencia,max_length=40, verbose_name='dependencia',on_delete=models.CASCADE, null=True,blank=True)
    sede = models.CharField(max_length=80, verbose_name='Sede', default='ADMINISTRATIVA' , choices=sede, null=True,blank=True) #choices
    #######################################################################
    ubicacionlaboral = models.CharField(max_length=60, verbose_name='Ubicacion laboral', null=True,blank=True)
    fechafinalcontrato = models.CharField(max_length=90,verbose_name='Fecha final del contrato', null=True,blank=True)
    tarjetapf = models.CharField(max_length=60, verbose_name='Tarjeta profesional', null=True,blank=True)
    ############## SISTEMA DE INFORMACION REQUERIDO #########################
    tiposolicitud = models.CharField(max_length=40, verbose_name='Tipo de solicitud', default='Consultar', choices=tiposolicitud,null=True,blank=True)
    aplicativo=models.ForeignKey(aplicativo,null=True,blank=True,on_delete=models.CASCADE)
    modulo=models.ForeignKey(modulo,null=True,blank=True,on_delete=models.CASCADE)
    observaciones = models.CharField(max_length=200, verbose_name='Observaciones', null=True,blank=True)
    observacionessup = models.CharField(max_length=200, verbose_name='Observaciones del supervisor', null=True,blank=True)
    #usuario = models.CharField(max_length=100, verbose_name='Usuario', null=True,blank=True)
    #contrasena = models.CharField(max_length=100, verbose_name='Contraseña', null=True,blank=True)
    observacionesadm = models.CharField(max_length=200, verbose_name='Observaciones del administrador', null=True,blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

### el paz y salvo debe ser una llave foranea de un un usuario registrado
class pazysalvoaprobado(models.Model):
    id = models.AutoField(primary_key=True)
    usuario=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)
    permisos = models.BooleanField(default=False)
    rfid = models.BooleanField(default=False, verbose_name='Tarjeta control de acceso')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.usuario.nombre if self.usuario else "Sin usuario"

class pazysalvorechazado(models.Model):
    id = models.AutoField(primary_key=True)
    usuario=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)
    permisos = models.BooleanField(default=False)
    rfid = models.BooleanField(default=False, verbose_name='Tarjeta control de acceso')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.usuario.nombre if self.usuario else "Sin usuario"
  