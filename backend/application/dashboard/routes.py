import requests
from flask import render_template, request, abort
from flask_login import login_required, current_user

from application import db
from application.models import User
from . import dashb

@dashb.route('/')
@login_required
def index():
    jobs = requests.get('http://localhost/api/jobs').json()
    return render_template('dashboard.html', jobs=jobs)

@dashb.route('/job/<string:id>', methods=['GET', 'POST'])
@login_required
def job(id):
    # get more info about a job or take this job 
    if request.method == 'GET':
        job = requests.get(f'http://localhost/api/job/{id}').json()
        return render_template('job.html', job=job)
    else:
        # user want to sign up
        # post a request to api endpoints about this action
        response = requests.post(f'http://localhost/api/job/{id}')
        if response.status_code == 200:
            # add doc's id to user model
            jobs = current_user.jobs.copy()
            jobs.append(id)
            current_user.jobs = jobs 
            db.session.commit()
            return {}, 200
        abort(500)