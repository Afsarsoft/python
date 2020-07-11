# +++++++++++++++++++++++++++++++++++++++++++++
# Flask 
# +++++++++++++++++++++++++++++++++++++++++++++
# Flask is a very popular Micro framework for building Python web application 
#
#  http://flask.pocoo.org/docs/1.0/quickstart/
## Installation for windows: 
# Note: Use "command Prompt" and run it as adminstrator
# 1- Make a project folder  
#
# 2- Go to the project folder
#
# 3- Create an environment as follow:
# py -3 -m venv venv
#
# 4- Activate the environment as follow:
# venv\Scripts\activate
#
# 5- Install Flask as follow:
# pip install Flask
#
# 6- Create hello.py as follow 
'''
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
'''
# 7- Set your flask app as following example:
# Note: Never call your app flask.py
# A- set FLASK_APP=hello.py
# B- set FLASK_ENV=development
# Note: will notice more info related to "Environment: development, Debug mode: on ..."
# This does the following things:
# - it activates the debugger
# - it activates the automatic reloader
# - it enables the debug mode on the Flask application.
# Also can control debug mode separately from the environment by exporting FLASK_DEBUG=1.
# C- flask run
#
# Note: will have somthing as follow:
# Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# You can see your site using the following:
# http://127.0.0.1:5000
# OR
# http://localhost:5000
#
# To uninstall flask:
# pip uninstall flask
#
# To remove the activated environment, delete folder "venv" from your project folder
# +++++++++++++++++++++++++++++++++++++++++++++
#
# Sample app "Hello World", geting started 
#  http://flask.pocoo.org/docs/1.0/quickstart/
#
# Let's change the sample app a little 
'''
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<H1>Hello World!</H1>"
'''
# Chaneg the code to have about page 
'''
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Home Page!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page!</h1>"
'''
#
# Will have about page in following link:
# http://localhost:5000/about
#
# We can have the home page and root page be same as follow:
# http://localhost:5000 or http://localhost:5000/home
'''
from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page!</h1>"
'''




