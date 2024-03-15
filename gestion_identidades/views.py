from django.shortcuts import render

def seguimientohtml(request):
    nombre = ""
    return render(request, 'seguimiento.html', {'nombre': nombre})
