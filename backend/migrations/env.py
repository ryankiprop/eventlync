from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool
from flask import current_app

# Alembic Config object
config = context.config

# Use Flask's app config for DB URL and metadata
if current_app:
    config.set_main_option("sqlalchemy.url", str(current_app.config["SQLALCHEMY_DATABASE_URI"]))
    # Prefer metadata from Flask-Migrate extension if available
    mig = current_app.extensions.get("migrate") if hasattr(current_app, "extensions") else None
    target_metadata = getattr(mig.db, "metadata", None) if mig else None
else:
    target_metadata = None


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
    )
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