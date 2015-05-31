from django.conf.urls import patterns, url

from .views import single, ajax_update, PersonEdit

urlpatterns = patterns(
    '',
    url(r'^$', single, name='single'),
    url(r'^edit/$', PersonEdit.as_view(), name='edit'),

    url(r'edit/ajax$', ajax_update, name='ajax-update')
)
