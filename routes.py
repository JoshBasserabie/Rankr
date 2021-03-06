from random import sample
from server import app, RankrSystem
from flask import render_template, request, redirect, url_for, abort
from flask_nav import Nav
from flask_nav.elements import Navbar, View

nav = Nav()

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        newList = RankrSystem.create_list(request.form['ListName'])
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
    voting_pair = voting_list.get_random_pair()
    if request.method == "POST":
        vote = request.form['submit']
        winner, loser = [int(i) for i in vote.split()]
        voting_list.handleVote(winner, loser)
        winner = voting_list.items[winner].name
        loser = voting_list.items[loser].name
        print(voting_list)
        return render_template("vote.html", hasVoted = True, listName = listName, first = voting_pair[0], second = voting_pair[1], winner=winner, loser=loser)
    print(voting_pair)
    return render_template("vote.html", hasVoted = False, listName = listName, first = voting_pair[0], second = voting_pair[1])

@app.route("/results/<listName>/", methods=['GET'])
def results(listName):
    voting_list = RankrSystem.get_list(listName)
    print(voting_list.sortedList)
    return render_template("results.html", voting_list = voting_list)


@nav.navigation()
def mynavbar():
    return Navbar(
        'Rankr',
        View('Home', 'home'),
    )

nav.init_app(app)