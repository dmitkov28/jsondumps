from src.sources.lobsters import get_lobsters
from src.model import Source


def _fake_feed(entries):
    def parse_fn(_url):
        return {"entries": entries}

    return parse_fn


def test_parses_entry():
    entries = [
        {
            "title": "Cool Project",
            "guid": "https://lobste.rs/s/abc123",
            "pubDate": (2026, 5, 2, 8, 0, 0, 4, 122, 0),
            "tags": [{"term": "rust"}, {"term": "programming"}],
        }
    ]
    result = get_lobsters(parser_fn=_fake_feed(entries))
    assert result == [
        Source(
            title="Cool Project",
            date=1777708800,
            url="https://lobste.rs/s/abc123",
            tags=["rust", "programming"],
        )
    ]


def test_empty_feed():
    result = get_lobsters(parser_fn=_fake_feed([]))
    assert result == []


def test_missing_tags():
    entries = [
        {
            "title": "No Tags",
            "guid": "https://lobste.rs/s/xyz",
            "pubDate": (2026, 5, 1, 0, 0, 0, 3, 121, 0),
        }
    ]
    result = get_lobsters(parser_fn=_fake_feed(entries))
    assert result[0].tags == []
