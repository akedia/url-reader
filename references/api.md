# URL Reader API Reference

## Programmatic Usage

```python
from url_reader import fetch_url, save_content
from pathlib import Path

# Fetch content
result, config = fetch_url("https://example.com/article")

if result.success:
    print(f"Title: {result.metadata['title']}")
    print(f"Content: {result.content[:200]}...")

    # Save to disk
    save_dir, img_map, img_data = save_content(
        result.content,
        result.metadata,
        Path("./output"),
        dl_images=True,
        cfg=config
    )
```

## Core Classes

### FetchResult
```python
class FetchResult:
    content: str      # Markdown content
    metadata: dict    # {title, url, platform, images, ...}
    success: bool     # True if fetch succeeded
    error: str        # Error message if failed
```

### PlatformConfig
```python
@dataclass
class PlatformConfig:
    name: str                    # Display name
    patterns: List[str]          # URL regex patterns
    preferred_strategy: str      # 'jina', 'firecrawl', 'playwright'
    user_agent: str             # Custom UA string
    referer: str                # Required referer header
    needs_js: bool              # Requires JS rendering
    wait_time: int              # Playwright wait ms
```

## Functions

### fetch_url(url, strategy='auto')
Fetch content from URL using specified or auto-selected strategy.

Returns: `Tuple[FetchResult, PlatformConfig]`

### save_content(content, meta, outdir, dl_images, cfg)
Save content to disk with optional image downloading.

Returns: `Tuple[Path, Dict, Dict]` (save_dir, img_map, img_data)

### gen_html(content, meta, img_map, img_data, embed, cfg)
Generate styled HTML from Markdown content.

Returns: `str` (HTML content)

## Strategy Functions

| Function | Description |
|----------|-------------|
| `fetch_jina(url)` | Jina Reader API (free) |
| `fetch_firecrawl(url)` | Firecrawl API (AI-powered) |
| `fetch_playwright(url, cfg)` | Browser rendering (async) |
| `fetch_fxtwitter(url)` | Twitter/X specialized API |

## Environment Variables

| Variable | Description |
|----------|-------------|
| `FIRECRAWL_API_KEY` | Firecrawl API key (optional) |
