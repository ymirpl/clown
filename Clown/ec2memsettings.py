import dj_database_url
DATABASES = {'default': dj_database_url.config()}
DOMAIN = "blade-clown.herokuapp.com"

CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': '10.195.193.58:11211',
        'BINARY': True,
        'TIMEOUT': 500
    }
}
