import enum
from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import ARRAY
from werkzeug.security import generate_password_hash, check_password_hash

from application import db, login


class Gender(enum.Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3 


class User(UserMixin, db.Model):
    '''
    User Model
        - Might only works for PostgreSQL
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15), index=True, nullable=False)
    last_name = db.Column(db.String(15), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    dob = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    gender = db.Column(db.Enum(Gender), nullable=False)
    location = db.Column(db.String())
    jobs = db.Column(ARRAY(db.String))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User(name={self.first_name} {self.last_name},' \
               f'email={self.email},' \
               f'dob={self.dob},' \
               f'gender={self.gender},' \
               f'location={self.location})'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))