window.addEventListener('load', function() {
  const footer = document.querySelector('.print-note');
  if (footer) {
    // Try to append to main content area first
    const mainContent = document.querySelector('main') || 
                       document.querySelector('article') || 
                       document.querySelector('.post-content') ||
                       document.querySelector('.markdown-body') ||
                       document.body;
    mainContent.appendChild(footer);
  }
});
