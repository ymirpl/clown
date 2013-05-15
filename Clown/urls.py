from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from tuitter.api import TuitResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(TuitResource())
v1_api.register(UserResource())

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tuit/', include('tuitter.urls')),
    url(r'^accounts/', include('profiles.urls')),
    url(r'^mu-.*$', 'misc.views.return_42', {}, '42'),
    url(r'^$', 'misc.views.index', {}, 'index'),
    url(r'^without_user/$', 'misc.views.index_wo_user', {}, 'index_wo_user'),
    url(r'^jinja2/$', 'misc.views.index_jinja2', {}, 'index_jinja2'),
    url(r'^jinja2/without_user/$', 'misc.views.index_wo_user_jinja2', {}, 'index_wo_user_jinja2'),
    url(r'^json/without_user/$', 'misc.views.index_wo_user_json', {}, 'index_wo_user_json'),
    url(r'^api/', include(v1_api.urls)),
)

if settings.SERVE_STATIC_FILES:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
