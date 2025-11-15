class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        from lib.author import Author
        from lib.magazine import Magazine

        if not isinstance(author, Author):
            raise Exception("author must be an Author instance.")
        if not isinstance(magazine, Magazine):
            raise Exception("magazine must be a Magazine instance.")
        # allow short titles used in tests like "AI" and "ML" (min length 2)
        if not isinstance(title, str) or not (2 <= len(title) <= 50):
            raise Exception("Title must be a string 2-50 characters long.")

        self._title = title
        self._author = author
        self._magazine = magazine
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from lib.author import Author
        if not isinstance(value, Author):
            raise Exception("author must be an Author instance.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from lib.magazine import Magazine
        if not isinstance(value, Magazine):
            raise Exception("magazine must be a Magazine instance.")
        self._magazine = value
