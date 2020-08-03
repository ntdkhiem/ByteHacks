from flask_wtf import FlaskForm
from wtforms import (
    StringField, 
    PasswordField, 
    BooleanField, 
    RadioField,
    SelectField,
    SubmitField,
)
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, Email, EqualTo, Required

from application.models import User, Gender


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[Required()])
    last_name = StringField('Last Name', validators=[Required()])
    # dob = DateField('Date Of Birth')])
    dob = DateField('Date Of Birth', validators=[Required()], format='%Y-%m-%d')

    gender = SelectField('Gender',
                        choices=[
                            ('MALE', 'Male'),
                            ('FEMALE', 'Female'),
                            ('OTHER', 'Other'),
                        ],
                        validators=[Required()])
    location = SelectField('Location',
                            choices=[
                               ('ma', 'Massachusetts'), 
                               ('ca', 'California'),
                               ('ny', 'New York'),
                            ],
                            validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    password2 = PasswordField(
        'Repeat Password', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('A user with this email already existed')