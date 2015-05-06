from django.conf.urls import patterns, url

from .views import single

urlpatterns = [
    url(r'^$', single, name='single')
]
