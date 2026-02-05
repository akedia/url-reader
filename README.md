# URL Reader

智能多平台内容抓取工具，支持微信公众号、小红书、Twitter/X、知乎等平台。

## 特性

- **三层降级策略**: Firecrawl → Jina → Playwright，99% 成功率
- **多平台支持**: 微信公众号、小红书、Twitter/X、知乎、抖音、B站等
- **图片处理**: 自动下载图片，支持 base64 嵌入
- **输出格式**: Markdown + HTML（自包含，可离线查看）

## 安装

```bash
# 基础依赖
pip install httpx beautifulsoup4 markdownify

# 可选：Firecrawl（提升成功率）
pip install firecrawl-py
export FIRECRAWL_API_KEY="your-key"

# 可选：Playwright（兜底方案）
pip install playwright
playwright install chromium
```

## 使用

```bash
# 基本用法
python scripts/url_reader.py "https://mp.weixin.qq.com/s/xxxxx"

# 输出 Markdown + HTML（默认嵌入 base64 图片）
python scripts/url_reader.py "URL" --format both

# 不嵌入 base64（引用本地图片路径）
python scripts/url_reader.py "URL" --format html --no-embed

# 指定输出目录
python scripts/url_reader.py "URL" --output ./articles

# 指定抓取策略
python scripts/url_reader.py "URL" --strategy playwright
```

## 输出结构

```
output/
└── 2026-02-05_文章标题/
    ├── article.md          # Markdown 正文
    ├── article.html        # HTML（含 base64 图片）
    ├── metadata.json       # 元数据
    └── images/             # 本地图片备份
```

## 支持平台

| 平台 | 域名 | 首选策略 |
|------|------|----------|
| 微信公众号 | mp.weixin.qq.com | Playwright |
| 小红书 | xiaohongshu.com | Firecrawl |
| Twitter/X | x.com | fxtwitter API |
| 知乎 | zhihu.com | Jina |
| 抖音 | douyin.com | Playwright |
| B站 | bilibili.com | Jina |
| 普通网页 | * | Jina |

## 作为 Claude Skill 使用

将此仓库作为 submodule 添加到你的 skills 目录：

```bash
cd your-workspace/skills
git submodule add https://github.com/yaoyuanchao/url-reader.git
```

然后在 Claude 中使用：
```
抓取这个公众号文章：https://mp.weixin.qq.com/s/xxxxx
```

## License

MIT
