from django import forms
from .models import Producto, Cliente

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'fecha_de_registro': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'  # Si quieres agregar una clase CSS personalizada
            }),
        }
        