from django import forms
from apps.vincula_tt.models import *

class TrabajosTerminalesForm(forms.ModelForm):
    creado_por=forms.CharField(widget=forms.HiddenInput(),required=False)
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
    "creado_por",
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
        if instance:
            cleaned_data["creado_por"] = instance.creado_por
        if instance and instance.creado_por and not instance.es_duenio(self.request.user):
            self.add_error("creado_por","No puedes editar este Trabajo Terminal")
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=commit)
        if not instance.creado_por:
            instance.creado_por = self.request.user
            instance.save()
        return instance