from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = 'thisisnotacookie'

@app.route('/')
def counting():
	if 'counter' not in session:
		session['counter'] = 0

	for counter in session:
		session['counter'] += 1


	return render_template("index.html", counter = session['counter'])
app.run(debug = True)