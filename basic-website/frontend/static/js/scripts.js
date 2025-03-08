document.addEventListener('DOMContentLoaded', function() {
    const greetingElement = document.getElementById('greeting');
    
    if (greetingElement) {
        greetingElement.textContent = 'Welcome to the Basic Website!';
    }

    const button = document.getElementById('actionButton');
    if (button) {
        button.addEventListener('click', function() {
            alert('Button clicked!');
        });
    }
});