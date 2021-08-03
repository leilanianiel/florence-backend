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


def create_app(test_config=None):
    app = Flask(__name__)

    if os.environ.get("FLASK_ENV") == "development":
        app.config['secrets'] = dotenv_values('.env.secrets')
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.url_map.strict_slashes = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel
    from app.models.item import Item
    from app.models.category import Category
    from app.models.fridge import Fridge
    from app.models.customer import Customer

    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    from .category_routes import category_bp
    from .customer_routes import customer_bp
    from .fridge_routes import fridge_bp
    from .item_routes import item_bp
    from .auth_routes import auth_bp

    # Register Blueprints here
    app.register_blueprint(category_bp)
    app.register_blueprint(fridge_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(item_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)

    CORS(app)

    oauth_config.init(app)

    return app
