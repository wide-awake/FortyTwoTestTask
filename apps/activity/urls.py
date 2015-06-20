from django.conf.urls import url

from .views import HttpRequestList, ajax_polling

urlpatterns = [
    url(r'^$', HttpRequestList.as_view(), name='list'),
    url(r'^ajax/get_httpreq$', ajax_polling, name='ajax_polling')

]
