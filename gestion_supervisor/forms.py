from django import forms

from .models import cuentasupervisorcontratista

##GESTION DE CUENTA DEL SUPERVISOR
class InsertForms(forms.ModelForm):
    class Meta:
        model = cuentasupervisorcontratista
        fields = '__all__'