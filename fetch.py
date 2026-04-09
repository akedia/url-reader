#!/usr/bin/env python3
"""
url-reader wrapper — 修复 output 默认路径问题
原脚本 scripts/url_reader.py 默认 --output ./output，exec cwd 不固定导致落错目录。
本 wrapper 自动注入正确的 --output 路径。
"""
import sys
import os
import subprocess
from pathlib import Path

SCRIPT = Path(__file__).parent / "scripts" / "url_reader.py"
OUTPUT = Path(__file__).parent / "output"

# 如果调用方没有显式指定 --output，注入默认值
args = sys.argv[1:]
if "--output" not in args and "-o" not in args:
    args = args + ["--output", str(OUTPUT)]

result = subprocess.run([sys.executable, str(SCRIPT)] + args)
sys.exit(result.returncode)
