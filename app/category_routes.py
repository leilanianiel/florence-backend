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

# example_bp = Blueprint('example_bp', __name__)
category_bp = Blueprint("category", __name__, url_prefix="/category")


@category_bp.route("", methods=["GET", 'POST', 'DELETE'], strict_slashes=False)
def category():
    if request.method == "GET":
        categories = Category.query.all()

        return jsonify(categories), 200

    if request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body or "id" not in request_body:
            return make_response(jsonify({"details": "Invalid data"}), 400)

        category = Category(name=request_body["name"], id=request_body["id"])

        db.session.add(category)
        db.session.commit()

        return jsonify(category), 201

    if request.method == "DELETE":
        db.session.delete(Category.id)
        # db.session.query(Category).delete()
        db.session.commit()

        return "Done", 201


@category_bp.route("{id}", methods=["GET", 'POST', 'DELETE'], strict_slashes=False)
def category_single(id):
    if request.method == "GET":
        categories = Category.query.all()

        return jsonify(categories), 200

    if request.method == "POST":
        request_body = request.get_json()
        if "name" not in request_body or id is None:
            return make_response(jsonify({"details": "Invalid data"}), 400)

        category = Category(name=request_body["name"], id=id)

        db.session.add(category)
        db.session.commit()

        return jsonify(category), 201

    if request.method == "DELETE":
        db.session.query(Category).filter(Category.id == id).delete()
        db.session.commit()

        return "Done", 201
