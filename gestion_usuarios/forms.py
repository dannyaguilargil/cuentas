from django import forms
from .models import usolicitudes

class User(forms.ModelForm):
    class Meta:
        model = usolicitudes
        fields = '__all__'
        #['nombre', 'segundonombre', 'primerapellido', 'segundoapellido', 'cargo', 'email', 'supervisor', 'tipodocumento', 'cedula']