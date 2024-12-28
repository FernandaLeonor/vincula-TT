from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.conf.urls.static import static

# Endpoint for swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Documentation about the API",
        default_version="v0",
        description="Swagger",
        license=openapi.License(name="FreeBSD License"),
        contact=openapi.Contact(email="default@email.com", name="Default"),
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # Path de API de Swagger
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path(
        "swagger/api/v1/user/login/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="rest_framework_login",
    ),
    path(
        "swagger/api/v1/user/logout/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="rest_framework_logout",
    ),
    path("", include("dashboard.urls")),
    # API
    path("api/v1/", include(("api.urls", "api"), namespace="api")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
