from settings.setting_base import *  # NOQA

# NOQA的作用是，告诉PEP 8规范工具，这里不需要检测

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 自定义组件
    'user',

    # DRF
    'rest_framework',
]

# 数据库设置
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

# 导包路径更改
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

ROOT_URLCONF = 'settings.urls'

WSGI_APPLICATION = 'settings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

# 自定义用户模块声明
AUTH_USER_MODEL = 'user.UserModel'
