import pytest

from lib.article import Article
from lib.magazine import Magazine
from lib.author import Author


@pytest.fixture(autouse=True)
def clear_state():
    """Ensure global class lists are cleared before each test to avoid state leakage between tests."""
    Article.all_articles.clear()
    Magazine.all_magazines.clear()
    Author.all_authors.clear()
    yield
    # clear again after test for extra safety
    Article.all_articles.clear()
    Magazine.all_magazines.clear()
    Author.all_authors.clear()
