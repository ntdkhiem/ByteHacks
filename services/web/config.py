import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    '''
    Configuration options retrieve from environment variables
    '''
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'super-secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError('Missing Database URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False