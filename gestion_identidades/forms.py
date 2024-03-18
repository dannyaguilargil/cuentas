from django import forms

from .models import solicitudsistema

class Formidentidades(forms.ModelForm):
    class Meta:
        model = solicitudsistema
        fields = '__all__'