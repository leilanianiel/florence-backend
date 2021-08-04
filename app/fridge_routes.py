from app.models.fridge import Fridge
from flask import Blueprint, jsonify
from app import db
from app.models.fridge import Fridge
from flask_login import login_required


# example_bp = Blueprint('example_bp', __name__)
fridge_bp = Blueprint("fridge", __name__, url_prefix="/fridge")


@fridge_bp.route("", methods=["POST"], strict_slashes=False)
@login_required
def new_fridge():

    fridge = Fridge()
    db.session.add(fridge)
    db.session.commit()

    return jsonify(fridge), 201


@fridge_bp.route("", methods=["GET"], strict_slashes=False)
@login_required
def all_fridges():

    fridges = Fridge.query.all()
    return jsonify(fridges), 200


@fridge_bp.route("/<id>/items", methods=["GET"], strict_slashes=False)
@login_required
def fridge_items(id):

    fridge = Fridge.query.get(id)

    return jsonify(fridge.items), 200
