from flask import Blueprint

dashb = Blueprint('Dashboard', __name__)

from . import routes