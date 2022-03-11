from .base import *
import os

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': env("POSTGRES_ENGINE"),
        'NAME': env("POSTGRES_DB"),
        'USER':env("POSTGRES_USER"),
        'PASSWORD':env("POSTGRES_PASSWORD"),
        'HOST':env("PG_HOST"),
        'PORT':env("PG_PORT"),
    }
}