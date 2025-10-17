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

        # Ensure psycopg3 dialect
        if scheme == 'postgresql':
            scheme = 'postgresql+psycopg'

        # Enforce SSL for Postgres if not explicitly set
        if scheme.startswith('postgresql'):
            if 'sslmode' not in query:
                query['sslmode'] = ['require']

        # Rebuild URL
        url = urlunparse((
            scheme,
            netloc,
            path,
            '',
            urlencode(query, doseq=True),
            ''
        ))
        SQLALCHEMY_DATABASE_URI = url
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/eventlync.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key'
    CLOUDINARY_CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME')
    CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY')
    CLOUDINARY_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET')
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
    FRONTEND_URL = os.environ.get('FRONTEND_URL', 'http://localhost:3000')
