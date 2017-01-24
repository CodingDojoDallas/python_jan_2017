from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'ninjas/index.html')

def show_turtle(request, color):
    context = {
        'color': color
    }
    return render(request, 'ninjas/show.html', context)
