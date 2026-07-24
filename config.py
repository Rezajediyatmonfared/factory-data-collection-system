import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-very-secure-secret-key'
    DB_NAME = os.environ.get('DB_NAME') or 'factory_management_new.db'
