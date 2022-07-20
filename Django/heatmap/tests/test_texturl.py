import unittest

import texturl as dc


class TestDataClasses(unittest.TestCase):

    def test_texturl(self):
        # Set up
        test = dc.TextUrl("text", "url")
        test2 = dc.TextUrl("text", "url")
        testSameURL = dc.TextUrl("url", "url")
        testSameText = dc.TextUrl("text", "text")
        testNone = dc.TextUrl(None, None)
        testEmpty = dc.TextUrl("", "")

        # Test attributes
        self.assertIsInstance(test, dc.TextUrl)
        self.assertEqual(test.text, "text")
        self.assertEqual(test.url, "url")

        # Equality (same class)
        self.assertEqual(test, test2)
        self.assertNotEqual(test, testSameURL)
        self.assertNotEqual(test, testSameText)
        self.assertEqual(testNone, testEmpty)

        # Equality (other classes)
        self.assertNotEqual(test, None)
        self.assertNotEqual(test, "text")
        self.assertNotEqual(test, "url")
        self.assertNotEqual(test, {"text": "text", "url": "url"})

        # str and repr
        self.assertEqual(str(test), "text")
        self.assertEqual(repr(test), "text")

    def test_organization(self):
        # Set up
        test = dc.Organization(
            **{"name": "text", "URL": "url", "role": "role"})
        test2 = dc.Organization(
            **{"name": "text", "URL": "url", "role": "other"})
        testSameURL = dc.Organization(
            **{"name": "url", "URL": "url", "role": "role"})
        testSameText = dc.Organization(
            **{"name": "text", "URL": "text", "role": "role"})
        testNone = dc.Organization(**{"name": None, "URL": None, "role": None})
        testEmpty = dc.Organization(**{"name": "", "URL": "", "role": ""})

        # Attributes
        self.assertIsInstance(test, dc.TextUrl)
        self.assertIsInstance(test, dc.Organization)
        self.assertEqual(test.text, "text")
        self.assertEqual(test.url, "url")
        self.assertEqual(test.role, "role")
        self.assertEqual(test.name, test.text)

        # Equality (same class)
        self.assertEqual(test, test2)
        self.assertNotEqual(test, testSameURL)
        self.assertNotEqual(test, testSameText)
        self.assertEqual(testNone, testEmpty)

        # Equality (other classes)
        self.assertEqual(test, dc.TextUrl("text", "url"))
        self.assertNotEqual(test, None)
        self.assertNotEqual(test, "text")
        self.assertNotEqual(test, "url")
        self.assertNotEqual(test, {"text": "text", "url": "url"})

        # str and repr
        self.assertEqual(str(test), "text")
        self.assertEqual(repr(test), "text")

    def test_article(self):
        # Set up
        test = dc.Article(**{"journal": "journal", "title": "text",
                          "year": 2049, "articleId": "url"})
        test2 = dc.Article(
            **{"journal": "other", "title": "text", "year": 0, "articleId": "url"})
        testSameURL = dc.Article(
            **{"journal": "journal", "title": "other", "year": 2049, "articleId": "url"})
        testSameText = dc.Article(
            **{"journal": "other", "title": "text", "year": 0, "articleId": "other"})
        testNone = dc.Article(
            **{"journal": None, "title": None, "year": None, "articleId": None})
        testEmpty = dc.Article(
            **{"journal": "", "title": "", "year": "", "articleId": ""})

        # Attributes
        self.assertIsInstance(test, dc.TextUrl)
        self.assertIsInstance(test, dc.Article)
        self.assertEqual(test.text, "text")
        self.assertEqual(test.url, "url")
        self.assertEqual(test.journal, "journal")
        self.assertEqual(test.year, 2049)
        self.assertEqual(test.title, test.text)
        self.assertEqual(test.articleId, test.url)

        # Equality (same class)
        self.assertEqual(test, test2)
        self.assertNotEqual(test, testSameURL)
        self.assertNotEqual(test, testSameText)
        self.assertEqual(testNone, testEmpty)

        # Equality (other classes)
        self.assertEqual(test, dc.TextUrl("text", "url"))
        self.assertNotEqual(test, None)
        self.assertNotEqual(test, "text")
        self.assertNotEqual(test, "url")
        self.assertNotEqual(test, {"text": "text", "url": "url"})

        # str and repr
        self.assertEqual(str(test), "text")
        # self.assertEqual(repr(test), "text")

    def test_ontology(self):
        # Set up
        test = dc.Ontology("text", "url")
        test2 = dc.Ontology("text", "url")
        testSameURL = dc.Ontology("url", "url")
        testSameText = dc.Ontology("text", "text")
        testNone = dc.Ontology(None, None)
        testEmpty = dc.Ontology("", "")

        # Attributes
        self.assertIsInstance(test, dc.TextUrl)
        self.assertIsInstance(test, dc.Ontology)
        self.assertEqual(test.text, "text")
        self.assertEqual(test.url, "url")

        # Equality (same class)
        self.assertEqual(test, test2)
        self.assertNotEqual(test, testSameURL)
        self.assertNotEqual(test, testSameText)
        self.assertEqual(testNone, testEmpty)

        # Equality (other classes)
        self.assertEqual(test, dc.TextUrl("text", "url"))
        self.assertNotEqual(test, None)
        self.assertNotEqual(test, "text")
        self.assertNotEqual(test, "url")
        self.assertNotEqual(test, {"text": "text", "url": "url"})

        # str and repr
        self.assertEqual(str(test), "text")
        self.assertEqual(repr(test), "text")

    def test_textunit(self):
        # Set up
        test = dc.TextUnit(**{"text": "text", "unit": "url"})
        test2 = dc.TextUnit(**{"text": "text", "unit": "url"})
        testSameURL = dc.TextUnit(**{"text": "url", "unit": "url"})
        testSameText = dc.TextUnit(**{"text": "text", "unit": "text"})
        testNone = dc.TextUnit(None, None)
        testEmpty = dc.TextUnit("", "")

        # Attributes
        self.assertIsInstance(test, dc.TextUrl)
        self.assertIsInstance(test, dc.TextUnit)
        self.assertEqual(test.text, "text")
        self.assertEqual(test.url, "url")
        self.assertEqual(test.unit, test.url)

        # Equality (same class)
        self.assertEqual(test, test2)
        self.assertNotEqual(test, testSameURL)
        self.assertNotEqual(test, testSameText)
        self.assertEqual(testNone, testEmpty)

        # Equality (other classes)
        self.assertEqual(test, dc.TextUrl("text", "url"))
        self.assertNotEqual(test, None)
        self.assertNotEqual(test, "text")
        self.assertNotEqual(test, "url")
        self.assertNotEqual(test, {"text": "text", "url": "url"})

        # str and repr
        self.assertEqual(str(test), "text")
        self.assertEqual(repr(test), "text url")

    def test_file(self):
        # Set up
        test = dc.File(**{"filename": "text", "url": "url"})
        test2 = dc.File(**{"filename": "text", "url": "url"})
        testSameURL = dc.File(**{"filename": "url", "url": "url"})
        testSameText = dc.File(**{"filename": "text", "url": "text"})
        testNone = dc.File(None, None)
        testEmpty = dc.File("", "")

        # Attributes
        self.assertIsInstance(test, dc.TextUrl)
        self.assertIsInstance(test, dc.File)
        self.assertEqual(test.text, "text")
        self.assertEqual(test.url, "url")
        self.assertEqual(test.filename, test.text)

        # Equality (same class)
        self.assertEqual(test, test2)
        self.assertNotEqual(test, testSameURL)
        self.assertNotEqual(test, testSameText)
        self.assertEqual(testNone, testEmpty)

        # Equality (other classes)
        self.assertEqual(test, dc.TextUrl("text", "url"))
        self.assertNotEqual(test, None)
        self.assertNotEqual(test, "text")
        self.assertNotEqual(test, "url")
        self.assertNotEqual(test, {"text": "text", "url": "url"})

        # str and repr
        self.assertEqual(str(test), "text")
        self.assertEqual(repr(test), "text")
