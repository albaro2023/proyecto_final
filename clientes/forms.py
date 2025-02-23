# CLientes forms
from django import forms
from .models import Cliente

class ClienteCreateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control border-primary shadow'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control border-primary shadow'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border-primary shadow'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control border-primary shadow', 'placeholder': 'Ejemplo: +591 12345678'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control border-primary shadow'}),
        }
        
class ClienteUpdateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control border-primary shadow'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control border-primary shadow'}),
            'email': forms.EmailInput(attrs={'class': 'form-control border-primary shadow'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control border-primary shadow'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control border-primary shadow'}),
        }