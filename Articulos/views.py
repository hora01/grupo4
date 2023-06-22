from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ComentarioForm, InscripccionAlumnoForm, InscripccionProfesoresForm
#from django.http import HttpResponse, HttpResponseNotFound
from .models import  Alumno, Clase, Tarea
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
def home(request):
  return render(request,"bienvenida.html")

def enviar_consulta(request):
   if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['nombre'])

            messages.add_message(request, messages.SUCCESS, 'Comentario enviado', extra_tags="tag1")

            return redirect("enviar_consulta")
   else:
    
        form = ComentarioForm()

        context = {'form': form}

        return render(request, 'enviar_consulta.html', context)
   
class Clases(ListView):
    model = Clase
    context_object_name = 'Clase'
    template_name = 'inicio.html'


@login_required
def inscripccion_alumno(request):
    context = {}

    if request.method == "POST":
        form = InscripccionAlumnoForm(request.POST)

        if form.is_valid():

            form.save()
            messages.add_message(request, messages.SUCCESS, 'Usted se inscribió')
            return redirect("inscripccion_alumno")

    else:
        form = InscripccionAlumnoForm()

    context['form'] = form

    return render(request, 'inscripccion_alumno.html', context)

@permission_required('Articulos.add_profesor')
def inscripccionprofesores(request):
    context = {}

    if request.method == "POST":
        form = InscripccionProfesoresForm(request.POST)

        if form.is_valid():

            form.save()
            messages.add_message(request, messages.SUCCESS, 'Usted se inscribió')
            return redirect("inscripccionprofesores")

    else:
        form = InscripccionProfesoresForm()

    context['form'] = form

    return render(request, 'inscripccionprofesores.html', context)

class AlumnosInscriptos(ListView):
    model = Alumno
    context_object_name = 'Alumno'
    template_name = 'alumnos_inscriptos.html'

class Tareas(ListView):
    model = Tarea
    context_object_name = 'Tarea'
    template_name = 'tareas.html'

