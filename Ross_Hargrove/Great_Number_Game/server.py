from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "GNG.key"

@app.route("/")
def home():
    randomNumber = int(random.random() * 100)
    if "n" not in session:
        session["n"] = randomNumber
        print session["n"]
    return render_template("home.html")

@app.route("/guess", methods=["POST"])
def userGuess():
    guess = request.form["guess"]
    guess = int(guess)
    if session["n"]>guess:
        session["incorrect"]="Too Low"
    elif session["n"]<guess:
        session["incorrect"]="Too High"
    else:
        if "incorrect" in session:
            session.pop("incorrect")
        session["correct"]="The Number was {}".format(session["n"])
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")

app.run(debug=True)