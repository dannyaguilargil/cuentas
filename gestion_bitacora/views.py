from django.shortcuts import render
from rest_framework import viewsets
from .serializer import bitacoraSerializer
from .models import bitacora

# Create your views here.
class bitacoraView(viewsets.ModelViewSet):
    serializer_class = bitacoraSerializer
    queryset = bitacora.objects.all()
