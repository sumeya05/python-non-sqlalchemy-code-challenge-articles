# code challenge of this week
class Author:

    all = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # name is immutable → ignore any change
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        mags = [article.magazine for article in Article.all if article.author == self]
        return list(set(mags))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = [
            article.magazine.category
            for article in Article.all
            if article.author == self
        ]
        if len(topics) == 0:
            return None
        return list(set(topics))


class Magazine:
    all = []

    def __init__(self, name, category):
        # validate name
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            self._name = None

        # validate category
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            self._category = None

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        # else ignore invalid values

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        # else ignore invalid values

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(
            set([article.author for article in Article.all if article.magazine == self])
        )

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        if len(titles) == 0:
            return None
        return titles

    def contributing_authors(self):
        authors = []
        for author in self.contributors():
            count = len(
                [a for a in Article.all if a.magazine == self and a.author == author]
            )
            if count > 2:
                authors.append(author)
        if len(authors) == 0:
            return None
        return authors


class Article:
    all = []

    def __init__(self, author, magazine, title):
        # title validation
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title

        # author + magazine validation
        if isinstance(author, Author):
            self._author = author
        if isinstance(magazine, Magazine):
            self._magazine = magazine

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # immutable → ignore any change
        pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
