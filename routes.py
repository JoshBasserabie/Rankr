from server import app
from flask import render_template, request, redirect, url_for, abort
from flask_nav import Nav
from flask_nav.elements import Navbar, View

nav = Nav()

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@nav.navigation()
def mynavbar():
    return Navbar(
        'Carry Me Daddy',
        View('Home', 'home'),
        View('Team Stats', 'stats'),
        View('Team Page', 'team')
    )

nav.init_app(app)