---
layout: page
title: Tags
permalink: /tags/
---

<a class="top-link hide" href="#" id="js-top">↑</a>

<div class="container">
	<div class="row">
		<div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">

			<div id='tag_cloud' class="tags">
				{% for tag in site.tags %}
				<a href="#{{ tag[0] }}" title="{{ tag[0] }}" rel="{{ tag[1].size }}">{{ tag[0] }}</a>
				{% endfor %}
			</div>

			{% for tag in site.tags %}
			<div class="one-tag-list">
			  <span class="fa fa-tag listing-separator" id="{{ tag[0] }}">
                    <span class="tag-text"> {{ tag[0] }} </span>
          </span>
      	
				{% for post in tag[1] %}
				 <div class="post-preview">
				    <a href="{{ post.url | prepend: site.baseurl }}">
				        <h3 class="post-title">
                            {{ post.title }}
				        </h3>
				        {% if post.subtitle %}
				        <h3 class="post-subtitle">
				            {{ post.subtitle }}
				        </h3>
				        {% endif %}
				    </a>
				</div>
				<hr>
				{% endfor %}
			</div>
			{% endfor %}

		</div>
	</div>
</div>
