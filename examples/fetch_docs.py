"""Fetch the Markdown version of the gpt-realtime docs page plus llms.txt.

The OpenAI developer docs serve a Markdown twin of every page when you append
'.md' to the URL, and a full index at /llms.txt. Saving both lets a coding
agent work from the current docs instead of stale memory.

Usage:
    python3 examples/fetch_docs.py
"""
import pathlib
import re
import sys
import urllib.request

PAGE = 'https://developers.openai.com/api/docs/models/gpt-realtime.md'
INDEX = 'https://developers.openai.com/llms.txt'
OUT = pathlib.Path(__file__).with_name('docs')


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={'User-Agent': 'gpt-realtime-examples/1.0'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode('utf-8', errors='replace')


def headings(markdown: str) -> list[str]:
    return re.findall(r'^#{1,3} (.+)$', markdown, flags=re.M)


def main() -> int:
    OUT.mkdir(exist_ok=True)
    for url, name in ((PAGE, 'gpt-realtime.md'), (INDEX, 'llms.txt')):
        try:
            text = fetch(url)
        except Exception as exc:  # network errors are the only expected failure
            print(f'failed {url}: {exc}')
            return 1
        (OUT / name).write_text(text, encoding='utf-8')
        print(f'saved {OUT / name} ({len(text)} chars)')
        for h in headings(text)[:20]:
            print(f'  - {h}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
