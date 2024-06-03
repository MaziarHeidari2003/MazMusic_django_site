from maz_music.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%wz_k&ex%@5umh!38yceu+9pvtx0)a59udh0+**^3w8(mzt$)1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
SITE_ID = 2


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}





DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'maziarheidari1124@gmail.com'
#EMAIL_HOST_PASSWORD= os.environ.get('AA_EMAIL_HOST_PASSWORD')
EMAIL_HOST_PASSWORD= "txws rtfi ptmo jmzw"

EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "My App"


MEDIA_ROOT = BASE_DIR / 'media'
STATIC_ROOT = BASE_DIR / 'static'


STATICFILES_DIRS = [
    BASE_DIR / "statics",
]



