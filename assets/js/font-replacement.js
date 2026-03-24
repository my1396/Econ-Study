// Replace Chinese font names in inline styles with web font equivalents
(function() {
  function replaceFonts() {
    // Font mapping: system font -> local font in assets/fonts/ folder
    const fontMap = {
      'STKaiti': 'WebKaiti',
      'Xingkai': 'WebXingkai',
      'Kaiti SC': 'WebKaiti',
      'Hannotate': 'WebHannotate',
    };

    // Sort by key length (descending) to match longer names first
    const sortedFonts = Object.entries(fontMap).sort((a, b) => b[0].length - a[0].length);

    // Find all elements with inline styles
    const elementsWithStyle = document.querySelectorAll('[style*="font-family"]');
    
    elementsWithStyle.forEach(element => {
      const styleAttr = element.getAttribute('style');
      if (!styleAttr) return;
      
      let newStyle = styleAttr;
      let modified = false;
      
      // Replace each font in the map (longest first to avoid partial matches)
      for (const [oldFont, newFont] of sortedFonts) {
        // Escape special regex characters in font name
        const escapedFont = oldFont.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        
        // Match font with quotes or as a complete word with boundaries
        // This prevents matching "Xingkai" inside "WebXingkai"
        const regex = new RegExp(
          `(['"])${escapedFont}\\1|\\b${escapedFont}\\b`,
          'g'
        );
        
        // Check if this font appears in the style
        if (regex.test(styleAttr)) {
          // Reset regex for replace operation
          regex.lastIndex = 0;
          newStyle = newStyle.replace(regex, `'${newFont}'`);
          modified = true;
        }
      }
      
      // Update the style attribute if we made changes
      if (modified) {
        console.log('Font replacement:', styleAttr, '->', newStyle);
        // Set cssText directly to force browser to re-parse and apply
        element.style.cssText = newStyle;
      }
    });
  }
  
  // Run on DOM ready and after fonts load
  function init() {
    replaceFonts();
    
    // Re-run after fonts are loaded to handle timing issues
    if (document.fonts && document.fonts.ready) {
      document.fonts.ready.then(() => {
        console.log('Fonts loaded, re-applying replacements');
        replaceFonts();
      });
    }
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
