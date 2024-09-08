from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY')

DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['techrahis.vercel.app','techrahis.com', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core",
    "blogs",
    "projects",
    "compressor",
]

COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = False
COMPRESS_OFFLINE = False

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "tech_rahis.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = "tech_rahis.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('PG_DATABASE'),
        'USER': config('PG_USER'),
        'PASSWORD': config('PG_PASSWORD'),
        'HOST': config('PG_HOST'),
        'PORT': config('PG_PORT'),
        'OPTIONS': {
            'sslmode': config('PG_SSLMODE', default='require'),
        },
    }
}

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Cloudflare R2 Configurations
CLOUDFLARE_R2_BUCKET = config('CLOUDFLARE_R2_BUCKET')
CLOUDFLARE_R2_ACCESS_KEY_ID = config('CLOUDFLARE_R2_ACCESS_KEY_ID')
CLOUDFLARE_R2_SECRET_KEY = config('CLOUDFLARE_R2_SECRET_KEY')
CLOUDFLARE_R2_BUCKET_ENDPOINT = config('CLOUDFLARE_R2_BUCKET_ENDPOINT')

CLOUDFLARE_R2_CONFIG_OPTIONS = {
    "bucket_name": CLOUDFLARE_R2_BUCKET,
    "default_acl": "public-read",
    "signature_version": "s3v4",
    "endpoint_url": config("CLOUDFLARE_R2_BUCKET_ENDPOINT"),
    "access_key": config("CLOUDFLARE_R2_ACCESS_KEY_ID"),
    "secret_key": config("CLOUDFLARE_R2_SECRET_KEY"),
}

if not DEBUG:
    STORAGES = {
        "default": {
                "BACKEND": "helpers.cloudflare.storages.MediaFilesStorage",
                "OPTIONS": CLOUDFLARE_R2_CONFIG_OPTIONS,
            },
            "staticfiles": {
                "BACKEND": "helpers.cloudflare.storages.StaticFilesStorage",
                "OPTIONS": CLOUDFLARE_R2_CONFIG_OPTIONS,
            },
    }
    
else:
    MEDIA_URL = f"https://pub-95a9accfe57c4be5be0b8b1b4d28e9e2.r2.dev/media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email settings
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

# Load Redis configuration from .env
REDIS_HOST = config('REDIS_HOST', default='localhost')
REDIS_PORT = config('REDIS_PORT', default='6379', cast=int)
REDIS_PASSWORD = config('REDIS_PASSWORD', default='')
REDIS_SSL = config('REDIS_SSL', default=False, cast=bool)

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"rediss://default:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "SSL": REDIS_SSL,
        }
    }
}