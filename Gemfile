# frozen_string_literal: true

source "https://rubygems.org"
gemspec

gem "jekyll", ENV["JEKYLL_VERSION"] if ENV["JEKYLL_VERSION"]
gem "kramdown-parser-gfm" if ENV["JEKYLL_VERSION"] == "~> 3.9"
gem "github-pages", "~> 228", group: :jekyll_plugins

group :jekyll_plugins do
  gem 'jekyll-sitemap'
  gem 'jekyll-feed'
  gem 'jekyll-seo-tag'
  gem 'jekyll-pdf-embed'
  gem 'jekyll-scholar'
end

gem "webrick", "~> 1.8"
gem 'uri', '= 0.12.0'
