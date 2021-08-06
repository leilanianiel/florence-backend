from authlib.integrations.flask_client import OAuth
from flask_login import LoginManager
import os

oauth = None
login_manager = None


def init(app):
    app.secret_key = 'hey this is a super secret key'

    global login_manager
    login_manager = LoginManager()
    login_manager.init_app(app)

    if "development" in os.environ.get("FLASK_ENV"):
        app.config["GOOGLE_CLIENT_ID"] = app.config['secrets']["GOOGLE_CLIENT_ID"]
        app.config["GOOGLE_CLIENT_SECRET"] = app.config['secrets']["GOOGLE_CLIENT_SECRET"]
    else:
        app.config["GOOGLE_CLIENT_ID"] = os.environ["GOOGLE_CLIENT_ID"]
        app.config["GOOGLE_CLIENT_SECRET"] = os.environ["GOOGLE_CLIENT_SECRET"]

    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'

    global oauth
    oauth = OAuth(app)
    oauth.register(
        name='google',
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
