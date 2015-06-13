from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import single, ajax_update, PersonEdit

urlpatterns = patterns(
    '',
    url(r'^$', single, name='single'),
    url(r'^edit/$', login_required(PersonEdit.as_view()), name='edit'),

    url(r'edit/ajax$', login_required(ajax_update), name='ajax-update')
)
