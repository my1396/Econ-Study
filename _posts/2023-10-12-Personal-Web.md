---
layout: post
title: Create Personal Website on GitHub
tag: programming
update: 2023-10-12
---

Reserve this url to 

- build your own site: <http://username.github.io> 

- build project websites: <http://username.github.io/repository>

Nice personal website template from a professor: <https://ryancordell.org>



**Make your site and pages appear on Google Search result**

If your webpages are not indexed, they can't be served on Google and hence not searchable. In order to index your website, need to 

1. set up a `sitemap` for your website, and 
2. submit it to Google Search Engine.

`sitemap` address: <https://my1396.github.io/sitemap.xml>

<https://victor2code.github.io/blog/2019/07/04/jekyll-github-pages-appear-on-Google.html>

What is a <span style='color:#32CD32'>**Sitemap**</span> for?

>If your website doesn’t have any posts or pages, you may not need a sitemap. But for a blog with several posts, a sitemap is necessary (if you want to rank better in search engines). You can submit your sitemap to major search engines like Google, Bing, Yahoo etc., so that their respective bots crawl your site and index them. Only after indexing, your website link appears in the search results.

**Google Search Console** (check if your page is indexed successfully or not)

1.   create a property on Google Search Console

2.   submit the address of your sitemap file to Google Search Engine

<https://search.google.com/search-console/sitemaps?resource_id=https%3A%2F%2Fmy1396.github.io%2F>

>   For my case, I could not search my site via site name until **2 days** after I submit the sitemap file. And it is **5 days** for posts to be searchable via title name. It takes some patience.
>
>   It takes days to weeks for a website to be indexed.



How to generate `sitemap.xml` for Github Pages websites?

My site is hosted on github-pages. It seems github pages now supports this.

Jekyll blogs will not have sitemap by default. You can always generate them using a small snippet of code. Just had to add to `_config.yml`:

```bash
gems:
  - jekyll-sitemap
```

You will not be able to see the XML file created for sitemap inside your directory.

Now, commit the changes and hit the URL `yourwebsite.com/sitemap.xml`. You should see all your links listed there.



**Write your own `sitemap.xml`**

1. Create `<urlset>` and put your webpage address in `<url>` and `<loc>` tags.

2. Put the `sitemap.xml` file in the publishing source folder, i.e., `/docs` for Github Pages sites.

```xml
<urlset xmlns="https://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
	<loc>https://my1396.github.io/EK369E/</loc>
  </url>
  <url>
	<loc>https://my1396.github.io/EK369E/w1.html</loc>
  </url>
  <url>
	<loc>https://my1396.github.io/EK369E/w2.html</loc>
  </url>
  <url>
	<loc>https://my1396.github.io/EK369E/w3.html</loc>
  </url>
  <url>
	<loc>https://my1396.github.io/EK369E/w4.html</loc>
  </url>
</urlset>
```





**Discovered but not indexed**

<https://github.com/orgs/community/discussions/50379>

Why can I do to speed up indexing?

- inspect URL and **request indexing** [this takes a few days, but it works]
- build backlinks to your repository from other reputable websites.



**Google Analytics** (GA)

1. create a account and a property.

2. find your `Mesurement ID` at Admin $\rightarrow$ Data Streams $\rightarrow$ Measurement ID

   <img src="https://drive.google.com/thumbnail?id=1eXuRrsE-3YAiO55SD6kbOPOT82vCFgEO&sz=w1000" alt="image-20230802191239492" style="zoom:80%;" />





How to get custom domain name?

- Go Daddy buy a domain name, or

- Go to DNS Management page from where you buy your domain.



**Difference btw Gist and Project Repository**

My personal understanding or to say my personal usage of Gist and GitHub is:

- GitHub

  A big project work. If you want to build websites, develop mobile or web applications, or do your assignments with your teammates, of course use GitHub.

- Gist

  More like a memo. For example, you can write the implementation of a small feature and share it to your blog, or write down what you think about the project and share it with your teammates. Gist is used for more like code *snippet* thing. So normally if you work on a project, you use GitHub.



___

Q: How to check if a gem is installed?  
A: To get the full list of gems that are installed: `gem list`.  To test for a particular gem, you can use `-i` with a regex: `gem list -i "^gem_name$"`.
