---
layout: post
title: Prompt Engineering Templates
description: Browse all prompt templates and learn when to use each one.
permalink: /prompt-engineering/acronyms/
---

<div class="card card-soft mb-4">
  <div class="card-body p-4">
    <h2 class="h4">Prompt Templates are your fast-start toolkit</h2>
    <p class="mb-0">Use prompt templates when you want a reliable structure without starting from a blank page.</p>
  </div>
</div>

{% assign stages = site.pages | where_exp: "p", "p.path contains 'prompt-engineering/stage-'" | where_exp: "p", "p.path contains '/index.md'" | sort: "path" %}
{% for stage in stages %}
  {% assign stage_folder = stage.path | split: '/' | slice: 1, 1 | first %}
  {% assign stage_root = 'prompt-engineering/' | append: stage_folder | append: '/' %}
  {% assign acronyms = site.pages | where_exp: "p", "p.path contains stage_root" | where_exp: "p", "p.path contains '/acronyms/'" | sort: "path" %}
  <section class="mb-4">
    <h2 class="h5 mb-3">{{ stage.title }}</h2>
    <div class="row g-3">
      {% for item in acronyms %}
        <div class="col-md-6">
          {% include acronym-card.html item=item %}
        </div>
      {% endfor %}
    </div>
  </section>
{% endfor %}
