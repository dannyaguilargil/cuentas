from django.shortcuts import render

# Create your views here.
def seguimientohtml(request):
    nombre = ""
    return render(request, 'seguimiento.html', {'nombre': nombre})