import blog1
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='inicio'),
    path('enviar_consulta/',views.enviar_consulta, name="enviar_consulta"),
    path('inicio/', views.Clases.as_view(), name="inicio"),
    path('alumnos_inscriptos/', views.AlumnosInscriptos.as_view(), name='alumnos_inscriptos'),
    path('inscripccion_alumno/', views.inscripccion_alumno, name="inscripccion_alumno"),
    path('inscripccionprofesores/', views.inscripccionprofesores, name="inscripccionprofesores"),
    path('tareas/', views.Tareas.as_view(), name='tareas')
    ]