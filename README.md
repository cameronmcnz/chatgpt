# 7 Day Condensed ChatGPT Masterclass Site

This repository is configured as a full Jekyll site for the course, using Bootstrap 5, Lineicons, and Xennial-inspired branding.

## Local run

1. Install Ruby and Bundler.
2. From this folder, run:

```bash
bundle install
bundle exec jekyll serve --config _config.yml,_config.local.yml
```

3. Open the local URL shown in the terminal, usually http://127.0.0.1:4000.

## GitHub Pages deployment

- Production config in `_config.yml` is set for the GitHub Pages project site at `/micro-learning`.
- CI deployment workflow is in `.github/workflows/pages.yml`.

## Site structure

- Home page: /index.md with layout course
- Day hubs: /day-01/ through /day-07/
- Lesson pages: all markdown files under day folders
- Prompt Engineering hub: /prompt-engineering/
- Stage hubs: /prompt-engineering/stage-01/ through /prompt-engineering/stage-07/
- Terms index: /prompt-engineering/terms/
- Templates index: /prompt-engineering/acronyms/ 

## No-index policy

This site is configured to discourage search indexing:

- robots.txt disallows all crawling.
- Global meta tags add noindex, nofollow, noarchive, nosnippet, and noimageindex directives.
- `_headers` sets `X-Robots-Tag` and strict cache controls for hosts that support static header files.
- `netlify.toml` and `vercel.json` enforce `X-Robots-Tag` and cache-control headers on those platforms.

Important: HTTP response headers such as X-Robots-Tag require hosting or server-level support. Plain GitHub Pages cannot always enforce custom header rules unless handled by a proxy or CDN layer.

## Operational checklist

- Confirm `robots.txt` is publicly reachable and returns `Disallow: /`.
- Confirm page HTML contains robots and crawler-specific noindex meta tags.
- Confirm HTTP response headers include `X-Robots-Tag` in production.
- If deploying on GitHub Pages directly, put Cloudflare or another reverse proxy in front to set headers.
