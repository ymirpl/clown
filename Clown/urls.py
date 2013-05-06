from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tuit/', include('tuitter.urls')),
    url(r'^accounts/', include('profiles.urls')),
    url(r'^mu-.*$', 'misc.views.return_42', {}, '42'),
    url(r'^$', 'misc.views.index', {}, 'index'),
    url(r'^jinja2/$', 'misc.views.index_jinja2', {}, 'index_jinja2'),
)

if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
