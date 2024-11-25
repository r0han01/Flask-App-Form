document.addEventListener('DOMContentLoaded', function() {
    // For example, show an alert when the form is submitted
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const name = document.getElementById('name').value;
        if (!name) {
            alert('Please enter your name!');
            event.preventDefault();  // Prevent form submission
        }
    });
});
