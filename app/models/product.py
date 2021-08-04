from app import db
from dataclasses import dataclass


@dataclass
class Product(db.Model):
    id: int
    name: str
    image: str
    barcode: str
    category_id: int

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, unique=True)

    name = db.Column(db.String)
    image = db.Column(db.String)
    barcode = db.Column(db.String, unique=True)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    item = db.relationship("Item", backref="Product", passive_deletes=True)
