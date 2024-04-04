from django import forms

from .models import solicitudsistema

class Formidentidades(forms.ModelForm):
    class Meta:
        model = solicitudsistema
        fields = ['nombre','segundonombre','primerapellido','segundoapellido','cargo','email','supervisor','tipodocumento','cedula','lugarexpedicion','dependencia','sexo','telefono','celular','direccion','sede','fechafinalcontrato','tiposolicitud','apicativo','observaciones']

