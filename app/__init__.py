from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv, dotenv_values
import os
from flask_cors import CORS
from . import oauth_config as oauth_config

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

app = None


def create_app(test_config=None):
    global app
    app = Flask(__name__, static_folder="frontend",
                template_folder="frontend")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.url_map.strict_slashes = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    if "development" in os.environ.get("FLASK_ENV"):
        app.config['secrets'] = dotenv_values('.env.secrets')
        app.config['LOGIN_DISABLED'] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = app.config['secrets']["SQLALCHEMY_DATABASE_URI"]

    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel
    from app.models.item import Item
    from app.models.category import Category
    from app.models.fridge import Fridge
    from app.models.customer import Customer
    from app.models.product import Product

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    oauth_config.init(app)

    from .category_routes import category_bp
    from .customer_routes import customer_bp
    from .fridge_routes import fridge_bp
    from .product_routes import product_bp
    from .item_routes import item_bp
    from .auth_routes import auth_bp
    from .frontend_routes import app_bp
    from .recipes_routes import recipes_bp

    # Register Blueprints here
    app.register_blueprint(category_bp)
    app.register_blueprint(fridge_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(item_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(app_bp)
    app.register_blueprint(recipes_bp)

    CORS(app, origins=["http://localhost:3000", "https://florence-fridge-app.herokuapp.com"])

    return app
