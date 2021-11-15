from .models import Despacho
from django import forms
from django.forms.widgets import SelectDateWidget, TextInput


class DespachoModelForm(forms.ModelForm):
    class Meta:
        model = Despacho
        fields = '__all__'
        labels = {
            'nombre_cliente': ('Nombre Cliente'),
            'dirección_cliente': ('Dirección Cliente'),
            'telefono_cliente': ('Número Telefónico Cliente'),
            'numero_despacho': ('Número | Código para el Despacho'),
            'productos_cliente': ('Ingrese Productos del Cliente'),
            'peso_productos': ('Ingrese Peso de los Productos (en Kg)'),
            'estado_despacho': ('Ingrese Estado (Por Enviar | Entregado)'),
            'profundidad_despacho': ('Ingrese Profundidad (En Centímetros)'),
            'ancho_despacho': ('Ingrese Ancho (En Centímetros)'),
            'alto_despacho': ('Ingrese Alto (En Centímetros)'),
            'fecha_ingreso_despacho': ('Fecha de Ingreso del Despacho'),
            'fecha_envio_despacho': ('Fecha Envío del Despacho'),
        }
        widgets = {
            'fecha_ingreso_despacho': SelectDateWidget(),
            'fecha_envio_despacho': SelectDateWidget(),
            'nombre_cliente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese Nombre Completo',
            }),
            'dirección_cliente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Vicuña Mackenna 4917, San Joaquín',
            }),
            'telefono_cliente': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+56 9 XXXXXXXX'
            }),
            'numero_despacho': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: D001, D002, D003…'
            }),
            'productos_cliente': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Almendas 1kg, Nueces 550grs, Nuez Moscada 220grs…'
            }),
            'peso_productos': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': 0,
                'placeholder': 1
            }),
            'estado_despacho': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'select'
            }),
            'profundidad_despacho': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': 1,
                'placeholder': 1
            }),
            'ancho_despacho': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': 1,
                'placeholder': 1
            }),
            'alto_despacho': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'number',
                'min': 1,
                'placeholder': 1
            })
        }


class BuscarForm(forms.Form):
    n_despacho = forms.CharField(max_length=30, label='Número de Despacho',widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingresar el número del despacho aquí.'
    }))

    def clean_n_despacho(self):
        n_despacho = self.cleaned_data.get('n_despacho')
        qs = Despacho.objects.filter(numero_despacho__iexact=n_despacho)
        if not qs.exists():
            raise forms.ValidationError('Número de despacho no existe.')
        return n_despacho