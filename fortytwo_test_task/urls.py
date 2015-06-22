from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('bio.urls', namespace='bio')),
    url(r'^requests/', include('activity.urls', namespace='activity')),

    url(r'^admin/', include(admin.site.urls)),
)

# for local development
# if settings.DEBUG:
urlpatterns += patterns(
    'django.views.static',
    url(r'^static/(.*)$', 'serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^uploads/(.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}))