from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/projects')
def projects():
    return render_template("projects.html")

@views.route('/workshop')
def blog():
    return render_template("workshop.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/resume')
def resume():
    return render_template('resume.html')
