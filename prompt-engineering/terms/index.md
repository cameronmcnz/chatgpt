---
layout: post
title: Prompt Engineering Terms
description: Browse all prompt engineering term lessons by stage.
permalink: /prompt-engineering/terms/
---

<div class="card card-soft mb-4">
  <div class="card-body p-4">
    <h2 class="h4">Why terms matter</h2>
    <p class="mb-0">Terms are the language of prompt quality. When you know which ingredient is missing, you can fix weak prompts in seconds.</p>
  </div>
</div>

{% assign stages = site.pages | where_exp: "p", "p.path contains 'prompt-engineering/stage-'" | where_exp: "p", "p.path contains '/index.md'" | sort: "path" %}
{% for stage in stages %}
  {% assign stage_folder = stage.path | split: '/' | slice: 1, 1 | first %}
  {% assign stage_root = 'prompt-engineering/' | append: stage_folder | append: '/' %}
  {% assign stage_pages = site.pages | where_exp: "p", "p.path contains stage_root" | sort: "path" %}
  <section class="mb-4">
    <h2 class="h5 mb-3">{{ stage.title }}</h2>
    <div class="row g-3">
      {% for item in stage_pages %}
        {% unless item.path contains '/acronyms/' or item.path contains '/index.md' %}
          <div class="col-md-6">
            {% include term-card.html item=item %}
          </div>
        {% endunless %}
      {% endfor %}
    </div>
  </section>
{% endfor %}
