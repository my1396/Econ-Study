// Set a variable (handle) for our button element.
const scrollToTopButton = document.getElementById('js-top');

// shows the scroll-to-top button if the user scrolls beyond the height of the initial window.
const scrollFunc = () => {
    // Get the current scroll value
    let y = window.scrollY;
    
    // shows the scroll-to-top button if the user scrolls beyond the height of the initial window
    if (y > 0) {
      scrollToTopButton.className = "top-link show";
    } else {
      scrollToTopButton.className = "top-link hide";
    }

  };
window.addEventListener("scroll", scrollFunc);

function scrollToTop() {
    // Let's set a variable for the number of pixels we are from the top of the document.
  const c = document.documentElement.scrollTop || document.body.scrollTop;
  
  // If that number is greater than 0, we'll scroll back to 0, or the top of the document.
  // We'll also animate that scroll with requestAnimationFrame:
  // https://developer.mozilla.org/en-US/docs/Web/API/window/requestAnimationFrame
  if (c > 0) {
    window.requestAnimationFrame(scrollToTop);
    // ScrollTo takes an x and a y coordinate.
    // Increase the '10' value to get a smoother/slower scroll!
    window.scrollTo(0, c - c / 10);
  }
};

// When the button is clicked, run our ScrolltoTop function above!
scrollToTop.onclick = function(e) {
    e.preventDefault();
    scrollToTop();
};


function displayResult() {
  document.getElementById("myHeader").innerHTML = "Have a nice day!";
}
