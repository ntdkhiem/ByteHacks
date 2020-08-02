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


@api.route('/job/<string:job_id>', methods=['GET', 'POST'])
def job(job_id):
    if request.method == 'GET':
        job = jobs_ref.document(job_id).get()
        return jsonify(job.to_dict()), 200
    else:
        # decrement total_workers when user signed up
        try:
            job = jobs_ref.document(job_id)
            total_workers = job.get().get('total_workers')
            job.update({'total_workers': total_workers - 1})
        except Exception as e:
            return f"An Error occured: {e}"        
        finally:
            return {}, 200