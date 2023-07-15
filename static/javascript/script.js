// Select the navbar element
var navbar = document.querySelector('.navbar');

// Add a scroll event listener to the window object
window.addEventListener('scroll', function () {
  // If the user has scrolled down more than 4 pixels
  if (window.scrollY > 40) {
    // Add the 'navbar-white' class to the navbar element
    navbar.classList.add('navbar-white');
  } else {
    // Remove the 'navbar-white' class from the navbar element
    navbar.classList.remove('navbar-white');
  }
});

// Initialize the Typed.js library to create a typing effect
var typed = new Typed('.letter_typed', {
  strings: ['Manish Bhusal', 'Website Developer', 'Backend Developer'],
  typeSpeed: 20,
  backSpeed: 45,
  startDelay: 300,
  loop: true,
});

// Get the element with the class "alert"
var message = document.querySelector('.alert');

// Check if the element exists
if (message) {
  // Display the message by setting its display property to "block"
  message.style.display = 'block';

  // Set a timeout function to hide the message after 5000 milliseconds (5 seconds)
  setTimeout(function() {
    message.style.display = 'none';
  }, 5000);
}
