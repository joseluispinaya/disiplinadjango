from django.urls import path
from . import views

urlpatterns = [
    path('contact/<str:name>', views.contact),
    path('carreras/', views.carreras, name="carrera"),
    path('estudiantes/', views.estudianteFormView, name="estudiante"),
    path('', views.index),
]