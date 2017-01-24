from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<id>\d+)$', views.show, name="show"),
    url(r'^new/$', views.new_book, name="new_book"),
    url(r'^new_review/$', views.new_review, name="new_review"),
    url(r'^create/$', views.create, name="create"),
    url(r'^edit/(?P<id>\d+)$', views.edit, name="edit"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete")
]
