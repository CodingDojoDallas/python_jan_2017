from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add_course$', views.add_course, name="add_course"),
    url(r'^destroy/(?P<id>\d+)', views.delete, name="destroy"),
    url(r'^courses/destroy/(?P<id>\d+)', views.delete_course, name="destroy_confirmation"),
    url(r'^coursetouser/$', views.course_to_user, name="course_user"),
    url(r'^process_course_user$', views.process_course_user, name="process_course_user")
]
