from django.shortcuts import render, redirect
import random, string
# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'mywordgen/index.html')
    
def word(request):
    if request.method == "POST":
        request.session['count'] +=1
        randomstring = ''.join(random.choice(string.ascii_uppercase + string.digits) for n in xrange(32))
        context = {
            "randomstring":randomstring
        }
        request.session['mystring'] = randomstring
    return redirect('/')

def clear(request):
    if request.method == "POST":
        request.session.clear()
    return redirect('/')
    