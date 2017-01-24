from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new/$', views.add, name="add"),
    url(r'^(?P<id>)$', views.show, name="show"),
    url(r'^create$', views.create, name="create")
]
