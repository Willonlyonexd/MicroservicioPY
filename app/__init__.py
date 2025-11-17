from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Registrar blueprints
    from app.routes.inventory_routes import inventory_bp
    app.register_blueprint(inventory_bp, url_prefix="/items")

    return app
