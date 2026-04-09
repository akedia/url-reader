# How I built 13,000+ pages in 3 hours and grew SEO traffic +466% in 60 days


60 days ago, the pages driving most of our SEO traffic didn't exist.


Today:

- 13,000+ programmatic pages live
- Weekly organic clicks went from 971 to 5,500
- +466% (or 5.7x) traffic increase in 60 days
- And ~50% of pages aren't even indexed yet

No template spam, no city-name swaps, no thin AI content.


Instead, we built a system where content isn’t written page by page...


It’s built like software.


13,000+ useful pages generated in under 3 hours.


And the curve is still going up:


At some point it clicked: this isn’t traditional programmatic SEO.


I might be early in saying it, but this looks like the future of AI-powered programmatic SEO to me...


Programmatic SEO 2.0.


> Note: I reveal the website and show the exact pages in section 7.


Inside this article

1. 6 content categories behind the system
1. How the pSEO 2.0 system works
1. Most important part of the entire system
1. How 1,000s of pages get generated at scale
1. What happened after publishing 13,000+ pages
1. “13,000 AI-generated pages?!” I hear you scream
1. Website reveal: What these pages actually look like
1. What this experiment taught me

1. 6 content categories behind the system


Most people hear “programmatic SEO” and think of:

- Top-list pages
- Location pages
- Comparison pages

But we went much wider.


Right now, the system has generated 13,000+ pages across 6 different content categories.


Comparison pages are actually the smallest category (only 1%). Most pSEO practitioners would usually start here, making these “obvious” plays the smallest opportunity.


Resource pages make up the bulk of our pages. 34 different content types (idea lists, checklists, calendars, guides, and templates) across 309 niches.


That’s how one system produces 7,600+ pages.


Free tools are interesting because they’re not just text pages. They are actual working tools, each one including niche-specific examples and context. All created programmatically.


2. How the pSEO 2.0 system works


If you take just one thing from this article, make it this:


For programmatic pages, we never ask the AI to write freeform content.


We ask it to fill a strict JSON schema.


## How it works in simple terms

1. Niche context: 309 niches with audience, pain points, and strategies
1. Gemini Flash: Fills strict JSON schemas with niche-aware content
1. Validated JSON: 13,000+ type-safe content files
1. 20+ renderers: Specialised React components per content types

AI generates the data and the front end (components) handles the presentation.


These two layers never mix.


This matters because freeform AI generation breaks at scale.

- Inconsistent structure
- Unpredictable output quality
- Pages that are impossible to validate

Schemas solve that because every page follows the exact same structure.


This means you get:

- Consistent UI/UX
- Predictable output quality
- Reliable large-scale generation

When you're generating 13,000 pages, structure isn't a limitation.


It’s the key to making programmatic SEO work.


## Example schema


Each section must include 15–20 items.


Each item must include a difficulty level and a potential score.


That constraint forces the AI to generate consistent, usable output. Without it, you might get 8 items on one page and 40 items on the next.


With schemas, every page stays structured.


## Content and design stay separate


Another benefit of this architecture:

- Content = JSON
- Design = React components

That means we can redesign the entire website without regenerating any content.


We’ve already updated page layouts multiple times and not a single content file changed.


Each content type has its own specialised renderer.


For example:

- Blog idea pages has filtering by category and difficulty
- SEO checklists has interactive checkboxes
- Tool comparisons has structured tables

In total we built 20+ purpose-built components, all consuming the same structured JSON.


When you separate generation, structure, and presentation, you can scale programmatic SEO without the usual quality problems.


3. Most important part of the entire system


The real scale comes from the niche taxonomy.


We built structured context for 309 different niches, each including:

- Audience
- Pain points
- Monetization strategies
- Content formats that perform
- Key subtopics

This is probably the most important part of the entire system, and the part most people would underinvest in.


When the system generates something like: “SEO Checklist for Travel Bloggers”


It doesn't just replace the word “travel” and create a generic checklist; the model instead receives structured context about that niche.


For example:


This context gets injected into the generation process.


So instead of producing generic output, the system produces niche-specific content.


A health blogger’s checklist might focus on:

- E-E-A-T
- Authority signals
- YMYL compliance

A travel blogger’s checklist might focus on:

- Seasonal keyword planning
- Destination competition
- Google hotel results

Same schema, completely different substance.


> Important note: We spent more time on niche taxonomy than anything else. Rich niche context is what turns programmatic SEO from templated name-swapped filler into useful content at scale.


## 4. How 1,000s of pages get generated at scale


The generation system itself is surprisingly simple.


We used Gemini Flash to produce the content.


At this scale, the most important factor isn’t peak model quality, it's the cost-to-quality ratio.


Gemini Flash works well because it supports native structured JSON output. That means the model returns valid JSON directly rather than wrapping responses in text or markdown.


This eliminates a whole category of parsing issues.


The system runs 100 concurrent workers.


Most AI APIs can handle far more parallel requests than people expect. At this level of concurrency, the full corpus of 13,000+ pages is generated in under 3 hours.


The main bottleneck isn’t the model, it’s API rate limits.


One important detail: titles are not generated by AI.


Instead, we use deterministic templates like: “100 Blog Post Ideas for Travel Bloggers in 2026”


This keeps titles:

- Consistent
- Predictable
- Optimised for search

In practice, a well-designed template produces better titles than AI.


5. What happened after publishing 13,000+ pages


We rolled the pages out progressively over several weeks and monitored indexing and traffic as we went.


Here’s where things landed 60 days later:

- 13,000+ pages live
- +466% (or 5.7x) traffic increase
- ~50% pages indexed (so far)
- <3 hrs full generation time

With each batch of pages indexed, they rank for long-tail keywords within days and add incremental traffic.


The weekly numbers tell the story best: We went from 971 clicks per week before launch to 5,500 clicks per week in just 60 days.


Some key insights so far:


## 1. Resource pages drove most of the traffic


Blog post ideas, SEO checklists, and content guides make up the majority of our traffic.


These pages target informational queries at scale: high volume, lower competition.


## 2. Free tools perform extremely well


Tool pages have higher engagement than pure content pages. People use the tool, then explore the rest of the website.


Different intent, different part of the funnel.


## 3. Indexing is still the bottleneck


Only around 50% of the pages are indexed so far, which means we’re not even close to the system’s full potential yet.


## 4. No negative signals from Google


Pages index cleanly, rank on merit, and stick.


And Google's "helpful content" updates haven’t touched us.


6. “13,000 AI-generated pages?!” I hear you scream


When people hear “13,000 AI-generated pages”, the immediate reaction is usually the same.


“Isn’t that exactly the kind of thing Google is cracking down on?”


That would be a fair assumption, but this system works differently from traditional programmatic SEO.


## 1. These pages aren’t just text


Most pSEO pages fail because they’re thin content.


They’re usually:

- Template pages
- Variable substitutions
- Same content with various words changed

Our pages are structured and functional.


For example:


A page like “100 Blog Post Ideas for Finance Bloggers” isn’t just a wall of text.


It includes:

- Structured sections
- Filtering by category and difficulty
- Copy-to-clipboard functionality

The page can actually be used.


SEO checklist pages include interactive checkboxes. Tool pages include real working tools.


These pages behave more like product pages than blog posts.


## 2. The presentation layer matters


Every content type has its own purpose-built React component.


That means:

- Filtering and search
- Structured tables
- Proper UX
- Schema markup
- Breadcrumbs
- FAQ schema

These aren’t markdown pages dumped into a generic template.


They’re fully structured pages designed for a specific use case.


## 3. The test we use


For every page, we ask two simple questions:


“Would this still be useful if search engines didn’t exist?”


“If someone bookmarked the page and came back later, would it still provide value?”


For most of these pages, the answer is yes.


## 4. Why traditional pSEO fails this test


Traditional programmatic SEO usually fails this test.


This is because it typically relies on systems like variable substitution into a template or same content with different city names swapped in.


The result is 1,000s of pages that technically exist, but provide very little value.


## 5. Why this pSEO system works


Structured AI generation changes that because:

- Schemas enforce completeness
- Niche context creates relevance
- Components create usable UX

Which results in pages that are different, useful, and specific to their niche.


Not just text generated at scale. Actually useful pages generated at scale.


7. Website reveal: What these pages actually look like


Quick context:


Earlier this year we rebuilt Byword from scratch.


Version 1 had been running for a few years, but the codebase had accumulated enough technical debt that shipping new features was becoming increasingly slower.


We wanted a clean foundation so we could move faster.


One of the greatest outcomes of the rebuild was the system we’ve just explained.


A programmatic SEO engine capable of generating 1,000s of genuinely different pages, instead of the traditional pSEO approach where variables are swapped into a template.


This is a system built around:

- Structured schemas
- Niche context injection
- Specialised renderers
- Component-driven pages

One that could produce useful pages at the kind of scale that would take a content team years.


Now let me show you…


We ran this experiment on our very own website.


Here’s the page breakdown again:


Examples for each category:

- 100 Motorcycle Blog Name Ideas
- AI Content for E-Commerce
- Paragraph Rewriter Tool
- Programmatic SEO Templates for Travel
- Best SEOwriting.ai Alternatives
- AI Content Writer

8. What this experiment taught me


We’re still early.


Only around 50% of the pages are indexed.


The niches we’ve covered are still relatively broad. So there’s a whole layer of deeper, more specific content we haven’t yet generated.


The system itself is already built to handle that scale with no architectural changes required.


## A few things differently for next time


The execution of this experiment wasn't perfect. If we were building this system again, a few things would change.


Here are 5 examples:

- Start with the taxonomy: Niche context is the foundation. I’d spend ~60% of the time here.
- Build more page types: Comparison pages felt obvious, but ended up being a very small category. Resource pages and tools drove most traffic.
- Ship in batches: Progressive rollout means indexing can be monitored and adjustments made before scaling further.
- Use native JSON output: Structured responses eliminate parsing issues and make large-scale generation reliable.
- Invest in the frontend: Purpose-built components are what make programmatic pages actually useful.

## The interesting part isn’t the page count


13,000+ pages sounds impressive.


But that’s not the real advantage. The real gain is in the feedback loop.


Every week we learn:

- Which niches perform best
- Which content types attract traffic
- Where the long tail actually lives

This data feeds back into the taxonomy, which in turn improves the next generation run.


The system improves as it scales.


## Built, not written


This experiment only reinforced something we already believed when building Byword.


AI works best when it operates inside constraints.


Not in writing freeform content, but in filling structured systems designed by humans.


In other words:


AI content should be built, not written.


Closing note


This kind of system doesn’t really exist out of the box. Most CMS platforms actually make it very difficult to implement structured, schema-driven programmatic SEO like this without building custom infrastructure.


We’re working on solving that by building a dedicated CMS layer inside Byword (join the pSEO 2.0 waitlist). And if you want to implement a complete SEO system, the team at Contact can help.
