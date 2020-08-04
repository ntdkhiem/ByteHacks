# Helploy 

The Great Depression job search website 

## Software Stack
<img src="images/bootstrap.png" width="150">
<img src="images/web-lang.png" width="230">
<img src="images/flask.png" width="200">
<img src="images/socketio.jpg" width="200">
<img src="images/firebase.png" width="200">
<img src="images/postgresql.png" width="200">
<img src="images/docker.png" width="200">


### Notes
- You need to have [Docker](https://docker.com/get-started) installed
- You need to create a [Firebase](https://firebase.google.com/) project and get its [service account key](https://console.firebase.google.com/u/0/project/_/settings/serviceaccounts)

### How to run
1. Rename your firebase service account key to `bfk.json`

2. Place `bfk.json` in `./backend/api`

3. Make sure you have `.env` in the repository's root folder

4. Execute: `docker-compose up`

*NOTE: First time installing will be very slow but it will run much faster subsequently*