from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_p^b4l%aoj3$481u50h)=@3-2^bu--wf2i#)mfz$$tytc#5uc%'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
NEWSLETTER_CONFIRM_EMAIL = False
SITE_ID = 1

try:
    from .local import *
except ImportError:
    pass

# COMPRESS_OFFLINE = True
# LIBSASS_OUTPUT_STYLE = 'compressed'
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
