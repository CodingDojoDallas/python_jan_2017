from flask import Flask, request, render_template, url_for, redirect, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'emails')
app.secret_key = "MyHamsterAteHisCarrots"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
	successmsg = 'The email address you entered'+' '+request.form['email']+' '+'is a VALID email address! Thank you!'
	query = "INSERT INTO emails (email, created_at) VALUES (:email, NOW())"
	data = {
	'email': request.form['email']
	}
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Email is invalid!")
		return redirect('/')
	else:
		session['successmessage'] = successmsg
		mysql.query_db(query, data)
		return redirect("/success")

@app.route('/success')
def stuff():
	query = "SELECT * FROM emails"
	emails = mysql.query_db(query)
	return render_template("success.html", all_emails = emails)

app.run(debug=True)