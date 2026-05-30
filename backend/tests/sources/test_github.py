from unittest.mock import patch, Mock

from src.sources.github import get_trending_repos
from src.model import Source

FAKE_HTML = """
<html><body>
<article class="Box-row">
  <h2><a href="/owner/repo">owner / repo</a></h2>
  <span itemprop="programmingLanguage">Python</span>
</article>
<article class="Box-row">
  <h2><a href="/other/project">other / project</a></h2>
</article>
</body></html>
"""


def _mock_response(html):
    resp = Mock()
    resp.text = html
    return resp


@patch("src.sources.github.httpx.get")
def test_parses_trending(mock_get):
    mock_get.return_value = _mock_response(FAKE_HTML)
    result = get_trending_repos()
    assert len(result) == 2
    assert result[0] == Source(
        title="owner/repo",
        date=result[0].date,
        url="https://github.com/owner/repo",
        tags=["Python"],
    )
    assert result[1].title == "other/project"
    assert result[1].tags == []


@patch("src.sources.github.httpx.get")
def test_empty_page(mock_get):
    mock_get.return_value = _mock_response("<html><body></body></html>")
    result = get_trending_repos()
    assert result == []
