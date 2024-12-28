from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import parser_classes, action
from rest_framework.parsers import MultiPartParser

from .serializers import (
    TrabajosTerminalesListSerializer,
    TrabajosTerminalesCreateSerializer,
    TrabajosTerminalesUpdateSerializer,
    TrabajosTerminales,
)
from api.pagination import CustomPagination


@parser_classes([MultiPartParser])
class TrabajosTerminalesViewSet(ModelViewSet):
    http_method_names = ["get", "post", "patch"]
    serializer_class = TrabajosTerminalesListSerializer
    lookup_field = "pk"
    queryset = TrabajosTerminales.objects.all()
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["create"]:
            return TrabajosTerminalesCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return TrabajosTerminalesUpdateSerializer
        return TrabajosTerminalesListSerializer
