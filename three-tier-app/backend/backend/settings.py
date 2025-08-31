import os

SECRET_KEY = os.environ.get("SECRET_KEY", "dummy")
DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.auth",          # ✅ required for permissions & auth
    "django.contrib.contenttypes",  # ✅ required dependency
    "django.contrib.sessions",      # ✅ often needed by auth
    "django.contrib.messages",      # ✅ safe to include
    "django.contrib.staticfiles",
    "rest_framework",               # ✅ DRF
    "corsheaders",                  # ✅ CORS
    "api",                          # ✅ your app
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",   # ✅ required for auth
    "django.middleware.csrf.CsrfViewMiddleware",              # ✅ security
    "django.contrib.auth.middleware.AuthenticationMiddleware",# ✅ required
    "django.contrib.messages.middleware.MessageMiddleware",   # ✅ required
]

ROOT_URLCONF = "backend.urls"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("DB_HOST", "db"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

STATIC_URL = "/static/"

# ✅ CORS Settings
CORS_ALLOW_ALL_ORIGINS = True
# For production, restrict like this:
# CORS_ALLOWED_ORIGINS = [
#     "http://18.209.211.124:3000",
# ]

# ✅ REST Framework Settings
if DEBUG:
    # Browsable API enabled only in DEBUG
    REST_FRAMEWORK = {
        "DEFAULT_RENDERER_CLASSES": [
            "rest_framework.renderers.JSONRenderer",
            "rest_framework.renderers.BrowsableAPIRenderer",
        ]
    }
else:
    # Production = JSON only
    REST_FRAMEWORK = {
        "DEFAULT_RENDERER_CLASSES": [
            "rest_framework.renderers.JSONRenderer",
        ]
    }

