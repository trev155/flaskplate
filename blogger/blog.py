from flask import Blueprint, render_template, request
from .models import User, Post
from . import db

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    users = User.query.all()
    posts = Post.query.all()
    return render_template("blog/index.html", users=users, posts=posts)


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

    if request.method == "GET":
        posts = Post.query.all()
        return render_template("blog/posts.html", posts=posts)
