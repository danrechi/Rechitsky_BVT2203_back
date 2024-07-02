from flask import Flask
from config import Config
from app.models import db
from app.routes import api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.register_blueprint(api, url_prefix='/api')

    return app
