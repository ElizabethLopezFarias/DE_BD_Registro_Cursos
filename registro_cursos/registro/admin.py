from django.contrib import admin

from .models import Estudiante, Direccion, Curso, Profesor, CursoEstudiante

admin.site.register(Estudiante)
admin.site.register(Direccion)
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(CursoEstudiante)
