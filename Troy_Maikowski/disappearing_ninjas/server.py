from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "SecretSecretKey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
@app.route('/ninja/<color>')
def ninja(color=None):
    return render_template("turtles.html", color=color)

app.run(debug=True)