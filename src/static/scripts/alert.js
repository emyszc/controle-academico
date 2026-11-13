const alertList = document.querySelectorAll('.alert.alert-success')
const alerts = [...alertList].map(element => new bootstrap.Alert(element))

for ( const alert of alerts) {
    setTimeout(function() {
        alert.close()
    }, 2000)
}
