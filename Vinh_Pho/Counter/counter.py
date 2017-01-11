from flask import Flask, render_template, session,redirect
app=Flask(__name__)
app.secret_key="12345"

@app.route('/')
def counter():
    if 'counter' not in session:
        session['counter']=0
    
    session['counter']=session['counter']+1
    print session['counter']
    return render_template('index.html')

@app.route('/reset',methods=['POST'])
def session_reset():
    session.clear()
    return redirect('/')

@app.route('/ninjas',methods=['POST'])
def ninjas():
    session['counter']=session['counter']+1
    print session['counter']
    return redirect('/')

    

app.run(debug=True)