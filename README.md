# flaskplate
This is a template web application that uses Flask and Flask-SQLAlchemy.

It shows most of the basics in Flask, and it provides a guide for project structure.
Of course more could be added to this, perhaps as time goes on.

## Information
Using Python 3.6, Flask 1.0.2, Flask-SQLAlchemy 2.3.2. 

Info on project organization:
http://exploreflask.com/en/latest/organizing.html

Flask Tutorial:
- this goes through the process of developing a full, small webapp
- http://flask.pocoo.org/docs/1.0/tutorial/

Flask-SQLAlchemy Tutorial:
http://flask-sqlalchemy.pocoo.org/2.3/quickstart/#a-minimal-application

SQLite and Flask-SQLAlchemy:
- https://gehrcke.de/2015/05/in-memory-sqlite-database-and-flask-a-threading-trap/
- you have to set this config as some actual location (eg. in this repo)

SQLite does not enforce foreign key constraints by default:
https://stackoverflow.com/questions/31794195/how-to-correctly-add-foreign-key-constraints-to-sqlite-db-using-sqlalchemy

Flask-Login - good example:  
https://www.youtube.com/watch?v=2dEM-s3mRLE


## Usage
After cloning, start a virtual environment:
```
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install flask
pip install flask-sqlalchemy
pip install flask-login
```

To run, use the `run.py` script:
`python run.py`

### Backend - examples
See `examples.py` and run through the lines.

## Todo
- login / logout functionality
