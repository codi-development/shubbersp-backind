import os
from pathlib import Path
from dotenv import load_dotenv
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-change-me-in-production')

DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

INSTALLED_APPS = [
    'unfold',
    'unfold.contrib.filters',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'portfolio',
    'contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ─── Internationalization ───
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Baghdad'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('ar', _('العربية')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Static & Media
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS
CORS_ALLOWED_ORIGINS = os.getenv(
    'CORS_ALLOWED_ORIGINS',
    'http://localhost:5173,http://localhost:3000,http://localhost:5174'
).split(',')

# Email
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True').lower() == 'true'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
CONTACT_EMAIL = os.getenv('CONTACT_EMAIL', '')

# ─── Unfold Admin Theme ───
UNFOLD = {
    "SITE_TITLE": "Shubber SB",
    "SITE_HEADER": "Shubber SB",
    "SITE_SUBHEADER": _("Administration Panel"),
    "SITE_URL": "/",
    "SITE_SYMBOL": "local_pharmacy",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "SHOW_LANGUAGES": True,
    "LANGUAGE_FLAGS": {
        "en": "🇬🇧",
        "ar": "🇮🇶",
    },
    "THEME": "light",
    "STYLES": [
        lambda request: static("admin/css/rtl-fixes.css"),
    ],
    "COLORS": {
        "primary": {
            "50": "#FFF7ED",
            "100": "#FFEDD5",
            "200": "#FED7AA",
            "300": "#FDBA74",
            "400": "#FB923C",
            "500": "#E26314",
            "600": "#D45A10",
            "700": "#B54D0E",
            "800": "#8C3D0F",
            "900": "#6B3010",
            "950": "#3D1A08",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "title": _("Dashboard"),
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Home"),
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index"),
                    },
                ],
            },
            {
                "title": _("Content Management"),
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("News"),
                        "icon": "newspaper",
                        "link": reverse_lazy("admin:portfolio_news_changelist"),
                    },
                    {
                        "title": _("Gallery"),
                        "icon": "photo_library",
                        "link": reverse_lazy("admin:portfolio_galleryimage_changelist"),
                    },
                    {
                        "title": _("Partners"),
                        "icon": "handshake",
                        "link": reverse_lazy("admin:portfolio_partner_changelist"),
                    },
                ],
            },
            {
                "title": _("Careers"),
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Job Positions"),
                        "icon": "work",
                        "link": reverse_lazy("admin:portfolio_career_changelist"),
                    },
                    {
                        "title": _("Applications"),
                        "icon": "assignment_ind",
                        "link": reverse_lazy("admin:portfolio_jobapplication_changelist"),
                    },
                ],
            },
            {
                "title": _("Messages"),
                "separator": True,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Contact Messages"),
                        "icon": "mail",
                        "link": reverse_lazy("admin:contact_contactmessage_changelist"),
                        "badge": "contact.utils.unread_count",
                    },
                ],
            },
            {
                "title": _("Settings"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "group_work",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
        ],
    },
}
