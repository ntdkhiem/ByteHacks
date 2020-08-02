const serverURL = "http://" + document.domain + ":" + location.port;  
socketio = io.connect(serverURL)


socketio.on('connect', () => {
    console.log('Server connected!')

    socket.on('messages', (data) => {
        console.log('received messages', data)
    })
})


document.querySelectorAll('#btnRegister').forEach(btn => {
    btn.addEventListener('click', (e) => {
        fetch(`http://localhost/dashboard/job/${e.target.parentNode.id}`, {
            method: 'post'
        }).then(res => res.status == 200)
        .catch(err => {
            console.error(err)
        })
    })
})