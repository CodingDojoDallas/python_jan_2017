from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^show/(?P<id>\d+)$', views.show, name="show"),
    url(r'^edit/(?P<id>\d+)$', views.edit, name="edit"),
    url(r'^new/$', views.add, name="add"),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name="destroy"),
    url(r'^update/(?P<id>\d+)$', views.update, name="update"),
    url(r'^create/$', views.create, name="create")
]
