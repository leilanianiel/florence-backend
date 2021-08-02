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

customer_bp = Blueprint("customer", __name__, url_prefix="/customer")


@customer_bp.route("", methods=["GET", 'POST'], strict_slashes=False)
def customer():
    if request.method == "GET":
        categories = Category.query.all()

        return jsonify(categories), 200

    if request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body:
            return make_response(jsonify({"details": "Invalid data"}), 400)

        category = Category(name=request_body["name"])

        db.session.add(category)
        db.session.commit()

        return jsonify(category), 201
