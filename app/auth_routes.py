from app.models.fridge import Fridge
from flask import Blueprint, request, jsonify, make_response
from dotenv import load_dotenv
import os
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transpost.requests import Request
# from googleapiclient.discovery import build
import requests
from app import db
from app.models.item import Item
from flask import Flask, jsonify, url_for, redirect, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 

oauth = OAuth(app)
google= oauth.register(
        name= "google",
        client_id="",
        client_secret="",
        access_token_url="https://accounts.google.com/o/oauth2/token",
        access_token_params=None,
        authorize_url="http://localhost:5000",
        authorize_params=None,
        api_base_url="https://www.googleapis.com/oauth2/v1/",
        client_kwargs={"scope": "openid profile email"}
)
# google = oauth.register('google', {...})


@app.route('/login')
def login():
    google = oauth.create_client("google")
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client("google")
    token = google.authorize_access_token()
    # you can save the token into database
    resp = google.get("userinfo")
    user_info = resp.json()
    return jsonify(user_info)


# flow = InstalledAppFlow.from_clients_secrets_file("client_secrests.json",
# )

# example_bp = Blueprint('example_bp', __name__)
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("token", methods=["GET"], strict_slashes=False)
def get_token():
    if request.method == "GET":
        fridge = Fridge.query.all()
        fridge_response = []

        return jsonify(fridge_response)
