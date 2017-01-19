from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def survey():
    return render_template("survey.html")

@app.route("/info", methods=["POST"])
def info():
    userName = request.form["name"]
    userLoc = request.form["location"]
    userLang = request.form["language"]
    comment = request.form["comment"]
    return render_template("complete.html", name=userName, loc=userLoc, lang=userLang, comment=comment)

app.run(debug=True)