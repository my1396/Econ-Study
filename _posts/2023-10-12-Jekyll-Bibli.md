---
layout: post
title: Add Bibliography Using Jekyll Plugin 
tag: programming
update: 2023-10-12
toc: true
---

<a class="top-link hide" href="#" id="js-top">↑</a>

Use [`Jekyll-Scholar`](https://github.com/inukshuk/jekyll-scholar) plugin to enable citation and add bibliography.

Github Pages doesn't support the plugin. Two options provide a workaround:

- Change between two branches of your site repository.

  - Build your site locally and push the results to the `source` branch. This is where you keep your entire project, e.g., sources, configuration and plugins, where you make changes and build your site locally. 

    - `_site` folder should be in the `.gitignore`. It contains Jekyll compiled HTML fies. Once build (locally), these files can be uploaded directly to a server, e.g., GitHub Pages, for hosting.

  -  `master` or `gh-pages` branch. This is where GitHub Pages are deployed. Consists solely of the compiled sites which GitHub Pages can use directly.
    - Create a `_nojekyll` file to tell GitHub Pages not to run Jekyll each time you push things. This is very important if you have directories beginning with `_` since they have a special treatment with Jekyll (they are not deployed on the Web site).
    - Meanwhile, in the `_config.yml` of the `source` branch, under the `include` key, we need to add `- .nojekyll`.

  - Note: It is recommended to change your default branch to `source`. Optionally, you can make the `source` branch protected to prevent it from being accidently deleted or overriden.

- Alternatively, you can use a [Github Actions](https://github.com/features/actions) called [jekyll-action](https://github.com/helaili/jekyll-action) to deploy your site to Github Pages.

  > This saves you time to manage different branches every time you make a change in your repo.
  >
  > Building and deployment is done through Github Actions automatically. I would **recommend** this approach if you don't mind waiting because it takes much longer time for GitHub Pages to build than does locally. 
  >
  > It takes about 4 minutes for GitHub Pages to finish building and deployment.

  You only need to manage your remote Github Page repository. Github Actions will deploy your website automatically. Using the following codes to push your local changes to remote:

  ```bash
  git add .
  git commit -m "post update"
  git push
  ```

  Combinging multiple cmds using `&&`:
  ```bash
  git add . &&
  git commit -m "post update" &&
  git push
  ```
  `&&` is conditionally run. The following cmd runs only if the previous cmd is successful.


___

### Installation

In `Gemfile`, add `gem 'jekyll-scholar'` .

Create a `_bibliography` directory to sotre your bibliography `.bib` files. The `_` in the directory name means that Jekyll will not copy it in the generated site (`_site` by default). If you want that your bibliography file is visible to your site visitors, then you should take this into account and, e.g., store the file in a `bibliography` directory instead. 

#### 1. Use GitHub Actions to build and deploy GitHub Pages site

For security reasons, only a limited number of [third-party plugins are supported by the GitHub Pages][github-pages-dependencies] automated build pipeline using the default ```'Deploy from a branch'``` method. It is possible, however, to use GitHub's continuous integration and continuous delivery (CI/CD) platform, [Github Actions][github-actions], and [create a custom workflow][github-actions-github-pages] that installs any jekyll plugin. This is actually very easy to do from your GitHub Pages repository page:  

1. Open the ```Settings```--> ```Pages``` tab 
2. Under ```'Build and Deployment'```, change the ```'Source'``` from ```'Deploy from a branch'``` to ```'GitHub Actions'```
3. Add the suggested workflow yaml file (saved under ```.github/workflows```)

You can see my final workflow file [here][github-workflow].

Note: if you have a ```Gemfile.lock``` file committed to your repo then it may cause issues: add it to ```.gitignore``` and remove it from your git cache (```git rm --cache Gemfile.lock```)

#### 2. Add the jekyll-scholar plugin

This is also straightforward:
1. Add ```gem "jekyll-scholar", group: :jekyll_plugins``` to your ```Gemfile``` (you can see mine [here][gemfile])
2. Add ```- jekyll-scholar``` to your ```_config.yml``` (see mine [here][config])

#### 3. Downgrade ruby

Ideally, the two steps above would be all that is needed to get up and running with jekyll-scholar on GitHub Pages, but when I tried adding a citation and building my site locally I got the error message ```Liquid Exception: tried to create Proc object without a block```. 

After a lot of googling I landed on the most likely source of the problem being [incompatible ruby versions][ruby-issue] between [github-pages][github-pages-gems] and jekyll-scholar. I have not spent a lot of time trying to dig into this to figure out why it is an issue, or if there is a better way to solve it, but downgrading ruby from ```3.1.2``` to ```2.7.2``` solved the problem and so this is what I am doing for now.

##### Downgrade ruby locally

1. Install older ruby version locally using [chruby][chruby] (```ruby-install 2.7.2```)
2. Restart your terminal
3. Select older ruby version with ```chruby 2.7.2```
4. Re-run ```bundle install``` to update gems
5. Run ```bundle exec jekyll serve``` to validate fix

##### Downgrade ruby in build pipeline

1. Add a ```.ruby-version``` file to the root of your repo and specify ruby version ```2.7.2```
2. Remove the ruby version line from the ```jekyll.yml``` workflow



### Configuration

You can configure the way Jekyll-Scholar works using your `_config.yml` configuration file. The default is (see [here](https://github.com/inukshuk/jekyll-scholar) for the meaning of the options):

```css
scholar:
  style: apa
  locale: en

  sort_by: none
  order: ascending

  group_by: none
  group_order: ascending

  source: ./_bibliography
  bibliography: references.bib
  bibliography_template: ""

  replace_strings: true
  join_strings:    true

  use_raw_bibtex_entry: false

  details_dir:    bibliography
  details_layout: bibtex.html
  details_link:   Details

  query: "@*"
```



- Add your bib to `./_bibliography/references.bib`



### Citation

<ol>
<li> Add citation with liquid tags. <br> 
Use `cite` tag with the appropriate key of the item you want to cite. <br>

{% highlight liquid %}{% raw %}{% cite Wallace2018 %}{% endraw %}{% endhighlight %} <p style="margin-top:-1.5cm;">&nbsp;</p>
will always show a parenthesis citing: {% cite Wallace2018 %}
</li>

<li> 	Add bibliography. <br> 
The `--cited` option includes only those entries you cited on the page. <br>
{% highlight liquid %}{% raw %}{% bibliography --cited %}{% endraw %}{% endhighlight %} 
</li>

</ol>



Special thanks to the tutorials in the blogs from [{% cite Danks %}](https://open-research.gemmadanks.com) and [{% cite Poizat %}](https://pages.lip6.fr/Pascal.Poizat/blog/posts/2016/02/01/jekyll-and-bibtex/#:%20:text=You%20can%20use%20a%20_bibliography,site%20(%20_site%20by%20default).).

This blog is build on their original contents. 



___

**References**

{% bibliography --cited %}



[apa-csl]: https://github.com/citation-style-language/styles/blob/master/apa.csl
[bibtex]: http://www.bibtex.org/
[chruby]: https://github.com/postmodern/chruby
[config]: https://github.com/my1396/Econ-Study/blob/main/_config.yml
[csl-styles]: https://github.com/citation-style-language/styles
[gemfile]: https://github.com/gemmadanks/gemmadanks.github.io/blob/main/Gemfile
[github-actions]: https://docs.github.com/en/actions
[github-actions-github-pages]: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow
[github-pages]: https://pages.github.com/
[github-pages-dependencies]: https://pages.github.com/versions
[github-pages-gems]: https://rubygems.org/gems/github-pages/versions/227
[github-workflow]: https://github.com/gemmadanks/gemmadanks.github.io/blob/main/.github/workflows/jekyll.yml
[html-list-style]: https://developer.mozilla.org/en-US/docs/Web/CSS/list-style
[jekyll]: https://jekyllrb.com/
[jekyll-scholar]: https://github.com/inukshuk/jekyll-scholar
[jekyll-scholar-citations]: https://github.com/inukshuk/jekyll-scholar#citations
[jekyll-scholar-issue-75]: https://github.com/inukshuk/jekyll-scholar/issues/75
[jekyll-scholar-issue-160]: https://github.com/inukshuk/jekyll-scholar/issues/160
[latex]: https://www.latex-project.org/
[my-research-process]: https://open-research.gemmadanks.com/planning/my-research-process/
[ruby-issue]: https://github.com/alshedivat/al-folio/issues/161
[zotero]: https://www.zotero.org/
[zotero-style-repo]: https://www.zotero.org/styles



 





