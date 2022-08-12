from typing import Dict, List

from pydantic import BaseModel

from ._defaults import BASE_URL


class Page(BaseModel):
    title: str
    content: Dict[str, str]

    def get_url(self):
        return f"{BASE_URL}/{self.title.lower()}"


pages: List[Page] = []


class Pagetor:
    def add_page(
        self,
        name: str,
        content: str,
        content_type: str = "markdown",
        replace: bool = True,
    ) -> Page:
        """Add page to site.

        Args:
            name (str): title and link (like example.com/{name})
            content (str): markdown or html content
            content_type (str, optional): must be "markdown" or "html". Defaults to "markdown".

        Returns:
            Page: _description_
        """
        new_page = Page(
            title=name,
            content={"content": content, "content_type": content_type},
        )

        if replace:
            try:
                pages.remove(new_page)
            except ValueError:
                pass

        pages.append(new_page)
        return new_page
