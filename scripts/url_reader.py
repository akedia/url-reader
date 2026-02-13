#!/usr/bin/env python3
"""
URL Reader - 智能多平台内容抓取工具

三层降级策略: Firecrawl → Jina → Playwright
"""

import os
import re
import sys
import json
import base64
import asyncio
import urllib.request
import urllib.parse
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple, Dict, List
from dataclasses import dataclass


# ============ 平台配置 ============

@dataclass
class PlatformConfig:
    name: str
    patterns: List[str]
    preferred_strategy: str = 'jina'
    user_agent: str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    referer: str = ''
    needs_js: bool = False
    wait_time: int = 2000


PLATFORMS = {
    'wechat': PlatformConfig(
        name='微信公众号', patterns=[r'mp\.weixin\.qq\.com'],
        preferred_strategy='playwright',  # 微信必须用 playwright
        user_agent='Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 MicroMessenger/8.0',
        referer='https://mp.weixin.qq.com/', needs_js=True
    ),
    'xiaohongshu': PlatformConfig(
        name='小红书', patterns=[r'xiaohongshu\.com', r'xhslink\.com'],
        preferred_strategy='firecrawl',
        referer='https://www.xiaohongshu.com/', needs_js=True
    ),
    'twitter': PlatformConfig(
        name='Twitter/X', patterns=[r'twitter\.com', r'x\.com'],
        preferred_strategy='fxtwitter'
    ),
    'zhihu': PlatformConfig(
        name='知乎', patterns=[r'zhihu\.com'],
        preferred_strategy='jina', referer='https://www.zhihu.com/'
    ),
    'douyin': PlatformConfig(
        name='抖音', patterns=[r'douyin\.com'],
        preferred_strategy='playwright', needs_js=True, wait_time=3000
    ),
    'bilibili': PlatformConfig(
        name='B站', patterns=[r'bilibili\.com', r'b23\.tv'],
        preferred_strategy='jina', referer='https://www.bilibili.com/'
    ),
    'weibo': PlatformConfig(
        name='微博', patterns=[r'weibo\.com', r'weibo\.cn'],
        preferred_strategy='jina', referer='https://weibo.com/'
    ),
    'taobao': PlatformConfig(
        name='淘宝', patterns=[r'taobao\.com', r'tmall\.com'],
        preferred_strategy='playwright', needs_js=True
    ),
    'jd': PlatformConfig(
        name='京东', patterns=[r'jd\.com'],
        preferred_strategy='playwright', needs_js=True
    ),
    'feishu': PlatformConfig(
        name='飞书', patterns=[r'feishu\.cn'],
        preferred_strategy='firecrawl', needs_js=True,
        referer='https://www.feishu.cn/'
    ),
}


def identify_platform(url: str) -> Tuple[str, PlatformConfig]:
    for pid, cfg in PLATFORMS.items():
        for p in cfg.patterns:
            if re.search(p, url, re.I):
                return pid, cfg
    return 'generic', PlatformConfig(name='通用', patterns=[], preferred_strategy='jina')


# ============ 抓取策略 ============

class FetchResult:
    def __init__(self, content='', metadata=None, success=False, error=''):
        self.content = content
        self.metadata = metadata or {}
        self.success = success
        self.error = error


def fetch_fxtwitter(url: str) -> FetchResult:
    """Twitter/X 专用 API"""
    match = re.search(r'(?:twitter|x)\.com/(\w+)/status/(\d+)', url)
    if not match:
        return FetchResult(error="无效推文URL")
    
    user, sid = match.groups()
    api = f"https://api.fxtwitter.com/{user}/status/{sid}"
    
    try:
        req = urllib.request.Request(api, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode())
        
        if data.get('code') != 200:
            return FetchResult(error=data.get('message', '失败'))
        
        tweet = data.get('tweet', {})
        author = tweet.get('author', {})
        article = tweet.get('article', {})
        images = []
        
        if article:
            title = article.get('title', '')
            blocks = article.get('content', {}).get('blocks', [])
            parts = [f"# {title}\n"]
            
            for b in blocks:
                text = b.get('text', '').strip()
                bt = b.get('type', 'unstyled')
                if bt == 'header-two':
                    parts.append(f"\n## {text}\n")
                elif bt == 'blockquote':
                    parts.append(f"\n> {text}\n")
                elif bt in ('unordered-list-item',):
                    parts.append(f"- {text}")
                elif bt in ('ordered-list-item',):
                    parts.append(f"1. {text}")
                elif text:
                    parts.append(f"\n{text}\n")
            
            for m in article.get('media_entities', []):
                img = m.get('media_info', {}).get('original_img_url', '')
                if img:
                    images.append(img)
            
            content = '\n'.join(parts)
        else:
            title = tweet.get('text', '')[:50]
            content = tweet.get('text', '')
        
        return FetchResult(
            content=content, success=True,
            metadata={
                'title': title, 'author': author.get('name', ''),
                'url': url, 'platform': 'twitter', 'images': images,
                'stats': {'views': tweet.get('views', 0), 'likes': tweet.get('likes', 0)}
            }
        )
    except Exception as e:
        return FetchResult(error=str(e))


def fetch_markdown_direct(url: str) -> FetchResult:
    """直接请求 markdown (Cloudflare Markdown for Agents 等支持 Accept: text/markdown 的站点)"""
    headers = {
        'Accept': 'text/markdown, text/html;q=0.9',
        'User-Agent': 'Mozilla/5.0 (compatible; AgentFetch/1.0)'
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as r:
            ct = r.headers.get('Content-Type', '')
            if 'markdown' not in ct:
                return FetchResult(error="站点未返回 markdown")
            content = r.read().decode('utf-8')

        if len(content) < 50:
            return FetchResult(error="内容太短")

        token_count = None
        # Cloudflare 返回 x-markdown-tokens header
        try:
            token_count = r.headers.get('x-markdown-tokens')
        except:
            pass

        title = 'Untitled'
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('# '):
                title = line[2:].strip()
                break
            elif line.startswith('title:'):
                title = line[6:].strip()
                break

        images = re.findall(r'!\[.*?\]\((https?://[^\)]+)\)', content)
        meta = {'title': title, 'url': url, 'platform': 'markdown-direct', 'images': list(set(images))[:30]}
        if token_count:
            meta['token_count'] = token_count

        return FetchResult(
            content=content, success=True, metadata=meta
        )
    except Exception as e:
        return FetchResult(error=str(e))


def fetch_jina(url: str) -> FetchResult:
    """Jina Reader - 免费"""
    jina_url = f"https://r.jina.ai/{url}"
    headers = {'Accept': 'text/markdown', 'User-Agent': 'Mozilla/5.0'}
    
    try:
        req = urllib.request.Request(jina_url, headers=headers)
        with urllib.request.urlopen(req, timeout=60) as r:
            content = r.read().decode('utf-8')
        
        if len(content) < 50:
            return FetchResult(error="内容太短")
        
        # 提取标题
        title = 'Untitled'
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('Title:'):
                title = line[6:].strip()
                break
            elif line.startswith('# '):
                title = line[2:].strip()
                break
        
        images = re.findall(r'!\[.*?\]\((https?://[^\)]+)\)', content)
        images += re.findall(r'(https?://\S+\.(?:jpg|jpeg|png|gif|webp))', content, re.I)
        
        return FetchResult(
            content=content, success=True,
            metadata={'title': title, 'url': url, 'platform': identify_platform(url)[0], 'images': list(set(images))[:30]}
        )
    except Exception as e:
        return FetchResult(error=str(e))


def fetch_firecrawl(url: str) -> FetchResult:
    """Firecrawl - AI驱动"""
    api_key = os.environ.get('FIRECRAWL_API_KEY')
    if not api_key:
        return FetchResult(error="未设置 FIRECRAWL_API_KEY")
    
    try:
        from firecrawl import FirecrawlApp
        app = FirecrawlApp(api_key=api_key)
        result = app.scrape(url)
        
        content = getattr(result, 'markdown', '') or ''
        if len(content) < 100:
            return FetchResult(error="内容太短")
        
        title_match = re.search(r'^#\s+(.+)$', content, re.M)
        title = title_match.group(1).strip() if title_match else 'Untitled'
        
        images = re.findall(r'!\[.*?\]\((https?://[^\)]+)\)', content)
        if hasattr(result, 'images') and result.images:
            images.extend(result.images)
        
        return FetchResult(
            content=content, success=True,
            metadata={'title': title, 'url': url, 'platform': identify_platform(url)[0], 'images': list(set(images))[:30]}
        )
    except ImportError:
        return FetchResult(error="未安装 firecrawl-py")
    except Exception as e:
        return FetchResult(error=str(e))


async def fetch_playwright(url: str, cfg: PlatformConfig) -> FetchResult:
    """Playwright - 浏览器渲染"""
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        return FetchResult(error="未安装 playwright")
    
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            ctx = await browser.new_context(user_agent=cfg.user_agent)
            page = await ctx.new_page()
            
            if cfg.referer:
                await page.set_extra_http_headers({'Referer': cfg.referer})
            
            await page.goto(url, wait_until='networkidle', timeout=60000)
            await page.wait_for_timeout(cfg.wait_time)
            
            html = await page.content()
            title = await page.title()
            await browser.close()
        
        # 转 Markdown
        try:
            from bs4 import BeautifulSoup
            import markdownify
            
            soup = BeautifulSoup(html, 'html.parser')
            for t in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                t.decompose()
            
            # 提取标题 - 优先从 h1 或 og:title
            if not title or title == '微信公众平台':
                og_title = soup.find('meta', property='og:title')
                if og_title:
                    title = og_title.get('content', '')
                if not title:
                    h1 = soup.find('h1')
                    if h1:
                        title = h1.get_text(strip=True)
            
            # 处理懒加载图片：把 data-src 复制到 src
            for img in soup.find_all('img'):
                data_src = img.get('data-src')
                if data_src and data_src.startswith('http'):
                    img['src'] = data_src
                # 移除 SVG 占位符
                src = img.get('src', '')
                if 'svg+xml' in src or '1px' in src or not src:
                    img.decompose()
            
            for sel in ['article', '.article', '.content', '.post-content', '.rich_media_content', '#js_content', 'main']:
                elem = soup.select_one(sel)
                if elem and len(elem.get_text(strip=True)) > 100:
                    content = markdownify.markdownify(str(elem))
                    break
            else:
                content = markdownify.markdownify(str(soup.body or soup))
            
            # 提取图片 - 包括 data-src
            images = []
            for img in soup.find_all('img'):
                src = img.get('data-src') or img.get('src') or ''
                if src and src.startswith('http') and 'svg' not in src and '1px' not in src:
                    images.append(src)
            
        except ImportError:
            content = html
            images = []
        
        # 清理标题
        if title:
            title = re.sub(r'\s*\|\s*.*$', '', title)  # 去掉 | 后面的部分
        
        return FetchResult(
            content=content.strip(), success=True,
            metadata={'title': title, 'url': url, 'platform': identify_platform(url)[0], 'images': images[:30]}
        )
    except Exception as e:
        return FetchResult(error=str(e))


# ============ 图片下载 ============

def download_image(url: str, cfg: PlatformConfig) -> Tuple[Optional[bytes], str]:
    proxy_url = f"https://wsrv.nl/?url={urllib.parse.quote(url, safe='')}"
    headers = {'User-Agent': cfg.user_agent}
    if cfg.referer:
        headers['Referer'] = cfg.referer
    
    try:
        req = urllib.request.Request(proxy_url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
            ct = r.headers.get('Content-Type', 'image/jpeg')
        
        ext = '.jpg'
        for k, v in {'png': '.png', 'gif': '.gif', 'webp': '.webp'}.items():
            if k in ct.lower():
                ext = v
                break
        return data, ext
    except:
        return None, '.jpg'


def img_to_b64(data: bytes, ext: str) -> str:
    mime = {'.jpg': 'image/jpeg', '.png': 'image/png', '.gif': 'image/gif', '.webp': 'image/webp'}.get(ext, 'image/jpeg')
    return f"data:{mime};base64,{base64.b64encode(data).decode()}"


# ============ 保存 ============

def extract_title(content: str, meta_title: str) -> str:
    """从内容中提取标题"""
    if meta_title and meta_title != 'Untitled' and len(meta_title) > 2:
        return meta_title
    
    # 从 Markdown 中提取
    for line in content.split('\n')[:20]:
        line = line.strip()
        # # 标题
        if line.startswith('# '):
            return line[2:].strip()
        # === 下划线标题
        if line and not line.startswith(('!', '[', 'http', '*', '-', '>')):
            next_lines = content.split('\n')
            idx = next_lines.index(line) if line in next_lines else -1
            if idx >= 0 and idx + 1 < len(next_lines):
                next_line = next_lines[idx + 1].strip()
                if next_line.startswith('==='):
                    return line
    
    return meta_title or 'Untitled'


def save_content(content: str, meta: Dict, outdir: Path, dl_images: bool, cfg: PlatformConfig) -> Tuple[Path, Dict]:
    """保存内容，返回 (保存目录, 图片映射)"""
    
    # 提取标题
    title = extract_title(content, meta.get('title', ''))
    meta['title'] = title
    
    safe = re.sub(r'[^\w\u4e00-\u9fff\-]', '_', title)[:50].strip('_') or 'article'
    date = datetime.now().strftime('%Y-%m-%d')
    
    save_dir = outdir / f"{date}_{safe}"
    save_dir.mkdir(parents=True, exist_ok=True)
    
    img_map = {}  # url -> local_path
    img_data = {}  # url -> (bytes, ext)
    if dl_images and meta.get('images'):
        img_dir = save_dir / 'images'
        img_dir.mkdir(exist_ok=True)
        
        total = len(meta['images'])
        print(f"下载图片 ({total} 张)...")
        for i, url in enumerate(meta['images']):
            if not url or not url.startswith('http'):
                continue
            data, ext = download_image(url, cfg)
            if data:
                name = f"img_{i+1:03d}{ext}"
                (img_dir / name).write_bytes(data)
                img_map[url] = f"images/{name}"
                img_data[url] = (data, ext)
                print(f"  [{i+1}/{total}] {name}")
    
    # 替换图片路径后保存 Markdown
    md_content = content
    for orig, local in img_map.items():
        md_content = md_content.replace(orig, local)
    
    (save_dir / 'article.md').write_text(md_content, encoding='utf-8')
    meta['saved_at'] = datetime.now().isoformat()
    meta['local_images'] = len(img_map)
    (save_dir / 'metadata.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2))
    
    return save_dir, img_map, img_data


def gen_html(content: str, meta: Dict, img_map: Dict, img_data: Dict, embed: bool, cfg: PlatformConfig) -> str:
    """生成 HTML，embed=True 时嵌入 base64 图片"""
    
    title = meta.get('title', 'Untitled')
    
    h = content
    
    # 清理 Markdown
    # 移除 === 和 --- 标题下划线
    h = re.sub(r'^={3,}$', '', h, flags=re.M)
    h = re.sub(r'^-{3,}$', '', h, flags=re.M)
    
    # 标题转换
    h = re.sub(r'^### (.+)$', r'<h3>\1</h3>', h, flags=re.M)
    h = re.sub(r'^## (.+)$', r'<h2>\1</h2>', h, flags=re.M)
    h = re.sub(r'^# (.+)$', r'<h1>\1</h1>', h, flags=re.M)
    
    # 粗体
    h = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', h)
    
    # 引用
    h = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', h, flags=re.M)
    
    # 图片 - 处理本地和远程
    def repl_img(m):
        alt, src = m.group(1), m.group(2)
        # 跳过空图片和 SVG 占位符
        if not src or 'svg+xml' in src or src == '()':
            return ''
        
        if embed:
            # 优先用已下载的图片数据
            if src in img_data:
                data, ext = img_data[src]
                src = img_to_b64(data, ext)
            elif src.startswith('http'):
                # 没下载过的远程图片，现场下载
                data, ext = download_image(src, cfg)
                if data:
                    src = img_to_b64(data, ext)
        else:
            # 不嵌入时，用本地路径
            if src in img_map:
                src = img_map[src]
        
        return f'<figure><img src="{src}" alt="{alt}"></figure>'
    
    h = re.sub(r'!\[([^\]]*)\]\(([^\)]*)\)', repl_img, h)
    
    # 移除空的图片标记
    h = re.sub(r'!\[\]\(\)', '', h)
    
    # 链接
    h = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2" target="_blank">\1</a>', h)
    
    # 处理表格 (简单处理)
    h = re.sub(r'\|[^\n]+\|', lambda m: f'<p>{m.group(0)}</p>', h)
    
    # 段落处理
    lines = []
    for ln in h.split('\n'):
        ln = ln.strip()
        if not ln:
            continue
        if ln.startswith('- '):
            lines.append(f'<li>{ln[2:]}</li>')
        elif ln.startswith(('<h', '<p', '<figure', '<blockquote', '<li', '<strong', '<a ')):
            lines.append(ln)
        elif ln.startswith('|'):
            continue  # 跳过表格分隔行
        elif ln == '---' or ln.startswith('==='):
            continue
        else:
            lines.append(f'<p>{ln}</p>')
    
    h = '\n'.join(lines)
    
    # 清理多余空标签
    h = re.sub(r'<p>\s*</p>', '', h)
    h = re.sub(r'<figure>\s*</figure>', '', h)
    
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'PingFang SC',sans-serif;line-height:1.8;color:#333;background:#f5f5f5}}
.container{{max-width:800px;margin:0 auto;padding:40px 20px}}
.header{{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;padding:50px 40px;border-radius:16px;margin-bottom:30px;text-align:center}}
.header h1{{font-size:1.6em;margin-bottom:10px}}
.header .meta{{opacity:0.9;font-size:0.9em}}
.content{{background:#fff;padding:40px;border-radius:16px;box-shadow:0 2px 20px rgba(0,0,0,.05)}}
h1,h2,h3{{margin:30px 0 15px}}
h2{{font-size:1.4em;color:#667eea;border-bottom:2px solid #eee;padding-bottom:10px}}
h3{{font-size:1.2em;color:#555}}
p{{margin-bottom:16px;text-align:justify}}
blockquote{{background:#f8f9fa;border-left:4px solid #667eea;padding:15px 20px;margin:20px 0;border-radius:0 8px 8px 0}}
figure{{margin:25px 0;text-align:center}}
figure img{{max-width:100%;border-radius:8px;box-shadow:0 4px 15px rgba(0,0,0,.1)}}
ul,ol{{margin:16px 0;padding-left:24px}}
li{{margin-bottom:8px}}
a{{color:#667eea;text-decoration:none}}
a:hover{{text-decoration:underline}}
.footer{{text-align:center;margin-top:30px;color:#666;font-size:.9em}}
</style>
</head>
<body>
<div class="container">
<div class="header">
<h1>{title}</h1>
<p class="meta">{meta.get('platform', '')} | {meta.get('author', '')}</p>
</div>
<div class="content">{h}</div>
<div class="footer"><a href="{meta.get('url', '')}" target="_blank">查看原文</a></div>
</div>
</body>
</html>'''


# ============ 主函数 ============

def fetch_url(url: str, strategy: str = 'auto') -> Tuple[FetchResult, PlatformConfig]:
    pid, cfg = identify_platform(url)
    print(f"平台: {cfg.name}")
    
    if strategy == 'auto':
        strats = []
        if pid == 'twitter':
            strats = ['fxtwitter', 'jina']
        elif cfg.preferred_strategy == 'firecrawl':
            strats = ['firecrawl', 'jina', 'playwright']
        elif cfg.preferred_strategy == 'playwright':
            strats = ['playwright', 'jina', 'firecrawl']
        else:
            strats = ['markdown-direct', 'jina', 'firecrawl', 'playwright']
    else:
        strats = [strategy]
    
    for s in strats:
        print(f"尝试: {s}")
        if s == 'fxtwitter':
            r = fetch_fxtwitter(url)
        elif s == 'markdown-direct':
            r = fetch_markdown_direct(url)
        elif s == 'jina':
            r = fetch_jina(url)
        elif s == 'firecrawl':
            r = fetch_firecrawl(url)
        elif s == 'playwright':
            r = asyncio.run(fetch_playwright(url, cfg))
        else:
            continue
        
        if r.success:
            print(f"  成功!")
            return r, cfg
        else:
            print(f"  失败: {r.error}")
    
    return FetchResult(error="所有策略均失败"), cfg


def main():
    import argparse
    
    p = argparse.ArgumentParser(description='智能URL内容抓取')
    p.add_argument('url', help='URL')
    p.add_argument('--output', '-o', default='./output', help='输出目录')
    p.add_argument('--format', '-f', choices=['md', 'html', 'both'], default='md')
    p.add_argument('--strategy', '-s', choices=['auto', 'firecrawl', 'jina', 'playwright', 'fxtwitter'], default='auto')
    p.add_argument('--no-images', action='store_true', help='不下载图片')
    p.add_argument('--embed', action='store_true', default=True, help='HTML嵌入base64图片（默认开启）')
    p.add_argument('--no-embed', action='store_true', help='不嵌入base64图片')
    
    args = p.parse_args()
    
    print(f"URL: {args.url}\n")
    
    result, cfg = fetch_url(args.url, args.strategy)
    
    if not result.success:
        print(f"\n抓取失败: {result.error}")
        sys.exit(1)
    
    print(f"\n标题: {result.metadata.get('title', 'Unknown')}")
    print(f"图片: {len(result.metadata.get('images', []))} 张")
    
    outdir = Path(args.output)
    save_dir, img_map, img_data = save_content(result.content, result.metadata, outdir, not args.no_images, cfg)
    
    if args.format in ('html', 'both'):
        print("\n生成 HTML...")
        embed = args.embed and not args.no_embed
        html = gen_html(result.content, result.metadata, img_map, img_data, embed, cfg)
        (save_dir / 'article.html').write_text(html, encoding='utf-8')
    
    print(f"\n完成! 保存到: {save_dir}")
    return str(save_dir)


if __name__ == '__main__':
    main()
