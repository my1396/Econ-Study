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
				{% for tag_name in site.tag_order %}
					{% if site.tags[tag_name] %}
					<a href="#{{ tag_name }}" title="{{ tag_name }}" rel="{{ site.tags[tag_name].size }}">{{ tag_name }}</a>
					{% endif %}
				{% endfor %}
			{% assign sorted_tags = site.tags | sort %}
			{% for tag in sorted_tags %}
				{% unless site.tag_order contains tag[0] %}
				<a href="#{{ tag[0] }}" title="{{ tag[0] }}" rel="{{ tag[1].size }}">{{ tag[0] }}</a>
				{% endunless %}
			{% endfor %}
		</div>

		{% for tag_name in site.tag_order %}
		{% if site.tags[tag_name] %}
		<div class="one-tag-list">
		  <span class="fa fa-tag listing-separator" id="{{ tag_name }}">
                    <span class="tag-text"> {{ tag_name }} </span>
          </span>
      	
			{% for post in site.tags[tag_name] %}
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
		{% endif %}
		{% endfor %}

		{% assign sorted_tags = site.tags | sort %}
		{% for tag in sorted_tags %}
		{% unless site.tag_order contains tag[0] %}
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
		{% endunless %}
		{% endfor %}

	</div>
	</div>
</div>

