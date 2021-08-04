from app import db
from sqlalchemy.orm import relationship
from dataclasses import dataclass


@dataclass
class Category(db.Model):
    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String)

    product = db.relationship(
        "Product", backref="Category", passive_deletes=True)
