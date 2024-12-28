from django.urls import path
from .views import CreateUser

urlpatterns = [
    path("user-create/", CreateUser, name="user-create")
]