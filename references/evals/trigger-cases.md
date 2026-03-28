# URL Reader Skill — Trigger Eval Cases

20 sample prompts to evaluate whether the url-reader skill should activate.

## Should Trigger (10)

| # | Prompt | Should Trigger | Notes |
|---|--------|---------------|-------|
| 1 | `帮我读一下这个链接 https://mp.weixin.qq.com/s/abc123` | Yes | Explicit URL + Chinese "read this link" |
| 2 | `Read this page: https://www.zhihu.com/question/12345` | Yes | English "read this page" + URL |
| 3 | `https://x.com/elonmusk/status/999888777` | Yes | Bare URL, should auto-trigger |
| 4 | `抓取这个公众号文章 https://mp.weixin.qq.com/s/xyz` | Yes | Chinese "fetch this WeChat article" |
| 5 | `Fetch the content from https://www.xiaohongshu.com/explore/abc` | Yes | English "fetch content" + Xiaohongshu URL |
| 6 | `打开链接看看写了什么 https://bilibili.com/read/cv12345` | Yes | Chinese "open link and see what it says" |
| 7 | `Can you extract the text from this webpage? https://example.com/blog/post` | Yes | "extract text from webpage" + URL |
| 8 | `帮我把这篇文章保存成 Markdown https://feishu.cn/docs/abc` | Yes | "save as Markdown" + Feishu URL |
| 9 | `读取网页内容 https://www.weibo.com/detail/abc123` | Yes | Chinese "read webpage content" + Weibo |
| 10 | `What does this link say? https://news.ycombinator.com/item?id=12345` | Yes | "what does this link say" + general URL |

## Should NOT Trigger (10 — near-miss cases)

| # | Prompt | Should Trigger | Notes |
|---|--------|---------------|-------|
| 1 | `Search the web for recent news about AI` | No | Web search request, no specific URL |
| 2 | `Find information about Python asyncio` | No | Information lookup, no URL involved |
| 3 | `Google "best restaurants in Shanghai"` | No | Search engine query, not URL reading |
| 4 | `帮我搜索一下最新的 AI 新闻` | No | Chinese "search for latest AI news" — search, not fetch |
| 5 | `What is the URL format for WeChat articles?` | No | Question about URLs, not reading one |
| 6 | `Create a web scraper using Python` | No | Coding task to build a scraper, not using this skill |
| 7 | `Download the file at /tmp/report.pdf` | No | Local file path, not a web URL |
| 8 | `Can you summarize the Wikipedia article about quantum computing?` | No | No URL given; would need search first |
| 9 | `Open my browser to google.com` | No | Browser control request, not content extraction |
| 10 | `网上有什么关于 Rust 语言的教程？` | No | "What tutorials exist online about Rust" — search intent |
