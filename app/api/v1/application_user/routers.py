from rest_framework.routers import DefaultRouter

from .views import UserViewSet

router = DefaultRouter()

router.register(
    prefix="create-user",
    viewset=UserViewSet,
    basename="create-user-api",
)
