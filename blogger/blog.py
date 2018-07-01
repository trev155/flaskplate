from flask import Blueprint, render_template, request
from .models import User, Post
from . import db

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    return render_template("blog/index.html")


@bp.route("/user", methods=("GET", "POST"))
def user():
    if request.method == "POST":
        # add user
        name = request.form["name"]
        email = request.form["email"]
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return "OK"

    users = User.query.all()
    return render_template("blog/users.html", users=users)


@bp.route("/post", methods=("GET", "POST"))
def post():
    if request.method == "POST":
        # add post
        title = request.form["title"]
        body = request.form["body"]
        posted_by = int(request.form["posted_by"])
        post = Post(title=title, body=body, posted_by=posted_by)
        db.session.add(post)
        db.session.commit()
        return "OK"

    posts = Post.query.all()
    return render_template("blog/posts.html", posts=posts)
