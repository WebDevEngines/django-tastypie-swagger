try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from django.contrib.auth.decorators import login_required
from .views import SwaggerView, ResourcesView, SchemaView

urlpatterns = [
    url(r'^$', login_required(SwaggerView.as_view()), name='index'),
    url(r'^resources/$', login_required(ResourcesView.as_view()), name='resources'),
    url(r'^schema/(?P<resource>\S+)$', login_required(SchemaView.as_view())),
    url(r'^schema/$', login_required(SchemaView.as_view()), name='schema')
]

from django import get_version
from distutils.version import StrictVersion

if StrictVersion(get_version()) < StrictVersion("1.10"):
    try:
        from django.conf.urls import patterns
    except ImportError:
        from django.conf.urls.defaults import patterns
    urlpatterns = patterns('', *urlpatterns)
