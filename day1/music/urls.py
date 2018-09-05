from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^music_info/$', show_info),
    url(r'^first$', first_views),
    url(r'^second$', second_views, name='my'),
    url(r'^show/(\d+)/(\d+)/$', show_views, name='show')
]
