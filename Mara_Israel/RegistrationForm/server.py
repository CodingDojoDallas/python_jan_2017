from flask import Flask, request, render_template, url_for, redirect, flash
import re
import time
from datetime import datetime
app = Flask(__name__)
app.secret_key = "MyHamsterAteHisCarrots"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/register', methods=["POST"])
def process():
  email = request.form['email']
  first = request.form['first_name']
  last = request.form['last_name']
  password = request.form['pass']
  password_confirm = request.form['confirm_pass']
 
  try:
    bday = time.strptime(request.form['bday'], "%Y-%m-%d")
  except:
    bday = ""

  if not (first and last):
      flash("Field(s) cannot be left blank!")
      return redirect('/')
  elif not (first.isalpha() and last.isalpha()):
  		flash("First and Last name contain invalid characters!")
  		return redirect('/')
  elif not (EMAIL_REGEX.match(email) and email) :
      flash("Email is INVALID!")
      return redirect('/')
  elif not (bday < time.localtime(time.time()) and bday):
      flash("Birthdate is INVALID!")
      return redirect('/')
  elif not (len(password) > 8 and password == password_confirm):
      flash("Passwords do not match or are not longer than 8 characters!")
      return redirect('/')
  flash("Thank you {} for registering! A confirmation email has been sent to {}".format(first,email) )
  return redirect('/')
    
app.run(debug=True)