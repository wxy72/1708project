from django.conf.urls import url

from post import views



urlpatterns = [
 	url(r'^list/$', views.post_list),
    url(r'^create/$', views.create_post),
    url(r'^edit/$', views.edit_post),
    url(r'^read/$', views.read_post),
]