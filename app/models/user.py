from flask import current_app
from sqlalchemy.orm import relationship
from app import db
from app.models.item import Item
from datetime import timedelta, datetime


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), unique = True, autoincrement=True)
    item = db.relationship("Item", back_populates="user")

    # def __init__(self,username,id, item):
    #     self.username = username
    #     self.id = id
    #     self.item = item

    # def __rep__(self):
    #     return'<User %r>' % self.username



    # def to_json(self):

    #     regular_response = {

    #         "id": self.customer_id,
    #         "name": self.name,
    #         "registered_at": self.registered_at,
    #         "postal_code": self.postal_code,
    #         "phone": self.phone,
    #         "videos_checked_out_count": self.videos_checked_out_count
    #     }
    #     return regular_response