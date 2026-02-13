---
name: url-reader
description: >
  Multi-platform URL content fetcher with automatic fallback strategies.
  Use when user shares a URL or asks to read/fetch/extract web content.
  Supports: WeChat (微信公众号), Xiaohongshu (小红书), Twitter/X, Zhihu (知乎),
  Douyin (抖音), Bilibili (B站), Weibo (微博), Taobao, JD, Feishu (飞书),
  and any general webpage. Triggers: URL, 网页, 链接, read this page, fetch url,
  抓取, 读取网页, 打开链接, 公众号文章, 帮我看看这个链接.
  Three-layer strategy: Markdown Direct -> Firecrawl -> Jina -> Playwright (auto fallback).
  Outputs Markdown + HTML with embedded images.
---

# URL Reader Skill

智能 URL 内容抓取工具，支持多平台内容提取，自动保存为 Markdown 并下载图片到本地。

## Instructions

### Core Strategy: Four-Layer Auto Fallback

```
Markdown Direct（最快）→ Firecrawl（AI驱动）→ Jina（免费）→ Playwright（兜底）
```

- **Markdown Direct**: 直接请求 `Accept: text/markdown`，Cloudflare 等支持的站点直接返回 markdown，零额外成本，省 80% token
- **Firecrawl**: AI 驱动，能搞定 96% 的网站（免费 500 页/月）
- **Jina**: 完全免费，大部分网站效果好
- **Playwright**: 浏览器渲染，什么都能搞

### Quick Start

```bash
cd ~/clawd/skills/url-reader

# 基本用法
python3 scripts/url_reader.py "https://mp.weixin.qq.com/s/xxxxx"

# 同时输出 Markdown 和 HTML
python3 scripts/url_reader.py "URL" --format both

# 保存到指定目录
python3 scripts/url_reader.py "URL" --output ./articles

# 不下载图片
python3 scripts/url_reader.py "URL" --no-images

# HTML 中嵌入 base64 图片（离线可看）
python3 scripts/url_reader.py "URL" --format html --embed

# 不嵌入 base64（引用本地图片路径）
python3 scripts/url_reader.py "URL" --format html --no-embed

# 指定策略
python3 scripts/url_reader.py "URL" --strategy firecrawl
python3 scripts/url_reader.py "URL" --strategy jina
python3 scripts/url_reader.py "URL" --strategy playwright
```

### Supported Platforms

| 平台 | 域名 | 首选策略 | 备注 |
|------|------|----------|------|
| 微信公众号 | mp.weixin.qq.com | Firecrawl | 短链接(/s/xxx)更稳定 |
| 小红书 | xiaohongshu.com | Firecrawl | 自动处理 Referer |
| Twitter/X | x.com, twitter.com | fxtwitter | 专用 API，支持长文 |
| 知乎 | zhihu.com | Jina | 免费好用 |
| 抖音 | douyin.com | Playwright | 需要 JS 渲染 |
| B站 | bilibili.com | Jina | 支持文章 |
| 微博 | weibo.com | Jina | |
| 淘宝/天猫 | taobao.com | Playwright | 需要登录态 |
| 京东 | jd.com | Playwright | |
| 飞书文档 | feishu.cn | Firecrawl | |
| 普通网页 | * | Jina | 默认 |

### Environment Setup

```bash
# 必需：基础依赖
pip install httpx beautifulsoup4 markdownify

# 可选：Firecrawl（提升成功率）
pip install firecrawl-py
export FIRECRAWL_API_KEY="your-key"  # 获取: https://firecrawl.dev

# 可选：Playwright（兜底方案）
pip install playwright
playwright install chromium
```

### Output Structure

```
output/
└── 2026-02-05_文章标题/
    ├── article.md          # Markdown 正文
    ├── article.html        # HTML 版本（可选）
    ├── metadata.json       # 元数据（标题、URL、平台等）
    └── images/
        ├── img_001.jpg
        └── ...
```

### API Usage

```python
from url_reader import fetch_url, save_content
from pathlib import Path

result, config = fetch_url("https://example.com/article")
if result.success:
    print(f"标题: {result.metadata['title']}")
    save_dir = save_content(
        result.content, result.metadata,
        Path("./output"), dl_images=True, cfg=config
    )
```

## Examples

```bash
# 微信公众号
python3 scripts/url_reader.py "https://mp.weixin.qq.com/s/xxxxx" --format both

# Twitter/X 长文
python3 scripts/url_reader.py "https://x.com/user/status/123" --output ./articles

# 知乎问题
python3 scripts/url_reader.py "https://www.zhihu.com/question/xxx" --no-images

# 小红书笔记
python3 scripts/url_reader.py "https://www.xiaohongshu.com/explore/xxx"
```

## Troubleshooting

### 微信公众号
- **用短链接**：`/s/xxxxx` 格式，长链接容易触发验证码
- Firecrawl 效果最好，Jina 次之

### 小红书
- 图片下载需要正确的 Referer 头（已自动处理）
- 部分内容需要登录态，Firecrawl 可能抓不到

### Firecrawl v2 返回值
- v2 返回 Document 对象，用 `getattr(result, 'markdown')` 而非 `.get()`

### 标题提取
- 第一行可能是元数据（"来源:xxx"），需要跳过

### Cost

| 工具 | 成本 | 限制 |
|------|------|------|
| Jina | 免费 | 无 |
| Firecrawl | 免费 | 500页/月 |
| Playwright | 免费 | 需要约200MB存储 |
