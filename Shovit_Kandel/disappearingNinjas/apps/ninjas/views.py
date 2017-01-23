from django.shortcuts import render

# Create your views here.
def index(request):
	print "hello"
	return render(request, 'ninjas/index.html')

def ninjas(request):
	return render(request, 'ninjas/ninjas.html')

def color(request, id):
	print id
	context = {
	"id": id
	}
	return render(request, "ninjas/1ninja.html", context)