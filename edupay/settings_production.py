from settings import *

DEBUG = False

STATIC_ROOT = '/home/deone/webapps/edupay_static'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'edupay',
        'USER': 'edupay',
        'PASSWORD': '3dUpASs',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}