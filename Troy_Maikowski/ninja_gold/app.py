from flask import Flask, url_for, render_template, request, session, redirect
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = "Massive secret ninja gold key"

@app.route('/')
def index():
    if not session.has_key('gold_count'):
        session['gold_count'] = 0
    if not session.has_key('activities'):
        session['activities'] = []
    return render_template("index.html")

@app.route('/process_money', methods=["POST"])
def process_money():
    location = request.form['building']
    if location == "farm":
        gold = round(random.random()*10+10)
        activity = "Earned {} golds from the farm! ({})".format(gold, datetime.today())
    elif location == "cave":
        gold = round(random.random()*5+5)
        activity = "Earned {} golds from the cave! ({})".format(gold, datetime.today())
    elif location == "house":
        gold = round(random.random()*3+2)
        activity = "Earned {} golds from the house! ({})".format(gold, datetime.today())
    else: #casino
        earn_or_lose = random.random()
        gold = round(random.random()*50)
        activity = "Entered the casino and won {} golds! Congrats! ({})".format(gold, datetime.today())
        if earn_or_lose < 0.5:
            gold *= -1
            activity = "Entered a casino and lost {} golds... Ouch. ({})".format(gold * -1, datetime.today())
    session['activities'].append(activity)
    session['gold_count'] += gold
    return redirect('/')

app.run(debug=True)