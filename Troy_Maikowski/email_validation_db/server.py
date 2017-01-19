from flask import Flask, request, render_template, url_for, redirect, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, "email_db")
app.secret_key = "majorsecretkey"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/process_email", methods=["POST"])
def process_email():
    email = request.form['email']
    if len(email) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(email):
        flash("Email is not valid!")
        return redirect('/')
    else:
        query = """INSERT INTO emails (email, created_at, updated_at)
                   VALUES (:email, NOW(), NOW());"""
        data = {
            'email': email
        }
        mysql.query_db(query, data)
    flash("The email address you entered ({}) is a VALID email address! Thank you!".format(email))
    return redirect('/show')

@app.route("/show")
def show():
    query = "SELECT * FROM emails;"
    data = mysql.query_db(query)
    return render_template("show_email.html", data=data)

@app.route('/delete_email', methods=["POST"])
def delete_email():
    query = "DELETE FROM emails WHERE id = :email_id"
    data = {
        'email_id': request.form['email_id']
    }
    mysql.query_db(query, data)
    flash("Successfully deleted the email")
    return redirect('/show')

app.run(debug=True)
