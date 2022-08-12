from typing import Optional

from bottle import route, run

from ._defaults import BASE_PORT, BASE_URL
from ._pagetor import pages
from ._template_engine import render_template


@route("/<page_name>")
def _paginator(page_name: str):
    for page in pages:
        if page.title.upper() == page_name.upper():
            return render_template(page)

    return "<h1>Page Not Found</h1>"


class Yawpg:
    def __init__(self) -> None:
        self.running = False

    def run(self, host: Optional[str] = None, port: Optional[int] = None):
        if not self.running:
            run(host=host or BASE_URL, port=port or BASE_PORT)
        else:
            print("Host already launched!")
