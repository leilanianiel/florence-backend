from app.models.fridge import Fridge
from flask import Blueprint, request, jsonify, make_response
from dotenv import load_dotenv
import os
import requests
from app import db
from app.models.item import Item
from app.models.fridge import Fridge
from app.models.customer import Customer
import datetime
import json
from flask_login import login_required

customer_bp = Blueprint("customer", __name__, url_prefix="/customer")


@customer_bp.route("", methods=["GET", 'POST'], strict_slashes=False)
@login_required 
def customer():
    if request.method == "GET":
        categories = Customer.query.all()

        return jsonify(categories), 200

@customer_bp.route("<id>", methods=["GET", 'DELETE'], strict_slashes=False)
@login_required 
def single_customer(id):
    if request.method == "DELETE":
        customer = Customer.query.get(id)
        
        db.session.delete(customer)
        db.session.commit()
        return "Done", 200
