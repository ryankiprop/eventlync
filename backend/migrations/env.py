from logging.config import fileConfig  # imported but not used; our ini has no logging sections
import os
import sys

from alembic import context
from sqlalchemy import engine_from_config, pool

# Alembic config
config = context.config
# Do NOT call fileConfig(config.config_file_name) since our alembic.ini has no logging sections

# Make the app importable (so "from app import create_app" works)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# Import Flask app and metadata
from app import create_app
from app.extensions import db

app = create_app()
with app.app_context():
    # Point Alembic at the same DB URL the app uses
    config.set_main_option('sqlalchemy.url', app.config['SQLALCHEMY_DATABASE_URI'])
    target_metadata = db.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()