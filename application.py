from flask import Flask, redirect, render_template, session, url_for
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route(f"/<var>")
def func(var):
    files = os.listdir("templates")
    if (var in files):
        return render_template(var)
    else:
        return render_template("404.html")

print("This is the newbranch version of the application.py!")
print("I wonder what'll happen when we merge?")



print("x")