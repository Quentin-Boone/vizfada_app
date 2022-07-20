from .base import *

DEBUG = True

DATA_SERVER = {"cluster": "http://data-test-svc:90",
               "external": "https://viz.faang.org/data"}

SESSION_COOKIE_DOMAIN = "viz.faang.org"
SESSION_SAVE_EVERY_REQUEST = True

ALLOWED_HOSTS = ["45.88.80.133", "localhost", "127.0.0.1", "django-test-svc", "viz.faang.org"]

# INTERNAL_IPS = ["0.0.0.0"]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^http://localhost:[0-9]*",
    r"^http://45.88.80.133:[0-9]*",
    r"^http://127.0.0.1:[0-9]*",
    r"^http://viz.faang.org/.*",
    r"^https://viz.faang.org/.*"
]

CORS_ALLOWED_ORIGINS = [
    'http://45.88.80.133/',
    'http://45.88.80.133',
    'http://localhost:4200',
    'http://127.0.0.1:4200',
    'http://0.0.0.0:4200',
    'http://localhost:8080',
    'http://127.0.0.1:8080',
    'http://0.0.0.0:8080',
    'http://localhost:90',
    'http://127.0.0.1:90',
    'http://0.0.0.0:90',
    'http://data-test-svc:90/',
    'http://ng-test-svc:4200/',
    'http://django-test-svc:8000/',
    'http://viz.faang.org/*',
    'https://viz.faang.org/*'
]

CSRF_TRUSTED_ORIGIN = [
    'https://viz.faang.org/*'
]
SESSION_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_SAMESITE = "Lax"

SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = True
# SECURE_SSL_HOST = "https://viz.faang.org/django"