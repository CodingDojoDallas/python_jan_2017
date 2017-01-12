from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random
app = Flask(__name__)
app.secret_key = 'mysuperdupersecretkey'

timestamp = datetime.now().strftime('%Y/%m/%d %-I:%S %p')
print timestamp

# session['history'] = []
# msg = {
#     'msg':'afadfa',
#     'class': 'red' or 'green'
# }

@app.route('/')
def index():
    if 'bank' not in session:
        session['bank'] = 0       

    elif 'luck' 'farm' 'cave' 'house' 'casino' 'bank' not in session:
        session['luck'] = random.randrange(0,2)
        session['farm'] = random.randrange(10,21)
        session['cave'] = random.randrange(5,11)
        session['house'] = random.randrange(2,6)
        session['casino'] = random.randrange(0,51)
        

    return render_template('index.html')

@app.route('/process_gold', methods = ['POST'])
def game():
    if request.form['location'] == 'farm':
        session['history'] += "Earned {} gold from the farm! ( {} )".format(session['farm'], timestamp)
        session['bank'] += session['farm']

    if request.form['location'] == 'cave':
        session['history'] += "Earned {} gold from exploring a cave! ( {} )".format(session['cave'], timestamp)
        session['bank'] += session['cave']
    
    if request.form['location'] == 'house':
        session['history'] += "Earned {} gold from the house! ( {} )".format(session['house'], timestamp)
        session['bank'] += session['house']
    
    if request.form['location'] == 'casino':
        if session['luck'] == 1 :
            session['history'] += "Earned {} gold from the casino! ( {} )".format(session['casino'], timestamp)
            session['bank'] += session['casino']
        else:
            session['history'] += "Entered a casino and lost {} gold... Ouch.. ( {} )".format(session['casino'], timestamp)
            session['bank'] -= session['casino']
     
    
    print session['bank']
    return redirect('/')


app.run(debug = True)