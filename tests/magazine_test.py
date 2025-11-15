import pytest
from lib.magazine import Magazine
from lib.author import Author

def test_magazine_init():
    mag = Magazine("Tech Today", "Technology")
    assert mag.name == "Tech Today"
    assert mag.category == "Technology"

def test_magazine_articles_and_contributors():
    author = Author("John Doe")
    mag = Magazine("Tech Today", "Technology")
    article = author.add_article(mag, "AI in 2025")
    assert article in mag.articles()
    assert author in mag.contributors()

def test_article_titles():
    author = Author("Jane")
    mag = Magazine("Health Mag", "Health")
    author.add_article(mag, "Eat Well")
    author.add_article(mag, "Exercise More")
    titles = mag.article_titles()
    assert "Eat Well" in titles
    assert "Exercise More" in titles

def test_contributing_authors():
    author = Author("Sam")
    mag = Magazine("Tech Mag", "Technology")
    author.add_article(mag, "AI")
    author.add_article(mag, "ML")
    author.add_article(mag, "Robotics")
    authors = mag.contributing_authors()
    assert author in authors

def test_top_publisher():
    mag1 = Magazine("Tech Mag", "Technology")
    mag2 = Magazine("Health Mag", "Health")
    author = Author("Max")
    author.add_article(mag1, "Tech 1")
    author.add_article(mag1, "Tech 2")
    author.add_article(mag2, "Health 1")
    top = Magazine.top_publisher()
    assert top == mag1
