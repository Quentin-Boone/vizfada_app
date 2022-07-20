from .base import *

DEBUG = True
DATA_SERVER = {"cluster": "https://viz.faang.org/data",
               "external": "https://viz.faang.org/data"}

SESSION_COOKIE_DOMAIN = "127.0.0.1"
SESSION_SAVE_EVERY_REQUEST = True

ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0"]

INTERNAL_IPS = ["0.0.0.0"]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOWED_ORIGINS = [
    'http://localhost:4200',
    'http://127.0.0.1:4200',
    'http://0.0.0.0:4200',
    'http://localhost:8080',
    'http://127.0.0.1:8080',
    'http://0.0.0.0:8080',
    'http://localhost:90',
    'http://127.0.0.1:90',
    'http://0.0.0.0:90'
]

CSRF_TRUSTED_ORIGIN = [
    'http://localhost:4200',
    'http://127.0.0.1:4200',
    'http://0.0.0.0:4200',
]

SESSION_COOKIE_HTTPONLY = False
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_SAMESITE = "Lax"

"""
CSRF_COOKIE_HTTPONLY = False
CSRF_USE_SESSIONS = False
CSRF_COOKIE_NAME = 'CSRF-TOKEN'
CSRF_HEADER_NAME = 'HTTP_X_CSRF_TOKEN'
"""