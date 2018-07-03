from flask import Flask
from flask_bootstrap import Bootstrap
from Model.System import System

RankrSystem = System()

app = Flask(__name__)
app.config['TRAP_BAD_REQUEST_ERRORS'] = True
Bootstrap(app)
