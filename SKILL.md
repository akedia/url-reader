---
name: url-reader
description: |
  Intelligent URL content fetcher with multi-platform support. Extracts article content,
  downloads images locally, and saves as Markdown/HTML.
  AUTOMATICALLY TRIGGER when user shares URLs or asks to read/fetch/extract web content.
  Supports: WeChat articles (mp.weixin.qq.com), Xiaohongshu, Twitter/X, Zhihu, Douyin,
  Bilibili, Weibo, Feishu docs, and general websites.
  Triggers: "read this URL", "fetch this article", "extract content from",
  "save this page", "download this article", "抓取这个链接", "读取这篇文章",
  "保存这个网页", "帮我抓一下", "提取内容"
---

# URL Reader

Fetch web content via CLI with automatic strategy selection and image downloading.

## Quick Start

```bash
# Basic usage
python "<skill_path>/scripts/url_reader.py" "https://mp.weixin.qq.com/s/xxxxx"

# With HTML output
python "<skill_path>/scripts/url_reader.py" "URL" --format both

# Custom output directory
python "<skill_path>/scripts/url_reader.py" "URL" --output ./articles
```

`<skill_path>` = directory containing this SKILL.md. Always use absolute path.

## Strategy Selection

Three-tier fallback: **Firecrawl** → **Jina** → **Playwright**

| Platform | Domain | Auto Strategy |
|----------|--------|---------------|
| WeChat | mp.weixin.qq.com | Playwright (JS required) |
| Xiaohongshu | xiaohongshu.com | Firecrawl |
| Twitter/X | x.com, twitter.com | fxtwitter API |
| Zhihu | zhihu.com | Jina |
| Douyin | douyin.com | Playwright |
| Bilibili | bilibili.com | Jina |
| Feishu | feishu.cn | Firecrawl |
| Others | * | Jina (default) |

Override: `--strategy firecrawl|jina|playwright|fxtwitter`

## Output Structure

```
output/
└── 2026-02-05_Article_Title/
    ├── article.md          # Markdown content
    ├── article.html        # HTML version (if --format both/html)
    ├── metadata.json       # Title, URL, platform, etc.
    └── images/
        └── img_001.jpg...  # Downloaded images
```

## Common Options

| Flag | Description |
|------|-------------|
| `--format md\|html\|both` | Output format (default: md) |
| `--output DIR` | Output directory (default: ./output) |
| `--no-images` | Skip image downloading |
| `--no-embed` | Don't embed base64 images in HTML |
| `--strategy NAME` | Force specific strategy |

## Environment Setup

```bash
# Required
pip install httpx beautifulsoup4 markdownify

# Optional: Better success rate
pip install firecrawl-py
export FIRECRAWL_API_KEY="your-key"  # https://firecrawl.dev

# Optional: JS-heavy sites fallback
pip install playwright && playwright install chromium
```

## Troubleshooting

See [references/troubleshooting.md](references/troubleshooting.md) for:
- WeChat short link format tips
- Xiaohongshu Referer handling
- Firecrawl v2 API changes

## API Usage

See [references/api.md](references/api.md) for programmatic usage.
