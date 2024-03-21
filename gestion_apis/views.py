from django.shortcuts import render

# Create your views here.
def nuevaeps(request):
    return render(request, 'apis.html')

def nuevaepsbasicos(request):
    return render(request, 'basicos.html')

def nuevaepscontacto(request):
    return render(request, 'contacto.html')