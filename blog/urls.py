from django.conf.urls import url
from blog import views

urlpatterns = [
    url('^$', views.post_list, name='index'),
    url('^posts/$', views.post_list, name='post_list'),
    url('^posts/new/$', views.post_new, name='post_new'),
    url('^posts/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url('^posts/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]
