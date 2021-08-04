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
from flask_login import login_required

# example_bp = Blueprint('example_bp', __name__)
category_bp = Blueprint("category", __name__, url_prefix="/category")

# GET ALL AND CREATE NEW CATEGORY
@login_required 
@category_bp.route("", methods=["GET", 'POST'], strict_slashes=False)
def category():
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



# GET, UPDATE, DELETE 1 SPECIIC CATEGORY
# @login_required 
@category_bp.route("/<id>", methods=['GET', 'PATCH', 'DELETE'], strict_slashes=False)
def handle_category(id):

    category = Category.query.get(id)

    if request.method == "GET":
        return jsonify(category), 200



    if request.method == "PATCH": 
        request_body = request.get_json(id)
        if "name" not in request_body:
            return (jsonify({"details": "Invalid data"}), 400)
            
        category.name = request_body["name"]
        db.session.commit()
        return jsonify(category), 201


    if request.method == "DELETE":
        db.session.delete(category)
        db.session.commit()
    return make_response({
        "Deleted": category.name,
        "id" : category.id
        }, 200)
