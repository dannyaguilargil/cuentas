from django import forms
from .models import usolicitudes
from .models import usuario
from .models import contrato
from .models import rp
from .models import actainicio
from .models import planilla
from .models import actividades
from .models import actapago
from .models import certificadoseguimiento
from .models import prueba
from .models import cuentausuario

class Users(forms.ModelForm):
    class Meta:
        model = usolicitudes
        fields = '__all__'
        #['nombre', 'segundonombre', 'primerapellido', 'segundoapellido', 'cargo', 'email', 'supervisor', 'tipodocumento', 'cedula']

class Usuario(forms.ModelForm):
    class Meta:
        model = usuario
        fields = '__all__'
        #AQUI PUEDEN IR WIDGETS
        
class Contrato(forms.ModelForm):
    class Meta:
        model = contrato
        fields = '__all__'

class Rp(forms.ModelForm):
    class Meta:
        model = rp
        fields = '__all__'
        
class Actainicio(forms.ModelForm):
    class Meta:
        model = actainicio
        fields = '__all__'
        
class Planilla(forms.ModelForm):
    class Meta:
        model = planilla
        fields = '__all__'

class Actividades(forms.ModelForm):
    class Meta:
        model = actividades
        fields = '__all__'

class Actapago(forms.ModelForm):
    class Meta:
        model = actapago
        fields = '__all__'
        
class Certificadoseguimiento(forms.ModelForm):
    class Meta:
        model = certificadoseguimiento
        fields = '__all__'
        
class Prueba(forms.ModelForm):
    class Meta:
        model = prueba
        fields = '__all__'

#gestion de pasar la cuenta de usuario
#cuenta de usuario el nombre no porque ya debe estar arriba
class Cusuario(forms.ModelForm):
    class Meta:
        model = cuentausuario
        fields = ['supervisor', 'cedula', 'dependencia', 'numero', 'objeto','fechaperfeccionamiento','valor','fechacontrato','fechaterminacion','duracion','numerorp','fecharp','numeroactainicio','fechaactainicio']