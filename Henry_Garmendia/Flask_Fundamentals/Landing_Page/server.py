from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', name='Henry Garmendia')

@app.route('/ninjas')
def ninjas():
	return render_template('ninjas.html', name='Real Ninjas')

@app.route('/dojos/new')
def dojos():
	return render_template('dojos.html', name='Henry Garmendia | Real Ninja')

app.run(debug=True)