from logging import log
from flask import Blueprint, render_template, url_for, redirect, session
from . import oauth_config as oauth_config

auth_bp = Blueprint("auth", __name__, url_prefix="/")

@auth_bp.route("/", methods=["GET"], strict_slashes=False)
def home():
    user = session.get('user')
    return render_template('home.html', user=user)

@auth_bp.route("/login", methods=["GET"], strict_slashes=False)
def login():
    redirect_uri = url_for('auth.auth', _external=True)
    print(redirect_uri)
    return oauth_config.oauth.google.authorize_redirect(redirect_uri)


@auth_bp.route("/auth", strict_slashes=False)
def auth():
    token = oauth_config.oauth.google.authorize_access_token()
    user = oauth_config.oauth.google.parse_id_token(token)
    session['user'] = user
    return redirect('/')


@auth_bp.route("/logout", strict_slashes=False)
def logout():
    session.pop('user', None)
    return redirect('/')


