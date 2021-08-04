# from flask import Blueprint, url_for, redirect, session
# from flask.json import jsonify
# from flask.templating import render_template
# from . import oauth_config as oauth_config
# from app.models.customer import Customer
# from app.models.fridge import Fridge
# from app import db
# from flask_login import current_user, login_required, login_user, logout_user
# import json

# auth_bp = Blueprint("auth", __name__, url_prefix="/")


# @oauth_config.login_manager.user_loader
# def get_user(id):
#     customer = Customer.query.get(int(id))
#     return customer


# @auth_bp.route("/", methods=["GET"], strict_slashes=False)
# def anon_home():
#     return render_template('home.html', user=None)


# @auth_bp.route("/secureHome", methods=["GET"], strict_slashes=False)
# @login_required
# def home():
#     return render_template('home.html', user=get_user(current_user.id))


# @auth_bp.route("/login", methods=["GET"], strict_slashes=False)
# def login():
#     redirect_uri = url_for('auth.auth', _external=True)
#     return oauth_config.oauth.google.authorize_redirect(redirect_uri)


# @auth_bp.route("/register", methods=["GET"], strict_slashes=False)
# def register():
#     redirect_uri = url_for('auth.auth_register', _external=True)
#     return oauth_config.oauth.google.authorize_redirect(redirect_uri)


# @auth_bp.route("/authRegister", strict_slashes=False)
# def auth_register():
#     token = oauth_config.oauth.google.authorize_access_token()
#     user = oauth_config.oauth.google.parse_id_token(token)
#     print(user.email)
#     print(user.name)

#     existing_customers = db.session.query(Customer).filter(
#         Customer.email == user.email).all()

#     # need to show user that something is wrong
#     if len(existing_customers) > 0:
#         return redirect('/')

#     fridge = Fridge()
#     db.session.add(fridge)
#     db.session.commit()
#     customer = Customer(user_name=user.name, email=user.email,
#                         picture=user.picture, fridge_id=fridge.id)
#     db.session.add(customer)
#     db.session.commit()

#     login_user(customer)
#     return redirect('/')


# @auth_bp.route("/auth", strict_slashes=False)
# def auth():
#     token = oauth_config.oauth.google.authorize_access_token()
#     user = oauth_config.oauth.google.parse_id_token(token)

#     existing_customer = db.session.query(Customer).filter(
#         Customer.email == user.email).all()
#     if len(existing_customer) == 0:
#         raise "Customer doesn't exist"
#     print(jsonify(existing_customer[0]))
#     login_user(existing_customer[0])
#     return redirect('/')


# @auth_bp.route("/logout", strict_slashes=False)
# @login_required
# def logout():
#     session.pop('user', None)
#     logout_user()
#     return redirect('/')
