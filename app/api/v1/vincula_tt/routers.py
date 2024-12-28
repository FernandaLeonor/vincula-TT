from rest_framework.routers import DefaultRouter

from .views import TrabajosTerminalesViewSet

router = DefaultRouter()

router.register(
    prefix="tt",
    viewset=TrabajosTerminalesViewSet,
    basename="tt-api",
)
