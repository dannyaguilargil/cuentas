from django import forms
from .models import entecontrol,dependencia,informe,entrega,evidencia
#from task2.tasks import send_review_email_task

class fente(forms.ModelForm):
    class Meta:
        model = entecontrol
        fields = ['nombre','descripcion']

class fdependencia(forms.ModelForm):
    class Meta:
        model = dependencia
        fields = ['nombre','responsable','correoresponsable']

###formulario de creaccion del informe, tener en cuenta llaves foraneas de ente de control 
## y dependencias a ver si las toma
class finforme(forms.ModelForm):
    class Meta:
        model = informe
        fields = ['nombre','entecontrol','normativa','dependencia','descripcion','fechaentregainicial','periodicidad','periodicidadtipo','alarmas']#pendiente totalentregas

### formulario basado en clase de prueba para envio de emails
class ReviewForm(forms.Form):
    name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))
    email = forms.EmailField(
        max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email'}))
    review = forms.CharField(
        label="Review", widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))

    def send_email(self):
        send_review_email_task.delay(
            self.cleaned_data['name'], self.cleaned_data['email'], self.cleaned_data['review'])

##tomare el nombre como la fecha de entrega por ahora, puede ser que haga un cuadro aparte de observaciones
class fevidencia(forms.ModelForm):
    class Meta:
        model = evidencia
        fields = ['entrega', 'nombre','archivo']
## por ahora solo entrega luego valido con nombre(fecha) y archivo
