from server import app, RankrSystem
from flask import render_template, request, redirect, url_for, abort
from flask_nav import Nav
from flask_nav.elements import Navbar, View

nav = Nav()

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        RankrSystem.createList()
        print(request.form)
        for item in request.form:
            print(request.form[item])
    return render_template("index.html")

@app.route("/vote", methods=['GET', 'POST'])
def vote():
    return render_template("vote.html")

@nav.navigation()
def mynavbar():
    return Navbar(
        'Rankr',
        View('Home', 'home'),
    )

nav.init_app(app)