import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from .extensions import db, migrate, jwt
from .routes import register_routes
from config import Config
from .cli import register_cli
from flask_migrate import upgrade
from sqlalchemy import inspect
from .models.payment import Payment


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Extensions
    CORS(app, supports_credentials=True, origins=[app.config.get('FRONTEND_URL', '*')])
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    if (os.environ.get('RUN_MIGRATIONS_ON_START') or '').lower() in ('1', 'true', 'yes'):
        try:
            with app.app_context():
                upgrade()
        except Exception:
            app.logger.exception("alembic upgrade failed")

    try:
        with app.app_context():
            insp = inspect(db.engine)
            if 'payments' not in insp.get_table_names():
                Payment.__table__.create(bind=db.engine)
    except Exception:
        app.logger.exception("ensure payments table failed")

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

    @app.get('/')
    def root():
        return {"service": "eventlync-api", "status": "ok"}, 200

    return app
