from django.urls import path

from .views import list_tt, create_or_update_tt

urlpatterns = [
    path("list/",list_tt,name="tt-list"),
    path("create-tt/", create_or_update_tt, name="tt-create"),
    path("detail-tt/<int:pk>/",create_or_update_tt, name="tt-update" )
]
