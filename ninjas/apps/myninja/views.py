from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'myninja/index.html')

def allninja(request):
    return render(request,'myninja/allninjas.html')

def aninja(request,color):
    context = {
        "color":color
    }
    return render(request,'myninja/aninja.html',context)
