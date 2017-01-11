from flask import Flask, render_template, request, url_for, redirect, session, flash

app = Flask(__name__)
app.secret_key = "This is a huge secret"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=["POST"])
def result():
    if request.form['full_name']:
        full_name = request.form['full_name']
        session['name'] = full_name
    else:
        flash("Full name field cannot be empty.")
        return redirect('/')
    dojo_loc = request.form['dojo_loc']
    fav_lang = request.form['fav_lang']
    if request.form['comment'] and len(request.form['comment']) <= 120:
        comment = request.form['comment']
    else:
        flash("Comment box cannot be empty and cannot exceed 120 characters.")
        return redirect('/')
    data = [full_name, dojo_loc, fav_lang, comment]
    return render_template("result.html", data=data)

@app.route('/show')
def show_info():
    return render_template("show.html")

app.run(debug=True)