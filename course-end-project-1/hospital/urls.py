"""hospital URL Configuration."""

from django.conf.urls import include, url

urlpatterns = [
    url(r'^commoninfo/', include('commoninfo.urls')),
]
