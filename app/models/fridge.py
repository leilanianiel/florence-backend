from app import db
from sqlalchemy.orm import relationship

# fridge table
# add ForeignKey to connect with item table
class Fridge(db.Model):
    fridge_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    items = db.relationship("Item", backref="fridge")
