from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Email():
    
    def __init__(self, data):
        self.id = data['id']
        self.email_address = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_new_email(cls, data):
        query = 'INSERT INTO emails (email_address) VALUES (%(email_address)s);'
        new_email_id = connectToMySQL('email_addresses').query_db(query,data)
        return new_email_id

    @classmethod
    def show_emails(cls):
        query = 'SELECT * FROM emails;'
        results = connectToMySQL('email_addresses').query_db(query)
        emails = []
        for item in results:
            new_email = Email(item)
            emails.append(new_email)
        return emails

    @classmethod
    def get_email(cls, data):
        query = 'SELECT * FROM emails WHERE email_address=%(email_address)s;'
        results = connectToMySQL('email_addresses').query_db(query,data)
        emails = []
        for item in results:
            emails.append(Email(item))
        return emails

    @staticmethod
    def validate_email(info):
        email_regex = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$") 
        is_valid = True
        if not email_regex.match(info['email_address']):
            flash("Invalid email address! Try again!")
            is_valid = False
        if len(Email.get_email({'email_address':info['email_address']})) !=0:
            flash("This email address is already in use. Try again!")
            is_valid = False
        return is_valid