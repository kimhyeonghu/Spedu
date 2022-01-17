from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import pyrebase
import sys
sys.path.insert(0, '../Model')
import random
from Course import Course
from Product import Product
from Forms import *
from User import *
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__, template_folder='../View/HTML', static_folder='../View/static')
app.secret_key = "1ae11153fae277ef2a41b70152692513"
cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "signin"
# login_manager.login_message_category = "info"

# firebaseConfig = {
#   "apiKey": "AIzaSyAhONsOYfqp3ox_L5bCy0cpX_f-iQxdc9I",
#   "authDomain": "spedu-3fd4f.firebaseapp.com",
#   "projectId": "spedu-3fd4f",
#   "storageBucket": "spedu-3fd4f.appspot.com",
#   "messagingSenderId": "297243626132",
#   "databaseURL":"https://spedu-3fd4f-default-rtdb.asia-southeast1.firebasedatabase.app/",
#   "appId": "1:297243626132:web:129e6edfab962e5ab24281"
# }
# cred = credentials.Certificate("../serviceAccountKey.json")
# firebase_admin.initialize_app(cred, firebaseConfig)
# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()
# storage = firebase.storage()
# user_email = 'test@gmail.com'
# user_password = '1234test'
# login_stat = False
# try:
#     auth.sign_in_with_email_and_password(user_email,user_password)
#     user = auth.current_user
# except:
#     print("Unable to login")
# if auth.current_user != None:
#     login_stat = True
# else:
#     login_stat = False


@login_manager.user_loader
def user_loader(id):
    # given id, return user object
    user = db.collection("Users").where("id", "==", id).get()
    if user:
        user = User.from_dict(user[0].to_dict())
        return user


@app.route('/')
def homepage():
    return render_template('homepage.html')


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
        'video_link':course.video_link
        }
        db.collection('Courses').document().set(new_course_data)
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
        docs = db.collection('Courses').where("courseID","==",course.courseID).get()
        for doc in docs:
            key = doc.id
            db.collection('Courses').document(key).update({
                'description':course.description,
                'short_description':course.short_description,
                'duration':course.duration,
                'image':course.image,
                'learning_outcome':course.learning_outcome,
                'level':course.level,
                'price':course.price,
                'trainer':course.trainer,
                'video_link':course.video_link
            })
    elif method == 'delete':
        courseID = course
        try:
            docs = db.collection('Courses').where("courseID","==",courseID).get()
            for doc in docs:
                key = doc.id
                db.collection('Courses').document(key).delete()
        except:
            print("Unable to delete course!")

        print("HELoo delete")


@app.route('/sports_courses/')
def sports_courses():
    return render_template('sports_courses.html', courses=course_CRUD(course=None,method='load'))


@app.route('/sports_courses/about_course/', methods=['GET'])
def view_selected_course():
    selected_courseID = request.args.get("selected_courseID")
    print(selected_courseID)
    selected_course = db.collection('Courses').where("courseID","==",selected_courseID).get()[0].to_dict()
    return render_template('selected_course.html', selected_course=selected_course)


@app.route('/Shopping Cart/')
def shopping_cart():
    return render_template('Shopping Cart.html')


@app.route('/spedu_store/')
def spedu_store():
    return render_template('store_searchpage.html', products=load_products())


@app.route('/Checkout/')
def Checkout():
    return render_template('Checkout.html')


@app.route('/admin_page/')
def admin_page():
    return render_template('admin_page.html')


@app.route('/admin_page/courses/')
def admin_page_courses():
    return render_template('admin_page_courses.html', courses=course_CRUD(course=None, method='load'))


@app.route('/admin_page/courses/new_course')
def new_course():
    return render_template('new_course.html')



@app.route('/admin_page/courses/about_course/',methods=['GET'])
def view_admin_selected_course():
    selected_courseID = request.args.get("selected_courseID")
    print(selected_courseID)
    selected_course = db.collection('Courses').where("courseID","==",selected_courseID).get()[0].to_dict()
    return render_template('admin_selected_course.html', selected_course=selected_course)


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
    course_reviews = [{'rating':0,'reviewer':'','review':''}]
    students_count = 0
    new_course = Course(courseID, course_desc, course_short_desc, course_duration, course_image, learning_outcome, course_level, course_name, course_price, course_rating, course_reviews, students_count, course_trainer, video_link)
    course_CRUD(course=new_course, method='create')
    return render_template('admin_page_courses.html', courses=course_CRUD(course=None, method='load'))


@app.route('/admin_page/courses/about_course/', methods=['POST'])
def update_delete_course():
    current_courseID = request.form['current_course']
    action_input_value = request.form['action_input']
    print(action_input_value)
    if action_input_value == 'delete':
        course_CRUD(course=current_courseID,method='delete')
        return redirect("/admin_page/courses/")
    else:
        return redirect(url_for('update_page', current_courseID=current_courseID))


@app.route('/admin_page/courses/about_course/update/<current_courseID>')
def update_page(current_courseID):
    current_course = db.collection('Courses').where("courseID", "==", current_courseID).get()[0].to_dict()
    print(current_course)
    return render_template('edit_course_page.html', selected_course=current_course)


@app.route('/admin_page/courses/about_course/update/', methods=['POST'])
def update_course():
    course_name = ""
    courseID = request.form['courseID']
    course_trainer = request.form['course_trainer']
    course_short_desc = request.form['course_short_desc']
    course_desc = request.form['course_desc']
    course_duration = request.form['course_duration']
    course_price = request.form['course_price']
    learning_outcome = request.form['learning_outcome']
    course_level = request.form['course_level']
    video_link = request.form['video_link']
    course_image = request.form['course_image']
    course_rating = ""
    course_reviews = []
    students_count = 0
    course = Course(courseID, course_desc, course_short_desc, course_duration, course_image, learning_outcome, course_level, course_name, course_price, course_rating, course_reviews, students_count, course_trainer, video_link)
    course_CRUD(course=course, method='update')
    return redirect("/admin_page/courses/")


@app.route('/admin_page/products/')
def admin_page_products():
    return render_template('admin_page_products.html', products=load_products())


@app.route('/admin_page/products/new_product')
def new_product():
    return render_template('new_product.html')


@app.route('/admin_page/products/update_product')
def update_product():
    return render_template('update_product.html')


def load_products():
    products = []
    products_docs = db.collection('Products').get()
    for doc in products_docs:
        category = doc.to_dict()['category']
        image = doc.to_dict()['image']
        name = doc.to_dict()['name']
        price = doc.to_dict()['price']
        reviews = doc.to_dict()['reviews']
        rating = doc.to_dict()['rating']
        product = Product(category, image, name, price, reviews, rating,)
        products.append(product)
    return products


@app.route('/admin_page/products/', methods=['POST'])
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
    return render_template('admin_page_courses.html', products=load_products())


@app.route('/signup', methods=['GET', 'POST'])
def signup1():
    if current_user.is_authenticated:
        return redirect(url_for("homepage"))
    sign_up_form1 = SignUpForm1(request.form)
    if request.method == "POST" and sign_up_form1.validate():
        users_dict = db.collection("Users").get()
        for user in users_dict:
            if user.to_dict()["email"] == sign_up_form1.email.data:
                flash("Email already registered.")
                return render_template('signup.html', form=sign_up_form1)
        try:
            id = db.collection("Users").order_by("id", direction=firestore.Query.DESCENDING).limit(1).get()[0].to_dict()["id"] + 1
        except:
            id = 1
        user = User(sign_up_form1.username.data, sign_up_form1.email.data, sign_up_form1.password.data, id)
        db.collection("Users").document(str(id)).set(user.to_dict())
        return redirect(url_for("signin"))

    return render_template('signup.html', form=sign_up_form1)


@app.route('/signup2', methods=['GET', 'POST'])
def signup2():
    sign_up_form2 = SignUpForm2(request.form)
    return render_template('signup2.html', form=sign_up_form2)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    sign_in_form = SignInForm(request.form)
    if request.method == "POST":
        user = db.collection("Users").where("email", "==", sign_in_form.email.data).get()
        if user:
            if user[0].to_dict()["password"] == sign_in_form.password.data:
                user = User.from_dict(user[0].to_dict())
                login_user(user)
                # login_user(user, remember=sign_in_form.remember.data)
                return redirect(url_for("homepage"))
            else:
                flash("Incorrect Login Credentials.")
                render_template('signin.html', form=sign_in_form)
        else:
            flash("Incorrect Login Credentials.")
            render_template('signin.html', form=sign_in_form)
    return render_template('signin.html', form=sign_in_form)


@app.route("/signout")
@login_required
def signout():
    logout_user()
    return redirect(url_for("homepage"))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    user = db.collection("Users").document(str(current_user.get_id())).get().to_dict()
    display_info = DisplayInfo(request.form)
    print(request.method == "GET")
    if request.method == "GET":
        display_info.username.data = user["username"]
    if request.method == "POST" and display_info.validate():
        if request.form["displayInfo"] == "Discard":
            display_info.username.data = user["username"]
            return redirect(url_for("account"))
        elif request.form["displayInfo"] == "Update":
            db.collection("Users").document(str(current_user.get_id())).update({"username": display_info.username.data})
            return redirect(url_for("account"))
    # else:
    #     display_info.username.data = user["username"]
    #     return render_template("account.html", user=user, displayinfo=display_info)
    print(request.method == "POST", request.form.get("delete") == "Delete Account", "deletetest")
    # if request.method == "POST" and request.form["delete"] == "Delete Account":
    #     db.collection("Users").document(str(current_user.get_id())).delete()
    #     logout_user()
    #     redirect(url_for("homepage"))
    return render_template("account.html", user=user, displayinfo=display_info)


if __name__ == "__main__":
     app.run(debug=True)
