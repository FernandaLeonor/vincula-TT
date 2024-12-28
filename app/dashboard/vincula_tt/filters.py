from django_filters import filters
from core.filters import BaseFilterSet
from apps.vincula_tt.models import TrabajosTerminales

class TrabajosTerminalesFilterSet(BaseFilterSet):
    titulo = filters.CharFilter(label="Título", lookup_expr="icontains")
    numero_tt = filters.CharFilter(label="Número TT", lookup_expr="icontains")
    palabras_clave = filters.CharFilter(label="Palabras clave", lookup_expr="icontains")
    anio = filters.NumberFilter(label="Año")

    class Meta: 
        model = TrabajosTerminales
        fields = ["titulo", "anio", "numero_tt", "palabras_clave"]
