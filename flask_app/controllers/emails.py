from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.email import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_email', methods = ["POST"])
def create_email():
    if not Email.validate_email(request.form):
        return redirect('/')
    Email.create_new_email(request.form)
    return redirect ('/success')

@app.route('/success')
def results():
    emails = Email.show_emails()
    email_name = emails[len(emails)-1]
    return render_template('success.html', emails = emails, email_name = email_name)
