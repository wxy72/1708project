from django.conf.urls import url

from user import views



urlpatterns = [
 	url(r'^login_in/$', views.login_in),
    url(r'^register/$', views.register),
    url(r'^info/$', views.info),
    url(r'^loginout/$', views.loginout),

]