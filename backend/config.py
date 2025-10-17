import os
from dotenv import load_dotenv
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    _raw_db_url = os.environ.get('DATABASE_URL')
    if _raw_db_url:
        url = _raw_db_url.strip()
        if url.startswith('postgres://'):
            url = 'postgresql://' + url[len('postgres://'):]

        # Parse and normalize
        parsed = urlparse(url)
        scheme = parsed.scheme
        netloc = parsed.netloc
        path = parsed.path
        query = parse_qs(parsed.query, keep_blank_values=True)

        # Move host from query into authority if netloc has only creds
        host_from_query = (query.get('host') or [None])[0]
        if host_from_query and (netloc.endswith('@') or netloc == ''):
            # Extract creds if present
            creds = netloc[:-1] if netloc.endswith('@') else ''
            netloc = (creds + '@' if creds else '') + host_from_query
            # Remove host from query
            query.pop('host', None)

        # Remove channel_binding if present (Neon sometimes adds it)
        query.pop('channel_binding', None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configure PostgreSQL-specific settings if using PostgreSQL
    if SQLALCHEMY_DATABASE_URI.startswith('postgresql+psycopg2://'):
        SQLALCHEMY_ENGINE_OPTIONS = {
            'pool_pre_ping': True,
            'pool_recycle': 300,
            'pool_size': 5,
            'max_overflow': 10,
            'connect_args': {
                'connect_timeout': 5,
                'sslmode': 'disable'  # Disable SSL for now
            }
        }
    
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-change-me')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600))
    CLOUDINARY_CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME')
    CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY')
    CLOUDINARY_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET')
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
    FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:3000')
