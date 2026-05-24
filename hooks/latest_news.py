"""MkDocs hook: inject latest N news posts into any page with the <!-- latest-news --> marker."""

from __future__ import annotations

import glob
import os
import re
from datetime import date, datetime

import yaml

MARKER = "<!-- latest-news -->"
N_POSTS = 5
POSTS_SUBDIR = os.path.join("news", "posts")


def on_page_markdown(markdown, *, page, config, files):
    if MARKER not in markdown:
        return markdown

    posts = _get_latest_posts(config["docs_dir"], N_POSTS)
    return markdown.replace(MARKER, _render_section(posts))


def _get_latest_posts(docs_dir: str, n: int) -> list[dict]:
    pattern = os.path.join(docs_dir, POSTS_SUBDIR, "*.md")
    posts = []
    for filepath in glob.glob(pattern):
        post = _parse_post(filepath)
        if post:
            posts.append(post)
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts[:n]


def _parse_post(filepath: str) -> dict | None:
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not fm_match:
        return None

    try:
        fm = yaml.safe_load(fm_match.group(1)) or {}
    except yaml.YAMLError:
        return None

    raw_date = fm.get("date")
    if not raw_date:
        return None
    if isinstance(raw_date, str):
        post_date = datetime.strptime(raw_date, "%Y-%m-%d").date()
    elif isinstance(raw_date, datetime):
        post_date = raw_date.date()
    elif isinstance(raw_date, date):
        post_date = raw_date
    else:
        return None

    body = content[fm_match.end() :]

    title = fm.get("title") or _extract_h1(body) or os.path.basename(filepath)
    excerpt = _extract_excerpt(body)
    url = _post_url(post_date, title)

    return {
        "date": post_date,
        "title": title,
        "excerpt": excerpt,
        "url": url,
        "categories": fm.get("categories") or [],
    }


def _extract_h1(body: str) -> str:
    m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    return m.group(1).strip() if m else ""


def _extract_excerpt(body: str) -> str:
    more = re.search(r"<!--\s*more\s*-->", body)
    raw = body[: more.start()].strip() if more else body.strip()

    # Drop heading lines, keep first substantive paragraph
    paragraphs = [p.strip() for p in raw.split("\n\n") if p.strip()]
    text = ""
    for para in paragraphs:
        if not para.startswith("#"):
            text = para
            break

    # Strip inline markdown (bold, italic, links, code)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`]{1,3}(.+?)[*_`]{1,3}", r"\1", text)

    if len(text) > 220:
        text = text[:220].rsplit(" ", 1)[0] + "…"
    return text


def _post_url(post_date: date, title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = slug.replace(" ", "-")
    return f"/news/{post_date.year}/{post_date.month:02d}/{post_date.day:02d}/{slug}/"


def _render_section(posts: list[dict]) -> str:
    if not posts:
        return "[See all news :material-arrow-right:{ .middle }](news/index.md)"

    lines = [
        "## Latest News",
        "",
        '<div class="grid cards" markdown>',
        "",
    ]

    for post in posts:
        d = post["date"]
        date_str = f"{d.strftime('%B')} {d.day}, {d.year}"
        cats = " &middot; ".join(post["categories"])
        meta = f":material-calendar: {date_str}"
        if cats:
            meta += f" &middot; {cats}"

        lines += [
            f"-   **[{post['title']}]({post['url']})**",
            "",
            "    ---",
            "",
            f"    {meta}",
        ]
        if post["excerpt"]:
            lines += [
                "",
                f"    {post['excerpt']}",
            ]
        lines.append("")

    lines += [
        "</div>",
        "",
        "[See all news :material-arrow-right:{ .middle }](news/index.md)",
    ]

    return "\n".join(lines)
