from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/?$', views.addUserInfo, name='add'),
    url(r'^fetch/?$', views.fetchUserInfo, name='fetch'),
]
