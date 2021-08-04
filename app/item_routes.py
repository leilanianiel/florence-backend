from app.models.fridge import Fridge
from flask import Blueprint, request, jsonify, make_response
from dotenv import load_dotenv
import os
import requests
from app import db
from app.models.item import Item
from app.models.fridge import Fridge
from app.models.category import Category
import datetime
import json

item_bp = Blueprint("item", __name__, url_prefix="/item")


# GET ALL ITEMS
@item_bp.route("", methods=["GET"], strict_slashes=False)
def get_item():
    if request.method == "GET":
        items = Item.query.all()
        return jsonify(items)


# CREATE NEW ITEM 
@item_bp.route("", methods=["POST"], strict_slashes=False)
def create_item():
    

    if request.method == "POST":

        request_body = request.get_json()
        if "name" not in request_body or "item_inventory" not in request_body or "category_id" not in request_body:
            return jsonify({"details": "Invalid data"}), 400

        category_id = request_body["category_id"]
        category = Category.query.get(category_id)
        
        #if category is not a currently made, return 404
        if category is None:
            return jsonify({"details": "Invalid data, no category found"}), 404

        # expiration: datetime
        if 'expiration' not in request_body:
            expiration = datetime.datetime.now() + datetime.timedelta(days=7)
        else:
            expiration = datetime(request_body['expiration'])
        
        item = Item(
            category_id=category_id,
            name=request_body["name"],
            item_inventory=request_body["item_inventory"],
            expiration=expiration,
            # total_inventory = self.total_inventory
        )

        db.session.add(item)
        db.session.commit()

        return jsonify(item), 201



# GET, UPDATE, DELETE 1 SPECIIC ITEM 
@item_bp.route("/<id>", methods=['GET', 'PATCH', 'DELETE'], strict_slashes=False)
def handle_item(id):

    item = Item.query.get(id)

    if request.method == "GET":
        return jsonify(item), 200



    if request.method == "PATCH": 
        request_body = request.get_json()
        if "name" not in request_body or "item_inventory" not in request_body or "category_id" not in request_body:
            return jsonify({"details": "Invalid data"}), 400

        item.name = request_body["name"]
        item.item_inventory = request_body["item_inventory"]
        item.category_id = request_body["category_id"]

        db.session.commit()
        return jsonify(item), 201



    if request.method == "DELETE":
        db.session.delete(item)
        db.session.commit()
    return make_response({
        "Deleted": item.name,
        "id" : item.id
        }, 200)
