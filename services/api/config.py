
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    '''
    Configuration options retrieve from environment variables
    '''
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY') or 'super-secret'