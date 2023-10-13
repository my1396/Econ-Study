---
layout: post
title: Create Personal Website
tag: programming
update: 2023-10-12
---



# Set up `github.io`

https://pages.github.com/?(null)

*username*.github.io: Build your own site.

http://*username*.github.io/*repository*: Build project websites.



https://www.smashingmagazine.com/2014/08/build-blog-jekyll-github-pages/

See a personal website template from a professor  https://ryancordell.org

How to get custom domain name?

1.   Go Daddy buy a domain name.
2.   Go to DNS Management page from where you buy your domain.



Set up data collection (i.e. add the Google tag to your site)

**Make your site and pages appear on Google search result**

Set up sitemap for your website and submit it to a search engine.

`sitemap` address: https://my1396.github.io/sitemap.xml

https://victor2code.github.io/blog/2019/07/04/jekyll-github-pages-appear-on-Google.html

What is a <span style='color:chartreuse'>**Sitemap**</span> for?

>If your website doesn’t have any posts or pages, you may not need a sitemap. But for a blog with several posts, a sitemap is necessary (if you want to rank better in search engines). You can submit your sitemap to major search engines like Google, Bing, Yahoo etc., so that their respective bots crawl your site and index them. Only after indexing, your website link appears in the search results.

**Google Search console** (check if your page is indexed successfully or not)

1.   create a property on Google Search Console

2.   submit the address of your sitemap file to Google Search Engine

https://search.google.com/search-console/sitemaps?resource_id=https%3A%2F%2Fmy1396.github.io%2F

>   For my case, I could not search my site via site name until **2 days** after I submit the sitemap file. And it is **5 days** for posts to be searchable via title name. It takes some patience.
>
>   It takes days to weeks for a website to be indexed.



Publishing on Github Pages (make your repositories public as a website)

https://idratherbewriting.com/documentation-theme-jekyll/mydoc_publishing_github_pages.html



How to generate `sitemap.xml` for Github Pages websites.

My site is hosted on github-pages. It seems github pages now supports this.

Jekyll blogs will not have sitemap by default. You can always generate them using a small snippet of code. Just had to add to `_config.yml`:

```bash
gems:
  - jekyll-sitemap
```

(You can optionally add to your Gemfile, but mine was already included via dependency).

You will not be able to see the XML file created for sitemap inside your directory.

Now, commit the changes and hit the URL `yourwebsite.com/sitemap.xml`. You should see all your links listed there.



**Google Analytics** (GA)

1. create a account and a property.

2. find your `Mesurement ID` at Admin $\rightarrow$ Data Streams $\rightarrow$ Measurement ID

   <img src="https://drive.google.com/uc?id=1eXuRrsE-3YAiO55SD6kbOPOT82vCFgEO" alt="image-20230802191239492" style="zoom:80%;" />



