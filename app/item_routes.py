from app.models.product import Product
from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.item import Item
from app.models.fridge import Fridge
import datetime
from flask_login import login_required

item_bp = Blueprint("item", __name__, url_prefix="/item")


# GET ALL ITEMS
@item_bp.route("", methods=["GET"], strict_slashes=False)
@login_required
def get_item():
    items = Item.query.all()
    return jsonify(items)


# CREATE NEW ITEM
@item_bp.route("", methods=["POST"], strict_slashes=False)
@login_required
def create_item():
    request_body = request.get_json()
    if "count" not in request_body or "product_id" not in request_body or "fridge_id" not in request_body:
        return jsonify({"details": "Invalid data"}), 400

    product_id = request_body["product_id"]
    product = Product.query.get(product_id)

    # if product is not currently made, return 404
    if product is None:
        return jsonify({"details": "Invalid data, no product found"}), 404

    fridge_id = request_body["fridge_id"]
    fridge = Fridge.query.get(fridge_id)

    # if fridge is not currently made, return 404
    if fridge is None:
        return jsonify({"details": "Invalid data, no fridge found"}), 404

    # expiration: datetime
    if 'expiration' not in request_body:
        expiration = datetime.datetime.now() + datetime.timedelta(days=7)
    else:
        expiration = datetime(request_body['expiration'])

    item = Item(
        count=request_body["count"],
        expiration=expiration,
        fridge_id=fridge_id,
        product_id=product_id,
    )

    db.session.add(item)
    db.session.commit()

    return jsonify(item), 201


# GET, UPDATE, DELETE 1 SPECIIC ITEM (not working yet)
@item_bp.route("/<id>", methods=['GET', 'PATCH', 'DELETE'], strict_slashes=False)
def handle_item(id):
    item = Item.query.get(id)

    if request.method == "GET":
        return jsonify(item), 200

    if request.method == "PATCH":
        request_body = request.get_json()
        if "name" not in request_body or "count" not in request_body or "product_id" not in request_body:
            return jsonify({"details": "Invalid data"}), 400

        item.name = request_body["name"]
        item.count = request_body["count"]
        item.product_id = request_body["product_id"]

        db.session.commit()
        return jsonify(item), 201

    if request.method == "DELETE":
        db.session.delete(item)
        db.session.commit()
        return make_response({
            "id": item.id
        }, 200)


# # Decrease inventory count 
# @item_bp.route("/<id>/decrease_count", methods=['POST'])
# @login_required
# def decrease_count(id):

    
#     item = Item.query.get(id)

#     item.count -= 1
#     db.session.add(item)
#     db.session.commit()

    return make_response({"New item count": item.count}, 200)


# Decrease inventory count 
@item_bp.route("/<id>/decrease_count", methods=['POST'])
@login_required
def decrease_count(id):

    item = Item.query.get(id)

    # When count is equal to 0, delete item from fridge 
    if item.count < 2:
        item.count -= 1
        db.session.delete(item)
        db.session.commit()

        
    # decrease count of item
    else: 
        item.count -= 1
        db.session.add(item)
        db.session.commit()

    return make_response({"New item count": item.count}, 200)