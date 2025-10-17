import logging
import os
import sys
from sqlalchemy import text, create_engine
from sqlalchemy.exc import SQLAlchemyError

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def test_database_connection():
    try:
        # Get database URL from environment or use default SQLite
        db_url = os.environ.get('DATABASE_URL', 'sqlite:///eventlync.db')
        logger.info(f"Attempting to connect to database: {db_url}")
        
        # Create engine
        engine = create_engine(db_url)
        
        # Test connection
        with engine.connect() as conn:
            logger.info("Connection established successfully")
            
            # Get database version
            if 'sqlite' in db_url:
                version = conn.execute(text('SELECT sqlite_version()')).scalar()
                logger.info(f"SQLite version: {version}")
            else:
                version = conn.execute(text('SELECT version()')).scalar()
                logger.info(f"Database version: {version}")
            
            # List tables
            inspector = inspect(engine)
            tables = inspector.get_table_names()
            logger.info(f"Found {len(tables)} tables: {', '.join(tables) if tables else 'None'}")
            
            return True
            
    except Exception as e:
        logger.error(f"Database connection failed: {str(e)}", exc_info=True)
        return False

if __name__ == "__main__":
    from sqlalchemy import inspect
    
    logger.info("Starting database connection test...")
    if test_database_connection():
        logger.info("✅ Database connection test completed successfully")
        sys.exit(0)
    else:
        logger.error("❌ Database connection test failed")
        print("\nTroubleshooting steps:")
        print("1. Check if the database server is running")
        print("2. Verify the DATABASE_URL in your environment variables")
        print("3. Ensure all database dependencies are installed")
        print("4. Check the database credentials and permissions")
        if 'postgresql' in os.environ.get('DATABASE_URL', ''):
            print("\nFor PostgreSQL:")
            print("- Make sure PostgreSQL is running")
            print("- Check if the database exists and is accessible")
            print("- Verify the username and password in the connection string")
            print("- Check if the server is configured to accept connections")
        sys.exit(1)
