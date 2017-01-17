from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'survey/index.html')

def process_survey(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
    if request.method == "POST":
        request.session['name'] = request.POST['fname']
        request.session['dojo_loc'] = request.POST['dojo_loc']
        request.session['fav_lang'] = request.POST['fav_lang']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect("/")

def result(request):
    return render(request, 'survey/result.html')
