---
layout: page
title: Search Results
permalink: /search/
---

<style>
#search-results {
  list-style: none;
  padding: 0;
  margin: 0;
}

#search-results li {
  margin-bottom: 25px;
  padding: 20px;
  border: 1px solid #e1e5e9;
  border-radius: 8px;
  background-color: #ffffff;
  box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  transition: box-shadow 0.2s ease;
}

#search-results li:hover {
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.result-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 12px;
}

.result-header h3 {
  margin: 0;
  font-size: 1.3em;
  line-height: 1.3;
  flex: 1;
}

.result-header h3 a {
  text-decoration: none;
  color: #2c5aa0;
  font-weight: 600;
}

.result-header h3 a:hover {
  text-decoration: underline;
  color: #1a4480;
}

.result-date {
  color: #6c757d;
  font-size: 0.9em;
  font-weight: normal;
  margin-left: 15px;
  white-space: nowrap;
}

.result-excerpt {
  color: #495057;
  line-height: 1.6;
  font-size: 0.95em;
}

.result-excerpt mark {
  background-color: #fff3cd;
  padding: 2px 4px;
  border-radius: 3px;
  font-weight: 600;
  color: #856404;
}

.search-info {
  margin-bottom: 20px;
  padding: 15px 20px;
  background-color: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 6px;
  font-size: 0.95em;
  color: #495057;
}

.no-results {
  text-align: center;
  padding: 60px 20px;
  color: #6c757d;
  font-style: italic;
  font-size: 1.1em;
  background-color: #f8f9fa;
  border-radius: 8px;
  border: 1px solid #dee2e6;
}

/* Responsive design */
@media (max-width: 768px) {
  .result-header {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .result-date {
    margin-left: 0;
    margin-top: 5px;
    font-size: 0.85em;
  }
  
  #search-results li {
    padding: 15px;
  }
}
</style>

<!-- Search info will be populated by JavaScript -->
<div id="search-info" class="search-info" style="display: none;"></div>

<!-- List where search results will be rendered -->
<ul id="search-results"></ul>

<!-- Include Lunr.js library -->
<script src="{{site.baseurl}}/assets/js/lunr.js"></script>

<script>
  // Template to generate the JSON to search
  window.store = {
    {% for post in site.posts %}
      "{{ post.url | slugify }}": {
        "title": "{{ post.title | xml_escape }}",
        "author": "{{ post.author | xml_escape }}",
        "category": "{{ post.category | xml_escape }}",
        "content": {{ post.content | strip_html | strip_newlines | jsonify }},
        "url": "{{ site.baseurl }}{{ post.url | xml_escape }}"
      }
      {% unless forloop.last %},{% endunless %}
    {% endfor %}
  };

  // Clean math equations from search content
  function cleanMathFromContent(content) {
    if (!content) return '';
    
    // Remove display math: $$...$$
    content = content.replace(/\$\$[\s\S]*?\$\$/g, ' [math equation] ');
    
    // Remove inline math: $...$
    content = content.replace(/\$[^$]*?\$/g, ' [math] ');
    
    // Remove LaTeX display math: \[...\]
    content = content.replace(/\\\[[\s\S]*?\\\]/g, ' [math equation] ');
    
    // Remove LaTeX inline math: \(...\)
    content = content.replace(/\\\([\s\S]*?\\\)/g, ' [math] ');
    
    // Remove equation environments
    content = content.replace(/\\begin\{equation\}[\s\S]*?\\end\{equation\}/g, ' [equation] ');
    content = content.replace(/\\begin\{align\}[\s\S]*?\\end\{align\}/g, ' [equation] ');
    content = content.replace(/\\begin\{aligned\}[\s\S]*?\\end\{aligned\}/g, ' [equation] ');
    content = content.replace(/\\begin\{split\}[\s\S]*?\\end\{split\}/g, ' [equation] ');
    
    // Clean up multiple spaces
    content = content.replace(/\s+/g, ' ').trim();
    
    return content;
  }

  // Store original content and create cleaned version for search indexing
  for (var key in window.store) {
    if (window.store[key].content) {
      window.store[key].originalContent = window.store[key].content;
      window.store[key].content = cleanMathFromContent(window.store[key].content);
    }
  }
</script>

<!-- Custom search script -->
<script src="{{site.baseurl}}/assets/js/search.js"></script>

