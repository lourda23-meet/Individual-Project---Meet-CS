import pyrebase 
from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session  

config = {
  'apiKey': "AIzaSyCxWZjswWzuvI8pW53fFf-k5EJJaBAKLVY",
  'authDomain': "individual-project-lour-dahleh.firebaseapp.com",
  'databaseURL': "https://individual-project-lour-dahleh-default-rtdb.firebaseio.com",
  'projectId': "individual-project-lour-dahleh",
  'storageBucket': "individual-project-lour-dahleh.appspot.com",
  'messagingSenderId': "295877846751",
  'appId': "1:295877846751:web:b6ad36454fc7955adf6b6a",
  'measurementId': "G-8HN895G628"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask (__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = "KJHLIUHIUHUIHIHIUHUI"
@app.route('/todolist', methods=['GET', 'POST'])
def basic():
	if request.method == 'POST': 
		if request.form['submit']== 'add':
			name = request.form['name']
			db.child("TODO").push(name)
			TODOLIST = db.child("TODO").get().val()
			return render_template('index.html', T=TODOLIST)
		elif request.form['submit']=='delete':
			db.child("TODO").remove()
			return render_template('index.html')
	return render_template('index.html')



@app.route('/', methods=['GET', 'POST'])
def signup():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['psw']
		# try:
		login_session['user'] = auth.create_user_with_email_and_password(email, password)
		return redirect(url_for('signin'))
		# except:
		error = "Authentication failed"
	return render_template("signup.html")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			login_session['user'] = auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for('basic'))
		except:
			error = "Authentication failed"
	return render_template("signin.html")

@app.route('/hello/<string:name>')
def hello_name_route(name):
    return render_template(
        'signin.html', n = name)


@app.route('/signout')
def signout():
	login_session['user'] = None
	auth.current_user = None
	return redirect(url_for('signin'))

if __name__=='__main__': 
	app.run(debug=True)

#db.child("names").push({"name":"lour"})
#db.child("names").child.("name").update({"name":"dahleh"})
#users = db.child("names").child("name").get
#print(users.key())

#db.child("names").child.("name").remove()