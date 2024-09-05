from django import forms

from .models import solicitudsistema,solicitudsistemasupervisor

class Formidentidades(forms.ModelForm):
    class Meta:
        model = solicitudsistema
        fields = ['nombre','segundonombre','primerapellido','segundoapellido','cargo','email','supervisor','tipodocumento','cedula','lugarexpedicion','dependencia','sexo','telefono','celular','direccion','sede','fechafinalcontrato','tiposolicitud','aplicativo','observaciones']

class FormidentidadesSupervisor(forms.ModelForm):
    class Meta:
        model = solicitudsistemasupervisor
        fields = ['nombre','segundonombre','primerapellido','segundoapellido','cargo','email','supervisor','tipodocumento','cedula','lugarexpedicion','dependencia','sexo','telefono','celular','direccion','sede','fechafinalcontrato','tiposolicitud','apicativo','observaciones', 'observacionessupervisor']
