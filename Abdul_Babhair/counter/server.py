from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')

def index():
	count = 0
	if "count" not in session:
		session["count"]=count
 	
 	session["count"]+=1
	# session ["counter"] = counter

	print session['count']


	return render_template("index.html")


app.run(debug=True) 