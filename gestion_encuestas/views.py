from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def consultaexterna(request):
    username = request.user.username
    es_staff = request.user.is_staff
    return render(request, 'consultaexterna.html', {'username': username, 'es_staff': es_staff})

def odontologia(request):
    username = request.user.username
    es_staff = request.user.is_staff
    return render(request, 'odontologia.html', {'username': username, 'es_staff': es_staff})

def enfermeria(request):
    username = request.user.username
    es_staff = request.user.is_staff
    return render(request, 'enfermeria.html', {'username': username, 'es_staff': es_staff})
