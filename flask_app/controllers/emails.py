# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_email
from flask_app.models.model_email import Email


@app.route('/')
def index():
    return render_template('saved_emails.html')