import os
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

"""env"""

env = environ.Env()
env_path = os.path.join(BASE_DIR.parent.parent, '.env')
env.read_env(env_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'user.User'
# LOGIN_REDIRECT_URL = 'home'
# LOGOUT_REDIRECT_URL = 'home'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.parent / 'static'
STATICFILES_DIRS = [
    'user/static/',
    'blog/static/',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent / 'media'

DB_NAME = env('DB_NAME')
DB_USER = env('DB_USER')
DB_PASS = env('DB_PASS')
DB_HOST = env('DB_HOST')
DB_PORT = env('DB_PORT')

