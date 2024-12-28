from django import forms
from apps.vincula_tt.models import *

class TrabajosTerminalesForm(forms.ModelForm):
    class Meta:
        model = TrabajosTerminales
        fields = ["titulo",
    "numero_tt",
    "autores",
    "asesores",
    "sinodales",
    "escrito",
    "anio",
    "palabras_clave",
    "resumen",
    ]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(TrabajosTerminalesForm, self).__init__(*args, **kwargs)
        fields = ["titulo", "asesores", "sinodales", "palabras_clave", "resumen",]
        for field in fields:
            self.fields[field].widget.attrs.update(
                {"class": "materialize-textarea"}
            )
        user = self.request.user
        if not user.is_authenticated:
            for field in self.fields.values():
                field.disabled = True
    
    def clean(self):
        cleaned_data = super().clean()
        instance = self.instance
        if instance and instance.creado_por and not instance.es_duenio(self.request.user):
            self.add_error("creado_por","No puedes editar este Trabajo Terminal")
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=commit)
        if not instance.creado_por:
            instance.creado_por = self.request.user
            instance.save()
        return instance