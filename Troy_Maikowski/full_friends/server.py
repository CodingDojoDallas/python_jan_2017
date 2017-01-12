from flask import Flask, redirect, render_template, request, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')
app.secret_key = "supersecretkey"

@app.route('/')
def index():
    query = "SELECT * FROM friend;"
    data = mysql.query_db(query)
    return render_template('index.html', data=data)

@app.route('/friends', methods=["POST"])
def create():
    query = """INSERT INTO friend (first_name, last_name, email, created_at, updated_at)
               VALUES (:first_name, :last_name, :email, NOW(), NOW());"""
    data = {
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'email': request.form['email']
    }
    mysql.query_db(query, data)
    flash("Saved {} into the database!".format(request.form['fname']))
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM friend WHERE id = :id;"
    data = {
        'id': id
    }
    results = mysql.query_db(query, data)
    return render_template("edit.html", results=results)

@app.route('/friends/<id>', methods=["POST"])
def update(id):
    query = """UPDATE friend SET first_name = :first_name,
                                 last_name = :last_name,
                                 email = :email,
                                 updated_at = NOW()
               WHERE id = :id"""
    data = {
        'id': request.form['id'],
        'first_name': request.form['fname'],
        'last_name': request.form['lname'],
        'email': request.form['email'],
    }
    mysql.query_db(query, data)
    flash("Successfully updated {}'s record!".format(request.form['fname']))
    return redirect('/')

@app.route('/friends/<id>/delete')
def destroy(id):
    query = "DELETE FROM friend WHERE id = :id;"
    data = {
        'id': id
    }
    mysql.query_db(query, data)
    flash("Deleted.")
    return redirect('/')

app.run(debug=True)
