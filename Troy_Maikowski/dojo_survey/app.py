from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = "This is a huge secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=["POST"])
def result():
    full_name = request.form['full_name']
    session['name'] = full_name
    dojo_loc = request.form['dojo_loc']
    fav_lang = request.form['fav_lang']
    comment = request.form['comment']
    data = [full_name, dojo_loc, fav_lang, comment]
    return render_template("result.html", data=data)

@app.route('/show')
def show_info():
    return render_template("show.html")

app.run(debug=True)