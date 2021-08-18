from flask.helpers import make_response
from app.customer_routes import customer
from app.models.fridge import Fridge
from app.models.customer import Customer
from flask import Blueprint, jsonify
from app import db
from app.models.fridge import Fridge
from flask_login import login_required


# example_bp = Blueprint('example_bp', __name__)
fridge_bp = Blueprint("fridge", __name__, url_prefix="/fridge")

# GET ALL FRIGES 
@fridge_bp.route("", methods=["GET"], strict_slashes=False)
@login_required
def all_fridges():

    fridges = Fridge.query.all()
    return jsonify(fridges), 200


# ADD NEW FRIDGE 
@fridge_bp.route("", methods=["POST"], strict_slashes=False)
@login_required
def new_fridge():

    fridge = Fridge()
    db.session.add(fridge)
    db.session.commit()

    return jsonify(fridge), 201


# GET ALL ITEMS IN 1 FRIDGE 
@fridge_bp.route("/<id>/items", methods=["GET"], strict_slashes=False)
@login_required
def fridge_items(id):
    # user_name = Customer()

    fridge = Fridge.query.get(id)
    
    return jsonify(fridge.items), 200
    



# DELETE 1 SPECIIC ITEM (not working yet)
@fridge_bp.route("/<id>", methods=["DELETE"], strict_slashes=False)
@login_required
def handle_fridge(id):
    fridge = Fridge.query.get(id)

    db.session.delete(fridge)
    db.session.commit()
    return make_response({

        "id": fridge.id
    }, 200)



