from flask import jsonify, request

from . import api, jobs_ref


@api.route('/jobs', methods=['GET'])
def jobs():
    # return a list of jobs available via Firestore
    try:
        jobs = []
        for doc in jobs_ref.stream():
            job = {}
            job['id'] = doc.id 
            job.update(doc.to_dict())
            jobs.append(job)
        return jsonify(jobs), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@api.route('/job/<int:id>', methods=['GET', 'POST'])
def job(id):
    if request.method == 'GET':
        todo = jobs_ref.document(todo_id).get()
        return jsonify(todo.to_dict()), 200
    else:
        # user signed up for this job
        pass