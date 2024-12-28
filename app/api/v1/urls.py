from django.urls import include, path
from rest_framework_simplejwt.views import token_obtain_pair

from .application_user.routers import router as application_user_router
from .vincula_tt.routers import router as vincula_tt_router

urlpatterns = [
    path("login/", token_obtain_pair, name="login"),
    path("", include(application_user_router.urls)),
    path("", include(vincula_tt_router.urls)),
]
