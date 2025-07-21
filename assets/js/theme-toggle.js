(function() {
  'use strict';

  // Get current theme preference
  function getCurrentTheme() {
    const stored = localStorage.getItem('theme-preference');
    if (stored) {
      return stored;
    }
    
    // Default to system preference
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  // Apply theme by manipulating CSS media queries
  function applyTheme(theme) {
    const root = document.documentElement;
    
    // Remove any existing forced theme styles
    const existingStyle = document.getElementById('force-theme-mode');
    if (existingStyle) {
      existingStyle.remove();
    }
    
    if (theme === 'dark') {
      // Force dark mode by adding a style that overrides the media query
      const darkStyle = document.createElement('style');
      darkStyle.id = 'force-theme-mode';
      darkStyle.textContent = `
        @media screen {
          :root {
            --minima-brand-color: #999999 !important;
            --minima-brand-color-light: #a3a3a3 !important;
            --minima-brand-color-dark: #5c5c5c !important;
            --minima-site-title-color: #a3a3a3 !important;
            --minima-text-color: #bbbbbb !important;
            --minima-background-color: #181818 !important;
            --minima-code-background-color: #212121 !important;
            --minima-link-base-color: #79b8ff !important;
            --minima-link-visited-color: #79b8ff !important;
            --minima-link-hover-color: #bbbbbb !important;
            --minima-border-color-01: #5c5c5c !important;
            --minima-border-color-02: #a3a3a3 !important;
            --minima-border-color-03: #999999 !important;
            --minima-table-text-color: #bbbbbb !important;
            --minima-table-zebra-color: #1d1d1d !important;
            --minima-table-header-bg-color: #282828 !important;
            --minima-table-header-border: #393939 !important;
            --minima-table-border-color: #5c5c5c !important;
          }
        }
      `;
      document.head.appendChild(darkStyle);
      root.setAttribute('data-theme', 'dark');
    } else {
      // Force light mode by overriding with light theme colors
      const lightStyle = document.createElement('style');
      lightStyle.id = 'force-theme-mode';
      lightStyle.textContent = `
        @media screen {
          :root {
            --minima-brand-color: #828282 !important;
            --minima-brand-color-light: #e8e8e8 !important;
            --minima-brand-color-dark: #424242 !important;
            --minima-site-title-color: #424242 !important;
            --minima-text-color: #111111 !important;
            --minima-background-color: #fdfdfd !important;
            --minima-code-background-color: #eeeeff !important;
            --minima-link-base-color: #2a7ae2 !important;
            --minima-link-visited-color: #1756a9 !important;
            --minima-link-hover-color: #111111 !important;
            --minima-border-color-01: #e8e8e8 !important;
            --minima-border-color-02: #e0e0e0 !important;
            --minima-border-color-03: #424242 !important;
            --minima-table-text-color: #383838 !important;
            --minima-table-zebra-color: #f7f7f7 !important;
            --minima-table-header-bg-color: #f0f0f0 !important;
            --minima-table-header-border: #dedede !important;
            --minima-table-border-color: #e8e8e8 !important;
          }
        }
      `;
      document.head.appendChild(lightStyle);
      root.setAttribute('data-theme', 'light');
    }
  }

  // Update toggle button appearance
  function updateToggleButton(theme) {
    const toggleButton = document.querySelector('.theme-toggle');
    if (toggleButton) {
      toggleButton.setAttribute('data-theme', theme);
      toggleButton.setAttribute('aria-label', 
        theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'
      );
    }
  }

  // Toggle theme
  function toggleTheme() {
    const currentTheme = getCurrentTheme();
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    localStorage.setItem('theme-preference', newTheme);
    applyTheme(newTheme);
    updateToggleButton(newTheme);
  }

  // Initialize theme on page load
  function initializeTheme() {
    const theme = getCurrentTheme();
    applyTheme(theme);
    updateToggleButton(theme);
    
    // Add click handler to toggle button
    const toggleButton = document.querySelector('.theme-toggle');
    if (toggleButton) {
      toggleButton.addEventListener('click', toggleTheme);
    }
  }

  // Listen for system theme changes
  function listenForSystemThemeChanges() {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    mediaQuery.addListener(function(e) {
      // Only update if user hasn't set a manual preference
      if (!localStorage.getItem('theme-preference')) {
        const theme = e.matches ? 'dark' : 'light';
        applyTheme(theme);
        updateToggleButton(theme);
      }
    });
  }

  // Run when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      initializeTheme();
      listenForSystemThemeChanges();
    });
  } else {
    initializeTheme();
    listenForSystemThemeChanges();
  }
})();
