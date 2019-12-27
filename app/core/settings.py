import environ
from pathlib import Path

env = environ.Env(
    DEBUG=(bool, False),
)

CORE_DIR = Path(__file__).parent
PROJECT_DIR = CORE_DIR.parent
BASE_DIR = PROJECT_DIR.parent

environ.Env.read_env(env_file=str(BASE_DIR / '.env'))

DEBUG = env.bool('DEBUG')

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticdist'

STATICFILES_DIRS = (
    PROJECT_DIR /'static',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR / 'core' / 'templates',],
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


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_extensions',
    "celery",
    "django_celery_beat",

    'core.apps.CoreConfig',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth.socialaccount.providers.slack',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.gitlab',
    # 'allauth.socialaccount.providers.openid',
]

AUTH_USER_MODEL = 'core.Member'

DATABASES = {
    'default': env.db_url(),
}

CACHES = {
    'default': env.cache_url(),
}

CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

LOGIN_REDIRECT_URL = 'home'

# SOCIALACCOUNT_PROVIDERS = {
#     'gitlab': {
#         'GITLAB_URL': 'https://gitlab.com',
#         'SCOPE': ['read_user'],
#     },
#     'openid': {
#         'SERVERS': [
#             # dict(id='google',
#             #      name='Google',
#             #      openid_url='https://www.google.com/accounts/o8/id'),
#         ]
#     }
# }

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
