import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

def test_author_init():
    author = Author("John Doe")
    assert author.name == "John Doe"

def test_author_articles():
    author = Author("Jane Doe")
    mag = Magazine("Tech Mag", "Technology")
    art = author.add_article(mag, "New Tech")
    assert art in author.articles()

def test_author_magazines():
    author = Author("Alice")
    mag1 = Magazine("Health Mag", "Health")
    mag2 = Magazine("Tech Mag", "Technology")
    author.add_article(mag1, "Healthy Life")
    author.add_article(mag2, "AI Future")
    mags = author.magazines()
    assert mag1 in mags and mag2 in mags

def test_author_topic_areas():
    author = Author("Bob")
    mag1 = Magazine("Health Mag", "Health")
    mag2 = Magazine("Tech Mag", "Technology")
    author.add_article(mag1, "Health Tips")
    author.add_article(mag2, "Tech Trends")
    topics = author.topic_areas()
    assert "Health" in topics and "Technology" in topics
