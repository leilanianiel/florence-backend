from authlib.integrations.flask_client import OAuth

oauth = None

def init(app):
    app.secret_key = '!secret'
    app.config["GOOGLE_CLIENT_ID"] = app.config['secrets']["GOOGLE_CLIENT_ID"]
    app.config["GOOGLE_CLIENT_SECRET"] = app.config['secrets']["GOOGLE_CLIENT_SECRET"]

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
