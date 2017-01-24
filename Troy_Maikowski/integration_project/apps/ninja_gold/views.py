from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from datetime import datetime
import random

# Create your views here.
def index(request):
    if 'gold_count' not in request.session:
        request.session['gold_count'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'ninja_gold/index.html')

def process_money(request):
    if request.method == "POST":
        if request.POST['building'] == "farm":
            gold = random.randrange(10,21)
            msg = "Earned {} golds from the farm! ({})".format(gold, datetime.now())
        elif request.POST['building'] == "cave":
            gold = random.randrange(5,11)
            msg = "Earned {} golds from the cave! ({})".format(gold, datetime.now())
        elif request.POST['building'] == "house":
            gold = random.randrange(2,6)
            msg = "Earned {} golds from the house! ({})".format(gold, datetime.now())
        else:
            gold = random.randrange(0,51)
            msg = "Earned {} golds from the casino! ({})".format(gold, datetime.now())
            if random.random() > 0.5:
                gold *= -1
                msg = "Lost {} golds from the casino... Ouch.".format(gold, datetime.now())
        request.session['gold_count'] += gold
        request.session['activities'].append(msg)
        # return redirect('/')
        return redirect(reverse("ninja_gold:home"))
    else:
        print "Redirected..."
        # return redirect('/')
        return redirect(reverse("ninja_gold:home"))
