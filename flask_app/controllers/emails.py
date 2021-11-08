# all @app.route() functions

from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models import model_email
from flask_app.models.model_email import Email


@app.route('/')
def index():
    return render_template('email.html')

@app.route('/register', methods=['POST'])
def register():
    if not Email.validate_user(request.form):
        return redirect('/')
    data = {
        # 'id' : id
        "email" : request.form['email'],
    }
    id = Email.create(data)
    return redirect(f'/saved_emails/{id}')

@app.route('/saved_emails/<int:id>')
def email_list(id):
    return render_template('saved_emails.html')