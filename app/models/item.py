from app import db
from datetime import timedelta, datetime
import datetime 



class Item(db.Model): 
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    tag = db.Column(db.String)
    total_inventory = db.Column(db.Integer, default=0)
    expiration = db.Column(db.DateTime, default=(datetime.datetime.now()) + (datetime.timedelta(days=(7))))

    def helper_function(self):
        helper_function = 0
        return helper_function



    
    # def to_json(self):


    #     regular_response = {

    #         "id": self.video_id,
    #         "title": self.title,
    #         "release_date": self.release_date.date.isoformat(),
    #         "total_inventory": self.total_inventory,
    #         "available_inventory": self.available_inventory
    #     }
    #     return regular_response 