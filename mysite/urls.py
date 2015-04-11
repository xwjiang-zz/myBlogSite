from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^polls/', include('polls.urls', namespace = "polls")),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
   #url('^accounts/', include('django.contrib.auth.urls')),
)
