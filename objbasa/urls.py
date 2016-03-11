from django.conf.urls import include, url, patterns
from . import views
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
admin.autodiscover()


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^listing/(?P<pk>[0-9]+)/$', views.listing_detail, name='listing_detail'),
    url(r'^listing/new/$', views.list_new, name='list_new'),
    url(r'^listing/(?P<pk>[0-9]+)/edit/$', views.list_edit, name='list_edit'),
    url(r'^drafts/$', views.list_draft_list, name='list_draft_list'),
    url(r'^listing/(?P<pk>[0-9]+)/publish/$', views.list_publish, name='list_publish'),
    url(r'^listing/(?P<pk>[0-9]+)/remove/$', views.list_remove, name='list_remove'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

]
