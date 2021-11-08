# This is where classes go (class User, @classmethod)

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #<--- Add to /model top


class Email():
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(input):
        print(input)
        is_valid = True 
        if not EMAIL_REGEX.match(input['email']): 
            flash("Email is not valid!")
            is_valid = False
        return is_valid

    # ***CREATE***

    @classmethod
    def create(cls,data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        email = connectToMySQL('email_validation').query_db(query,data)
        return email

    # ***Retreive***

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_validation').query_db(query)
        emails = []
        for email in results:
            emails.append(email)
        return emails

    @classmethod
    def get_one_email(cls,data):
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        results = connectToMySQL('email_validation').query_db(query,data)
        print(results)
        return cls(results[0])

    @classmethod
    def get_one(cls,data):
        print(data)
        query = "SELECT * FROM emails WHERE id = %(id)s;"
        results = connectToMySQL('email_validation').query_db(query,data)
        print(results)
        return results

    # ***Update***

    # ***Delete***