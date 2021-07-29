from app import db
from sqlalchemy.orm import relationship
from app.models.customer import Customer

class Category (db.Model):
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    
    items = db.relationship("Item", backref="category")
