from flask import Flask, render_template, session, redirect, request
from flask_app import app
from flask_app.models.user import User
from flask import flash

# home
@app.route("/")
def index():
    return render_template("index.html")