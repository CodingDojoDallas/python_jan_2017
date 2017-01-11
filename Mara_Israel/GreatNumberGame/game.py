from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'applesandbananas'

import random



@app.route('/')
def generate_game():
	if 'random' not in session:
		session['random'] = random.randrange(1,101)
	return render_template("index.html")

@app.route('/results', methods = ['POST'])

def results():
	return render_template("results.html")

	for random in session:
		if request.form['guess'] >= session['random'] + 1 :
			return 'Too High'
		elif request.form['guess'] >= session['random'] - 1 :
			return 'Too low'
		else:
			return session['random'], 'was the number.'
			session.pop('random')
	
	# return redirect('/results')


app.run(debug = True)
