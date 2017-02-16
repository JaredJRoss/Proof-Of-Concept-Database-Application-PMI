
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'OGDB',
    'USER':'admin',
    'PASSWORD':'admin' ,
    'HOST':'localhost',
    'PORT':'',
    }
}

DEBUG = True