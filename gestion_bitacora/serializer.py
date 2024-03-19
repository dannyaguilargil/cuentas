from rest_framework import serializers
from .models import bitacora

class bitacoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = bitacora
        fields = '__all__'

