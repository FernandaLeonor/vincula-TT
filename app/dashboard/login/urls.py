from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .forms import CustomAuthenticationForm

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="dashboard/login/main.html",
            authentication_form=CustomAuthenticationForm,
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="/list/"), name="logout"),
]