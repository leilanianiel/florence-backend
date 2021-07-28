from app import db
from sqlalchemy.orm import relationship
from app.models.item import Item

# fridge table
# add ForeignKey to connect with item table
class Fridge (db.Model):
    fridge_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.item_id'))

    item = relationship("Item", back_populates="fridge")

