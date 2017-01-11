from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secrete_key = 'kdine3m0jl2sgx898mcns'

@app.route('/')
def index():
	return render_template('index.html', name='Henry Garmendia')

@app.route('/result')
def result():
	return render_template('result.html')

@app.route('/users', methods=['POST'])
def create_user():
	print "Got Post Info"
	# we'll talk about the following two lines after we learn a little more
	# about forms
	session['fullName'] = request.form['full_name']
	session['cityLoc'] = request.form['location']
	session['favLang'] = request.form['fav-track']
	session['textArea'] = request.form['areatext']
	# redirects back to the '/' route
	return render_template('result.html')

app.run(debug=True)  # run our server