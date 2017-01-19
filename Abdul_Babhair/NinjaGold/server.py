from flask import Flask, render_template, session, redirect, request
import random
app = Flask (__name__)
#app.secret_key = "abc"

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def earn():
	if request.form['action'] == 'farm':
		earn = int(random.randrang(10,21))

	elif request.form['action'] == 'cave':
		earn = random.randrang(5,11)

	elif request.form['action'] == 'house':
		earn = random.randrang(2,6)

	else: #request.form['action'] == 'casion':
		earn = random.randrang(0,51)

	# print earn
	#if 'earn' not in session:
	#	session['earn'] = earn

	#if request.form['action'] == 'register':
  	#//do registration process
	#elif request.form['action'] == 'login':
  	#//do login process

	return redirect('/')


app.run(debug=True)