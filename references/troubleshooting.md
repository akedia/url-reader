# URL Reader Troubleshooting

## WeChat Articles (微信公众号)

### Use Short Links
- **Preferred**: `/s/xxxxx` format
- **Avoid**: Long links with `__biz=` params (trigger captcha)
- Playwright works best, Jina as fallback

### Content Not Extracted
- WeChat requires JS rendering → Playwright is mandatory
- If still fails, the article may be deleted or restricted

## Xiaohongshu (小红书)

### Images Not Downloading
- Referer header required (handled automatically)
- Some content requires login (Firecrawl may fail)
- Try `--strategy playwright` for login-required content

### Partial Content
- Video posts only extract cover image + text
- Full video download not supported

## Twitter/X

### Long Threads Not Complete
- fxtwitter API handles threads automatically
- For very long threads (50+ tweets), may truncate

### Article/Notes Support
- Twitter Notes (长文) fully supported via fxtwitter
- Includes embedded images from article content

## Firecrawl Issues

### v2 API Changes
- v2 returns Document object, not dict
- Use `getattr(result, 'markdown')` not `.get('markdown')`
- Already handled in script, but note if writing custom code

### Rate Limits
- Free tier: 500 pages/month
- Check quota at https://firecrawl.dev/dashboard

## Playwright Issues

### Chromium Not Found
```bash
playwright install chromium
```

### Timeout on Heavy Sites
- Default timeout: 60s
- For very slow sites, may need code modification
- Consider using Firecrawl instead

## General Issues

### "Content Too Short" Error
- Page may require login
- Content may be behind paywall
- Try different strategy

### Images Not Found
- Some sites use lazy loading (handled)
- Some use proprietary formats (may fail)
- Use `--no-images` to skip

### Title Extraction Wrong
- Falls back to page title if content title not found
- First `# ` heading in Markdown used as title
- Check `metadata.json` for actual extracted title
