import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# -- create the app object
app = Flask(__name__, instance_relative_config=True)

# -- configs
app.config["ENV"] = "development"
app.config["DEBUG"] = True
# point this to the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(os.path.dirname(os.path.abspath(__file__))) + "/app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# -- database setup
db = SQLAlchemy(app)
db.create_all()
