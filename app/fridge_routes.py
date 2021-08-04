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

    return jsonify(fridge), 200


@fridge_bp.route("", methods=["GET"], strict_slashes=False)
@login_required
def customers_fridge():

    fridge = Fridge.query.all()
    fridge_response = []

    for i in fridge:
        fridge_response.append(i)
    return jsonify(fridge_response)
