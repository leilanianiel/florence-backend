from app import db
from datetime import timedelta, datetime
import datetime


class Item(db.Model):
    item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    item_inventory = db.Column(db.Integer, default=0)
    total_inventory = db.Column(db.Integer, default=0)
    expiration = db.Column(db.DateTime, default=(datetime.datetime.now() + (datetime.timedelta(days=(7)))))
    fridge_id = db.Column(db.Integer, db.ForeignKey('fridge.fridge_id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))

    