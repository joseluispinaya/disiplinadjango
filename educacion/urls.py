from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'carreras', views.CarreraViewSet)
router.register(r'estudiantes', views.EstudianteViewSet)
router.register(r'tiposfaltas', views.TipoFaltaViewSet)

urlpatterns = [
    path('contact/<str:name>', views.contact),
    # path('carreras/', views.carreras, name="carrera"),
    # path('estudiantes/', views.estudianteFormView, name="estudiante"),
    # path('', views.index),
    path('', include(router.urls)),
    # path('carrera/', views.CarreraCreateView.as_view(), name='carrera-create'),
    path('carrera/count/', views.carrera_count, name='carrera-count'),
]