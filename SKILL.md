# URL Reader Skill

智能 URL 内容抓取工具，支持多平台内容提取，自动保存为 Markdown 并下载图片到本地。

## 核心思路：三层策略自动降级

```
Firecrawl（首选）→ Jina（备选）→ Playwright（兜底）
```

- **Firecrawl**: AI驱动，能搞定96%的网站（免费500页/月）
- **Jina**: 完全免费，大部分网站效果好
- **Playwright**: 浏览器渲染，什么都能搞

三层组合，基本能搞定99%的网站！

## 快速开始

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

# 指定策略
python3 scripts/url_reader.py "URL" --strategy firecrawl
python3 scripts/url_reader.py "URL" --strategy jina
python3 scripts/url_reader.py "URL" --strategy playwright
```

## 支持的平台

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

## 环境配置

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

## 输出结构

```
output/
└── 2026-02-05_文章标题/
    ├── article.md          # Markdown 正文
    ├── article.html        # HTML 版本（可选）
    ├── metadata.json       # 元数据（标题、URL、平台等）
    └── images/
        ├── img_001.jpg
        ├── img_002.png
        └── ...
```

## 踩坑提醒

### 1. 微信公众号
- **用短链接**：`/s/xxxxx` 格式，长链接容易触发验证码
- Firecrawl 效果最好，Jina 次之

### 2. 小红书
- 图片下载需要正确的 Referer 头（已自动处理）
- 部分内容需要登录态，Firecrawl 可能抓不到

### 3. Firecrawl v2 返回值
- v2 返回 Document 对象，用 `getattr(result, 'markdown')` 而非 `.get()`

### 4. 标题提取
- 第一行可能是元数据（"来源:xxx"），需要跳过

## 成本

| 工具 | 成本 | 限制 |
|------|------|------|
| Jina | 免费 | 无 |
| Firecrawl | 免费 | 500页/月 |
| Playwright | 免费 | 需要约200MB存储 |

**总成本: 0 元**

## API 使用示例

```python
from url_reader import fetch_url, save_content
from pathlib import Path

# 抓取
result, config = fetch_url("https://example.com/article")

if result.success:
    print(f"标题: {result.metadata['title']}")
    print(f"内容: {result.content[:200]}...")
    
    # 保存
    save_dir = save_content(
        result.content,
        result.metadata,
        Path("./output"),
        dl_images=True,
        cfg=config
    )
```

## 变现方向

- **内容采集服务**: 帮自媒体批量采集素材
- **竞品监控**: 监控竞争对手的公众号/小红书
- **数据分析**: 采集行业内容做分析报告
- **知识库建设**: 自动采集整理行业知识
