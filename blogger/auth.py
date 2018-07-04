from flask import Blueprint, request, render_template
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        # add user
        name = request.form["name"]
        password = request.form["password"]
        user = User(name=name, password=password)
        db.session.add(user)
        db.session.commit()
        return "OK"
    if request.method == "GET":
        return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        # verify password
        name = request.form["name"]
        password = request.form["password"]
        user = User.query.filter_by(name=name).first()

        if user is None:
            return "Name not found", 404
        if not user.check_password(password):
            return "Incorrect Password", 404

        # success - login user
        login_user(user)
        return "OK"

    if request.method == "GET":
        return render_template("auth/login.html")


@bp.route("/logout")
@login_required
def logout():
    print("Now logging out user:", current_user)
    logout_user()
    return "Logged Out!"
