from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CarreraSerializer, EstudianteSerializer, TipoFaltaSerializer
from .forms import EstudianteForm
from .models import Carrera, Estudiante, TipoFalta
from rest_framework import generics
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def contact(request, name):
    return HttpResponse(f"Hello {name}")

def carreras(request):
    post_nombre = request.POST.get("nombreCarrera")
    if post_nombre:
        q = Carrera(nombreCarrera=post_nombre)
        q.save()

    carreras = Carrera.objects.all()
    return render(request, "form_carreras.html", {
        "carreras": carreras
    })

def estudianteFormView(request):
    form = EstudianteForm(request.POST)

    if form.is_valid():
        form.save()
    return render(request, "form_estudiantes.html", {"form": form})

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class TipoFaltaViewSet(viewsets.ModelViewSet):
    queryset = TipoFalta.objects.all()
    serializer_class = TipoFaltaSerializer


class CarreraCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

@api_view(['GET'])
def carrera_count(request):
    try:
        cantidad = Carrera.objects.count()
        return JsonResponse({"cantidad": cantidad}, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, safe=False, status=500)