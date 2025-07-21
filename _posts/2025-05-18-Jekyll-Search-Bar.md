---
layout: post
title: Jekyll Search Field
tag: programming
update: 2025-05-18
---

Setting up `lunr.js` in Jekyll



Google didn’t index every page on my site, so using a Google custom search wasn’t worth it. 

Google search box uses the Google index to find its pages (which requires an [XML sitemap](https://jekyllcodex.org/without-plugin/sitemap) to help Google find the latest additions to your website).

`Lunr.js` provides a solution for searches on static sites.

The key features of `Junr.js` we will be using for searching static sites like Jekyll are:

- The ability to do full text search in JSON
- The ability to search in the browser



**Overview of steps**:

1. Creating the static site search results page `search.md`
2. Creating the static site search JavaScript `search.js`
3. Creating the static site search element `search-box.html`
4. Add `search-box.html` at the location where you want your system to display the search bar or functionality.



**Step-by-Step breakdown**:

`search.md`

Create search data. Located in the root directory of your website. The location where you have your `index.md` file.



`search.js`

Contains JavaScript that implement the search method.

It basically adds an event listener and once the required event is triggered it performs the search. 



`search-box.html`

This file has a search box, a placeholder for displaying results.



Error Message

Jekyll `lunr` search-box Cannot read properties of null (reading 'setAttribute')

```
search.js:38 Uncaught TypeError: Cannot read properties of null (reading 'setAttribute')
    at search.js:38:42
    at search.js:66:3
```

The error can be traced to

```js
document.getElementById('search-box').setAttribute("value", searchTerm);
```



Jekyllcodex provides a solution, but there are uni-code errors.

<https://jekyllcodex.org/without-plugin/search-lunr/>



[`jekyll-lunr-js-search`](https://github.com/slashdotdash/jekyll-lunr-js-search) plugin

<https://stackoverflow.com/questions/28255836/why-am-i-getting-an-error-when-installing-lunr-js-search-on-jekyll>

___

**References**:

- <https://kevquirk.com/blog/how-to-add-search-jekyll>

- <https://www.stephanmiller.com/static-site-search/>

- <https://learn.cloudcannon.com/jekyll/jekyll-search-using-lunr-js/>

- <https://github.com/rseng/rse/blob/master/rse/app/templates/search.html>

  Website: <https://rseng.github.io/rse/search/?q=conda>

- `search-box` null error: <https://talk.jekyllrb.com/t/lunr-js-not-giving-results/1466/3>

  