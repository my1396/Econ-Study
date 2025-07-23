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

// TOC Active Section Highlighting
function updateActiveTOCSection() {
    const toc = document.querySelector('.toc');
    if (!toc) return;
    
    const tocLinks = toc.querySelectorAll('a');
    const headings = document.querySelectorAll('h2, h3, h4, h5, h6');
    
    if (tocLinks.length === 0 || headings.length === 0) return;
    
    let activeHeading = null;
    const scrollPosition = window.scrollY + 100; // Offset for better detection
    
    // Find the current heading
    for (let i = headings.length - 1; i >= 0; i--) {
        const heading = headings[i];
        if (heading.offsetTop <= scrollPosition) {
            activeHeading = heading;
            break;
        }
    }
    
    // Clear all active classes
    tocLinks.forEach(link => {
        link.classList.remove('active');
        link.parentElement.classList.remove('active');
    });
    
    if (activeHeading) {
        const activeId = activeHeading.id;
        const activeLink = toc.querySelector(`a[href="#${activeId}"]`);
        
        if (activeLink) {
            // Mark current section as active
            activeLink.classList.add('active');
            activeLink.parentElement.classList.add('active');
        }
    }
}

// Update TOC on scroll
window.addEventListener('scroll', updateActiveTOCSection);
// Update TOC on page load
window.addEventListener('load', updateActiveTOCSection);

function displayResult() {
  document.getElementById("myHeader").innerHTML = "Have a nice day!";
}
