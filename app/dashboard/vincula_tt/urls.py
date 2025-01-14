from django.urls import path
from .views import list_tt, create_or_update_tt, delete_tt

urlpatterns = [
    # Listar trabajos terminales
    path("list/", list_tt, name="tt-list"),

    # Crear un nuevo trabajo terminal
    path("create-tt/", create_or_update_tt, name="tt-create"),

    # Editar un trabajo terminal existente
    path("detail-tt/<int:pk>/", create_or_update_tt, name="tt-update"),

    # Eliminar un trabajo terminal
    path("delete-tt/<int:pk>/", delete_tt, name="tt-delete"),  # Ruta para eliminación
]
