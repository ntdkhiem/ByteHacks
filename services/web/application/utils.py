from datetime import datetime
from flask_wtf.form import FlaskForm

from .models import User, Gender


def create_user(form: FlaskForm) -> User:
    '''
    Create a User instance based on given form
    '''
    user = User(
        first_name=form.first_name.data,
        last_name=form.last_name.data,
        # dob=form.dob.data,
        gender=form.gender.data,
        location=form.location.data,
        email=form.email.data,
    )
    user.set_password(form.password.data)
    return user