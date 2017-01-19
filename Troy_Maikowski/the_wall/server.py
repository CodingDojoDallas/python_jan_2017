from flask import Flask, request, render_template, url_for, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, "wall")
app.secret_key = "supersecretnesskey"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if 'logged_in' in session:
        return redirect('/wall')
    return render_template("landing.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/wall')
def wall():
    if not 'logged_in' in session or not session['logged_in']:
        return redirect('/')
    query = """SELECT CONCAT_WS(' ',users.first_name, users.last_name) AS full_name, messages.user_id, messages.id, messages.message, messages.updated_at
               FROM users JOIN messages ON users.id = messages.user_id ORDER BY messages.created_at DESC;"""
    messages = mysql.query_db(query)
    query = """SELECT comments.message_id, comments.comment, comments.created_at, CONCAT_WS(' ', users.first_name, users.last_name) AS full_name FROM comments
               JOIN users ON comments.user_id = users.id ORDER BY comments.created_at ASC;"""
    comments = mysql.query_db(query)
    return render_template("wall.html", messages=messages, comments=comments)

@app.route('/post_message', methods=["POST"])
def post_message():
    msg = request.form['post_body']
    if len(msg) > 5:
        query = """INSERT INTO messages (user_id, message, created_at, updated_at)
                   VALUES (:user_id, :message, NOW(), NOW());"""
        data = {
            'user_id': session['id'],
            'message': msg
        }
        mysql.query_db(query, data)
        flash("Message posted!")
    else:
        flash("Message too short. Please add more content")
    return redirect('/wall')

@app.route('/delete_message/<int:msg_id>')
def delete_message(msg_id):
    query1 = "DELETE FROM comments WHERE message_id = :msg_id"
    query2 = "DELETE FROM messages WHERE id = :msg_id;"
    data = {
        'msg_id': msg_id
    }
    mysql.query_db(query1, data)
    mysql.query_db(query2, data)
    return redirect('/wall')

@app.route('/add_comment', methods=["POST"])
def add_comment():
    comment = request.form['comment']
    message_id = request.form['post_id']
    query = """INSERT INTO comments (message_id, user_id, comment, created_at, updated_at)
               VALUES (:message_id, :user_id, :comment, NOW(), NOW());"""
    data = {
        'message_id': message_id,
        'user_id': session['id'],
        'comment': comment
    }
    mysql.query_db(query, data)
    flash("Comment added!")
    return redirect('/wall')

@app.route('/process_login', methods=["POST"])
def process_login():
    is_valid = True

    email = request.form['email']
    pw = request.form['pw']
    query = "SELECT * FROM users WHERE email = :email"
    data = {
        'email': email
    }
    user = mysql.query_db(query, data)
    if len(user) is 0:
        flash("Email does not exist, please try again or register")
        is_valid = False
    else:
        if not bcrypt.check_password_hash(user[0]['password'], pw):
            flash("Invalid password")
            is_valid = False
    if is_valid:
        session['logged_in'] = True
        session['id'] = user[0]['id']
        return redirect('/wall')
    else:
        return redirect('/')

@app.route('/process_registration', methods=["POST"])
def process_registration():
    is_valid = True

    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    pw = request.form['pw']
    pw_confirm = request.form['pw_confirm']

    query = "SELECT * FROM users WHERE email = :email" #check if email is already in db
    data = {
        'email': email
    }
    existing_email = mysql.query_db(query, data)

    if not len(fname) > 2 or not fname.isalpha():
        flash("First name must be greater than 2 characters and contain only letters")
        is_valid = False
    if not len(lname) > 2 or not lname.isalpha():
        flash("Last name must be greater than 2 characters and contain only letters")
        is_valid = False
    if not EMAIL_REGEX.match(email):
        flash("Invalid email")
        is_valid = False
    if existing_email:
        flash("Email already exists in the database.")
        is_valid = False
    if not len(pw) > 8 or not (pw == pw_confirm):
        flash("Password must be greater than 8 characters and must match the confirmation password")
        is_valid = False

    if is_valid:
        query = """INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES
                   (:first_name, :last_name, :email, :password, NOW(), NOW())"""
        data = {
            'first_name': fname,
            'last_name': lname,
            'email': email,
            'password': bcrypt.generate_password_hash(pw),
        }
        try:
            mysql.query_db(query, data)
        except:
            flash("Something went wrong. Please register again")
        session['logged_in'] = True
        session['id'] = mysql.query_db("SELECT last_insert_id() AS last_id;")[0]['last_id']
        return redirect('/wall')
    else:
        return redirect('/register')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
