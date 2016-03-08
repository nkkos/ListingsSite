from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^listing/(?P<pk>[0-9]+)/$', views.listing_detail, name='listing_detail'),
]
