# STJK - ByteHacks 2020

## Software Stack
- Flask
- PostgreSQL
- Firebase Firestore
- SocketIO
- Docker
- Kubernetes

### Notes
- You need to have [Docker](https://docker.com/gettingstarted) installed
- You need to create a [Firebase](https://firebase.google.com/) project and get its [service account key](https://console.firebase.google.com/u/0/project/_/settings/serviceaccounts)

### How to run
1. Rename your firebase service account key to `bfk.json`

2. Place `bfk.json` in `./backend/api`

3. Make sure you have `.env` in the repository's root folder

4. Execute: `docker-compose up`
