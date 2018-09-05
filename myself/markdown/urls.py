from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^add_md/$', add_markdown_views, name='add_md'),
    url(r'^show_md/(\d+)/$', show_markdown_views),
]


