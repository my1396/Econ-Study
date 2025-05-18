---
layout: post
title: Jekyll Search bar
tag: programming
update: 2025-05-18
---

Google didn’t index every page on my site, so using a Google custom search wasn’t worth it. 

Google search box uses the Google index to find its pages (which requires an [XML sitemap](https://jekyllcodex.org/without-plugin/sitemap) to help Google find the latest additions to your website).

`Lunr.js` provides a solution for searches on static sites.

The key features of `Junr.js` we will be using for searching static sites like Jekyll are:

- The ability to do full text search in JSON
- The ability to search in the browser

Overview of steps:

1. Creating the static site search results page
2. Creating the static site search element `search-box.html`
3. Creating the static site search JavaScript `search.js`



`search-box.html`

This file has a search box, a placeholder for displaying results.



Error Message

Jekyll lurn search-box Cannot read properties of null (reading 'setAttribute')

```
search.js:38 Uncaught TypeError: Cannot read properties of null (reading 'setAttribute')
    at search.js:38:42
    at search.js:66:3
```

The error can be traced to

```js
document.getElementById('search-box').setAttribute("value", searchTerm);
```





References:

- <https://www.stephanmiller.com/static-site-search/>

- <https://learn.cloudcannon.com/jekyll/jekyll-search-using-lunr-js/>

- <https://github.com/rseng/rse/blob/master/rse/app/templates/search.html>

  Website: <https://rseng.github.io/rse/search/?q=conda>

- `search-box` null error: <https://talk.jekyllrb.com/t/lunr-js-not-giving-results/1466/3>

- <https://jekyllcodex.org/without-plugin/search-lunr/>