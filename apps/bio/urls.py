from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^$', 'bio.urls', name='bio'),
]
