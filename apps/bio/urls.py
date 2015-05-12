from django.conf.urls import url

from .views import single

urlpatterns = [
    url(r'^$', single, name='single')
]
