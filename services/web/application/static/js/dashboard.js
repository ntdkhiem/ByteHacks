const serverURL = "http://" + document.domain + ":" + location.port;  
socketio = io.connect(serverURL)


socketio.on('connect', () => {
    console.log('Server connected!')

    socketio.on('message', (data) => {
        console.log('received messages', data)
        if (data) {
            if (data.is_full) {
                document.querySelector('#' + data.id).remove()
            }
            else {
                document.querySelector('#' + data.id)
                        .querySelector('.workers').textContent = data.total_workers   
            }
        }
    })
})


document.querySelectorAll('#btnRegister').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.target.disabled = true
        fetch(`http://localhost/dashboard/job/${e.target.parentNode.id}`, {
            method: 'post'
        }).then(res => res.json())
        .then(data => {
            console.log(data)
            console.log('Signed UP')
        })
        .catch(err => {
            console.error(err)
        })
    })
})