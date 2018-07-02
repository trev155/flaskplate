from flask import Blueprint, request, render_template, abort
from werkzeug.security import check_password_hash, generate_password_hash
from .models import User
from . import db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        # add user
        name = request.form["name"]
        password = generate_password_hash(request.form["password"])
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
        user = User.query.filter_by(name=name).first_or_404()
        if not check_password_hash(user.password, password):
            abort(404)
        return "OK"

    if request.method == "GET":
        return render_template("auth/login.html")
