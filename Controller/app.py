from flask import Flask, render_template
import pyrebase
import sys
sys.path.insert(0, '../Model')
from Course import Course
import firebase_admin
from firebase_admin import credentials, firestore
firebaseConfig = {
  "apiKey": "AIzaSyAhONsOYfqp3ox_L5bCy0cpX_f-iQxdc9I",
  "authDomain": "spedu-3fd4f.firebaseapp.com",
  "projectId": "spedu-3fd4f",
  "storageBucket": "spedu-3fd4f.appspot.com",
  "messagingSenderId": "297243626132",
  "databaseURL":"https://spedu-3fd4f-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "appId": "1:297243626132:web:129e6edfab962e5ab24281"
}

cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred, firebaseConfig)



firebase = pyrebase.initialize_app(firebaseConfig)
db = firestore.client()
auth = firebase.auth()
storage = firebase.storage()





app = Flask(__name__, template_folder='../View/HTML', static_folder='../View/static')






user_email = 'test@gmail.com'
user_password = '1234test'
login_stat = False
try:
    auth.sign_in_with_email_and_password(user_email,user_password)
    user = auth.current_user
except:
    print("Unable to login")
if auth.current_user != None:
    login_stat = True
else:
    login_stat = False






def load_courses():
    courses = []
    courses_docs = db.collection('Courses').get()
    for doc in courses_docs:

        description = doc.to_dict()['description'];
        duration = doc.to_dict()['duration'];
        image = doc.to_dict()['image'];
        learning_outcome = doc.to_dict()['learning_outcome'];
        level = doc.to_dict()['level'];
        name = doc.to_dict()['name'];
        price = doc.to_dict()['price'];
        rating = doc.to_dict()['rating'];
        reviews = doc.to_dict()['reviews'];
        students_count = doc.to_dict()['students_count'];
        trainer = doc.to_dict()['trainer'];
        course = Course(description, duration, image, learning_outcome, level, name, price, rating, reviews, students_count, trainer)
        courses.append(course)
    return courses



@app.route('/')
def homepage():
    return render_template('homepage.html',login_stat_html=login_stat)
@app.route('/sports_courses/')
def sports_courses():

    return render_template('sports_courses.html',login_stat_html=login_stat,courses=load_courses())
@app.route('/Shopping Cart/')
def shopping_cart():
    return render_template('Shopping Cart.html',login_stat_html=login_stat)
@app.route('/Checkout/')
def Checkout():
    return render_template('Checkout.html', login_stat_html=login_stat)
if __name__ == "__main__":
     app.run(debug=True)
