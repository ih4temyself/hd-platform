from django.urls import reverse_lazy
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_USER_MODEL = "accounts.User"

LOGIN_URL = reverse_lazy("authors:login") 
LOGIN_REDIRECT_URL = reverse_lazy("authors:dashboard")
LOGOUT_REDIRECT_URL = LOGIN_URL    
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-dpkt80l0as%zf0dw5$3b2t4(v#k*+gsja*q%c3b1!%z0_#c!p("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

if not DEBUG:                       # production-only hardening
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 60 * 60 * 24 * 365
else:                               # local dev: keep things simple
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_SSL_REDIRECT = False

# Application definition
INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'authors',
    'articles',
    'hd_platform',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_ckeditor_5'
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

ROOT_URLCONF = 'hd_platform.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'hd_platform.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Enhanced CKEditor 5 settings for web documentation
CKEDITOR_5_CONFIGS  = {
    'default': {
        'toolbar': [
            'heading', '|',
            'bold', 'italic', 'strikethrough', 'underline', '|',
            'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', '|',
            'alignment', '|',
            'numberedList', 'bulletedList', '|',
            'indent', 'outdent', '|',
            'link', 'blockQuote', 'insertTable', 'mediaEmbed', '|',
            'imageUpload', 'imageStyle:full', 'imageStyle:side', '|',
            'code', 'codeBlock', '|',
            'horizontalLine', 'specialCharacters', '|',
            'undo', 'redo', '|',
            'removeFormat'
        ],
        'height': 500,
        'width': '100%',
        'language': 'en',
        'image': {
            'toolbar': [
                'imageTextAlternative',
                'imageStyle:full',
                'imageStyle:side',
                'linkImage'
            ],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignCenter',
                'alignRight'
            ]
        },
        'table': {
            'contentToolbar': [
                'tableColumn',
                'tableRow',
                'mergeTableCells',
                'tableProperties',
                'tableCellProperties'
            ]
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'},
                {'model': 'heading4', 'view': 'h4', 'title': 'Heading 4', 'class': 'ck-heading_heading4'},
                {'model': 'heading5', 'view': 'h5', 'title': 'Heading 5', 'class': 'ck-heading_heading5'},
                {'model': 'heading6', 'view': 'h6', 'title': 'Heading 6', 'class': 'ck-heading_heading6'}
            ]
        },
        'fontSize': {
            'options': [10, 12, 14, 'default', 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        },
        'fontFamily': {
            'options': [
                'default',
                'Arial, Helvetica, sans-serif',
                'Courier New, Courier, monospace',
                'Georgia, serif',
                'Lucida Sans Unicode, Lucida Grande, sans-serif',
                'Tahoma, Geneva, sans-serif',
                'Times New Roman, Times, serif',
                'Trebuchet MS, Helvetica, sans-serif',
                'Verdana, Geneva, sans-serif'
            ]
        },
        'fontColor': {
            'colors': [
                {'label': 'Black', 'color': '#000000'},
                {'label': 'White', 'color': '#ffffff'},
                {'label': 'Red', 'color': '#ff0000'},
                {'label': 'Green', 'color': '#00ff00'},
                {'label': 'Blue', 'color': '#0000ff'},
                {'label': 'Yellow', 'color': '#ffff00'},
                {'label': 'Cyan', 'color': '#00ffff'},
                {'label': 'Magenta', 'color': '#ff00ff'},
                {'label': 'Gray', 'color': '#808080'},
                {'label': 'Dark Gray', 'color': '#404040'},
                {'label': 'Light Gray', 'color': '#c0c0c0'}
            ]
        },
        'fontBackgroundColor': {
            'colors': [
                {'label': 'Black', 'color': '#000000'},
                {'label': 'White', 'color': '#ffffff'},
                {'label': 'Red', 'color': '#ff0000'},
                {'label': 'Green', 'color': '#00ff00'},
                {'label': 'Blue', 'color': '#0000ff'},
                {'label': 'Yellow', 'color': '#ffff00'},
                {'label': 'Cyan', 'color': '#00ffff'},
                {'label': 'Magenta', 'color': '#ff00ff'},
                {'label': 'Gray', 'color': '#808080'},
                {'label': 'Dark Gray', 'color': '#404040'},
                {'label': 'Light Gray', 'color': '#c0c0c0'}
            ]
        },
        'link': {
            'decorators': {
                'addTargetToExternalLinks': True,
                'defaultProtocol': 'https://',
                'toggleDownloadable': {
                    'mode': 'manual',
                    'label': 'Downloadable',
                    'attributes': {
                        'download': 'file'
                    }
                }
            }
        },
        'code': {
            'languages': [
                {'language': 'html', 'label': 'HTML'},
                {'language': 'css', 'label': 'CSS'},
                {'language': 'javascript', 'label': 'JavaScript'},
                {'language': 'python', 'label': 'Python'},
                {'language': 'java', 'label': 'Java'},
                {'language': 'cpp', 'label': 'C++'},
                {'language': 'csharp', 'label': 'C#'},
                {'language': 'php', 'label': 'PHP'},
                {'language': 'sql', 'label': 'SQL'},
                {'language': 'bash', 'label': 'Bash'},
                {'language': 'json', 'label': 'JSON'},
                {'language': 'xml', 'label': 'XML'},
                {'language': 'yaml', 'label': 'YAML'},
                {'language': 'markdown', 'label': 'Markdown'}
            ]
        }
    },
}