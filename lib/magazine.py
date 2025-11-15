from lib.article import Article

class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Magazine name must be a string 2-16 characters long.")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string.")
        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Magazine name must be a string 2-16 characters long.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        arts = self.articles()
        return [art.title for art in arts] if arts else None

    def contributing_authors(self):
        authors = [a for a in self.contributors() if len([art for art in a.articles() if art.magazine == self]) > 2]
        return authors if authors else None

    @classmethod
    def top_publisher(cls):
        if not Article.all_articles:
            return None
        counts = {}
        for mag in cls.all_magazines:
            counts[mag] = len([art for art in Article.all_articles if art.magazine == mag])
        return max(counts, key=counts.get)
