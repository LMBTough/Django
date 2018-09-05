from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', origin_views),
]
