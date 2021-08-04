from app import db
from datetime import datetime
import datetime
from dataclasses import dataclass


@dataclass
class Item(db.Model):
    id: int
    count: int
    expiration: datetime
    fridge_id: int
    product_id: int

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, unique=True)
    count = db.Column(db.Integer, default=0)
    expiration = db.Column(db.DateTime, default=(
        datetime.datetime.now() + (datetime.timedelta(days=(7)))))

    fridge_id = db.Column(db.Integer, db.ForeignKey('fridge.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
