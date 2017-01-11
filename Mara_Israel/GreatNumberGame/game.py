from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'applesandbananas'


@app.route('/', methods = ['GET','POST'])
def game():
	if session.has_key('random'):
		session['random'] = random.randrange(1,101)
	return render_template('index.html')

@app.route('/process', methods = ['POST'])
def result():
	reset = False
	if int(request.form['guess']) == int(session['guess']):
		prompt = "YAY!" + str(session['guess']) + "was the number!!!"
		reset = True
	elif int(request.form['guess']) < int(session['guess']):
		prompt = "Too low!"
	else:
		prompt = "Too high!"
	return render_template('index.html', prompt = prompt, reset = reset)

@app.route('/reset', methods=['POST'])
def reset():
	session.pop('random')
	return redirect('/')

app.run(debug = True)
