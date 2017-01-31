from django.conf.urls import url

from . import views

app_name = 'website'
urlpatterns = [
    url(r'^run/(?P<package_id>[0-9a-zA-Z\-]+)/$', views.run, name="run"),
    url(r'^setup/$', views.setup, name="setup")
]