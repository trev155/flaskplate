"""
Can run through these lines at a time in a python console.
"""

from blogger.models import *
from blogger import db

# Drop all tables / data
db.drop_all()
# Create table / data (those in models.py)
db.create_all()

# Create and add users
u1 = User(name="bob", email="bob@gmail.com")
u2 = User(name="alice", email="alice@gmail")
u3 = User(name="joe", email="woah@hotmail.com")
db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.commit()
print(User.query.all())

# Create and add posts
p1 = Post(title="Hello World", body="This is a post", posted_by=1)
p2 = Post(title="Another post", body="it is another post!", posted_by=3)
p3 = Post(title="Woah!", body="the body of this post...", posted_by=3)
p4 = Post(title="wait, another post", body="okay, this is great, is it not great!!!", posted_by=3)
db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(p4)
db.session.commit()
print(Post.query.all())

# Selections

# Updates

# Deletions

# Note how we can access relationship data
usr = User.query.filter_by(name="joe").first_or_404()
print(usr.posts)

pst = Post.query.filter_by(title="Woah!").first_or_404()
print(pst.user)
