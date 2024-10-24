from django.db import models
from gestion_usuarios.choices import sexos, rol, tipodocumento, modulo
from gestion_supervisor.models import supervisor
from gestion_informes.models import dependencia
from django.contrib.auth.models import User


class usuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario autenticado', blank=True, null=True )
    nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre', blank=True, null=True)
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido', blank=True, null=True)
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido', blank=True, null=True)
    cargo = models.CharField(max_length=40, verbose_name='Cargo', blank=True, null=True)
    email = models.EmailField(max_length=40, verbose_name='Correo personal', blank=True, null=True)
    supervisor = models.ForeignKey(supervisor,max_length=40, verbose_name='supervisor',on_delete=models.CASCADE,related_name='supervisor_detail')
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento',choices=tipodocumento, default='CC')
    cedula = models.IntegerField(primary_key=True, verbose_name='Cedula')
    ##hast aqui va el de usuarios registrados
    lugarexpedicion = models.CharField(max_length=40, verbose_name='Lugar de expedicion', blank=True, null=True)
    dependencia = models.ForeignKey(dependencia,max_length=40, verbose_name='dependencia',on_delete=models.CASCADE, blank=True, null=True)
    sexo = models.CharField(max_length=40, verbose_name='Sexo', choices=sexos, default='F')
    telefono = models.IntegerField(verbose_name='Telefono fijo' , blank=True, null=True)
    #celular = models.IntegerField(verbose_name='Celular' , blank=True, null=True)
    direccion = models.CharField(max_length=40, verbose_name='Direccion', blank=True, null=True)
    rol = models.CharField(max_length=40, verbose_name='Rol',choices=rol, default='identidades')
    #imagen
    fechafinalcontrato = models.DateField(verbose_name='Fecha final del contrato', null=True,blank=True)
    imagen = models.ImageField(upload_to='imgs/',default='imgs/sinfoto.jpeg')
  
    #Dependiendo de como se muestre aqui se muestra en la relacion de la llave foranera
    def __str__(self):
        return self.nombre + ' ' + self.primerapellido
    
    
class prueba(models.Model):
    nombreprueba = models.CharField(max_length=40)
    cedula = models.IntegerField(primary_key=True)
    usuario=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)
    
    
class usolicitudes(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre', blank=True, null=True)
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido', blank=True, null=True)
    cargo = models.CharField(max_length=40, verbose_name='Cargo')
    email = models.CharField(max_length=40, verbose_name='Correo personal')
    supervisor = models.ForeignKey(supervisor,max_length=40, verbose_name='supervisor',on_delete=models.CASCADE, blank=False, null=False, default=1)
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento',choices=tipodocumento, default='CC')
    cedula = models.IntegerField(primary_key=True, verbose_name='Cedula')
    #modulo = models.CharField(max_length=40, verbose_name='Sistema',choices=modulo, default='identidades')

    def __str__(self):
        return 'Solicitud de usuario: ' + self.nombre + ' ' + self.primerapellido 
    
    #Aqui cambio los atributos de la tabla 
    class Meta:
        verbose_name = 'Solicitud de usuario'
        verbose_name_plural = 'Solicitudes de usuarios'
        db_table='Solicitudes de usuarios'

def obtener_archivo_predeterminado():
    return 'pdfs/'
#por ahora solo quiero hacer registros pero debo referenciarlo con llave foranea
class contrato(models.Model):
    numero = models.IntegerField(primary_key=True, verbose_name='Numero')
    numeroproceso = models.IntegerField(verbose_name='Numero de proceso')
    objeto = models.CharField(max_length=300, verbose_name='Objeto')
    fechaperfeccionamiento = models.CharField(max_length=300, verbose_name='Fecha de perfeccionamiento')
    valor = models.CharField(max_length=300, verbose_name='Valor del contrato')
    fechacontrato = models.CharField(max_length=300, verbose_name='Fecha inicial del  contrato')
    fechaterminacion = models.CharField(max_length=300, verbose_name='Fecha final del contrato')
    duracion = models.CharField(max_length=40, verbose_name='Duracion del contrato')
    supervisor = models.CharField(max_length=40, verbose_name='Supervisor', default='')
    archivo = models.FileField(upload_to='pdfs/', default=obtener_archivo_predeterminado, verbose_name='archivo')
    #pendiente validar como muestra la llave foranea
    usuario=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)
###################################################################################################
################ SOLO TENIA ARCHIVO EN CONTRATO ###################################################
    
class rp(models.Model):
    numero = models.IntegerField(primary_key=True, verbose_name='Numero del rp')
    fecha = models.CharField(max_length=300, verbose_name='Fecha del rp')
    duracion = models.CharField(max_length=40, verbose_name='Duracion del contrato')
    valor = models.CharField(max_length=300, verbose_name='Valor del contrato')
    archivo = models.FileField(upload_to='pdfs/', default='No cargado', verbose_name='archivo')#LO AGREGUE REVISAR
    #llave foranea
    usuario=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return 'REGISTRO PRESUPUESTAL: '+self.fecha
    
class actainicio(models.Model):
    numero = models.IntegerField(primary_key=True, verbose_name='Numero del proceso')
    fecha = models.CharField(max_length=300, verbose_name='Fecha de acta de inicio')
    duracion = models.CharField(max_length=40, verbose_name='Duracion del contrato')
    valor = models.CharField(max_length=300, verbose_name='Valor del contrato')
    archivo = models.FileField(upload_to='pdfs/', default='NO CARGADO', verbose_name='archivo')#LO AGREGUE REVISAR
    usuario=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)
    #llave foranea
    
    def __str__(self):
        return 'ACTA DE INICIO: '+self.fecha
 
#gestion de documentos del usuario    
class planilla(models.Model):
    numero = models.IntegerField(primary_key=True, verbose_name='Numero de la planilla')
    fecha = models.CharField(max_length=300, verbose_name='Fecha del pago de la planilla')
    periodo = models.CharField(max_length=40, verbose_name='Periodo de la planilla')
    valortotal = models.CharField(max_length=300, verbose_name='Valor total de la planilla')
    nombrepension = models.CharField(max_length=300, verbose_name='Nombre de la entidad de pension')
    valorpension = models.CharField(max_length=300, verbose_name='Valor de la pension')
    nombresalud = models.CharField(max_length=300, verbose_name='Nombre de la entidad de salud')
    valorsalud = models.CharField(max_length=300, verbose_name='Valor de la salud')
    nombrearl = models.CharField(max_length=300, verbose_name='Nombre de la entidad de arl')
    valorarl = models.CharField(max_length=300, verbose_name='Valor de arl')
    archivo = models.FileField(upload_to='pdfs/', default='NO CARGADO', verbose_name='archivo')#LO AGREGUE REVISAR
    usuario=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)
    #llave foranea

    def __str__(self):
        return 'PLANILLA: '+self.periodo
    
class actividades(models.Model):
    objeto = models.CharField(max_length=300, verbose_name='Objeto del contrato')
    lugar = models.CharField(max_length=40, verbose_name='Lugar donde realizo la actividad')
    fecha = models.CharField(max_length=40, verbose_name='Periodo de actividades')
    actividades = models.CharField(max_length=600, verbose_name='Actividades a realizar ')
    resultadoactvidades = models.CharField(max_length=600, verbose_name='Resultado de las actividades')
    #llave foranea
    archivo = models.FileField(upload_to='pdfs/', default='NO CARGADO', verbose_name='archivo')#LO AGREGUE REVISAR
    usuario=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return 'ACTA DE INICIO: '+self.objeto
    
class actapago(models.Model):
    objeto = models.CharField(max_length=300, verbose_name='Objeto del contrato')
    lugar = models.CharField(max_length=40, verbose_name='Lugar donde realizo la actividad')
    valor = models.CharField(max_length=40, verbose_name='Valor del contrato')
    fechaperfeccionamiento = models.CharField(max_length=40, verbose_name='Fecha de perfeccionamiento')
    numeroacta = models.IntegerField(verbose_name='Numero de acta de pago')
    fechacuenta = models.CharField(max_length=600, verbose_name='Fecha en la que pasa la cuenta') #aqui tomar el mes automaticamente y dia
    periodo = models.IntegerField( verbose_name='Periodo de pago')
    #llave foranea
    archivo = models.FileField(upload_to='pdfs/', default='NO CARGADO', verbose_name='archivo')#LO AGREGUE REVISAR
    usuario=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return 'ACTA DE PAGO: '+self.objeto
    
class certificadoseguimiento(models.Model):
    numerocontrato = models.IntegerField( verbose_name='Numero del contrato')
    fechacuenta = models.CharField(max_length=40, verbose_name='Fecha actual de la cuenta')
    objeto = models.CharField(max_length=40, verbose_name='Objeto del contrato')
    rp = models.CharField(max_length=40, verbose_name='Numero del registro presupuestal')
    fechasuscripcion = models.CharField(max_length=40, verbose_name='Fecha de suscripcion del contrato')
    fechaterminacion = models.CharField(max_length=40,verbose_name='Fecha terminacion del contrato')
    periodo = models.IntegerField( verbose_name='Periodo de pago')
    numeroplanilla = models.IntegerField( verbose_name='Numero de planilla de pago')
    nombresalud = models.CharField(max_length=40,verbose_name='Nombre de la entidad de salud')
    valorsalud = models.CharField(max_length=40,verbose_name='Valor de la salud')
    nombrepension = models.CharField(max_length=40,verbose_name='Nombre de la entidad de pension')
    valorpension = models.CharField(max_length=40,verbose_name='Valor de la entidad de pension')
    nombrearl = models.CharField(max_length=40,verbose_name='Nombre de la entidad de arl')
    valorarl = models.CharField(max_length=40,verbose_name='Valor de la entidad de arl')
    cuentapago = models.CharField(max_length=40,verbose_name='Nombre de la entidad bancaria')
    numerocuentapago = models.IntegerField( verbose_name='Numero de la entidad bancaria')
    #llave foranea
    archivo = models.FileField(upload_to='pdfs/', default='NO CARGADO', verbose_name='archivo')#LO AGREGUE REVISAR
    usuario=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return 'ACTA DE PAGO: '+self.objeto
    
class cuentausuario(models.Model): #la idea es no mostrar todo los datos de la cuenta, solo unos datos y pasarla
    #todo la informacion de los documentos traerlos con llave foranea, por ahora validar el registro inidvidual
    #Antes de eso validar que me lo traiga con el mero html
    ###########################################################################
    ########## SOLO PLANILLA Y ACTIVIDADES SE SUBEN LO DEMAS LO HACE EL SISTEMA
    ###########################################################################
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    #segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre')
    #primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    #segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido')
    email = models.CharField(max_length=40, verbose_name='Email')
    supervisor = models.CharField(max_length=40, verbose_name='Supervisor', default='No asignado')
    #tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento',choices=tipodocumento, default='CC')
    cedula = models.IntegerField(verbose_name='Cedula')#llevarlo por id de cuenta y relacionarlo con usuario
    dependencia = models.CharField(max_length=40, verbose_name='Dependencia', default='No asignado')
    #sexo = models.CharField(max_length=40, verbose_name='Sexo', choices=sexos, default='F')
    #gestion de contratacion, tener en cuenta el pdf
    #numero = models.IntegerField(verbose_name='Numero del contrato')
    objeto = models.CharField(max_length=400, verbose_name='Objeto')
    # este objeto de contrato debe remplazar al cargo en usuario
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
    #gestion de acta de inicio, tener en cuenta el pdf  

#PRIMERO ME TRAIGO LA INFORMACION    
#class perfil(models.Model):
#    nombre = models.CharField(max_length=40, verbose_name='Nombre completo')
#    apellidos = models.CharField(max_length=40, verbose_name='Apellidos')
#    cedula = models.IntegerField(verbose_name='Cedula')
#    email = models.CharField(verbose_name='Email')

class cuentabancaria(models.Model):
    numero = models.IntegerField(primary_key=True, verbose_name='Numero de cuenta bancaria')
    tipocuenta = models.CharField(max_length=40, verbose_name='Tipo de cuenta bancaria')
    nombrecb = models.CharField(max_length=40, verbose_name='Nombre de cuenta bancaria')
    usuario=models.ForeignKey(usuario,null=True,blank=True,on_delete=models.CASCADE)
    
class cuentacontratista(models.Model):
    id = models.AutoField(primary_key=True)
    numeroplanilla = models.CharField(max_length=40, default='001', verbose_name='Numero de planilla')
#    #email = models.CharField(max_length=40, verbose_name='Email')
#    #supervisor = models.CharField(max_length=40, verbose_name='Supervisor', default='No asignado')
    archivo = models.FileField(upload_to='pdfs/', default='pdfs/NOCARGADO', verbose_name='archivo')
    #tipocuenta = models.CharField(max_length=40, verbose_name='Tipo de cuenta bancaria')
    #nombrecb = models.CharField(max_length=40, verbose_name='Nombre de cuenta bancaria')
    cedula = models.IntegerField(verbose_name='Cedula', default=1)
    nombrecompleto = models.CharField(max_length=80, verbose_name='Nombre completo', default='No asignado')
    objetocontrato = models.CharField(max_length=200, verbose_name='Objeto del contrato', default='No asignado')
    pdfcontrato = models.CharField(max_length=200, verbose_name='Pdf del contrato', default='pdfs/NOCARGADO')
    pdfplanilla = models.CharField(max_length=200, verbose_name='Pdf de la planilla', default='pdfs/NOCARGADO')
    flujo = models.CharField(max_length=80, verbose_name='Flujo', default='Pendiente de pasar cuenta')
    #pdfactividades = models.CharField(max_length=80, verbose_name='Pdf de actividades', default='pdfs/NOCARGADO')

class solicitudrechazada(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Primer nombre')
    segundonombre = models.CharField(max_length=40, verbose_name='Segundo nombre', blank=True, null=True)
    primerapellido = models.CharField(max_length=40, verbose_name='Primer apellido')
    segundoapellido = models.CharField(max_length=40, verbose_name='Segundo apellido', blank=True, null=True)
    cargo = models.CharField(max_length=40, verbose_name='Cargo')
    email = models.CharField(max_length=40, verbose_name='Email')
    supervisor = models.ForeignKey(supervisor,max_length=40, verbose_name='supervisor',on_delete=models.CASCADE)
    tipodocumento = models.CharField(max_length=40, verbose_name='Tipo de documento',choices=tipodocumento, default='CC')
    cedula = models.IntegerField(primary_key=True, verbose_name='Cedula')
    #modulo = models.CharField(max_length=40, verbose_name='Sistema',choices=modulo, default='identidades')

    def __str__(self):
        return 'Solicitud rechazada: ' + self.nombre + ' ' + self.primerapellido
    