from django.conf.urls import url

from . import views

app_name = 'website'
urlpatterns = [
    url(r'^run/(?P<package_id>[0-9a-zA-Z\-]+)/$', views.run, name="run"),
    url(r'^run-process/(?P<package_id>[0-9a-zA-Z\-]+)/$', views.run_process, name="run-process"),
    url(r'^setup/$', views.setup, name="setup")
]