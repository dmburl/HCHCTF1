document.getElementById('loginForm').addEventListener('submit', function(event) {
    // Prevent the form from submitting in the traditional way (page refresh)
    event.preventDefault();

    // Get the values from the input fields
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Define the correct credentials
    const correctUsername = "admin";
    const correctPassword = "MediCore PM-2024";

    if (username === correctUsername && password === correctPassword) {
        // Set a session storage item to indicate a successful login
        sessionStorage.setItem("loggedIn", "true");
        
        // Redirect the user to the answer page
        window.location.href = "c9answer.html";
    } else {
        alert("Incorrect username or password. Please try again.");
    }
});