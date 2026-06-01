from src.sources.ars_technica import get_ars_technica
from src.model import Source


def _fake_feed(entries):
    def parse_fn(_url):
        return {"entries": entries}

    return parse_fn


def test_parses_entry():
    entries = [
        {
            "title": "Test Article",
            "link": "https://example.com/article",
            "published_parsed": (2026, 5, 1, 12, 0, 0, 3, 121, 0),
            "tags": [{"term": "AI"}, {"term": "Science"}],
        }
    ]
    result = get_ars_technica(parse_fn=_fake_feed(entries))
    assert result == [
        Source(
            title="Test Article",
            date=1777636800,
            url="https://example.com/article",
            tags=["AI", "Science"],
        )
    ]


def test_empty_feed():
    result = get_ars_technica(parse_fn=_fake_feed([]))
    assert result == []


def test_missing_tags():
    entries = [
        {
            "title": "No Tags",
            "link": "https://example.com/no-tags",
            "published_parsed": (2026, 5, 2, 8, 0, 0, 4, 122, 0),
        }
    ]
    result = get_ars_technica(parse_fn=_fake_feed(entries))
    assert result[0].tags == []


def test_missing_published_parsed():
    entries = [
        {
            "title": "No Date",
            "link": "https://example.com/no-date",
            "published_parsed": None,
            "tags": [],
        }
    ]
    result = get_ars_technica(parse_fn=_fake_feed(entries))
    assert result[0].date > 0
    assert result[0].title == "No Date"
