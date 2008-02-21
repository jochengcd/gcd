# Django settings for gcd project.
from os.path import abspath, dirname, join

# disable on production!
DEBUG          = True
TEMPLATE_DEBUG = DEBUG

# absolute path to the directory that holds templates.
TEMPLATE_DIRS = ( abspath(join(dirname(__file__), 'templates')), )

# absolute path to the directory that holds media.
# URL that handles the media served from MEDIA_ROOT.
MEDIA_ROOT = abspath(join(dirname(__file__), 'media'))
MEDIA_URL = "http://127.0.0.1:8000/site_media"

# Set to True to avoid hitting comics.org for every cover image.
# If True, the same cover image will be used for every issue.
FAKE_COVER_IMAGES = False

# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = 'GMT'

# Database settings. Override yours in a settings.local.py
# if you're not gonna stick with these development defaults.
DATABASE_ENGINE   = 'mysql'
DATABASE_NAME     = 'gcd_base'
DATABASE_USER     = 'gcd_dev'
DATABASE_PASSWORD = ''
DATABASE_HOST     = ''
DATABASE_PORT     = ''

# The router where all our site URLs is defined.
ROOT_URLCONF = 'urls'

# Corresponds to the django_site database table. As far
# as I know, we won't be using this for the GCD.
SITE_ID = 1

# Email these if there's a site exception and debug isn't on.
ADMINS = (
    ('Henry Andrews', 'andrews_henry at yahoo.com'),
    ('Morbus Iff', 'morbus@disobey.com'),
)
MANAGERS = ADMINS

# Used to provide a seed in secret-key hashing algorithms.
SECRET_KEY = 'th0lnu%wjs_8=r4u_km3shvogzd%1n)t-5eosi964g0ek+a4p+'

# Callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    # 'django.template.loaders.eggs.load_template_source',
)

# All enabled apps for this install.
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'apps.gcd',
)

