from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^listing/(?P<pk>[0-9]+)/$', views.listing_detail, name='listing_detail'),
    url(r'^listing/new/$', views.list_new, name='list_new'),
    url(r'^listing/(?P<pk>[0-9]+)/edit/$', views.list_edit, name='list_edit'),

]
