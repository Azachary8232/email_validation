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
    Email.create(data)
    return redirect('/saved_emails')

@app.route('/saved_emails')
def email_list():
    emails = Email.get_all()
    print(emails)
    return render_template('saved_emails.html', emails = emails)