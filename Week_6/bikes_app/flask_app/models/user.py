# import the function that will return an instance of a connection
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_bcrypt import Bcrypt
# from flask_app.models import 
import re

bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
DB = "bikes"

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.user_name = data["user_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.bikes_owned = []
        # What changes need to be made for this project?
        # What must be added here for class association?

    # Create Users Models
    @classmethod
    def create_user(cls, user_data):
        pass
    
    # Read Users Models


    # Update Users Models



    # Delete Users Models


    # Validation
    