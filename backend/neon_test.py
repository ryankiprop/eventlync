import os
from sqlalchemy import create_engine, text
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_neon_connection():
    db_url = 'postgresql+psycopg2://neondb_owner:npg_oVhL5pN9BblI@ep-withered-resonance-adm7679h-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require'
    try:
        engine = create_engine(db_url)
        with engine.connect() as conn:
            logger.info("Connection successful!")
            version = conn.execute(text('SELECT version()')).scalar()
            logger.info(f"PostgreSQL version: {version}")
            tables = conn.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")).fetchall()
            logger.info(f"Found {len(tables)} tables")
            return True
    except Exception as e:
        logger.error(f"Connection failed: {e}")
        return False

if __name__ == "__main__":
    test_neon_connection()
