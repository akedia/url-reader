# URL Reader Skill — Platform Success Rubric

Defines what "success" looks like for each supported platform.

## General Criteria (all platforms)

- **Output format**: Markdown file with YAML-frontmatter metadata (title, source URL, date, platform)
- **Minimum content threshold**: ≥ 200 characters of meaningful body text (excluding metadata/boilerplate)
- **Images**: Downloaded locally to `images/` subfolder; references updated in Markdown
- **Encoding**: UTF-8, no mojibake — especially critical for CJK content
- **Fallback chain verified**: If primary strategy fails, next strategy is attempted automatically

---

## Per-Platform Rubric

### WeChat (微信公众号) — `mp.weixin.qq.com`

| Criterion | Expected |
|-----------|----------|
| **Output format** | Markdown + optional HTML; images embedded or local |
| **Min content** | Full article body ≥ 500 chars; not just title/author stub |
| **Title** | Extracted from `<h1>` or og:title, not "微信公众平台" boilerplate |
| **Images** | All inline images downloaded; WeChat CDN URLs resolved |
| **Fallback chain** | Firecrawl → Jina → Playwright |
| **Success indicator** | Article text present, no "请在微信客户端打开" error message |
| **Known edge cases** | Long-URL vs short-URL (/s/xxx); CAPTCHA on long URLs |

### Twitter/X — `x.com`, `twitter.com`

| Criterion | Expected |
|-----------|----------|
| **Output format** | Markdown with tweet text, author, timestamp |
| **Min content** | Full tweet text including long-form tweets (Notes) |
| **Media** | Embedded images/video thumbnails downloaded |
| **Thread support** | Multi-tweet threads concatenated in order |
| **Fallback chain** | fxtwitter API → Jina → Playwright |
| **Success indicator** | Tweet body present, author handle extracted, no "This Tweet is unavailable" |
| **Known edge cases** | Protected accounts; tweets with polls; quote tweets |

### Xiaohongshu (小红书) — `xiaohongshu.com`

| Criterion | Expected |
|-----------|----------|
| **Output format** | Markdown with note text and image carousel |
| **Min content** | Full note body ≥ 200 chars |
| **Images** | All carousel images downloaded with correct Referer header |
| **Fallback chain** | Firecrawl → Jina → Playwright |
| **Success indicator** | Note body present, not login-wall placeholder |
| **Known edge cases** | Login-required content; video notes (text may be minimal) |

### Bilibili (B站) — `bilibili.com`

| Criterion | Expected |
|-----------|----------|
| **Output format** | Markdown; for articles (`/read/cv*`): full body; for videos: title + description |
| **Min content** | Articles: ≥ 500 chars body; Videos: title + description present |
| **Images** | Article inline images downloaded |
| **Fallback chain** | Jina → Firecrawl → Playwright |
| **Success indicator** | Content body present, not "请登录" or empty stub |
| **Known edge cases** | Video pages have minimal text; column articles vs video pages |

### General Webpage — `*`

| Criterion | Expected |
|-----------|----------|
| **Output format** | Markdown with clean body text, no nav/footer/ad boilerplate |
| **Min content** | ≥ 200 chars of meaningful body text |
| **Title** | Correct page title from `<title>` or `<h1>` |
| **Images** | Inline content images downloaded; skip icons/ads |
| **Fallback chain** | Markdown Direct → Jina → Firecrawl → Playwright |
| **Success indicator** | Readable article/page body; no raw HTML tags in output |
| **Known edge cases** | SPAs requiring JS rendering; paywalled content; cookie consent walls |

---

## Fallback Chain Verification

To confirm the fallback chain works correctly, test each platform with the primary strategy intentionally disabled:

1. **Layer 1 fail → Layer 2**: Set primary strategy to return empty → verify next layer activates
2. **All layers fail**: Verify graceful error message (not a stack trace) with the URL and reason
3. **Partial content**: If a strategy returns < min content threshold, it should be treated as failure and fall through

## Quality Checklist

- [ ] No raw HTML tags in Markdown output
- [ ] No "请在微信客户端打开" or similar access-denied messages treated as content
- [ ] CJK characters render correctly (no encoding issues)
- [ ] Image paths in Markdown point to existing local files
- [ ] metadata.json contains: title, source_url, platform, fetch_date, strategy_used
