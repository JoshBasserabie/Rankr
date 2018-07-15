from server import app, RankrSystem
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
        'Rankr',
        View('Home', 'home'),
    )

nav.init_app(app)