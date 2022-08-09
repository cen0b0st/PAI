from django.forms import *
from django import forms

from .models import Cargo, Formulariosr, Departamento, SubDepartamento, Seccion








"""
class FormularioSRForm(forms.ModelForm):
    
    class Meta:
        model = Formulariosr
        
        #CAMPOS DEL MODELO A UTILIZAR
        fields = (
            'cargo_id_cargo',
            'departamento_id_dpto',
            'sub_departamento_id_sub_dpto',
            'seccion_id_seccion',
            
        )
        #LABELS DEL FORMULARIO PARA LOS CAMPOS DEL MODELO
        labels = {
            'nombre_cargo' : 'Cargo',
        }
        #HACEN LAS ETIQUETAS HTML

        widgets = {
            'nombre_cargo' : forms.Select(),
        }
"""