from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config = None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if not test_config:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
        # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("RENDER_DATABASE_URI")
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")


    # Import models here for Alembic setup
    from app.models.pantry import Pantry
    from app.models.recipe import Recipe
    from app.models.user import User

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .routes import users_bp
    # from .routes import pantry_bp
    from .routes import recipes_bp
    app.register_blueprint(users_bp)
    # app.register_blueprint(pantry_bp)
    app.register_blueprint(recipes_bp)


    CORS(app)
    return app
