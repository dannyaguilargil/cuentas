from django import forms

from .models import cuentapresupuestocontratista

class InsertFormp(forms.ModelForm):
    class Meta:
        model = cuentapresupuestocontratista
        fields = '__all__'