from flask import Flask, render_template, url_for
import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyAhONsOYfqp3ox_L5bCy0cpX_f-iQxdc9I",
  "authDomain": "spedu-3fd4f.firebaseapp.com",
  "projectId": "spedu-3fd4f",
  "storageBucket": "spedu-3fd4f.appspot.com",
  "messagingSenderId": "297243626132",
    "databaseURL":"https://spedu-3fd4f-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "appId": "1:297243626132:web:129e6edfab962e5ab24281"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

app = Flask(__name__, template_folder='../View/HTML', static_folder='../View/static')

user_email = 'test@gmail.com'
user_password = '1234ttest'
login_stat = False
try:
    auth.sign_in_with_email_and_password(user_email,user_password)
    user = auth.current_user
except:
    print("Unable to login")
else:
    print("User:", user)

if auth.current_user != None:
    login_stat = True
    print("Hello")
else:
    login_stat = False
    print("Bye")
@app.route('/')
def homepage():
    return render_template('homepage.html',login_stat_html=login_stat)

if __name__ == "__main__":
     app.run(debug=True)