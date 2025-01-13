// This script handles the theme toggle functionality for the website.
// It checks the user's saved theme preference in local storage and 
// applies dark mode if the preference is set. It also updates the 
// webpage based on user interactions with the theme toggle switch, 
// saving the new preference in local storage for future visits.

document.addEventListener('DOMContentLoaded', function () {
    const themeToggle = document.getElementById('theme-toggle');
    const themeLabel = document.getElementById('theme-label');

    // Check for saved user preference in local storage
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-mode');
        themeToggle.checked = true;
        themeLabel.textContent = 'Dark Mode'; // Update label
    }

    // Add event listener for theme toggle
    themeToggle.addEventListener('change', function () {
        if (themeToggle.checked) {
            document.body.classList.add('dark-mode');
            themeLabel.textContent = 'Dark Mode';
            localStorage.setItem('theme', 'dark'); // Save preference
        } else {
            document.body.classList.remove('dark-mode');
            themeLabel.textContent = 'Light Mode';
            localStorage.setItem('theme', 'light'); // Save preference
        }
    });
});