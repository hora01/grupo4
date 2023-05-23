from django.contrib import messages
from email import message
#from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import Entrada
from .models import Comentario
from .forms import ComentarioForm

# Create your views here.
def home(request):
  articulos = Entrada.objects.all()
 
  return render(request,"bienvenida.html",{"articulos":articulos})

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