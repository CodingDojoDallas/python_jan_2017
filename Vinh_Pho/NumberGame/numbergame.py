from flask import Flask, render_template, session, redirect, request,flash
app=Flask(__name__)

import random
app.secret_key="12345"

@app.route('/')
def game():
    num=random.randrange(0,100,2)
    if 'num' not in session:
        session['num']=num
    print session['num']
    return render_template('index.html')


@app.route('/guess',methods=['POST'])
def guess():
    iguess=int(request.form['guess'])
    if iguess < session['num']:
        session['fail']='Too Low'
    elif iguess > session['num']:
        session['fail']='Too High'
    else:
        if 'fail' in session:
            session.pop('fail')
        session['success']='Way to to go. Number {}.'.format(session['num'])
        print session['success']
    return redirect('/')

@app.route('/again',methods=['POST'])
def playagain():
    session.clear()
    return redirect('/')
app.run(debug=True)