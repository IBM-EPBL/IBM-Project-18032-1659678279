from flask import Flask,blueprint,render_template,flash,request,session,redirect,url_for
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/signup")
def about():
    return render_template("signup.html")    
@app.route("/login")
def about():
    return render_template("login.html")    