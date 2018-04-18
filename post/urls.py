from django.conf.urls import url

urlpatterns = [
 	url(r'^list/$', post_view.post_list),
    url(r'^create/$', post_view.create_post),
    url(r'^edit/$', post_view.edit_post),
    url(r'^read/$', post_view.read_post),
]