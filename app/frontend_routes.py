
from flask import Blueprint, send_from_directory
from flask.templating import render_template
from . import oauth_config as oauth_config
from app.models.customer import Customer
from flask_login import current_user, login_required
from app import app

app_bp = Blueprint("app", __name__, url_prefix="/app")


@oauth_config.login_manager.user_loader
def get_user(id):
    customer = Customer.query.get(int(id))
    return customer


@app.route('/<path:filename>')
def root_files(filename):
    print(filename)
    return send_from_directory(app.static_folder, filename)


@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory(f'{app.static_folder}/static', path)


@app_bp.route("/")
def serve():
    print(app.static_folder)
    return render_template('index.html')
