import calendar
import time
from typing import Any

from core.model import Source

import feedparser


def get_ars_technica(
    parse_fn=feedparser.parse,
    url: str = "https://feeds.arstechnica.com/arstechnica/index",
) -> list[Source]:
    response: feedparser.FeedParserDict = parse_fn(url)
    entries: list[dict[str, Any]] = response.get("entries", [])  # type: ignore
    return [
        Source(
            title=str(entry["title"]),
            date=(
                int(calendar.timegm(entry["published_parsed"]))
                if entry.get("published_parsed")
                else int(time.time())
            ),
            url=str(entry["link"]),
            tags=[str(tag["term"]) for tag in entry.get("tags", [])],
        )
        for entry in entries
    ]
