from django.contrib import admin
from .models import Carrera, TipoFalta, Estudiante, Disiplina

admin.site.register(Carrera)

class TipofaltaAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'puntos')

admin.site.register(TipoFalta, TipofaltaAdmin)

admin.site.register(Disiplina)

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'carrera', 'nroci', 'correo', 'estado')
    ordering = ('nombres',)
    search_fields = ('nombres',)

admin.site.register(Estudiante, EstudianteAdmin)