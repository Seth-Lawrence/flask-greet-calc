from flask import Flask, request

app = Flask(__name__)

@app.get('/welcome')
def welcome():
    """takes nothing returns a string 'welcome'"""

    return "welcome"

@app.get('/welcome/home')
def welcome_home():
    """takes nothing returns a string 'welcome home"""

    return "welcome home"

@app.get('/welcome/back')
def welcome_back():
    """takes nothing returns a string 'welcome back"""

    return "welcome back"
