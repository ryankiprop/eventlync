from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from .extensions import db, migrate, jwt
from .routes import register_routes
from config import Config
from .cli import register_cli


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Extensions
    CORS(app, supports_credentials=True, origins=[app.config.get('FRONTEND_URL', '*')])
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Blueprints/Routes
    register_routes(app)

    # CLI commands
    register_cli(app)

    @app.get('/api/health')
    def health():
        return {"status": "ok"}, 200

    @app.get('/health')
    def health_alias():
        return {"status": "ok"}, 200

    return app
