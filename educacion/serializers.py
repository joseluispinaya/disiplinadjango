from rest_framework import serializers
from .models import Carrera, Estudiante, TipoFalta

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = "__all__"

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = "__all__"

class TipoFaltaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoFalta
        fields = "__all__"