from flask import Flask, render_template, session, redirect

#ASSIGNMENT: COUNTER
app = Flask(__name__)
app.secret_key = 'NinjaSuperSecret' # this is the secrete key for 

@app.route('/')
def index():
	if not 'counter' in session:
		session['counter'] = 0 
	session['counter'] += 1 # will increment the counter by 2

	return render_template('index.html', name='Henry Garmendia')

@app.route('/kick', methods=['POST'])
def kick():
	session['counter'] += 1 # will increment the counter by 2

	return redirect('/') # will refresh the broser and alway increment the counter

@app.route('/cool', methods=['POST'])
def cool():
	session['counter'] = 0 # this will decrement the counter to 1

	return redirect('/') # will refresh the browser

app.run(debug=True)  # always need it to run server