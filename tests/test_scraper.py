# tests/test_scraper.py
import pytest
from app.scraper import NewsScraper

def test_fetch_articles():
    base_url = "https://saharareporters.com"
    scraper = NewsScraper(base_url)
    articles = scraper.fetch_articles()
    assert isinstance(articles, list)
    if articles:
        assert "title" in articles[0]
        assert "link" in articles[0]
        assert "content" in articles[0]