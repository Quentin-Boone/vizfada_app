from utils.generic_functions import xstr


class Iter:

    def __init__(self, *objects):
        self.list = list(objects)
        self.index = 0

    def __next__(self):
        if self.index < len(self.list):
            result = self.list[self.index]
            self.index += 1
            return result
        raise StopIteration


class TextUrl:

    def __init__(self, text, url):
        self.text = xstr(text)
        self.url = xstr(url)

    def __str__(self):
        return self.text

    """
    def __dict__(self):
        return {'text': self.text, 'url': self.url}
    """

    def __repr__(self):
        return self.text

    def __eq__(self, other):
        if isinstance(other, TextUrl):
            return (self.text == other.text and self.url == other.url)
        else:
            return False

    def __iter__(self):
        return Iter(self)

    def __hash__(self):
        return hash((self.text, self.url))

    def to_dict(self):
        d = self.__dict__
        return d


class Organization(TextUrl):

    def __init__(self, name, role, URL):
        super().__init__(name, URL)
        self.name = self.text
        self.role = xstr(role)


class Article(TextUrl):

    def __init__(self, journal, title, year, articleId):
        super().__init__(title, articleId)
        self.title = self.text
        self.year = xstr(year)
        self.journal = journal
        self.articleId = self.url

    def __repr__(self):
        return f"{self.text} - {self.journal}, {self.year} ({self.url})"

    """
    def __dict__(self):
        return {'journal': self.journal, 'title': self.text, 'year': self.year, 'articleId': self.url}
    """


class Ontology(TextUrl):

    def __init__(self, text, ontologyTerms):
        super().__init__(text, ontologyTerms)
        #self.text = text
        #self.url = ontologyTerms
    """
    def __dict__(self):
        return {'text': self.text, 'ontologyTerms': self.url}
    """

    def __repr__(self):
        return self.text


class TextUnit(TextUrl):

    def __init__(self, text, unit):
        super().__init__(text, unit)
        self.unit = self.url
    """
    def __dict__(self):
        return {"text": self.text, "unit": self.unit}
    """

    def __repr__(self):
        return f"{self.text} {self.unit}"


class File(TextUrl):

    def __init__(self, filename, url):
        super().__init__(filename, url)
        self.filename = filename
        #self.url = url
    """
    def __dict__(self):
        return {'filename': self.text, 'url': self.url}
    """
