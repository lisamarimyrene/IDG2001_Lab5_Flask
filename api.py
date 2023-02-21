# Flask is a server, same as Express
from flask import Flask, request
from database import db

app = Flask(__name__)

@app.route('/')
def hello():
    documents = db.my_collection.find()
    return {"documents": documents}
    # return '<h1>Hello, World!</h1>'


@app.route('/about/')
def about():
    return '<h2>This is a Flask web application.</h2>'







# How to install and run flask server

# pip install flask
# export FLASK_APP=api.py
# export FLASK_ENV=development
# flask run

