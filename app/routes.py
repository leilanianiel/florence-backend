from app.models.fridge import Fridge
from flask import Blueprint, request, jsonify, make_response
from dotenv import load_dotenv
import os
import requests
from app import db
from app.models.item import Item


# example_bp = Blueprint('example_bp', __name__)
fridge_bp = Blueprint("fridge", __name__, url_prefix="/fridge")


@fridge_bp.route("", methods=["GET"], strict_slashes=False)
def customers_fridge():
        if request.method == "GET":
                fridge = Fridge.query.all()
                fridge_response = []

        for i in fridge:
                fridge_response.append(i.to_json())
        return jsonify(fridge_response)



