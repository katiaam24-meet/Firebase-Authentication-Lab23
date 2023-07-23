from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


conflig ={
  apiKey: "AIzaSyBK97k9ZwZAaKhBjXrdLcHleTyqerq_EWc",
  authDomain: "searswillwin.firebaseapp.com",
  projectId: "searswillwin",
  storageBucket: "searswillwin.appspot.com",
  messagingSenderId: "493830207082",
  appId: "1:493830207082:web:46e386368da2b1b47a7c13",
  measurementId: "G-9FN4XLYV0L"
  "databaseURL":""
  }

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/signin', methods=['GET', 'POST'])
def signin():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = 
auth.sign_in_with_email_and_password(email, password)
           return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
   return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = 
auth.create_user_with_email_and_password(email, password)
           return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
   return render_template("signup.html")

@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)