from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^add_post/$', views.add_post, name='add_post'),
        url(r'^list_post/$', views.list_post, name='list_post'),
        url(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post_detail')
        )


