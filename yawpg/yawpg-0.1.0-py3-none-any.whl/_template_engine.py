from pathlib import Path
from typing import Any

from bottle import template
from emoji import emojize
from markdown import markdown as generate_markdown

from ._pagetor import Page


def _content_middleware(md: str) -> str:
    md = md.strip()
    md = emojize(md)
    return md


def render_template(page: Page) -> Any:
    content = _content_middleware(page.content["content"])

    if page.content["content_type"] == "html":
        html = content
    else:
        html = generate_markdown(text=content)

    return template(
        f"{Path(__file__).parent.resolve()}/public/html/template.html",
        html=html,
        **page.dict(),
    )
