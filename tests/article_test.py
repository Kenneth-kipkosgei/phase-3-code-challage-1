import pytest
from lib.article import Article
from lib.author import Author
from lib.magazine import Magazine

def test_article_init():
    author = Author("John")
    mag = Magazine("Tech Mag", "Tech")
    art = Article(author, mag, "AI Trends")
    assert art.author == author
    assert art.magazine == mag
    assert art.title == "AI Trends"

def test_article_author_setter():
    author1 = Author("Alice")
    author2 = Author("Bob")
    mag = Magazine("Science Mag", "Science")
    art = Article(author1, mag, "New Discovery")
    art.author = author2
    assert art.author == author2

def test_article_magazine_setter():
    author = Author("Alice")
    mag1 = Magazine("Mag1", "Tech")
    mag2 = Magazine("Mag2", "Health")
    art = Article(author, mag1, "Title")
    art.magazine = mag2
    assert art.magazine == mag2
