from app import db
from app.models.fridge import Fridge
from datetime import timedelta, datetime
from sqlalchemy.orm import backref

from dataclasses import dataclass

@dataclass
class Customer(db.Model):
    id: int
    user_name :str
    email :str
    picture :str
    fridge_id:int

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    picture = db.Column(db.String)
    
    fridge_id = db.Column(db.Integer, db.ForeignKey('fridge.id'))

    fridge = db.relationship("Fridge", backref=backref("customer", uselist=False))
