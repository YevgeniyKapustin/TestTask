"""Django's settings for stripe project."""
from pathlib import Path
from typing import Any, List

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class DjangoSettings(BaseSettings):
    """Manage all the project settings"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.DATABASES: dict = self.__get_databases()

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    SECRET_KEY: str
    DEBUG: bool

    ALLOWED_HOSTS: List[str] = ['*']

    LANGUAGE_CODE: str = 'ru'
    TIME_ZONE: str = 'Europe/Moscow'
    USE_I18N: bool = True
    USE_TZ: bool = True

    INSTALLED_APPS: list[str] = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'main'
    ]

    MIDDLEWARE: list[str] = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF: str = 'config.urls'

    TEMPLATES: list[dict] = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [Path(BASE_DIR).joinpath('templates')],
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

    WSGI_APPLICATION: str = 'config.wsgi.application'

    DATABASE_ENGINE: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASES: dict = {'default': None}

    AUTH_PASSWORD_VALIDATORS: list[dict] = [
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

    STATIC_URL: str = 'static/'
    STATIC_ROOT: str = Path(BASE_DIR).joinpath('static').__str__()
    STATICFILES_DIRS: list[str] = []

    MEDIA_URL: str = 'media/'
    MEDIA_ROOT: str = Path(BASE_DIR).joinpath('media').__str__()

    DEFAULT_AUTO_FIELD: str = 'django.db.models.BigAutoField'

    def __get_databases(self) -> dict:
        return {
            'default': {
                'ENGINE': self.DATABASE_ENGINE,
                'NAME': self.DATABASE_NAME,
                'USER': self.DATABASE_USER,
                'PASSWORD': self.DATABASE_PASSWORD,
                'HOST': self.DATABASE_HOST,
                'PORT': self.DATABASE_PORT
            }
        }

    class Config:
        env_file: str = '../.env'
        env_file_encoding: str = 'utf-8'


load_dotenv()
_settings: dict = DjangoSettings().model_dump()


def __dir__() -> List[str]:
    """The list of available options from DjangoSettings object."""
    return list(_settings.keys())


def __getattr__(name: str) -> Any:
    """Turn the module access into a DjangoSettings access."""
    return _settings.get(name)
