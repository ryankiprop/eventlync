import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    _raw_db_url = os.environ.get('DATABASE_URL')
    if _raw_db_url:
        url = _raw_db_url
        if url.startswith('postgres://'):
            url = 'postgresql://' + url[len('postgres://'):]
        if url.startswith('postgresql://'):
            url = 'postgresql+psycopg://' + url[len('postgresql://'):]
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
