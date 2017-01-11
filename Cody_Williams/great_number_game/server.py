from flask import Flask, request, render_template, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'somethingverysecret'

@app.route('/')
def home():
	#check if num is not in session
	if 'num' not in session:
		#generate a random number
		random_num = int(random.random() * 100)
		#save the random number into session
		session['num'] = random_num
	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
	#stash the user input into a variable
	guess = request.form['guess']
	#convert the user input into an integer so we can compare against another integer
	guess = int(guess)
	#compare the user input against the number in session
	if guess < session['num']:
		session['fail'] = "Too Low"
	elif guess > session['num']:
		session['fail'] = "Too High"
	else:
		#if the user guesses correctly we need to check to see if there was a fail message and then clear it
		if 'fail' in session:
			session.pop('fail')
		#now we create the success message and save it into session
		session['success'] = 'The number was {}.  You guessed it correctly'.format(session['num'])
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	#clear the session
	session.clear()
	#redirect to homepage
	return redirect('/')
	
app.run(debug=True)






