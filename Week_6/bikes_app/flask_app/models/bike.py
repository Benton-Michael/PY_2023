from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

class Bike:
    DB = "bikes"
    def __init__(self, data):
        self.id = data['id']
        self.make = data['make']
        self.model = data['model']
        self.type = data['type']
        self.purchase_date = data['puchase_date']
        self.description = data['description']
        self.is_still_owned = data['is_still_owned']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.owner = None
        # Changes for this project?