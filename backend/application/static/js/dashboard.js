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