from rest_framework.viewsets import ModelViewSet

from .serializers import UserCreateSerializer, User


class UserViewSet(ModelViewSet):
    http_method_names = ["post"]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
