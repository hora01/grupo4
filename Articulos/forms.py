from django import forms
from django.core.exceptions import ValidationError
from .models import Alumno, Profesor

class ComentarioForm(forms.Form):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(label="Mail", required=True)
    nombre = forms.CharField(label='Nombre:' ,max_length=20)    
    mensaje = forms.CharField(widget=forms.Textarea)
    
class InscripccionAlumnoForm(forms.Form):
    nombre_apellido = forms.CharField(
        label="Nombre apellido", 
        widget=forms.TextInput(
            attrs={
                'id':'InscripccionAlumnoNombre'
            }),
        required=True
    )
    email = forms.EmailField(label="Email ", required=True)
    DNI = forms.IntegerField(label="Dni", required=True)

    def clean(self):   #Validacion de alumno para que no se repita
        email = self.cleaned_data["email"]
        if Alumno.objects.filter(email=email).exists():
            raise ValidationError("Existe un usuario con ese mail")

        return self.cleaned_data

    
class InscripccionProfesoresForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'