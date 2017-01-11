from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = "Huge Secret"

@app.route('/', methods=["GET", "POST"])
def index():
    if not session.has_key('guess'):
        session['guess'] = random.randrange(1,101)
    print session['guess'] #for ease of debugging. Remove in production
    return render_template("index.html")

@app.route('/process_guess', methods=["POST"])
def process_guess():
    reset_button = False
    if int(request.form['guess']) == int(session['guess']):
        message = "Congrats! " + str(session['guess']) + " was the correct answer!"
        reset_button = True
    elif int(request.form['guess']) < int(session['guess']):
        message = "Too low!"
    else:
        message = "Too high!"
    return render_template('index.html', message=message, reset_button=reset_button)

@app.route('/reset', methods=["POST"])
def reset():
    session.pop('guess')
    return redirect('/')

app.run(debug=True)