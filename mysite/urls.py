from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
admin.autodiscover()


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('objbasa.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
]
