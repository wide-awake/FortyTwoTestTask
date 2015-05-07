from django.conf.urls import url

from .views import HttpRequestList

urlpatterns = [
    url(r'^$', HttpRequestList.as_view(), name='list')
]
