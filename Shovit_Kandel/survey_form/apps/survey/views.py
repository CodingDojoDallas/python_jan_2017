from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
	return render(request, 'survey/form.html')

def process(request):
	
	if request.method == "POST":
		request.session['count'] = request.session['count']+1
		print request.POST 
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
	return redirect('/submit')
def post(request):
	return render(request, 'survey/submit.html')