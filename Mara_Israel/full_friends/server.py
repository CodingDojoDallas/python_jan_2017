from flask import Flask, render_template, flash, request, redirect
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
mysql = MySQLConnector(app, "friends")
app.secret_key = "SuperDuperSecret"


@app.route("/")
def index():
	query = "SELECT * FROM friends"

	friends = mysql.query_db(query)

	return render_template("index.html", friends = friends)


@app.route("/friends", methods=["POST"])
def create():
	is_valid = True

	if len(request.form['first_name']) == 0:
		flash("First name is required")
		is_valid = False

	if len(request.form['last_name']) == 0:
		flash("Last name is required")
		is_valid = False

	if len(request.form['email']) == 0:
		flash("Email is required")
		is_valid = False
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Email is invalid")
		is_valid = False

	if not is_valid:
		return redirect("/")

	query = "INSERT INTO friends(first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"

	data = {

			"first_name": request.form["first_name"],
			"last_name": request.form["last_name"],
			"email": request.form ["email"]
	}

	mysql.query_db(query, data)
	return redirect("/")

@app.route('/friends/<id>/edit')
def edit(id):
	query = "SELECT * FROM friends WHERE id=:id"

	data = {
			"id": id
	}

	friends = mysql.query_db(query, data)

	if len(friends) is 0:
		return redirect("/")

	return render_template("edit.html", id=id, friend = friends[0])

@app.route("/friends/<id>", methods=["POST"])
def update(id):
	is_valid = True

	if len(request.form['first_name']) == 0:
		flash("First name is required")
		is_valid = False

	if len(request.form['last_name']) == 0:
		flash("Last name is required")
		is_valid = False

	if len(request.form['email']) == 0:
		flash("Email is required")
		is_valid = False
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Email is invalid")
		is_valid = False

	if not is_valid:
		return redirect("/friends/"+id+"/edit")

	query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email WHERE id=:id"

	data = {
		"first_name": 		request.form["first_name"],
		"last_name": 			request.form["last_name"],
		"email": 					request.form ["email"],
		"id": 						id,
	}

	mysql.query_db(query, data)
	return redirect("/")

@app.route("/friends/<id>/delete")
def destroy(id):
	query = "DELETE FROM friends WHERE id=:id"
	
	data = {
			"id":id 
	}
	mysql.query_db(query, data)
	return redirect("/")

app.run(debug = True)

