from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    request.session.clear()
    if 'count' not in request.session:
        request.session['count'] = 0
        print "*"*50
        print request.session['count']
        print "*"*50
    return render(request, 'mysurvey/index.html')
def process(request):
    if request.method == "POST":
        request.session['count'] += 1
        request.session['name']= request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['lang'] = request.POST['language']
        request.session['comment'] = request.POST['comment']  
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    return render(request, 'mysurvey/result.html')

def goback(request):
    return redirect('/')
    
    

    
    