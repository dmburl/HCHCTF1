document.getElementById('loginForm').addEventListener('submit', function(event) {
    // Prevent the form from submitting in the traditional way (page refresh)
    event.preventDefault();

    // Get the values from the input fields
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Define the correct credentials
    const correctUsername = "CTF_user";
    const correctPassword = "CTF_password123";

    // Get the answer paragraph element
    const answer = document.getElementById('answer');

    // Check if the entered credentials are correct
    if (username === correctUsername && password === correctPassword) {
        // If correct, show the answer
        answer.style.display = "block";
    } else {
        // If incorrect, hide the answer and optionally provide an alert
        answer.style.display = "none";
        alert("Incorrect username or password. Please try again.");
    }
});