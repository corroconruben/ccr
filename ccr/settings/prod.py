from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 

ALLOWED_HOSTS = ['corroconruben.online']

# ALLOWED_HOSTS = ['0.0.0.0', 'corroconruben.online']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ccr',
        'USER': 'ruben',
        'PASSWORD': 'nebur',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [BASE_DIR / 'static']