from settings.setting_base import *  # NOQA

# NOQA�������ǣ�����PEP 8�淶���ߣ����ﲻ��Ҫ���

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # �Զ������
    'user',

    # DRF
    'rest_framework',
]

# ���ݿ�����
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": "root",
        "PASSWORD": "123",
        "NAME": "vue_django_advance",
    }
}

# ����·������
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

ROOT_URLCONF = 'settings.urls'

WSGI_APPLICATION = 'settings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

# �Զ����û�ģ������
AUTH_USER_MODEL = 'user.UserModel'
