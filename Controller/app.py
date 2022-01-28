from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import storage as storage_firbase_admin
import random
import sys
import json
sys.path.insert(0, '../Model')
from Course import Course
from Product import Product
from Forms import *
from User import *

app = Flask(__name__, template_folder='../View/HTML', static_folder='../View/static')
app.secret_key = "1ae11153fae277ef2a41b70152692513"
cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "signin"
# login_manager.login_message_category = "info"
bcrypt = Bcrypt(app)
firebaseConfig = {
  "apiKey": "AIzaSyAhONsOYfqp3ox_L5bCy0cpX_f-iQxdc9I",
  "authDomain": "spedu-3fd4f.firebaseapp.com",
  "projectId": "spedu-3fd4f",
  "storageBucket": "spedu-3fd4f.appspot.com",
  "messagingSenderId": "297243626132",
  "databaseURL":"https://spedu-3fd4f-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "appId": "1:297243626132:web:129e6edfab962e5ab24281"
}
# cred = credentials.Certificate("../serviceAccountKey.json")
# firebase_admin.initialize_app(cred, firebaseConfig)
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
storage = firebase.storage()
# user_email = 'test@gmail.com'
# user_password = '1234test'
# login_stat = False

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


def course_CRUD(course, method):
    if method == 'create':
        new_course_data = {
            'courseID': course.courseID,
            'description': course.description,
            'short_description': course.short_description,
            'duration': float(course.duration),
            'image': course.image,
            'learning_outcome': course.learning_outcome,
            'level': course.level,
            'name': course.name,
            'price': float(course.price),
            'rating': float(course.rating),
            'reviews': course.reviews,
            'students_count': int(course.students_count),
            'trainer': course.trainer,
            'video_link': course.video_link,
            'tag':course.tag
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
            tag = doc.to_dict()['tag']
            course = Course(courseID, description, short_description, duration, image, learning_outcome, level, name,
                            price, rating, reviews, students_count, trainer, video_link,tag)
            courses.append(course)
        return courses
    elif method == 'update':
        docs = db.collection('Courses').where("courseID", "==", course.courseID).get()
        for doc in docs:
            key = doc.id
            db.collection('Courses').document(key).update({
                'description': course.description,
                'short_description': course.short_description,
                'duration': course.duration,
                'image': course.image,
                'learning_outcome': course.learning_outcome,
                'level': course.level,
                'price': course.price,
                'trainer': course.trainer,
                'video_link': course.video_link,
                'tag':course.tag
            })
    elif method == 'delete':
        courseID = course
        try:
            docs = db.collection('Courses').where("courseID", "==", courseID).get()
            for doc in docs:
                key = doc.id
                db.collection('Courses').document(key).delete()
        except:
            print("Unable to delete course!")

        print("HELoo delete")


def load_top_courses(courses):
    top_course_list = []
    courses.sort(key=lambda x: x.rating*x.rating*x.students_count, reverse=True)
    if len(courses) >= 8:
        for i in range(8):
            top_course_list.append(courses[i])
    else:
        for course in courses:
            top_course_list.append(course)

    return top_course_list


def load_products():
    products = []
    products_docs = db.collection('Products').get()
    for doc in products_docs:
        productID = doc.to_dict()['productID']
        category = doc.to_dict()['category']
        image = doc.to_dict()['image']
        name = doc.to_dict()['name']
        price = doc.to_dict()['price']
        description = doc.to_dict()['description']
        rating = doc.to_dict()['rating']
        reviews = doc.to_dict()['reviews']
        product = Product(productID, category, image, name, price, description, rating, reviews)
        products.append(product)
    return products


@app.route('/admin_page/products/', methods=['POST'])
def create_new_product():
    product_name = request.form['product_name']
    productID = 'PR'+product_name.split(' ')[0][0] + product_name.split(' ')[0][1] + str(random.randrange(0, 1000))
    product_price = request.form['product_price']
    product_image = request.files['product_image']
    storage.child('/products/image_of_{}'.format(productID)).put(product_image)

  #  product_img_link = storage.child(f"/products/image_of_"+productID).get_url(auth.current_user["idToken"])

    product_img_link=""
    product_category = request.form['product_category']
    product_description = request.form['product_description']
    product_rating = 0
    product_reviews = [{'rating': 0, 'reviewer': '', 'review': ''}]
    new_product_data = {
        'productID': productID,
        'category': product_category,
        'image': product_img_link,
        'name': product_name,
        'price': product_price,
        'description': product_description,
        'rating': product_rating,
        'reviews': product_reviews,
    }
    db.collection('Products').document().set(new_product_data)
    return render_template('admin_page_products.html', products=load_products())


@app.route('/search/', methods=['GET'])
def search_result():
    search_input = request.args.get("search_input")
    print(search_input)
    return render_template('search_page.html', search_results=search_input)


def load_delete(productID):
    print("Delete")
    try:
        docs = db.collection('Products').where("productID", "==", productID).get()
        for doc in docs:
            key = doc.id
            db.collection('Products').document(key).delete()
    except:
        print("Unable to delete course!")


def load_update(productID):
    print("Hello")
    try:
        docs = db.collection('Products').where("productID", "==", productID).get()
        product_category = request.form['update_category']
        product_image = request.form['update_image']
        product_price = request.form['update_price']
        product_description = request.form['update_description']
        for doc in docs:
            key = doc.id
            db.collection('Products').document(key).update({
                 'category': product_category,
                 'image': product_image,
                 'price': product_price,
                 'description': product_description,
            })
    except:
        print("Unable to update course!")


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup1():
    if current_user.is_authenticated:
        return redirect(url_for("homepage"))
    sign_up_form1 = SignUpForm1(request.form)
    if request.method == "POST" and sign_up_form1.validate():
        try:
            if sign_up_form1.email.data == db.collection("Users").where("email", "==", sign_up_form1.email.data).get()[0].to_dict()["email"]:
                flash("Email already registered.")
                return render_template('signup.html', form=sign_up_form1)
        except:
            # user is not registered
            pass
        try:
            id = db.collection("Users").order_by("id", direction=firestore.Query.DESCENDING).limit(1).get()[0].to_dict()["id"] + 1
        except:
            id = 1
        hashed_password = bcrypt.generate_password_hash(sign_up_form1.password.data).decode('utf-8')
        user = User(sign_up_form1.username.data, sign_up_form1.email.data, hashed_password, id)
        db.collection("Users").document(str(id)).set(user.to_dict())
        login_user(user)
        try:
            auth.create_user_with_email_and_password(sign_up_form1.email.data, sign_up_form1.password.data)
            user = auth.current_user
        except:
            print("Unable to login")
        return redirect(url_for("signup2"))
    return render_template('signup.html', form=sign_up_form1)


@app.route('/signup2', methods=['GET', 'POST'])
@login_required
def signup2():
    sign_up_form2 = SignUpForm2(request.form)
    if request.method == "POST" and sign_up_form2.validate():
        user = User(current_user.get_email, current_user.get_username, current_user.get_password, current_user.get_id)
        user.set_security_qns({"qns1": sign_up_form2.qns1.data, "ans1": sign_up_form2.ans1.data, "qns2": sign_up_form2.qns2.data, "ans2": sign_up_form2.ans2.data, "qns3": sign_up_form2.qns3.data, "ans3": sign_up_form2.ans3.data})
        db.collection("Users").document(str(current_user.get_id())).update({"security_qns": user.get_security_qns()})
        return redirect(url_for("account"))
    return render_template('signup2.html', form=sign_up_form2)


@app.route('/signup3', methods=['GET', 'POST'])
@login_required
def signup3():
    sign_up_form3 = SignUpForm3(request.form)
    return render_template('signup3.html', form=sign_up_form3)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for("homepage"))
    sign_in_form = SignInForm(request.form)
    if request.method == "POST" and sign_in_form.validate():
        user = db.collection("Users").where("email", "==", sign_in_form.email.data).get()
        if user:
            if bcrypt.check_password_hash(user[0].to_dict()["password"], sign_in_form.password.data):
                user = User.from_dict(user[0].to_dict())
                # login_user(user)
                login_user(user, remember=sign_in_form.remember.data)
                try:
                    auth.sign_in_with_email_and_password(sign_in_form.email.data, sign_in_form.password.data)
                    user = auth.current_user
                except:
                    print("Unable to login")
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for("account  "))
        else:
            flash("Incorrect Login Credentials.")
            return render_template('signin.html', form=sign_in_form)
    return render_template('signin.html', form=sign_in_form)


@app.route("/signout")
@login_required
def signout():
    logout_user()
    return redirect(url_for("homepage"))


@app.route("/forget_password", methods=['GET', 'POST'])
def reset1():
    reset_form1 = ForgetPassword1(request.form)
    if request.method == "POST":
        if reset_form1.validate():
            print(reset_form1.email.data)
            user = db.collection("Users").where("email", "==", reset_form1.email.data).get()
            print(user)
            if user:
                return redirect(url_for("reset2", id=user[0].to_dict()["id"]))
        else:
            flash("Account does not exist!")
            return redirect(url_for("reset1"))
    return render_template("reset.html", form=reset_form1)


@app.route("/forget_password/<id>", methods=['GET', 'POST'])
def reset2(id):
    # reset_form2 = ForgetPassword2(request.form)
    user = db.collection("Users").document(str(id)).get().to_dict()
    qns = [user["security_qns"]["qns1"], user["security_qns"]["qns2"], user["security_qns"]["qns3"]]
    if request.method == "POST":
        if request.form["ans1"] == user["security_qns"]["ans1"] and request.form["ans2"] == user["security_qns"]["ans2"] and request.form["ans3"] == user["security_qns"]["ans3"]:
            return redirect(url_for("reset3", id=user["id"]))
    return render_template("reset2.html", qns=qns)


@app.route("/forget_password/<id>/reset", methods=['GET', 'POST'])
def reset3(id):
    reset_form3 = ForgetPassword3(request.form)
    if request.method == "POST" and reset_form3.validate():
        db.collection("Users").document(str(id)).update({"password": reset_form3.password.data})
        # user = User.from_dict(db.collection("Users").where("email", "==", sign_in_form.email.data).get()[0].to_dict())
        # login_user(user)
        return redirect(url_for("signin"))
    return render_template("reset3.html", form=reset_form3)


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
    if request.method == "POST" and request.form["delete"] == "Delete Account":
        db.collection("Users").document(str(current_user.get_id())).delete()
        logout_user()
        redirect(url_for("homepage"))
    return render_template("account.html", user=user, displayinfo=display_info)


@app.route('/sports_courses/', methods=['GET'])
def sports_courses_sorted():
    sort_attr = ''
    if request.method == 'GET':
        sort_attr = request.args.get("sort_attr")

    print(sort_attr)
    all_courses = course_CRUD(course=None, method='load')
    print(all_courses[0].name)
    courseID_array = []
    for course in all_courses:
        courseID_array.append(course.courseID)
    print(courseID_array)
    return render_template('sports_courses.html', courseID_array= json.dumps(courseID_array), courses=all_courses, top_courses=load_top_courses(all_courses), sort_attribute = sort_attr)


@app.route('/sports_courses/about_course/', methods=['GET'])
def view_selected_course():
    selected_courseID = request.args.get("selected_courseID")
    print(selected_courseID)
    selected_course = db.collection('Courses').where("courseID", "==", selected_courseID).get()[0].to_dict()

    try:
        username = current_user.get_username()
    except:
        username = ""
    return render_template('selected_course.html', selected_course=selected_course,current_username = username)


@app.route('/spedu_store/about_product/', methods=['GET'])
def view_selected_product():
    selected_productID = request.args.get("selected_productID")
    print(selected_productID)
    selected_product = db.collection('Products').where("productID", "==", selected_productID).get()[0].to_dict()
    print(current_user.get_username())
    return render_template('selected_product.html', selected_product=selected_product,current_username = current_user.get_username())


@app.route('/admin_page/products/about_product/', methods=['POST'])
def update_delete_product():
    current_productID = request.form['current_product']
    action_input_value = request.form['action_input_product']

    if action_input_value == 'delete':
        load_delete(current_productID)
        return redirect("/admin_page/products/")
    else:
        return redirect("/admin_page/products/")


@app.route('/Shopping Cart/')
def shopping_cart():
    promo_code_dict = db.collection('Promo codes').get()
    docs = db.collection('Users').where("username", "==", current_user.get_username()).get()
    for doc in docs:
        shopping_cart = doc.to_dict()['shopping_cart']
    print(shopping_cart)
    index = 0
    courses = []
    courseID_array = []
    products = []
    productID_array = []
    while index < len(shopping_cart):
        if shopping_cart[index][0:2]=="CR":
            courses_docs = db.collection("Courses").where("courseID", "==" , shopping_cart[index]).get()
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
                tag = doc.to_dict()['tag']
                course = Course(courseID, description, short_description, duration, image, learning_outcome, level, name,
                            price, rating, reviews, students_count, trainer, video_link,tag)
                courses.append(course)
                courseID_array.append(course.courseID)
        elif shopping_cart[index][0:2]=="PR":
            products_docs = db.collection('Products').where("productID", "==" , shopping_cart[index]).get()
            for doc in products_docs:
                productID = doc.to_dict()['productID']
                category = doc.to_dict()['category']
                image = doc.to_dict()['image']
                name = doc.to_dict()['name']
                price = doc.to_dict()['price']
                description = doc.to_dict()['description']
                rating = doc.to_dict()['rating']
                reviews = doc.to_dict()['reviews']
                product = Product(productID, category, image, name, price, description, rating, reviews)
                products.append(product)
                productID_array.append(product.productID)
        else:
            pass
        index+=1

    return render_template('Shopping Cart.html',courseID_array = json.dumps(courseID_array), productID_array = json.dumps(productID_array), courses_cart = courses, products_cart=products,current_username=current_user.get_username())


@app.route('/spedu_store/')
def spedu_store():
    return render_template('main_storepage.html', products=load_products())


@app.route('/store_searchpage/')
def spedu_searchpage():
    return render_template('store_searchpage.html', products=load_products())


@app.route('/Checkout/')
def Checkout():
    personal_details = PersonalInfo(request.form)
    return render_template('Checkout.html', form=personal_details)


@app.route('/admin_page/')
def admin_page():
    return render_template('admin_page.html')


@app.route('/admin_page/courses/')
def admin_page_courses():
    return render_template('admin_page_courses.html', courses=course_CRUD(course=None, method='load'))


@app.route('/admin_page/products/')
def admin_page_products():
    return render_template('admin_page_products.html', products=load_products())


@app.route('/admin_page/courses/new_course')
def new_course():
    return render_template('new_course.html')


@app.route('/admin_page/courses/about_course/', methods=['GET'])
def view_admin_selected_course():
    selected_courseID = request.args.get("selected_courseID")
    print(selected_courseID)
    selected_course = db.collection('Courses').where("courseID", "==", selected_courseID).get()[0].to_dict()
    return render_template('admin_selected_course.html', selected_course=selected_course)


@app.route('/admin_page/products/about_product/', methods=['GET'])
def view_admin_selected_product():
    selected_productID = request.args.get("selected_productID")
    print(selected_productID)
    selected_product = db.collection('Products').where("productID", "==", selected_productID).get()[0].to_dict()
    return render_template('admin_selected_products.html', selected_product=selected_product)


@app.route('/admin_page/courses/', methods=['POST'])
def create_new_course():
    course_name = request.form['course_name']
    courseID = 'CR'+course_name.split(' ')[0][0] + course_name.split(' ')[0][1] + str(random.randrange(0, 1000))
    course_trainer = request.form['course_trainer']
    course_short_desc = request.form['course_short_desc']
    course_desc = request.form['course_desc']
    course_duration = request.form['course_duration']
    course_price = request.form['course_price']
    learning_outcome = request.form['learning_outcome']
    course_level = request.form['course_level']
    video_link = request.form['video_link']
    course_image = request.files['course_image']
    tag = request.files['tag']



    storage.child('/courses/image_of_{}'.format(courseID)).put(course_image)

    course_img_link = storage.child('/courses/image_of_{}'.format(courseID)).get_url(auth.current_user["idToken"])

    print(course_img_link)
    course_rating = 0
    course_reviews = [{'rating': 0, 'reviewer': '', 'review': ''}]
    students_count = 0
    new_course = Course(courseID, course_desc, course_short_desc, course_duration, course_img_link, learning_outcome, course_level, course_name, course_price, course_rating, course_reviews, students_count, course_trainer, video_link)
    course_CRUD(course=new_course, method='create')
    return render_template('admin_page_courses.html', courses=course_CRUD(course=None, method='load'))


@app.route('/admin_page/courses/about_course/', methods=['POST'])
def update_delete_course():
    current_courseID = request.form['current_course']
    action_input_value = request.form['action_input']
    if action_input_value == 'delete':
        course_CRUD(course=current_courseID, method='delete')
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
    tag = request.form['tag']
    course_image = request.files['course_image']
    print(course_image.filename)
    if course_image.filename == '':
            print('No selected file')
    if course_image:
        storage.child('/courses/image_of_{}'.format(courseID)).put(course_image)
    course_img_link=request.form["course_image_input"]
    print(course_img_link)
    course_rating = ""
    course_reviews = []
    students_count = 0
    course = Course(courseID, course_desc, course_short_desc, course_duration,course_img_link, learning_outcome, course_level, course_name, course_price, course_rating, course_reviews, students_count, course_trainer, video_link,tag)
    course_CRUD(course=course, method='update')
    return redirect("/admin_page/courses/")


@app.route('/admin_page/products/new_product')
def new_product():
    return render_template('new_product.html')


@app.route('/admin_page/products/update_product')
def update_product():
    return render_template('update_product.html')


@app.route('/admin_page/Promo code/')
def admin_page_promo_codes():
    promo_code_dict = db.collection('Promo codes').get()
    return render_template('Promo code.html', promo_code_dict=promo_code_dict)


@app.route('/admin_page/promo_code_form/', methods=["POST","GET"])
def promo_code_form():
    promo_code_info = promo_code_information(request.form)
    if request.method == 'POST':
        pc_data = Promo_code_data(promo_code_info.name_of_code.data, promo_code_info.value.data)
        pc_data.set_code_name(promo_code_info.name_of_code.data)
        pc_data.set_code_value(promo_code_info.value.data)
        #Promo_code_data.set_code_name(promo_code_info.name_of_code.data)
        #Promo_code_data.set_code_value(promo_code_info.value.data)
        try:
            id = db.collection("Promo codes").order_by("id", direction=firestore.Query.DESCENDING).limit(1).get()[0].to_dict()["id"] + 1
        except:
            id = 1
        db.collection('Promo codes').document(str(id)).set({"Value": (pc_data.get_code_value()), "Name": (pc_data.get_code_name()), "id": id})
        return redirect(url_for('admin_page_promo_codes'))
    return render_template('promo_code_form.html', form=promo_code_info)

@app.route('/teach_on_spedu/')
def teach_on_spedu():
    return render_template('teach_on_spedu.html')


if __name__ == "__main__":
    app.run(debug=True)
