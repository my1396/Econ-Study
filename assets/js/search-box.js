// Search box functionality for header
document.addEventListener('DOMContentLoaded', function() {
  var searchBox = document.getElementById('search-box');
  var searchForm = document.querySelector('.header-search-form');
  
  if (searchBox) {
    searchBox.addEventListener('keypress', function(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        submitSearch();
      }
    });
  }
  
  if (searchForm) {
    searchForm.addEventListener('submit', function(e) {
      e.preventDefault();
      submitSearch();
    });
  }
  
  function submitSearch() {
    var searchTerm = searchBox.value.trim();
    if (searchTerm) {
      var baseUrl = window.location.origin;
      var sitePath = window.location.pathname.includes('/Econ-Study') ? '/Econ-Study' : '';
      window.location.href = baseUrl + sitePath + '/search/?query=' + encodeURIComponent(searchTerm);
    }
  }
});
