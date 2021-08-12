from flask import Blueprint, request, jsonify, make_response
from dotenv import load_dotenv
from app import db
from app.models.product import Product
from app.models.category import Category
import datetime
from flask_login import login_required

product_bp = Blueprint("product", __name__, url_prefix="/product")


# GET ALL PRODUCTS
@product_bp.route("", methods=["GET"], strict_slashes=False)
@login_required
def get_products():
    products = Product.query.all()
    return jsonify(products)


# CREATE NEW PRODUCT
@product_bp.route("", methods=["POST"], strict_slashes=False)
@login_required
def create_product():
    request_body = request.get_json()
    if "name" not in request_body or "category_id" not in request_body:
        return jsonify({"details": "Invalid data"}), 400

    category_id = request_body["category_id"]
    category = Category.query.get(category_id)

    # if category is not a currently made, return 404
    if category is None:
        return jsonify({"details": "Invalid data, no category found"}), 404

    barcode = None
    if "barcode" in request_body:
        barcode = request_body["barcode"]

    image = None
    if "image" in request_body:
        image = request_body["image"]

    product = Product(
        category_id=category_id,
        name=request_body["name"],
        barcode=barcode,
        image=image,
    )

    db.session.add(product)
    db.session.commit()

    return jsonify(product), 201


# GET, UPDATE, DELETE 1 SPECIIC PRODUCT 
@product_bp.route("/<id>", methods=['GET', 'PATCH', 'DELETE'], strict_slashes=False)
def handle_product(id):
    product = Product.query.get(id)

    if request.method == "GET":
        return jsonify(product), 200

    if request.method == "PATCH":
        request_body = request.get_json()
        if "name" not in request_body or "category_id" not in request_body:
            return jsonify({"details": "Invalid data"}), 400

        product.name = request_body["name"]
        product.category_id = request_body["category_id"]

        db.session.commit()
        return jsonify(product), 201

    if request.method == "DELETE":
        db.session.delete(product)
        db.session.commit()
        return make_response({
            "Deleted": product.name,
            "id": product.id
        }, 200)
