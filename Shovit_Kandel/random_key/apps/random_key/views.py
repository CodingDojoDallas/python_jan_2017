from django.shortcuts import render, redirect
import random
import string

# Create your views here.
def index(request):
	return render(request, 'random_key/home.html')

def key(request):
	print request.method
	if request.method == "POST":
		print("*"*50)

		request.session['test'] = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(17)])
		return redirect('/')
	else:
		return redirect('/')