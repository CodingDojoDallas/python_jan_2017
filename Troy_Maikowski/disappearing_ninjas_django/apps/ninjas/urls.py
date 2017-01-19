from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<color>\w+)', views.show_turtle)
]
