import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import firebase_admin
from firebase_admin import credentials, initialize_app

from config import Config

db = SQLAlchemy()
login = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)

    db.init_app(app)

    if not firebase_admin._apps:
        cred = credentials.Certificate('bfk.json')
        default_app = initialize_app(cred)

    login.init_app(app)
    login.login_view = 'Home.login'

    # # ensure the instance folder exists
    # try:
    #     os.makedirs(app.instance_path)
    # except OSError:
    #     pass

    with app.app_context():
        from application.home import home as home_bp
        from application.dashboard import dashb as dashboard_bp
        from application.api import api as api_bp
        
        app.register_blueprint(home_bp)
        app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
        app.register_blueprint(api_bp, url_prefix='/api')

        db.create_all()

    return app
