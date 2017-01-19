from flask import Flask, request, render_template, url_for, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, "login_db")
app.secret_key = "superdupersecretnesskey"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/welcome')
def welcome():
    if 'logged_in' in session and session['logged_in']:
        query = "SELECT * FROM users WHERE id = :id"
        data = {
            'id': session['id']
        }
        user_info = mysql.query_db(query, data)
        return render_template('welcome.html', user_info=user_info)
    flash("Please log in")
    return redirect('/login')

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/process_registration', methods=["POST"])
def process_registration():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    pw = request.form['password']
    pw_confirm = request.form['password_confirm']
    if not fname or not fname.isalpha() or not len(fname) > 2:
        flash("First name must contain only letters and be greater than 2 characters long")
        return redirect('/register')
    elif not lname or not lname.isalpha() or not len(lname) > 2:
        flash("Last name must contain only letters and be greater than 2 characters long")
        return redirect('/register')
    elif not EMAIL_REGEX.match(email):
        flash("Invalid email address")
        return redirect('/register')
    elif pw != pw_confirm or len(pw) < 8:
        flash("Password must be at least 8 characters and must match the confirmation password")
        return redirect('/register')
    else:
        query = """INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password);"""
        data = {
            'first_name': fname,
            'last_name': lname,
            'email': email,
            'password': bcrypt.generate_password_hash(pw)
        }
        mysql.query_db(query, data)
        session['id'] = mysql.query_db("SELECT last_insert_id() AS last_id;")[0]['last_id']
        session['logged_in'] = True
        flash("You have successfully registered! (id: {})".format(session['id']))
    return redirect('/welcome')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/process_login', methods=["POST"])
def process_login():
    email = request.form['email']
    pw = request.form['password']
    query = "SELECT * FROM users WHERE email = :email"
    data = {
        'email': email
    }
    user = mysql.query_db(query, data)
    if bcrypt.check_password_hash(user[0]['password'], pw):
        session['logged_in'] = True
        session['id'] = user[0]['id']
        flash("Welcome user!")
        return redirect('/welcome')
    flash("Invalid credentials. Please try logging in again")
    return redirect('/login')

app.run(debug=True)
