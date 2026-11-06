#!/usr/bin/env python3
"""One-time conversion of the GitBook sync repo into Starlight pages."""

from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path

import yaml

SOURCE = Path("/home/lucio/repos/metapool/gitbook-sync")
DEST = Path("/home/lucio/repos/metapool/docs-metapool-app")
DOCS = DEST / "src" / "content" / "docs"
ASSETS = DEST / "public" / "assets"

HINT_TYPES = {
    "info": "note",
    "warning": "caution",
    "danger": "danger",
    "success": "tip",
}
ASSET_RE = re.compile(
    r"(?:\./|\.\./)*\.gitbook/assets/(.+?\.(?:png|jpe?g|gif|svg|webp|pdf))",
    re.IGNORECASE,
)
CODE_RE = re.compile(r"```.*?```|~~~.*?~~~|`[^`\n]+`", re.DOTALL)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
HINT_RE = re.compile(
    r"\{%\s*hint\s+style=\"([^\"]+)\"\s*%\}(.*?)\{%\s*endhint\s*%\}",
    re.DOTALL,
)
FILE_RE = re.compile(r"\{%\s*file\s+src=\"([^\"]+)\"\s*%\}")
EMBED_RE = re.compile(r"\{%\s*embed\s+url=\"([^\"]+)\"\s*%\}")
CONTENT_REF_RE = re.compile(
    r"\{%\s*content-ref\s+url=\"[^\"]*\"\s*%\}(.*?)\{%\s*endcontent-ref\s*%\}",
    re.DOTALL,
)
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)


def asset_url(raw: str) -> str:
    name = raw.split("/")[-1].strip()
    return "/assets/" + quote_path(name)


def quote_path(name: str) -> str:
    from urllib.parse import quote

    return quote(name, safe="")


def rewrite_assets(text: str) -> str:
    return ASSET_RE.sub(lambda match: asset_url(match.group(1)), text)


def rewrite_readme_links(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        label, url = match.group(1), match.group(2)
        if url.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        url = re.sub(r"(^|/)README\.md(?=#|$)", r"\1index.md", url)
        return f"[{label}]({url})"

    return MD_LINK_RE.sub(repl, text)


def transform_body(text: str) -> tuple[str, bool]:
    text = CONTENT_REF_RE.sub(lambda match: match.group(1).strip(), text)
    text = FILE_RE.sub(
        lambda match: f"[{Path(match.group(1)).name}]({asset_url(match.group(1))})",
        text,
    )
    text = EMBED_RE.sub(lambda match: f"[{match.group(1)}]({match.group(1)})", text)
    text = rewrite_assets(text)
    text = re.sub(r"\(<(/assets/[^>]+)>\)", r"(\1)", text)
    text = re.sub(r'"(</assets/[^>]+)>"', r'"\1"', text)
    text = rewrite_readme_links(text)

    used_aside = False

    def hint_repl(match: re.Match[str]) -> str:
        nonlocal used_aside
        used_aside = True
        kind = HINT_TYPES.get(match.group(1).strip(), "note")
        inner = match.group(2).strip("\n")
        return f'\n<Aside type="{kind}">\n\n{inner}\n\n</Aside>\n'

    text = HINT_RE.sub(hint_repl, text)
    return text, used_aside


def escape_mdx(text: str) -> str:
    def escape_prose(chunk: str) -> str:
        chunk = chunk.replace("{", "&#123;").replace("}", "&#125;")
        chunk = re.sub(r"<(?![A-Za-z/!?])", "&lt;", chunk)
        chunk = re.sub(r"<br\s*/?>", "<br />", chunk, flags=re.IGNORECASE)
        chunk = re.sub(r"<hr\s*/?>", "<hr />", chunk, flags=re.IGNORECASE)

        def close_img(match: re.Match[str]) -> str:
            tag = match.group(0)
            if tag.rstrip().endswith("/>"):
                return tag
            return tag[:-1].rstrip() + " />"

        return IMG_RE.sub(close_img, chunk)

    pieces: list[str] = []
    last = 0
    for match in CODE_RE.finditer(text):
        pieces.append(escape_prose(text[last : match.start()]))
        pieces.append(match.group(0))
        last = match.end()
    pieces.append(escape_prose(text[last:]))
    return "".join(pieces)


def split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        data = {}
    return data, body


def page_title(body: str, fallback: str) -> tuple[str, str]:
    match = H1_RE.search(body)
    if not match:
        return fallback, body
    title = html.unescape(re.sub(r"<[^>]+>", "", match.group(1))).strip()
    body = (body[: match.start()] + body[match.end() :]).lstrip("\n")
    return title or fallback, body


def dest_for(relative: str, mdx: bool) -> Path:
    if relative == "README.md":
        stem = "index"
    elif relative.endswith("/README.md"):
        stem = relative[: -len("README.md")] + "index"
    else:
        stem = relative[: -len(".md")]
    return DOCS / f"{stem}.{'mdx' if mdx else 'md'}"


def href_to_entry(label: str, href: str) -> dict:
    if href.startswith(("http://", "https://")):
        return {"label": label, "link": href, "attrs": {"target": "_blank"}}
    path = href.split("#", 1)[0]
    if path == "README.md":
        slug = ""
    elif path.endswith("/README.md"):
        slug = path[: -len("/README.md")]
    else:
        slug = path[: -len(".md")] if path.endswith(".md") else path
    if slug == "":
        return {"label": label, "link": "/"}
    return {"label": label, "slug": slug}


def parse_summary(text: str) -> list[dict]:
    sections: list[dict] = []
    current: dict | None = None
    stack: list[tuple[int, dict]] = []
    for line in text.splitlines():
        if line.startswith("## "):
            current = {"label": html.unescape(line[3:].strip()), "items": []}
            sections.append(current)
            stack = [(-1, current)]
            continue
        match = re.match(r"^(\s*)\* \[(.*?)\]\((.*?)\)\s*$", line)
        if not match or current is None:
            continue
        indent = len(match.group(1).expandtabs(2))
        node = {
            "label": html.unescape(match.group(2).strip()),
            "href": match.group(3).strip(),
            "items": [],
        }
        while len(stack) > 1 and stack[-1][0] >= indent:
            stack.pop()
        stack[-1][1]["items"].append(node)
        stack.append((indent, node))
    return sections


def sidebar_node(node: dict) -> dict:
    children = [sidebar_node(child) for child in node["items"]]
    entry = href_to_entry(node["label"], node["href"])
    if not children:
        return entry
    return {"label": node["label"], "items": [entry, *children]}


def dump_frontmatter(data: dict) -> str:
    rendered = yaml.safe_dump(
        data,
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ).strip()
    return f"---\n{rendered}\n---\n\n"


def main() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    if ASSETS.exists():
        shutil.rmtree(ASSETS)
    DOCS.mkdir(parents=True)
    shutil.copytree(SOURCE / ".gitbook" / "assets", ASSETS)

    labels: dict[str, str] = {}
    summary = (SOURCE / "SUMMARY.md").read_text(encoding="utf-8")
    for section in parse_summary(summary):
        def walk(node: dict) -> None:
            href = node["href"]
            if not href.startswith("http"):
                labels[href.split("#", 1)[0]] = node["label"]
            for child in node["items"]:
                walk(child)

        for item in section["items"]:
            walk(item)

    pages = 0
    aside_pages = 0
    for path in sorted(SOURCE.rglob("*.md")):
        relative = path.relative_to(SOURCE).as_posix()
        if relative == "SUMMARY.md" or relative.startswith(".gitbook/"):
            continue
        raw = path.read_text(encoding="utf-8")
        meta, body = split_frontmatter(raw)
        fallback = labels.get(relative) or path.stem
        title, body = page_title(body, fallback)
        body, used_aside = transform_body(body)
        if used_aside:
            body = escape_mdx(body)
            body = "import { Aside } from '@astrojs/starlight/components';\n\n" + body
            aside_pages += 1
        front = {"title": title}
        description = meta.get("description")
        if isinstance(description, str) and description.strip():
            front["description"] = description.strip()
        out = dest_for(relative, used_aside)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(dump_frontmatter(front) + body.lstrip("\n"), encoding="utf-8")
        pages += 1

    sidebar = [
        {"label": section["label"], "items": [sidebar_node(item) for item in section["items"]]}
        for section in parse_summary(summary)
        if section["items"]
    ]
    sidebar_path = DEST / "sidebar.mjs"
    sidebar_path.write_text(
        "export default " + json.dumps(sidebar, ensure_ascii=False, indent=2) + ";\n",
        encoding="utf-8",
    )
    leftovers = []
    for path in DOCS.rglob("*"):
        if path.is_file() and "{%" in path.read_text(encoding="utf-8"):
            leftovers.append(path.relative_to(DEST).as_posix())
    if leftovers:
        raise SystemExit("GitBook tags remain:\n" + "\n".join(leftovers))
    print(f"pages {pages}, aside pages {aside_pages}, sidebar groups {len(sidebar)}")


if __name__ == "__main__":
    main()
