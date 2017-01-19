from flask import Flask, render_template, redirect, session, request
import random
app = Flask(__name__)
app.secret_key = 'abc'

@app.route('/')
def home():
	random_num = random.randrange(1, 101)
	if 'num' not in session:
		session['num'] = random_num
	return render_template('index.html')
	#print session['num']

@app.route('/guess', methods=['POST'])
def guess():
	guess = int(request.form['guess'])
	#guess = int(guess)
	#if session['num'] > random_num:
	if guess < session['num']:
		session['fail'] = "Too low"
	elif guess > session['num']:
		session['fail'] = "Too high"
	else:
		if 'fail' in session:
			session.pop('fail')
		session['success'] = 'The number was {}. You guessed it correctly'.format(session['num'])
	return redirect ('/')

@app.route('/reset', methods=['post'])
def reset():
	session.pop('success')
	session.pop('num')
	return redirect ('/')


app.run(debug=True)