from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^add_page/$', add_page_views, name='add_page'),
    url(r'^show_page/(.*)/$', show_page_views)
]
