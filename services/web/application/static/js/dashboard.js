const serverURL = "http://" + document.domain + ":" + location.port;  
socketio = io.connect(serverURL)


socketio.on('connect', () => {
    console.log('Server connected!')

    socketio.on('registered', (data) => {
        console.log('Received registered message', data)
        myJobs = document.querySelector('#myJobs')
        // initialization
        card = document.createElement('div')
        card.classList.add('card mb-1')
        cardHeader = document.createElement('div')
        cardHeader.classList.add('card-header')
        cardFlex = document.createElement('div')
        cardFlex.classList.add('d-flex justify-content-between')
        span1 = document.createElement('span')
        p1 = document.createElement('p')
        p1.classList.add('h4 font-bold text-capitalize')
        p1.text = data.name
        span2 = document.createElement('span')
        p2.classList.add('h3')
        p2.text = data.salary

        // wire it up
        span1.appendChild(p1)
        span2.appendChild(p2)
        cardFlex.appendChild(span1)
        cardFlex.appendChild(span2)
        cardHeader.appendChild(cardFlex)
        card.appendChild(cardHeader)
        myJobs.appendChild(card)
    })

    socketio.on('message', (data) => {
        console.log('received messages', data)
        if (Object.keys(data).length !== 0) {
            if (data.hasOwnProperty('is_full')) {
                document.querySelector('#' + data.id).remove()
            }
            else {
                el = document.querySelector('#' + data.id)
                if (el) {
                    el.querySelector('.nw').textContent = data.needed_workers   
                }
            }
        }
    })
})


document.querySelectorAll('#btnRegister').forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.target.disabled = true
        // e.target.(.d-flex).(.card-body).(.card).id
        cardID = e.target.parentNode.parentNode.parentNode.id
        fetch(`http://localhost/dashboard/job/${cardID}`, {
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