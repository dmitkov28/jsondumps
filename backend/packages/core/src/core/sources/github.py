import time

import httpx
from core.model import Source
from selectolax.parser import HTMLParser


def get_trending_repos(url: str = "https://github.com/trending") -> list[Source]:
    response = httpx.get(url)
    tree = HTMLParser(response.text)
    results = []
    for repo in tree.css("article.Box-row"):
        link = repo.css_first("h2 a")
        if not link:
            continue
        results.append(
            Source(
                title=link.text(strip=True).replace("\n", "").replace(" ", ""),
                date=int(time.time()),
                url="https://github.com" + (link.attributes.get("href") or ""),
                tags=[
                    t.text(strip=True)
                    for t in repo.css("span[itemprop='programmingLanguage']")
                ],
            )
        )
    return results
