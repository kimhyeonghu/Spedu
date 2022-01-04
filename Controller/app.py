from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='../View/HTML', static_folder='../View/static')

@app.route('/')
def homepage():
    return render_template('homepage.html')
if __name__ == "__main__":
     app.run(debug=True)