from pathlib import Path, os
from django.conf import settings
from dotenv import load_dotenv
import django_heroku
import dj_database_url

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.pages.apps.PagesConfig',
    'apps.users.apps.UsersConfig',
    'apps.main_crud.apps.MainCrudConfig',
    'apps.pictures.apps.PicturesConfig',
    'apps.search_location.apps.SearchLocationConfig',
    'rangefilter',
    "crispy_forms",
    "crispy_bootstrap4",
    "import_export",
    "storages",
    "django_bunny_storage",
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.pictures.middlewares.LargeFileUploadMiddleware',
    'apps.pictures.middlewares.AutoLogoutMiddleware',
]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'setup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "setup/static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files (uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Converted images storage
CONVERTED_IMAGES_DIR = os.path.join(MEDIA_ROOT, 'converted_images')
CONVERTED_IMAGES_URL = f'{MEDIA_URL}converted_images/'
os.makedirs(CONVERTED_IMAGES_DIR, exist_ok=True)

# Headers and CacheControl (equivalente ao AWS_S3_OBJECT_PARAMETERS)
BUNNY_HEADERS = {
    'Access-Control-Allow-Origin': '*',
    'CacheControl': 'max-age=86400',  # Configuração de cache
}

# Desabilitar a autenticação via querystring, similar ao AWS_QUERYSTRING_AUTH = False
BUNNY_QUERYSTRING_AUTH = False


#Authentication
LOGIN_REDIRECT_URL = 'userOrders--page'
LOGOUT_REDIRECT_URL = 'logout'
LOGIN_URL = 'login'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

DATA_UPLOAD_MAX_NUMBER_FILES = 10000 # or any number you need

DATA_UPLOAD_MAX_MEMORY_SIZE = 500 * 1024 * 1024 * 1024  # 500 GB
FILE_UPLOAD_MAX_MEMORY_SIZE = 500 * 1024 * 1024 * 1024  # 500 GB


AUTH_USER_MODEL = 'users.CustomUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', 
    'apps.users.authentication.EmailOrUsernameModelBackend',  
]

AUTO_LOGOUT_DELAY = 1800

SESSION_COOKIE_AGE = 1800  # 30 min

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_SAVE_EVERY_REQUEST = True
