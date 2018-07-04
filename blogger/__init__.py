import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# -- create the app object
app = Flask(__name__, instance_relative_config=True)

# -- configs
app.config["ENV"] = "development"
app.config["SECRET_KEY"] = "DEV"
app.config["DEBUG"] = True
# point this to the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(os.path.dirname(os.path.abspath(__file__))) + "/app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# -- database setup
db = SQLAlchemy(app)
db.create_all()

# -- sqlite foreign key enforcement
from sqlalchemy.engine import Engine
from sqlalchemy import event

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

# -- Flask-login
from .models import User
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# -- register blueprints (and their corresponding routes)
from . import auth
app.register_blueprint(auth.bp)

from . import blog
app.register_blueprint(blog.bp)
