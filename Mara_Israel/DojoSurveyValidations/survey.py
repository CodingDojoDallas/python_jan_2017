from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'supercalifragilisticexpialidocious'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process', methods=['POST'])
def validate():
	
@app.route('/result', methods=['POST'])
def result():
	if request.form['name'] and len(request.form['name']) < 1:
		flash('This field cannot be left empty')
	else:
		session.['name'] = request.form['name']
		return redirect('/')		
	location = request.form['dojoloc'] 
	language = request.form['language']
	if request.form['comment'] and len(request.form['comment']) <=120:
		comment = request.form['comment']
	else:
		flash('Comments cannot be blank or more than 120 characters')
		return redirect('/')
	
	return render_template("result.html", name = request.form['name']

app.run(debug=True) 