from app import db
from datetime import timedelta, datetime
import datetime
from dataclasses import dataclass
from app.models.fridge import Fridge
from app.models.category import Category

@dataclass #These classes don’t contain any additional functionality and can’t independently operate on the data that they own.
class Item(db.Model):
    id: int
    name: str
    image: str
    item_inventory: int
    total_inventory: int
    expiration: datetime
    fridge_id:int
    category_id:int
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    item_inventory = db.Column(db.Integer, default=0)
    total_inventory = db.Column(db.Integer, default=0)
    expiration = db.Column(db.DateTime, default=(datetime.datetime.now() + (datetime.timedelta(days=(7)))))
    
    fridge_id = db.Column(db.Integer, db.ForeignKey('fridge.id'), unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), unique=True)

#  Category.query.find()   
# { "name": "my item", "category": "my category" }
