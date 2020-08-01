from flask import Blueprint
from firebase_admin import firestore

api = Blueprint('Api', __name__)
fdb = firestore.client()
jobs_ref = fdb.collection('jobs')

from . import routes