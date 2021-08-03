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


@item_bp.route("", methods=["GET"], strict_slashes=False)
def get_item():
    if request.method == "GET":
        items = Item.query.all()

        return jsonify(items)


@item_bp.route("", methods=["POST"], strict_slashes=False)
def create_item():
    if request.method == "POST":

        request_body = request.get_json()
        if "name" not in request_body or "item_inventory" not in request_body or "category_id" not in request_body:
            return jsonify({"details": "Invalid data"}), 400

        category_id = request_body["category_id"]

        category = Category.query.get(category_id)

        if category is None:
            return jsonify({"details": "Invalid data"}), 404

        expiration: datetime
        if 'expiration' not in request_body:
            expiration = datetime.datetime.now() + datetime.timedelta(days=7)
        else:
            expiration = datetime.parse(request_body['expiration'])

        item = Item(
            category_id=category_id,
            name=request_body["name"],
            item_inventory=request_body["item_inventory"],
            expiration=expiration,
        )

        db.session.add(item)
        db.session.commit()

        return jsonify(item), 201
