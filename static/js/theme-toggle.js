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

    // Handle delete notification confirmation
    const deleteLinks = document.querySelectorAll('.delete-notification');

    deleteLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent the default action
            event.stopPropagation();

            const notificationId = this.getAttribute('data-id'); // Get the ID from the data attribute

            // Show the confirmation modal
            const confirmationModal = document.getElementById('confirmationModal');
            confirmationModal.style.display = 'block';

            // Confirm delete event
            document.getElementById('confirmDelete').onclick = function () {
                // Redirect to the delete URL
                window.location.href = `/notifications/delete/${notificationId}/`;
            };

            // Cancel delete event
            document.getElementById('cancelDelete').onclick = function () {
                confirmationModal.style.display = 'none'; // Hide modal
            };
        });
    });

    // This function will hide alert messages after a specified timeout
    setTimeout(function () {
        const messages = document.querySelectorAll('.alert'); // Select all alert messages
        messages.forEach(function (message) {
            message.style.display = 'none'; // Hide each alert message
        });
    }, 5000);
});