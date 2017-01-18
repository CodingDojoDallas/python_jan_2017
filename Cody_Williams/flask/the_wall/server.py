from flask import Flask, render_template, session, redirect, request, flash, url_for
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'shhdonttell'

bcrypt = Bcrypt(app)

mysql = MySQLConnector(app, 'flask_wall_10283')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
	name = request.form['name']
	email = request.form['email']
	password = request.form['password']
	hashed_pw = bcrypt.generate_password_hash(password)

	query = "INSERT INTO users (name, email, password, created_at, updated_at) VALUES (:name, :email, :password, NOW(), NOW());"
	data = {
		'name' : name,
		'email' : email,
		'password' : hashed_pw,
	}

	user_id = mysql.query_db(query, data)
	session['user_id'] = user_id
	return redirect('/wall')

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	query = 'SELECT * FROM users WHERE email = :email;'
	data = {'email': email}
	user = mysql.query_db(query, data)
	if user and bcrypt.check_password_hash(user[0]['password'], password):
		session['user_id'] = user[0]['id']
		return redirect('/wall')
	else:
		flash('invalid credentials')
		return redirect('/')

@app.route('/wall')
def wall():
	if 'user_id' not in session:
		return redirect('/')
	query = 'SELECT name FROM users WHERE id = :id;'
	data = {'id': session['user_id']}
	user = mysql.query_db(query, data)
	messages_query = "SELECT messages.content as 'message', messages.id as 'message_id', messages.created_at as 'message_date', comments.content as 'comment', comments.created_at as 'comment_date', comments.id as 'comment_id', users.name as 'message_username', comment_users.name as 'comment_username' FROM messages LEFT JOIN comments ON messages.id = comments.message_id LEFT JOIN users ON users.id = messages.user_id LEFT JOIN users as comment_users ON comment_users.id = comments.user_id ORDER BY messages.id;"
	messages = mysql.query_db(messages_query)
	new_messages = []
	message_ids = []
	for message in messages:
		if message['message_id'] not in message_ids:
			message_ids.append(message['message_id'])
			message_obj = {}
			message_obj['comments'] = []
			message_obj['message_id'] = message['message_id']
			message_obj['message'] = message['message']
			message_obj['message_user'] = message['message_username']
			new_messages.append(message_obj)
		if message['comment']:
			comment_obj = {}
			comment_obj['comment'] = message['comment']
			comment_obj['comment_user'] = message['comment_username']
			comment_obj['comment_date'] = message['comment_date']
			new_messages[-1]['comments'].append(comment_obj)
	return render_template('wall.html', current_user=user, messages=new_messages)

@app.route('/messages', methods=['POST'])
def create_message():
	message = request.form['message']
	user_id = session['user_id']
	query = 'INSERT INTO messages (content, user_id, created_at, updated_at) VALUES (:content, :user_id, NOW(), NOW());'
	data = {
		'content': message,
		'user_id': user_id,
	}
	mysql.query_db(query, data)
	return redirect('/wall')

@app.route('/comments', methods=['POST'])
def create_comment():
	comment = request.form['comment']
	message_id = request.form['message_id']
	user_id = session['user_id']
	query = 'INSERT INTO comments (content, message_id, user_id, created_at, updated_at) VALUES (:content, :message_id, :user_id, NOW(), NOW());'
	data = {
		'content': comment,
		'message_id': message_id,
		'user_id': user_id,
	}
	mysql.query_db(query, data)
	return redirect('/wall')

@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')

app.run(debug=True)








