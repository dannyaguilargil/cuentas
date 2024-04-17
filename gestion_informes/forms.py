from django import forms
from .models import entecontrol,dependencia

class fente(forms.ModelForm):
    class Meta:
        model = entecontrol
        fields = ['nombre','descripcion']

class fdependencia(forms.ModelForm):
    class Meta:
        model = dependencia
        fields = ['nombre','responsable','correoresponsable']

