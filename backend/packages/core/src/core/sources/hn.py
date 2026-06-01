import calendar
import time

import feedparser
from core.model import Source


def get_hn(url: str = "https://hnrss.org/frontpage", parser_fn=feedparser.parse):
    response = parser_fn(url)
    entries = response.get("entries")
    return [
        Source(
            title=str(entry["title"]),
            date=(
                int(calendar.timegm(entry["pubDate"]))
                if entry.get("pubDate")
                else int(time.time())
            ),
            url=str(entry["guid"]),
            tags=[],
        )
        for entry in entries
    ]
