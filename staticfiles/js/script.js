document.getElementById('newsForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var newsInput = document.getElementById('newsInput').value;
    fetch('/detectorapi/predict/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text: newsInput }),
    })
    .then(response => response.json())
    .then(data => {
        Swal.fire({
            title: 'Prediction',
            text: data.prediction,
            icon: 'info',
            confirmButtonText: 'OK'
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
