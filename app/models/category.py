from app import db
from sqlalchemy.orm import relationship


# category table 
# category id
# conected to item table 
class Category (db.Model):
    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    
    item = relationship("Item", back_populates="category")
    # video = relationship("Video", back_populates="rentals")

# @classmethod
#     def check_in(cls, customer_id, video_id):

#         customer = Customer.query.get(customer_id)
#         video = Video.query.get(video_id)
#         rentals = Rental.query.filter(Rental.video_id==video_id).all()