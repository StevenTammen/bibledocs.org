---
title: A Brief Technical Summary of This Site's Backend
date: 2021-01-10T21:42:05-05:00
tags: []
subsection: overview
weight: 40
summary: >-
   If you are interested in learning about the technical underpinnings of this website, this page is for you. In a single sentence: content is written in Markdown, converted to HTML via the static site generator Hugo, hosted on GitHub, and deployed via Netlify, which has an extremely fast global content delivery network (CDN) well-optimized for delivering fully static websites like this one.
---

See also the [GitHub repository's Readme](https://github.com/StevenTammen/bibledocs.org/blob/master/README.md).

## Content

The content of this site is written in [Markdown](https://www.markdownguide.org/getting-started/). I use [NeoVim](https://neovim.io/) with an excellent [Realtime Markdown Preview Plugin](https://github.com/iamcco/markdown-preview.nvim) as my editor of choice, along with a lot of macros and text expansions done through the Windows scripting language [AutoHotkey](https://www.autohotkey.com/).

If Vim is a bit scary, I would recommend either setting up [Netlify CMS](https://www.netlifycms.org/) and editing content through the online WYSIWYG interface, or using [Typora](https://typora.io/) (a Markdown editor) locally.

## Exporting to HTML

This site uses [Hugo](https://gohugo.io/) as its static site generator. Pages are run through templates to produce web-ready output. Hugo is incredibly fast, and has been in development long enough that the templating it offers is sufficient for such things as automatically creating content display pages (for all the content that matches a particular category, for example), or conditionally showing page elements depending on what “kind” (Hugospeak: taxonomy) of page is being generated.

## Hosting

This site has the source content located in a [GitHub repository](https://github.com/StevenTammen/bibledocs.org/), with the generated files being hosted on [Netlify](https://www.netlify.com/). Netlify has an extremely fast global content delivery Network (CDN) that caches the entire site, since everything is static. I am using Netlify as my DNS as well, since having the DNS through them lets the CDN work at maximum effectiveness with little configuration.

Netlify also allows for continuous deployment by means of a build command. [Netlify.toml](https://github.com/StevenTammen/bibledocs.org/blob/master/netlify.toml) contains information relating to the continuous deployment I use via Netlify (mainly information pertaining to the Hugo command to run on their server). Whenever a build is triggered (I push to the GitHub repository containing the source), Netlify automatically updates all the cache fingerprints for assets, so only the most recent files are on the CDN. Not having to worry about invalidating out of date assets has been one of my favorite things about this current workflow.

## Domain redirects and subdomains

Netlify automatically handles the 301s between the www and non-www versions of the site. I am keeping the www subdomain for several reasons:

1. Having a proper subdomain (rather than a CNAME at root, as in [CNAME flattening](https://blog.cloudflare.com/introducing-cname-flattening-rfc-compliant-cnames-at-a-domains-root/)) still has some practical performance benefits related to optimally directing DNS traffic. See [this page](https://www.netlify.com/blog/2017/02/28/to-www-or-not-www/#the-ideal-setup) on the Netlify blog.
2. Using a proper subdomain allows for cookie separation on subdomains. This is the biggie. Using an Apex domain does not allow you to be selective about which subdomains use the cookies of the main domain, which is a bad thing. Unnecessary cookies slightly increase security risk, and, perhaps more importantly, slow down page loads. This is especially noticeable if you store static assets on the same domain as your primary site (rather than using a separate site entirely, like some big websites do). This is because the cookies will get sent for *every single static asset loaded* – every style sheet, every script, every image. A few kilobytes of cookies can amount to a fairly significant increase in page size if many static assets are used. I much prefer to use a static subdomain on the main site for serving static content (rather than using a separate domain entirely), since it allows you to mirror static URLs to exactly correspond with the content URLs they are associated with. (For example, [www.mysite.com/posts/somepost/](www.mysite.com/posts/somepost/) might have an image stored at [static.mysite.com/posts/somepost/img1.png](static.mysite.com/posts/somepost/img1.png)). This is much more intuitive and easier for readers to link to, and also happens to save a not insubstantial amount of money in the long run by making extra domain registration costs unnecessary.
3. There is not any performance reason to use a bare domain if you can just type in the bare domain and get redirected to the www subdomain anyway (a redirect so fast a human could never process it). So you can still do less typing by ignoring the www if you wish, but the performance benefits of the www subdomain will still be in effect.

## TLS encryption

Netlify provides [easy HTTPS for custom domains](https://www.netlify.com/docs/ssl/) by partnering with [Let’s Encrypt](https://letsencrypt.org/). While security is not super important for this site as I don’t have user sessions or deal with credit card information, I am 100% behind encrypting everything simply on principle. Using HTTPS is also miles better for site SEO (search engine page-rank).

I force HTTPS sitewide. So all non-HTTPS requests will automatically get converted to HTTPS requests.

## Performance: gzipping, minification, etc.

Netlify automatically minifies and gzips many content types (including images, once you configure things). It is theoretically possible to gain a better compression level by running a more size-efficient DEFLATE encoder (like [Zopfli](https://en.wikipedia.org/wiki/Zopfli)), but the added cycles would slow down site builds for not much gain.

## Email

I use [forwardemail.net](https://forwardemail.net/en/pricing) to handle all email through the site (rather than, say, [Google Workspace](https://workspace.google.com/)).
