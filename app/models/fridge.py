from app import db
from sqlalchemy.orm import relationship

from dataclasses import dataclass

# fridge table
# add ForeignKey to connect with item table


@dataclass
class Fridge(db.Model):
    id: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    items = db.relationship("Item", backref="fridge")
