from flask import Flask, render_template, request
import pyrebase
import sys
sys.path.insert(0, '../Model')
from Course import Course
from Product import Product
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


def load_products():
    products = []
    products_docs = db.collection('Products').get()
    for doc in products_docs:
        category = doc.to_dict()['category'];
        image = doc.to_dict()['image'];
        name = doc.to_dict()['name'];
        price = doc.to_dict()['price'];
        reviews = doc.to_dict()['reviews'];
        rating = doc.to_dict()['rating'];
        product = Product(category, image, name, price, reviews, rating,)
        products.append(product)

    return products


@app.route('/')
def homepage():
    return render_template('homepage.html',login_stat_html=login_stat)
@app.route('/sports_courses/')
def sports_courses():
    return render_template('sports_courses.html',login_stat_html=login_stat,courses=load_courses())
@app.route('/Shopping Cart/')
def shopping_cart():
    return render_template('Shopping Cart.html',login_stat_html=login_stat)
@app.route('/spedu_store/')
def spedu_store():
    return render_template('store_searchpage.html', login_stat_html=login_stat, products=load_products())
@app.route('/Checkout/')
def Checkout():
    return render_template('Checkout.html', login_stat_html=login_stat)
@app.route('/admin_page/')
def admin_page():
    return render_template('admin_page.html')
@app.route('/admin_page/products/')
def admin_page_products():
    return render_template('admin_page_products.html', products=load_products())
@app.route('/admin_page/courses/')
def admin_page_courses():
    return render_template('admin_page_courses.html', courses=load_courses())
@app.route('/admin_page/courses/new_course')
def new_course():
    return render_template('new_course.html')
@app.route('/admin_page/courses/new_product')
def new_product():
    return render_template('new_product.html')
@app.route('/create_new_course', methods=['POST'])
def create_new_course():
    course_name = request.form['course_name']
    course_trainer = request.form['course_trainer']
    course_short_desc = request.form['course_short_desc']
    course_desc = request.form['course_desc']
    course_duration = request.form['course_duration']
    course_price = request.form['course_price']
    learning_outcome = request.form['learning_outcome']
    course_level = request.form['course_level']
    video_link = request.form['video_link']
    course_image = request.form['course_image']
    new_course_data = {
        'description':course_desc,
        'duration':course_duration,
        'image':course_image,
        'learning_outcome':learning_outcome,
        'level':course_level,
        'name':course_name,
        'price':course_price,
        'rating':0,
        'reviews':[{"rating":0,'review':"",'reviewer':""}],
        'short_description':course_short_desc,
        'video_link':video_link,
        'students_count':0,
        'trainer':course_trainer
    }
    db.collection('Courses').document().set(new_course_data)
    return ""

@app.route('/create_new_product', methods=['POST'])
def create_new_product():
    product_name = request.form['product_name']
    product_price = request.form['product_price']
    product_image = request.form['product_image']
    product_category = request.form['product_category']
    new_product_data = {
        'category': product_category,
        'image': product_image,
        'name': product_name,
        'price': product_price,
        'reviews': [{"rating": 0, 'review': "", 'reviewer': ""}],
        'rating': 0,
        'stock': 100,
    }
    db.collection('Products').document().set(new_product_data)
    return ""

if __name__ == "__main__":
     app.run(debug=True)
