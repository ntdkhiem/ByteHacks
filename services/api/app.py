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
    Send socket.io message when a change happens in firestore
    '''
    for doc in doc_snapshot:
        print(doc)
        send('New changes in firestore', broadcast=True)

# Socket.io messages
@socketio.on('connect')
def on_connect():
    print('[+] Received new connection')
    send({'status': 'ok'}, broadcast=True) 


@app.route('/jobs', methods=['GET'])
def jobs():
    '''
    Returns a json list of jobs available in Firestore
    '''
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
            total_workers = job.get().get('total_workers')
            job.update({'total_workers': total_workers - 1})
        except Exception as e:
            return f"An Error occured: {e}"        
        finally:
            return {}, 200

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)