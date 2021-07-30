from app import db
from sqlalchemy.orm import relationship
from dataclasses import dataclass

@dataclass
class Category(db.Model):
    id: int
    name: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    name = db.Column(db.String)

    item = db.relationship("Item", backref="Category")

# @classmethod
# def check_in(cls, category_id):

#     # customer = Customer.query.get(customer_id)
#     # video = Video.query.get(video_id)
#     item = Item.query.filter(Item.category_id==category_id).all()

#     return check_in()
