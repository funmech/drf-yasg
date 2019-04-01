import dj_database_url

from .base import *  # noqa: F403

SECRET_KEY = '64e21445366b55975b9c842f34943cf37ae638329a8c518ac6232cd9ef13fff6'

DEBUG = True

# In GAE Standard env, db is read-only
# log in needs to write to session tables?, so disable auth
SWAGGER_SETTINGS['USE_SESSION_AUTH'] = None

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

ALLOWED_HOSTS.append('.appspot.com')

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

SILENCED_SYSTEM_CHECKS = [
    'security.W004',  # SECURE_HSTS_SECONDS
    'security.W008',  # SECURE_SSL_REDIRECT
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = 'staticfiles'
