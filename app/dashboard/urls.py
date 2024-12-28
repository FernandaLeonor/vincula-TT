from django.urls import include, path

urlpatterns = [
    path("", include("dashboard.vincula_tt.urls")),
    path("", include("dashboard.login.urls")),
    path("", include("dashboard.application_user.urls")),
]