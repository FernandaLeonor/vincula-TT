from django.utils.translation import pgettext_lazy

from rest_framework import serializers

from apps.vincula_tt.models import TrabajosTerminales
from ..application_user.serializers import UserListSerializer


class TrabajosTerminalesListSerializer(serializers.ModelSerializer):
    autores = UserListSerializer(many=True)
    creado_por = UserListSerializer()

    class Meta:
        model = TrabajosTerminales
        fields = [
            "pk",
            "titulo",
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


class TrabajosTerminalesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrabajosTerminales
        fields = [
            "titulo",
            "numero_tt",
            "autores",
            "asesores",
            "sinodales",
            "escrito",
            "anio",
            "palabras_clave",
            "resumen",
        ]

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        validated_data["creado_por"] = user
        return super().create(validated_data)


class TrabajosTerminalesUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrabajosTerminales
        fields = [
            "titulo",
            "numero_tt",
            "autores",
            "asesores",
            "sinodales",
            "escrito",
            "anio",
            "palabras_clave",
            "resumen",
        ]

    def validate(self, validated_data):
        instance = self.instance
        request = self.cont
        user = request.user
        if instance and instance.creado_por and instance.creado_por != user:
            raise serializers.ValidationError(
                {
                    "error": pgettext_lazy(
                        "Serializer error message",
                        "You cannot update this instance because you're not the owner",
                    )
                }
            )
        return validated_data
