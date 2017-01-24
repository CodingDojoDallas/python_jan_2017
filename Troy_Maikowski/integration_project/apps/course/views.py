from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Count
from . import models
from ..login_register.models import User
# Create your views here.
def index(request):
    courses = models.Course.objects.all()
    context = {'courses': courses}
    return render(request, 'course/index.html', context)

def add_course(request):
    if request.method == "POST":
        models.Course.objects.create(
            name=request.POST['course_name'],
            description=request.POST['course_desc'],
        )
    return redirect(reverse('courses:index'))

def delete_course(request, id):
    course = models.Course.objects.get(id=id)
    context = {'course': course}
    return render(request, 'course/delete.html', context)

def delete(request, id):
    if request.method == "POST":
        models.Course.objects.filter(id=id).delete()
        print "Deleted"
    return redirect(reverse('courses:index'))

def course_to_user(request):
    users = User.objects.all()
    courses = models.Course.objects.all()
    # thing = models.Course.objects.all().aggregate(Count(user))
    thing = User.objects.all().aggregate(Count('course_id'))
    print "*"*50
    print thing
    print "*"*50

    users = User.objects.all().select_related()
    for user in users:
        print user.course.name

    print "*"*50
    courses = models.Course.objects.all().select_related()
    for course in courses:
        print course.enrolled_users.all()
    print "*"*50



    context = {
        'courses': courses,
        'users': users
    }
    return render(request, 'course/user_courses.html', context)

def process_course_user(request):
    user_id = request.POST['user_id']
    course_id = request.POST['course_id']
    print "*"*50
    print user_id
    print "*"*50
    print course_id
    print "*"*50
    user = User.objects.get(id=user_id)
    course = models.Course.objects.get(id=course_id)
    print "*"*50
    # print user.course_id
    print "*"*50
    user.course_id = course
    user.save()
    return redirect(reverse("courses:course_user"))
