import calendar
import time

import feedparser
from core.model import Source


def get_lobsters(url: str = "https://lobste.rs/top/1d/rss", parser_fn=feedparser.parse):
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
            tags=[tag.get("term") for tag in entry.get("tags", [])],
        )
        for entry in entries
    ]


if __name__ == "__main__":
    print(get_lobsters())
