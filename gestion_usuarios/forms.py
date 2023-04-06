from django import forms
from .models import usolicitudes
from .models import usuario
from .models import contrato

class User(forms.ModelForm):
    class Meta:
        model = usolicitudes
        fields = '__all__'
        #['nombre', 'segundonombre', 'primerapellido', 'segundoapellido', 'cargo', 'email', 'supervisor', 'tipodocumento', 'cedula']

class Usuario(forms.ModelForm):
    class Meta:
        model = usuario
        fields = '__all__'
        
class Contrato(forms.ModelForm):
    class Meta:
        model = contrato
        fields = '__all__'
