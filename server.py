from flask import Flask
from flask_bootstrap import Bootstrap
from Model.System import System

RankrSystem = System()
RankrSystem.create_list("Countries", ["Australia", "New Zealand", "China", "USA", "Russia", "UK", "Ghana", "Brazil"])

app = Flask(__name__)
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
Bootstrap(app)
