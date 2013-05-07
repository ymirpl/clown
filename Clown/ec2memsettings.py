import dj_database_url
DATABASES = {'default': dj_database_url.config()}
DOMAIN = "blade-clown.herokuapp.com"

CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'LOCATION': 'ec2-107-20-107-150.compute-1.amazonaws.com:11211',
        'BINARY': True,
        'TIMEOUT': 500
    }
}
