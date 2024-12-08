from django.http import HttpResponse
from django.shortcuts import render
from .forms import EstudianteForm
from .models import Carrera

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