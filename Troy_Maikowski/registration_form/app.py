from flask import Flask, request, render_template, url_for, redirect, flash
import re
import time
from datetime import datetime

app = Flask(__name__)
app.secret_key = "Massive secret key to hold secrets"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process_registration', methods=["POST"])
def process_registration():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    try:
        bday = time.strptime(request.form['bday'], "%Y-%m-%d")
    except:
        bday = ""
    password = request.form['password']
    password2 = request.form['password2']
    if not (fname and lname and fname.isalpha() and lname.isalpha()):
        flash("First Name and Last Name must not be empty and cannot contain any numbers")
        return redirect('/')
    elif not (EMAIL_REGEX.match(email) and email) :
        flash("Please input a valid email")
        return redirect('/')
    elif not (bday < time.localtime(time.time()) and bday):
        flash("The birthdate field cannot be empty and must be prior to the current date")
        return redirect('/')
    elif not (len(password) > 8 and password == password2):
        flash("Passwords must match and be greater than 8 characters long.")
        return redirect('/')
    flash("Thank you for registering!")
    return redirect('/')
    
app.run(debug=True)