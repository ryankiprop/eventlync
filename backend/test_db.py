from sqlalchemy import text
from app import create_app, db
import sys

def print_success(message):
    print(f"[SUCCESS] {message}")

def print_error(message):
    print(f"[ERROR] {message}", file=sys.stderr)

def test_database_connection():
    app = create_app()
    
    with app.app_context():
        try:
            # Test database connection with proper SQLAlchemy text()
            db.session.execute(text('SELECT 1'))
            db.session.commit()
            print_success("Database connection successful!")
            
            # Print database URL (with password hidden for security)
            db_url = app.config['SQLALCHEMY_DATABASE_URI']
            if 'postgresql' in db_url:
                # Hide password in the output
                import re
                safe_url = re.sub(r':([^:]+)@', ':********@', db_url)
                print(f"Database URL: {safe_url}")
            else:
                print(f"Database URL: {db_url}")
                
            # Check if tables are created
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"Found {len(tables)} tables in the database")
            if tables:
                print(f"Tables: {', '.join(tables)}")
            
            # Check database version
            if 'postgresql' in db_url:
                result = db.session.execute(text('SELECT version()')).scalar()
                print(f"Database version: {result}")
                
            return True
                
        except Exception as e:
            print_error(f"Database connection failed: {str(e)}")
            print("\nTroubleshooting steps:", file=sys.stderr)
            print("1. Check if the database server is running", file=sys.stderr)
            print("2. Verify the DATABASE_URL in your environment variables", file=sys.stderr)
            print("3. Ensure all database dependencies are installed", file=sys.stderr)
            print("4. Check the database credentials and permissions", file=sys.stderr)
            
            if 'postgresql' in str(e):
                print("\nPostgreSQL-specific checks:", file=sys.stderr)
                print("- Make sure PostgreSQL is running", file=sys.stderr)
                print("- Check if the database exists and is accessible", file=sys.stderr)
                print("- Verify the username and password in the connection string", file=sys.stderr)
                print("- Check if the server is configured to accept connections", file=sys.stderr)
            
            return False

if __name__ == "__main__":
    if test_database_connection():
        sys.exit(0)
    else:
        sys.exit(1)