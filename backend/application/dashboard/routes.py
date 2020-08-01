from flask import render_template
from flask_login import login_required

from . import dashb

@dashb.route('/')
@login_required
def index():
    return render_template('dashboard.html')