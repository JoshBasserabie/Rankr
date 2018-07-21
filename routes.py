from random import sample
from server import app, RankrSystem
from flask import render_template, request, redirect, url_for, abort
from flask_nav import Nav
from flask_nav.elements import Navbar, View

nav = Nav()

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        print(request.form['ListName'])
        newList = RankrSystem.createList(request.form['ListName'])
        for item in request.form:
            if item != "ListName":
                newList.addItem(request.form[item])
        print(newList)
        return redirect(url_for('vote', listName = newList.name))
    return render_template("index.html")

@app.route("/vote/<listName>/", methods=['GET', 'POST'])
def vote(listName):
    if not RankrSystem.contains(listName):
        return redirect(url_for('home'))
    voting_list = RankrSystem.get_list(listName)
    voting_pair = sample(voting_list, 2)
    return render_template("vote.html", listName = listName, first = voting_pair[0], second = voting_pair[1])

@nav.navigation()
def mynavbar():
    return Navbar(
        'Rankr',
        View('Home', 'home'),
    )

nav.init_app(app)