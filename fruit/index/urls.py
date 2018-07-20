from django.conf.urls import url
from .views import *
urlpatterns = [
    url('^login$', login_views),
]
urlpatterns += [
    url(r'^add_author/$', add_author_views),
    url(r'^add_book/$', add_book_views),
    url(r'^add_publisher/$', add_publisher_views),
]


urlpatterns += [
    url(r'^get_author/$', get_author_views),
]
