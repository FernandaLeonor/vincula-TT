import os
import datetime
from decouple import config
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ENVIRONMENT = os.environ.get("ENVIRONMENT", "local")

SECRET_KEY = config("SECRET_KEY")
# "django-insecure-b+!pz(be$p!6-g_$lha*0w$h_m87h-pxk*m8k+gc)ixgtng+14"

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Requirements Apps
    "drf_yasg",
    "rest_framework",
    "rest_framework_simplejwt",
    "psycopg2",  # When change DB manager for something like MySQL, MariaDB or any else DB System consider remove this
    "dj_database_url",
    "corsheaders",
    "simple_history",
    # Local Apps
    "apps.application_user",
    "apps.vincula_tt",
    "dashboard",
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Cors for handling any request from the outside
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    # Cors simple history
    "simple_history.middleware.HistoryRequestMiddleware",
    # Allow Locations and language support
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"


DB_NAME = config("DB_NAME")
DB_USER = config("DB_USER")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT", default="5432")
DB_PASSWORD = config("DB_PASSWORD")
DB_ENGINE = config("DB_ENGINE", default="django.db.backends.postgresql")

DATABASES = {
    "default": {
        "ENGINE": DB_ENGINE,
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    },
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "es-mx"
LOCALE_PATHS = (
    os.path.join(
        BASE_DIR, "locale"
    ),  # Customize this path to where your locale files will be
)

TIME_ZONE = "America/Mexico_City"

USE_I18N = True

USE_TZ = True

DEFAULT_CHARSET = "utf-8"

LANGUAGES = [
    ("en", "English"),
    ("es", "Spanish"),
]


# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Media Config
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# REST Config
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    # https://www.django-rest-framework.org/api-guide/exceptions/#custom-exception-handling
    "EXCEPTION_HANDLER": "api.exception_handler.custom_exception_handler",
}

# JWT headers
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
}

CORS_ALLOW_ALL_ORIGINS = config("CORS_ALLOW_ALL_ORIGINS", default=DEBUG, cast=bool)

CORS_ALLOW_HEADERS = [
    "accept",
    "accepts",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

# Swagger Settings
SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": config(
        "SWAGGER_USE_SESSION_AUTH", default=False, cast=bool
    ),  # Disable auth from swagger
    "SECURITY_DEFINITIONS": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        },
    },
    "LOGIN_URL": "rest_framework:login",
    "LOGOUT_URL": "rest_framework:logout",
}

# Enable field of HistoryAbstractModel history_change_reason as TextField
# https://django-simple-history.readthedocs.io/en/latest/historical_model.html#textfield-as-history-change-reason
SIMPLE_HISTORY_HISTORY_CHANGE_REASON_USE_TEXT_FIELD = True

# Auth custom model
AUTH_USER_MODEL = "application_user.User"

# Whitenoise
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}

LOGIN_REDIRECT_URL = "tt-list"
LOGIN_URL = "login"