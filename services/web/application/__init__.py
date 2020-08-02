import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

db = SQLAlchemy()
login = LoginManager()

def create_app() -> Flask:
    '''
    Application factory for STJK app
        - / : Main Page
        - /dashboard : Dashboard page (required login)
    '''
    app: Flask = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    login.init_app(app)
    login.login_view = 'Home.login'

    with app.app_context():
        from application.home import home as home_bp
        from application.dashboard import dashb as dashboard_bp
        
        app.register_blueprint(home_bp)
        app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

        db.create_all()

    return app
