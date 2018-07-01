from flask import Blueprint, render_template, jsonify
from .models import User, Post

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    return render_template("blog/index.html")


@bp.route("/users")
def get_users():
    users = User.query.all()
    return render_template("blog/users.html", users=users)


@bp.route("/posts")
def get_posts():
    posts = Post.query.all()
    return render_template("blog/posts.html", posts=posts)
