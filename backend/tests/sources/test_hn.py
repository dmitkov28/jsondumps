from src.sources.hn import get_hn
from src.model import Source


def _fake_feed(entries):
    def parse_fn(_url):
        return {"entries": entries}

    return parse_fn


def test_parses_entry():
    entries = [
        {
            "title": "Show HN: Something",
            "guid": "https://news.ycombinator.com/item?id=123",
            "pubDate": (2026, 5, 1, 12, 0, 0, 3, 121, 0),
        }
    ]
    result = get_hn(parser_fn=_fake_feed(entries))
    assert result == [
        Source(
            title="Show HN: Something",
            date=1777636800,
            url="https://news.ycombinator.com/item?id=123",
            tags=[],
        )
    ]


def test_empty_feed():
    result = get_hn(parser_fn=_fake_feed([]))
    assert result == []


def test_missing_pubdate():
    entries = [
        {
            "title": "No Date",
            "guid": "https://example.com",
        }
    ]
    result = get_hn(parser_fn=_fake_feed(entries))
    assert result[0].date > 0
    assert result[0].title == "No Date"
