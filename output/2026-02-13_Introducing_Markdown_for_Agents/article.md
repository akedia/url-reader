---
description: The way content is discovered online is shifting, from traditional search engines to AI agents that need structured data from a Web built for humans. It’s time to consider not just human visitors, but start to treat agents as first-class citizens. Markdown for Agents automatically converts any HTML page requested from our network to markdown.
title: Introducing Markdown for Agents
image: https://cf-assets.www.cloudflare.com/zkvhlag99gkb/6Df02zjRb4inGPazW51EyD/278afaa16719f1080f12936c35a6c0ef/BLOG-3162_OG.png
---

# Introducing Markdown for Agents

2026-02-12

* [![Celso Martinho](https://blog.cloudflare.com/cdn-cgi/image/format=auto,dpr=3,width=64,height=64,gravity=face,fit=crop,zoom=0.5/https://cf-assets.www.cloudflare.com/zkvhlag99gkb/2pzgat1zmt1oF1byi7hskH/7b25e8e00117ee44afe36ad27d7d8032/celso.png)](/author/celso/)  
[Celso Martinho](/author/celso/)
* [![Will Allen](https://blog.cloudflare.com/cdn-cgi/image/format=auto,dpr=3,width=64,height=64,gravity=face,fit=crop,zoom=0.5/https://cf-assets.www.cloudflare.com/zkvhlag99gkb/4EllgD62XLR1z6DEJVpVpu/e2841e9cea806330f4910c9ceedeec11/DSC_3850-H_Edited.jpg)](/author/will-allen/)  
[Will Allen](/author/will-allen/)

5 min read

![](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/rzmAhLxuiqzCffB9yZrdf/91858defbc03196c5f074a26117248f9/BLOG-3162_1.png)

The way content and businesses are discovered online is changing rapidly. In the past, traffic originated from traditional search engines, and SEO determined who got found first. Now the traffic is increasingly coming from AI crawlers and agents that demand structured data within the often-unstructured Web that was built for humans.

As a business, to continue to stay ahead, now is the time to consider not just human visitors, or traditional wisdom for SEO-optimization, but start to treat agents as first-class citizens. 

## Why markdown is important

[ ](#why-markdown-is-important) 

Feeding raw HTML to an AI is like paying by the word to read packaging instead of the letter inside. A simple `## About Us` on a page in markdown costs roughly 3 tokens; its HTML equivalent – `<h2 class="section-title" id="about">About Us</h2>` – burns 12-15, and that's before you account for the `<div>` wrappers, nav bars, and script tags that pad every real web page and have zero semantic value.

This blog post you’re reading takes 16,180 tokens in HTML and 3,150 tokens when converted to markdown. **That’s a 80% reduction in token usage**.

[Markdown](https://en.wikipedia.org/wiki/Markdown) has quickly become the _lingua franca_ for agents and AI systems as a whole. The format’s explicit structure makes it ideal for AI processing, ultimately resulting in better results while minimizing token waste.

The problem is that the Web is made of HTML, not markdown, and page weight has been [steadily increasing](https://almanac.httparchive.org/en/2025/page-weight#page-weight-over-time) over the years, making pages hard to parse. For agents, their goal is to filter out all non-essential elements and scan the relevant content.

The conversion of HTML to markdown is now a common step for any AI pipeline. Still, this process is far from ideal: it wastes computation, adds costs and processing complexity, and above all, it may not be how the content creator intended their content to be used in the first place.

What if AI agents could bypass the complexities of intent analysis and document conversion, and instead receive structured markdown directly from the source?

## Convert HTML to markdown, automatically

[ ](#convert-html-to-markdown-automatically) 

Cloudflare's network now supports real-time content conversion at the source, for [enabled zones](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) using [content negotiation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Content%5Fnegotiation) headers. Now when AI systems request pages from any website that uses Cloudflare and has Markdown for Agents enabled, they can express the preference for text/markdown in the request. Our network will automatically and efficiently convert the HTML to markdown, when possible, on the fly.

Here’s how it works. To fetch the markdown version of any page from a zone with Markdown for Agents enabled, the client needs to add the **Accept** negotiation header with `text/markdown`as one of the options. Cloudflare will detect this, fetch the original HTML version from the origin, and convert it to markdown before serving it to the client.

Here's a curl example with the Accept negotiation header requesting a page from our developer documentation:

`curl https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/ \ -H "Accept: text/markdown"` 

Or if you’re building an AI Agent using Workers, you can use TypeScript:

`` const r = await fetch(
  `https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/`,
  {
    headers: {
      Accept: "text/markdown, text/html",
    },
  },
);
const tokenCount = r.headers.get("x-markdown-tokens");
const markdown = await r.text();
 ``
            

We already see some of the most popular coding agents today – like Claude Code and OpenCode – send these accept headers with their requests for content. Now, the response to this request is formatted  in markdown. It's that simple.  
            

`HTTP/2 200 date: Wed, 11 Feb 2026 11:44:48 GMT content-type: text/markdown; charset=utf-8 content-length: 2899 vary: accept x-markdown-tokens: 725 content-signal: ai-train=yes, search=yes, ai-input=yes --- title: Markdown for Agents · Cloudflare Agents docs --- ## What is Markdown for Agents The ability to parse and convert HTML to Markdown has become foundational for AI. ...` 

Note that we include an `x-markdown-tokens` header with the converted response that indicates the estimated number of tokens in the markdown document. You can use this value in your flow, for example to calculate the size of a context window or to decide on your chunking strategy.

Here’s a diagram of how it works:

### Content Signals Policy

[ ](#content-signals-policy) 

During our last Birthday Week, Cloudflare [announced](https://blog.cloudflare.com/content-signals-policy/) Content Signals — [a framework](http://contentsignals.org) that allows anyone to express their preferences for how their content can be used after it has been accessed. 

When you return markdown, you want to make sure your content is being used by the Agent or AI crawler. That’s why Markdown for Agents converted responses include the `Content-Signal: ai-train=yes, search=yes, ai-input=yes` header signaling that indicates content can be used for AI Training, Search results and AI Input, which includes agentic use. Markdown for Agents will provide options to define custom Content Signal policies in the future.

Check our dedicated [Content Signals](https://contentsignals.org/) page for more information on this framework.

### Try it with the Cloudflare Blog & Developer Documentation 

[ ](#try-it-with-the-cloudflare-blog-developer-documentation) 

We enabled this feature in our [Developer Documentation](https://developers.cloudflare.com/) and our [Blog](https://blog.cloudflare.com/), inviting all AI crawlers and agents to consume our content using markdown instead of HTML.

Try it out now by requesting this blog with `Accept: text/markdown`.

`curl https://blog.cloudflare.com/markdown-for-agents/ \
  -H "Accept: text/markdown"`
            

The result is:
            

`--- description: The way content is discovered online is shifting, from traditional search engines to AI agents that need structured data from a Web built for humans. It’s time to consider not just human visitors, but start to treat agents as first-class citizens. Markdown for Agents automatically converts any HTML page requested from our network to markdown. title: Introducing Markdown for Agents image: https://blog.cloudflare.com/images/markdown-for-agents.png --- # Introducing Markdown for Agents The way content and businesses are discovered online is changing rapidly. In the past, traffic originated from traditional search engines and SEO determined who got found first. Now the traffic is increasingly coming from AI crawlers and agents that demand structured data within the often-unstructured Web that was built for humans. ...` 

### Other ways to convert to Markdown

[ ](#other-ways-to-convert-to-markdown) 

If you’re building AI systems that require arbitrary document conversion from outside Cloudflare or Markdown for Agents is not available from the content source, we provide other ways to convert documents to Markdown for your applications:

* Workers AI [AI.toMarkdown()](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) supports multiple document types, not just HTML, and summarization.
* Browser Rendering [/markdown](https://developers.cloudflare.com/browser-rendering/rest-api/markdown-endpoint/) REST API supports markdown conversion if you need to render a dynamic page or application in a real browser before converting it.

## Tracking markdown usage

[ ](#tracking-markdown-usage) 

Anticipating a shift in how AI systems browse the Web, Cloudflare Radar now includes content type insights for AI bot and crawler traffic, both globally on the [AI Insights](https://radar.cloudflare.com/ai-insights#content-type) page and in the [individual bot](https://radar.cloudflare.com/bots/directory/gptbot) information pages.

The new `content_type` dimension and filter shows the distribution of content types returned to AI agents and crawlers, grouped by [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME%5Ftypes) category. 

You can also see the requests for markdown filtered by a specific agent or crawler. Here are the requests that return markdown to OAI-Searchbot, the crawler used by OpenAI to power ChatGPT’s search: 

This new data will allow us to track the evolution of how AI bots, crawlers, and agents are consuming Web content over time. As always, everything on Radar is freely accessible via the [public APIs](https://developers.cloudflare.com/api/resources/radar/) and the [Data Explorer](https://radar.cloudflare.com/explorer?dataSet=ai.bots&groupBy=content%5Ftype&filters=userAgent%253DGPTBot&timeCompare=1). 

## Start using today

[ ](#start-using-today) 

To enable Markdown for Agents for your zone, log into the Cloudflare [dashboard](https://dash.cloudflare.com/), select your account, select the zone, look for Quick Actions and toggle the Markdown for Agents button to enable. This feature is available today in Beta at no cost for Pro, Business and Enterprise plans, as well as SSL for SaaS customers.

You can find more information about Markdown for Agents on our[ Developer Docs](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/). We welcome your feedback as we continue to refine and enhance this feature. We’re curious to see how AI crawlers and agents navigate and adapt to the unstructured nature of the Web as it evolves.

Cloudflare's connectivity cloud protects [entire corporate networks](https://www.cloudflare.com/network-services/), helps customers build [Internet-scale applications efficiently](https://workers.cloudflare.com/), accelerates any [website or Internet application](https://www.cloudflare.com/performance/accelerate-internet-applications/), [wards off DDoS attacks](https://www.cloudflare.com/ddos/), keeps [hackers at bay](https://www.cloudflare.com/application-security/), and can help you on [your journey to Zero Trust](https://www.cloudflare.com/products/zero-trust/).  
  
Visit [1.1.1.1](https://one.one.one.one/) from any device to get started with our free app that makes your Internet faster and safer.  
  
To learn more about our mission to help build a better Internet, [start here](https://www.cloudflare.com/learning/what-is-cloudflare/). If you're looking for a new career direction, check out [our open positions](http://www.cloudflare.com/careers).

[AI](/tag/ai/)[Agents](/tag/agents/)[Developers](/tag/developers/)[Developer Platform](/tag/developer-platform/)

Follow on X

Celso Martinho|[@celso](https://x.com/@celso)

Will Allen|[@williamallen](https://x.com/@williamallen)

Cloudflare|[@cloudflare](https://x.com/@cloudflare)

Related posts

February 05, 2026 2:00 PM

[2025 Q4 DDoS threat report: A record-setting 31.4 Tbps attack caps a year of massive DDoS assaults](/ddos-threat-report-2025-q4/)

The number of DDoS attacks more than doubled in 2025\. The network layer is under particular threat as hyper-volumetric attacks grew 700%....

By 
* [Omer Yoachimik](/author/omer/),
* [Jorge Pacheco](/author/jorge/),
* [Cloudforce One](/author/cloudforce/)

[DDoS Reports,](/tag/ddos-reports/) [DDoS,](/tag/ddos/) [Cloudforce One,](/tag/cloudforce-one/) [Security,](/tag/security/) [Advanced DDoS,](/tag/advanced-ddos/) [AI](/tag/ai/) 

January 30, 2026 5:01 PM

[Google’s AI advantage: why crawler separation is the only path to a fair Internet](/uk-google-ai-crawler-policy/)

Google's dual-purpose crawler creates an unfair AI advantage. To protect publishers and foster competition, the UK’s Competition and Markets Authority must mandate crawler separation for search and AI....

By 
* [Maria Palmieri](/author/maria-palmieri/),
* [Sebastian Hufnagel](/author/sebastian-hufnagel/)

[AI,](/tag/ai/) [AI Bots,](/tag/ai-bots/) [Google,](/tag/google/) [Legal,](/tag/legal/) [Policy & Legal](/tag/policy/) 

January 30, 2026 2:00 PM

[Building vertical microfrontends on Cloudflare’s platform](/vertical-microfrontends/)

Deploy multiple Workers under a single domain with the ability to make them feel like single-page applications. We take a look at how service bindings enable URL path routing to multiple projects....

By 
* [Brayden Wilmoth](/author/brayden-wilmoth/)

[Cloudflare Workers,](/tag/workers/) [Developer Platform,](/tag/developer-platform/) [Developers,](/tag/developers/) [Dashboard,](/tag/dashboard-tag/) [Front End,](/tag/front-end/) [Micro-frontends](/tag/micro-frontends/) 

January 29, 2026 2:00 PM

[Introducing Moltworker: a self-hosted personal AI agent, minus the minis](/moltworker-self-hosted-ai-agent/)

Moltworker is a middleware Worker and adapted scripts that allows running OpenClaw (formerly Moltbot, formerly Clawdbot) on Cloudflare's Sandbox SDK and our Developer Platform APIs. So you can self-host an AI personal assistant — without any new hardware....

By 
* [Celso Martinho](/author/celso/),
* [Brian Brunner](/author/brian-brunner/),
* [Sid Chatterjee](/author/sid/),
* [Andreas Jansson](/author/andreas-jansson/)

[AI,](/tag/ai/) [Agents,](/tag/agents/) [Cloudflare Workers,](/tag/workers/) [Containers,](/tag/containers/) [Sandbox](/tag/sandbox/) 