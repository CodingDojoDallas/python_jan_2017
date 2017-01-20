from django.shortcuts import render, HttpResponse
from django.utils import timezone
import datetime
# Create your views here.
def index(request):
    context = {
        "time":datetime.datetime.now().strftime('%B %Y, %I:%M:%S %p')
        #        "time":timezone.now()
    }
    return render(request,'timedisplay/index.html', context)
