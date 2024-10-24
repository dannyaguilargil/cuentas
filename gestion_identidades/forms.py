from django import forms
from django.contrib.auth.models import User 
from .models import solicitudsistema,solicitudsistemasupervisor,solicitudsistemaadmin,solicitudsistemarechazado,solicitudsistemarechazadoadm,pazysalvo,pazysalvoaprobado,pazysalvorechazado

class Formidentidades(forms.ModelForm):
    class Meta:
        model = solicitudsistema
        fields = ['nombre','segundonombre','primerapellido','segundoapellido','tipodocumento','cedula','lugarexpedicion','sexo','telefono','celular','direccion','cargo','email','supervisor','dependencia','sede','ubicacionlaboral','fechafinalcontrato','tarjetapf','tiposolicitud','aplicativo','modulo','observaciones']

    ## Aquí podrías agregar validaciones personalizadas si lo necesitas
    #def clean(self):
    #    cleaned_data = super().clean()
    #    # Ejemplo de validación personalizada
    #    cedula = cleaned_data.get('cedula')
    #    if not cedula:
    #        raise forms.ValidationError("El campo cédula es obligatorio.")
    #    return cleaned_data

class FormidentidadesSupervisor(forms.ModelForm):
    class Meta:
        model = solicitudsistemasupervisor
        fields = ['nombre', 'segundonombre','primerapellido','segundoapellido','tipodocumento','cedula','lugarexpedicion','sexo', 'telefono','celular','direccion','cargo','email','supervisor','dependencia', 'sede','ubicacionlaboral','fechafinalcontrato', 'tarjetapf','tiposolicitud','aplicativo','modulo','observaciones','observacionessup']
    id = forms.IntegerField(widget=forms.HiddenInput())

class FormidentidadesAdmin(forms.ModelForm):
    class Meta:
        model = solicitudsistemaadmin
        fields = ['nombre', 'segundonombre','primerapellido','segundoapellido','tipodocumento','cedula','lugarexpedicion','sexo', 'telefono','celular','direccion','cargo','email','supervisor','dependencia', 'sede','ubicacionlaboral','fechafinalcontrato', 'tarjetapf','tiposolicitud','aplicativo','modulo','observaciones','observacionessup','usuario','contrasena','observacionesadm']
    # Agregar un campo oculto para el ID de la solicitud
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    cedula = forms.CharField(required=False, widget=forms.HiddenInput()) 

class FormidentidadesSupervisorRechazado(forms.ModelForm):
    class Meta:
        model = solicitudsistemarechazado
        fields = ['nombre', 'segundonombre','primerapellido','segundoapellido','tipodocumento','cedula','lugarexpedicion','sexo', 'telefono','celular','direccion','cargo','email','supervisor','dependencia', 'sede','ubicacionlaboral','fechafinalcontrato', 'tarjetapf','tiposolicitud','aplicativo','modulo','observaciones','observacionessup']
    id = forms.IntegerField(widget=forms.HiddenInput())

class FormidentidadesRechazadoAdm(forms.ModelForm):
    class Meta:
        model = solicitudsistemarechazadoadm
        fields = ['nombre', 'segundonombre','primerapellido','segundoapellido','tipodocumento','cedula','lugarexpedicion','sexo', 'telefono','celular','direccion','cargo','email','supervisor','dependencia', 'sede','ubicacionlaboral','fechafinalcontrato', 'tarjetapf','tiposolicitud','aplicativo','modulo','observaciones','observacionessup','observacionesadm']
    # Agregar un campo oculto para el ID de la solicitud
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    cedula = forms.CharField(required=False, widget=forms.HiddenInput()) 

class pazysalvosolicitud(forms.ModelForm):
    class Meta:
        model = pazysalvo
        fields = ['usuario','permisos','rfid']
       

class pazysalvoaprobadoF(forms.ModelForm):
    class Meta:
        model = pazysalvoaprobado
        fields = ['usuario','permisos','rfid']
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())

class PazySalvoRechazado(forms.ModelForm):
    class Meta:
        model = pazysalvorechazado
        fields = ['usuario','permisos','rfid']
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
        
    