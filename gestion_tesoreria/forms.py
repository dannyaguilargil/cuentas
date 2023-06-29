from django import forms
from .models import cuentatesoreriacontratista

class InsertFormt(forms.ModelForm):
    class Meta:
        model = cuentatesoreriacontratista
        fields = '__all__'