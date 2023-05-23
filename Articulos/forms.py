from django import forms

class ComentarioForm(forms.Form):
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField(label="Mail", required=True)
    nombre = forms.CharField(label='Nombre:' ,max_length=20)    
    mensaje = forms.CharField(widget=forms.Textarea)
    
    
    
