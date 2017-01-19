from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "myKeyIsSecret"

@app.route("/")
def index():
    counter = 0
    if "count" not in session:
        session["count"]=counter
    session["count"]+=1
    print session["count"]
    return render_template("index.html")

@app.route("/addTwo", methods=["POST"])
def addTwo():
    session["count"]+=1
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session["count"]=0
    return redirect("/")

app.run(debug=True)