from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
# from werkzeug.urls import url_parse

from . import home
from .forms import LoginForm, RegistrationForm
from application import db
from application.models import User
from application.utils import create_user


@home.route('/')
def index():
    return render_template('index.html')


@home.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Dashboard.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email address or password')
            return redirect(url_for('.login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('Dashboard.index')
        return redirect(next_page)
    return render_template('login.html', form=form)


@home.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.index'))


@home.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('Dashboard.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = create_user(form)
        db.session.add(user)
        db.session.commit()
        flash('Created an account successfully')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)