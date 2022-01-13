from flask import Flask, render_template, request
import pyrebase
import sys
sys.path.insert(0, '../Model')
import random
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



def course_CRUD(course,method):
    if method == 'create':
        new_course_data = {
        'courseID':course.courseID,
        'description':course.description,
        'short_description':course.short_description,
        'duration':course.duration,
        'image':course.image,
        'learning_outcome':course.learning_outcome,
        'level':course.level,
        'name':course.name,
        'price':course.price,
        'rating':course.rating,
        'reviews':course.reviews,
        'students_count':course.students_count,
        'trainer':course.trainer,
        'video_link':course.video_link,
        }
        db.collection('Courses').document().set(new_course_data)
        pass
    elif method == 'load':
        courses = []
        courses_docs = db.collection('Courses').get()
        for doc in courses_docs:
            courseID = doc.to_dict()['courseID']
            description = doc.to_dict()['description']
            short_description = doc.to_dict()['short_description']
            duration = doc.to_dict()['duration']
            image = doc.to_dict()['image']
            learning_outcome = doc.to_dict()['learning_outcome']
            level = doc.to_dict()['level']
            name = doc.to_dict()['name']
            price = doc.to_dict()['price']
            rating = doc.to_dict()['rating']
            reviews = doc.to_dict()['reviews']
            students_count = doc.to_dict()['students_count']
            trainer = doc.to_dict()['trainer']
            video_link = doc.to_dict()['video_link']
            course = Course(courseID, description, short_description, duration, image, learning_outcome, level, name, price, rating, reviews, students_count, trainer, video_link)
            courses.append(course)
        return courses
    elif method == 'update':
        pass
    elif method == 'delete':
        pass



@app.route('/')
def homepage():
    return render_template('homepage.html',login_stat_html=login_stat)
@app.route('/sports_courses/')
def sports_courses():
    return render_template('sports_courses.html',login_stat_html=login_stat,courses=course_CRUD(course=None,method='load'))


@app.route('/sports_courses/about_course/', methods=['GET'])
def view_selected_course():
    selected_courseID = request.args.get("selected_courseID")
    print(selected_courseID)
    selected_course = db.collection('Courses').where("courseID","==",selected_courseID).get()[0].to_dict()
    return render_template('selected_course.html',login_stat_html=login_stat, selected_course=selected_course)





@app.route('/Shopping Cart/')
def shopping_cart():
    return render_template('Shopping Cart.html',login_stat_html=login_stat)
@app.route('/spedu_store/')
def spedu_store():
    return render_template('store_searchpage.html', login_stat_html=login_stat)
@app.route('/Checkout/')
def Checkout():
    return render_template('Checkout.html', login_stat_html=login_stat)
@app.route('/admin_page/')
def admin_page():
    return render_template('admin_page.html')

@app.route('/admin_page/courses/')
def admin_page_courses():
    return render_template('admin_page_courses.html',courses=course_CRUD(course=None,method='load'))
@app.route('/admin_page/courses/about_course')
def new_course():
    return render_template('new_course.html')
@app.route('/admin_page/courses/new_course',methods=['GET'])
def view_admin_selected_course():
    selected_courseID = request.args.get("selected_courseID")
    print(selected_courseID)
    selected_course = db.collection('Courses').where("courseID","==",selected_courseID).get()[0].to_dict()
    return render_template('selected_course.html',login_stat_html=login_stat, selected_course=selected_course)
@app.route('/admin_page/courses/', methods=['POST'])
def create_new_course():

    course_name = request.form['course_name']
    courseID = course_name.split(' ')[0][0] + course_name.split(' ')[0][1] + str(random.randrange(0, 1000))
    course_trainer = request.form['course_trainer']
    course_short_desc = request.form['course_short_desc']
    course_desc = request.form['course_desc']
    course_duration = request.form['course_duration']
    course_price = request.form['course_price']
    learning_outcome = request.form['learning_outcome']
    course_level = request.form['course_level']
    video_link = request.form['video_link']
    course_image = request.form['course_image']
    course_rating = 0
    course_reviews = []
    students_count = 0
    new_course = Course(courseID, course_desc, course_short_desc, course_duration, course_image, learning_outcome, course_level, course_name, course_price, course_rating, course_reviews, students_count, course_trainer, video_link)
    course_CRUD(course=new_course,method='create')
    return render_template('admin_page_courses.html',courses=course_CRUD(course=None,method='load'))
@app.route('/admin_page/courses/edit_course', methods=['POST'])
def selected_course():
    course_name = request.form['name']
    return render_template('edit_course_page.html', selected_course=course_name)

if __name__ == "__main__":
     app.run(debug=True)
