from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', include('bio.urls', namespace='bio')),
    url(r'^requests/', include('activity.urls', namespace='activity')),

    url(r'^admin/', include(admin.site.urls)),
]
