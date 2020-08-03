from flask import Flask, jsonify, request
from flask_socketio import SocketIO, send
from firebase_admin import credentials, initialize_app, firestore

from config import Config

# Flask Initialization
app = Flask(__name__)
app.config.from_object(Config)
# Firestore DB Initialization
cred = credentials.Certificate('bfk.json')
default_app = initialize_app(cred)
db = firestore.client()
# Get jobs collection from firestore
jobs_ref = db.collection('jobs')
# SocketIO Initialization
socketio = SocketIO(app)

# Subscribe for changes in firestore database
def on_snapshot(doc_snapshot, changes, read_time):
    '''
    Send socket.io message to all clients
    when a change happens in firestore
    '''
    if len(changes) == 1:
        documentChange = changes[0]
        documentSnapShot = documentChange.document
        payload = {
            'id': documentSnapShot.id,
        }
        # if job is full
        if documentSnapShot.get('total_workers') == documentSnapShot.get('needed_workers'):
            jobs_ref.document(documentSnapShot.id).update({'is_full': True})
            payload['is_full'] = True

        print("[+] CHANGES: ", changes[0].document.to_dict())
        payload['needed_workers'] = documentSnapShot.get('needed_workers')
        socketio.emit('message', {payload}, broadcast=True)

# Socket.io messages
@socketio.on('connect')
def on_connect():
    send({}, broadcast=True) 


@app.route('/jobs', methods=['GET'])
def jobs():
    '''
    Returns a json list of jobs available in Firestore
    '''
    try:
        jobs = {} 
        for doc in jobs_ref.stream():
            if not doc.get('is_full'):
                jobs[doc.id] = doc.to_dict()
        return jsonify(jobs), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@app.route('/job/<string:job_id>', methods=['GET', 'POST'])
def job(job_id):
    '''
    Job controller
        - GET: get a job description from given job's id in Firestore
        - POST: update a job description from given job's id in Firestore
    '''
    if request.method == 'GET':
        # return a single document given an id
        job = jobs_ref.document(job_id).get()
        return jsonify(job.to_dict()), 200
    else:
        # decrement total_workers when user signed up
        try:
            job = jobs_ref.document(job_id)
            needed_workers = job.get().get('needed_workers')
            needed_workers += 1
            job.update({'needed_workers': needed_workers})

            payload = {
                'id':job_id,
            }

            # Reject any more applications when the job is full
            if job.get().get('total_workers') == job.get().get('needed_workers'):
                job.update({'is_full': True})
                payload['is_full'] = True

            # send a live update to every clients
            payload['needed_workers'] = needed_workers
            socketio.send(payload, broadcast=True) 

            # Send an update to notify the client that the registration
            # is completed 
            name = job.get().get('name')
            salary = job.get().get('salary')
            socket.emit('registered', {'name': name, 'salary': salary}, room=request.sid)

        except Exception as e:
            return f"An Error occured: {e}"        
        finally:
            return {}, 200

if __name__ == "__main__":
    # Establish a watcher for Firestore changes
    # jobs_ref.on_snapshot(on_snapshot)
    socketio.start_background_task(jobs_ref.on_snapshot, on_snapshot)

    socketio.run(app, host='0.0.0.0', port=5000)