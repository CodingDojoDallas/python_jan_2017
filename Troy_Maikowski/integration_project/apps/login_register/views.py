from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import User

import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login_register/index.html')

def show(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'login_register/show.html', context)

def process_registration(request):
    if request.method == "POST":
        validation_obj = User.objects.register(request.POST)
        if 'errors' in validation_obj:
            for error in validation_obj['errors']:
                messages.add_message(request, messages.ERROR, error)
        elif 'user' in validation_obj:
            request.session['full_name'] = validation_obj['user']
            User.objects.create(
                first_name = request.POST['fname'],
                last_name = request.POST['lname'],
                email = request.POST['email'],
                password = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()),
                course_id=0
            )
            return redirect(reverse('login_registration:show'))
        else:
            print "Something went terribly wrong"
    return redirect('/')

def process_login(request):
    if request.method == "POST":
        validation_obj = User.objects.login(request.POST)
        if 'errors' in validation_obj:
            for error in validation_obj['errors']:
                messages.add_message(request, messages.ERROR, error)
        elif 'user' in validation_obj:
            request.session['full_name'] = validation_obj['user']
            return redirect(reverse('login_registration:show'))
        else:
            messages.add_message(request, messages.ERROR, "Something went horribly wrong")
    return redirect(reverse('login_registration:index'))
