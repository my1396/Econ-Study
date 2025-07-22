(function() {
  function showResults(results, store, searchTerm) {
    var searchResults = document.getElementById('search-results');
    var searchInfo = document.getElementById('search-info');

    // Show search info if element exists (on search page)
    if (searchInfo && searchTerm) {
      searchInfo.style.display = 'block';
      searchInfo.innerHTML = 'Showing results for: <strong>' + searchTerm + '</strong> (' + results.length + ' results found)';
    }

    if (results.length) { // If there are results...
      var appendString = '';

      for (var i = 0; i < results.length; i++) {  // Iterate over them and generate html
        var item = store[results[i].ref];
        var excerpt = createSmartExcerpt(item.originalContent || item.content, searchTerm, 200);
        var dateFromUrl = extractDateFromUrl(item.url);
        
        appendString += '<li>';
        appendString += '<div class="result-header">';
        appendString += '<a href="' + item.url + '"><h3>' + item.title + '</h3></a>';
        if (dateFromUrl) {
          appendString += '<span class="result-date">' + dateFromUrl + '</span>';
        }
        appendString += '</div>';
        appendString += '<div class="result-excerpt">' + excerpt + '</div>';
        appendString += '</li>';
      }

      searchResults.innerHTML = appendString;
    } else if (searchTerm) {
      searchResults.innerHTML = '<li class="no-results">No results found for "' + searchTerm + '"</li>';
    } else {
      // No search term provided
      searchResults.innerHTML = '<li class="no-results">Enter a search term to find posts</li>';
      if (searchInfo) {
        searchInfo.style.display = 'none';
      }
    }
  }

    // Create a smart excerpt that shows context around search terms
  function createSmartExcerpt(content, searchTerm, maxLength) {
    if (!searchTerm) {
      return content.substring(0, maxLength) + '...';
    }

    var lowerContent = content.toLowerCase();
    var lowerSearchTerm = searchTerm.toLowerCase();
    
    // Find the first occurrence of the search term
    var index = lowerContent.indexOf(lowerSearchTerm);
    
    if (index === -1) {
      // If exact term not found, just return the beginning
      return content.substring(0, maxLength) + '...';
    }
    
    // Calculate start position to show context before the search term
    var contextBefore = 60;
    var start = Math.max(0, index - contextBefore);
    
    // Find word boundaries to avoid cutting words
    if (start > 0) {
      var spaceIndex = content.indexOf(' ', start);
      if (spaceIndex !== -1 && spaceIndex - start < 20) {
        start = spaceIndex + 1;
      }
    }
    
    // Calculate end position
    var end = Math.min(content.length, start + maxLength);
    var spaceEndIndex = content.lastIndexOf(' ', end);
    if (spaceEndIndex > start + maxLength - 20) {
      end = spaceEndIndex;
    }
    
    var excerpt = content.substring(start, end);
    
    // Add ellipsis if we cut the content
    if (start > 0) excerpt = '...' + excerpt;
    if (end < content.length) excerpt = excerpt + '...';
    
    // Highlight the search term (case insensitive)
    var regex = new RegExp('(' + escapeRegex(searchTerm) + ')', 'gi');
    excerpt = excerpt.replace(regex, '<mark>$1</mark>');
    
    return excerpt;
  }

  // Extract date from URL pattern like /2025/07/21/post-name/
  function extractDateFromUrl(url) {
    var match = url.match(/\/(\d{4})\/(\d{2})\/(\d{2})\//);
    if (match) {
      var year = match[1];
      var month = match[2];
      var day = match[3];
      var date = new Date(year, month - 1, day);
      return date.toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'short', 
        day: 'numeric' 
      });
    }
    return null;
  }

  // Escape special regex characters
  function escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  // Get the search term
  function getQuery(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split('&');

    for (var i = 0; i < vars.length; i++) {
      var pair = vars[i].split('=');

      if (pair[0] === variable) {
        return decodeURIComponent(pair[1].replace(/\+/g, '%20'));
      }
    }
  }

  var searchTerm = getQuery('query');

  // Function to perform search (can be called manually)
  function performSearch(term) {
    var query = term || (document.getElementById('search-box') ? document.getElementById('search-box').value : '');
    if (!query) {
      showResults([], window.store, '');
      return;
    }
    
    // Initialize lunr.js with the fields to search
    var idx = lunr(function () {
      this.field('id');
      this.field('title', { boost: 10 });
      this.field('author');
      this.field('category');
      this.field('content');

      for (var key in window.store) {
        this.add({
          'id': key,
          'title': window.store[key].title,
          'author': window.store[key].author,
          'category': window.store[key].category,
          'content': window.store[key].content
        });
      }
    });

    var results = idx.search(query);
    showResults(results, window.store, query);
  }

  // Make performSearch globally available
  window.performSearch = performSearch;

  // Auto-perform search if there's a URL parameter or show empty state
  if (searchTerm) {
    performSearch(searchTerm);
  } else {
    // Show empty state message
    showResults([], window.store, '');
  }

  // Add event listener for Enter key in search box (if it exists on the page)
  document.addEventListener('DOMContentLoaded', function() {
    var searchBox = document.getElementById('search-box');
    if (searchBox) {
      searchBox.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
          e.preventDefault();
          var searchTerm = searchBox.value.trim();
          if (searchTerm) {
            window.location.href = (window.location.origin + '/search/?query=' + encodeURIComponent(searchTerm)).replace(/\/+/g, '/').replace(/:\//,'://');
          }
        }
      });
    }
    
    // Also handle form submission
    var searchForm = document.querySelector('.header-search-form');
    if (searchForm) {
      searchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        var searchTerm = searchBox.value.trim();
        if (searchTerm) {
          window.location.href = (window.location.origin + '/search/?query=' + encodeURIComponent(searchTerm)).replace(/\/+/g, '/').replace(/:\//,'://');
        }
      });
    }
  });
})();
