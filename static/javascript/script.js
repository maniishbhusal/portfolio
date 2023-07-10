// Select the navbar element
var navbar = document.querySelector('.navbar');

// Add a scroll event listener to the window object
window.addEventListener('scroll', function() {
  // If the user has scrolled down more than 4 pixels
  if (window.scrollY > 40) {
    // Add the 'navbar-white' class to the navbar element
    navbar.classList.add('navbar-white');
  } else {
    // Remove the 'navbar-white' class from the navbar element
    navbar.classList.remove('navbar-white');
  }
});