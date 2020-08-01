import requests
from flask import render_template
from flask_login import login_required

from . import dashb

@dashb.route('/')
@login_required
def index():
    jobs = requests.get('http://localhost/api/jobs').json()
    return render_template('dashboard.html', jobs=jobs)

@dashb.route('/job/<string:id>', methods=('GET', 'POST'))
@login_required
def job(id):
    # get more info about a job or take this job 
    job = requests.get(f'http://localhost/api/job/{id}').json()
    return render_template('job.html', job=job)