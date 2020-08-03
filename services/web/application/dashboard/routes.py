import requests
from requests import Response
from flask import render_template, request, abort
from flask_login import login_required, current_user

from application import db
from application.models import User
from . import dashb

@dashb.route('/')
@login_required
def index():
    '''
    Dashboard main page 
        - serves a list of available jobs
        - serves a list of jobs of current user
    '''
    jobs: Response = requests.get('http://api:5000/jobs').json()

    # get my job ids from postgresql then get those jobs from firestore
    my_jobs = []
    my_job_ids: list = current_user.jobs
    for jid in my_job_ids:
        job = requests.get(f'http://api:5000/job/{id}').json()
        if job:
            my_jobs.append(job)

    return render_template('dashboard.html', my_jobs=my_jobs, jobs=jobs)

@dashb.route('/job/<string:id>', methods=['GET', 'POST'])
@login_required
def job(id):
    '''
    Job's Description endpoint
        - GET: get a description given job's id
        - POST: add job's id to current user's job list and call firestore about the registration
    '''
    # get more info about a job or take this job 
    if request.method == 'GET':
        job = requests.get(f'http://api:5000/job/{id}').json()
        return render_template('job.html', job=job)
    else:
        # user want to sign up
        # post a request to api endpoints about this action
        response = requests.post(f'http://api:5000/job/{id}')
        if response.status_code == 200:
            # add doc's id to user model
            jobs = current_user.jobs.copy()
            jobs.append(id)
            current_user.jobs = jobs 
            db.session.commit()
            return {}, 200
        abort(500)