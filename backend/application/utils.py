from datetime import datetime

from .models import User, Gender


def create_user(form):
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

# def create_sample_user():
#     user = User(
#         first_name='Kevin',
#         last_name='Nguyen',
#         dob=datetime.now(),
#         gender=Gender.MALE,
#         location='ma',
#         email='ppkhiemnguyen@gmail.com'
#     )
#     user.set_password('12345')
#     return user