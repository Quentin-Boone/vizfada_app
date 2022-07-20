import unittest

from metadata import Metadata
import texturl as dc


class TestMetadata(unittest.TestCase):

    def test_base(self):
        texturl = {"text": "text", "url": "url"}
        ontology = {"text": "text", "ontologyTerms": "url"}
        file = {"filename": "text", "url": "url"}
        textunit = {"text": "text", "unit": "url"}
        article = {"title": "text", "articleId": "url",
                   "journal": "journal", "year": "year"}
        organization = {"name": "text", "URL": "url", "role": "role"}

        castingAll = {"exp1":  {"texturl": texturl,
                                "ontology": ontology,
                                "file": file,
                                "textunit": textunit,
                                "article": article,
                                "organization": organization}}

        emptyMeta = Metadata({})
        castingMeta = Metadata(castingAll)

        self.assertIsInstance(emptyMeta, Metadata)
        self.assertEqual(emptyMeta.json, {})
        self.assertEqual(emptyMeta.full_json, emptyMeta.json)
        self.assertEqual(emptyMeta.keys, [])
        self.assertEqual(emptyMeta.fields, {})

        self.assertIsInstance(castingMeta, Metadata)
        self.assertEqual(castingMeta.json, {'exp1': {'texturl': {'name': 'Texturl', 'value': dc.TextUrl(**texturl)},
                                                     'ontology': {'name': 'Ontology', 'value': dc.Ontology(**ontology)},
                                                     'file': {'name': 'File', 'value': dc.File(**file)},
                                                     'textunit': {'name': 'Textunit', 'value': dc.TextUnit(**textunit)},
                                                     'article': {'name': 'Article', 'value': dc.Article(**article)},
                                                     'organization': {'name': 'Organization', 'value': dc.Organization(**organization)}}
                                            })
        self.assertEqual(castingMeta.full_json, castingMeta.json)
        self.assertEqual(castingMeta.keys, ["exp1"])
        self.assertEqual(castingMeta.fields, {'texturl': {'values': {dc.TextUrl(**texturl): 1}, 'count': 1},
                                              'ontology': {'values': {dc.Ontology(**ontology): 1}, 'count': 1},
                                              'file': {'values': {dc.File(**file): 1}, 'count': 1},
                                              'textunit': {'values': {dc.TextUnit(**textunit): 1}, 'count': 1},
                                              'article': {'values': {dc.Article(**article): 1}, 'count': 1},
                                              'organization': {'values': {dc.Organization(**organization): 1}, 'count': 1}})

    def test_filter(self):
        exp1 = {"exp1": {"field1": "value1",
                         "field2": "value1", "field3": ["value1", "value2"]}}
        exp2 = {"exp2": {"field1": "value2",
                         "field2": "value2", "field3": ["value2", "value3"]}}
        exp3 = {"exp3": {"field1": "value1",
                         "field2": "value2", "field3": ["value1", "value3"]}}
        exp4 = {"exp4": {"field3": "value1"}}

        testDict = {**exp1, **exp2, **exp3, **exp4}

        testMeta = Metadata(testDict)

        filterExp13 = {"field1": ["value1"]}
        filterExp2 = {"field1": ["value2"], "field2": ["value2"]}
        filterExp12 = {"field3": ["value2"]}
        filterNoMatch = {"field4": ["value"]}
        filter134 = {"field3": ["value1"]}

        self.assertIsInstance(testMeta.filter({}), Metadata)

        self.assertEqual(testMeta.filter({}), Metadata({}))
        self.assertEqual(testMeta.filter(filterExp13),
                         Metadata({**exp1, **exp3}))
        self.assertEqual(testMeta.filter(filterExp2), Metadata({**exp2}))
        self.assertEqual(testMeta.filter(filterExp12),
                         Metadata({**exp1, **exp2}))
        self.assertEqual(testMeta.filter(filterExp2), Metadata({**exp2}))
        self.assertEqual(testMeta.filter(filter134),
                         Metadata({**exp1, **exp3, **exp4}))
        self.assertEqual(testMeta.filter(filterNoMatch), Metadata({}))

    def test_field_counts(self):
        exp1 = {"exp1": {"field1": "value1",
                         "field2": "value1", "field3": ["value1", "value2"]}}
        exp2 = {"exp2": {"field1": "value2",
                         "field2": "value2", "field3": ["value2", "value3"]}}
        exp3 = {"exp3": {"field1": "value1",
                         "field2": "value2", "field3": ["value1", "value3"]}}
        exp4 = {"exp4": {"field3": "value1"}}

        testDict = {**exp1, **exp2, **exp3, **exp4}

        testMeta = Metadata(testDict)
        emptyMeta = Metadata({})

        self.assertIsInstance(emptyMeta.fields_counts(), dict)
        self.assertIsInstance(testMeta.fields_counts(), dict)
        self.assertEqual(testMeta.fields, testMeta.fields_counts())

        self.assertEqual(emptyMeta.fields_counts(), {})
        self.assertEqual(Metadata(exp4).fields_counts(), {
                         "field3": {"values": {"value1": 1}, "count": 1}})
        self.assertEqual(testMeta.fields_counts(),
                         {'field1': {'values': {'value1': 2, 'value2': 1}, 'count': 2},
                          'field2': {'values': {'value1': 1, 'value2': 2}, 'count': 2},
                          'field3': {'values': {'value1': 3, 'value2': 2, 'value3': 2}, 'count': 3}})

    def test_get(self):
        exp1 = {"exp1": {"field": "value"}}

        testMeta = Metadata(exp1)

        self.assertIsInstance(testMeta.get("exp1"), dict)

        self.assertEqual(testMeta.get("invalidExp"), {})
        self.assertEqual(testMeta.get("exp1"), {
                         "exp1": {"field": {"value": "value", "name": "Field"}}})
