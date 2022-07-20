import unittest
import os

import utils.constants as const
import utils.generic_functions as gf
import utils.json_formatting as jf
import texturl as dc


class TestConstant(unittest.TestCase):

    def test_data_dir(self):
        self.assertTrue(os.path.isdir(const.DATA_DIR))
        self.assertTrue(os.access(const.DATA_DIR, os.R_OK))


class TestGeneric(unittest.TestCase):

    def test_xstr(self):
        self.assertEqual(gf.xstr(0), 0)
        self.assertEqual(gf.xstr(0.0), 0.0)
        self.assertEqual(gf.xstr(None), "")
        self.assertEqual(gf.xstr(False), False)
        self.assertEqual(gf.xstr(""), "")

    def test_split_on_upper(self):
        # Empty string
        self.assertEqual(gf.split_on_upper(""), "")

        # No dots
        self.assertEqual(gf.split_on_upper("nodots"), "Nodots")
        self.assertEqual(gf.split_on_upper("noDots"), "No dots")
        self.assertEqual(gf.split_on_upper("noDotsAndMultipleCaps"),
                         "No dots and multiple caps")

        # Dots
        self.assertEqual(gf.split_on_upper("one.dot"), "Dot")
        self.assertEqual(gf.split_on_upper("one.two.dots"), "Dots")
        self.assertEqual(gf.split_on_upper("one.dotAndMultipleCaps"),
                         "Dot and multiple caps")

        # Underscore
        self.assertEqual(gf.split_on_upper("one_underscore"), "One")
        self.assertEqual(gf.split_on_upper("one_two_underscore"), "One_two")
        self.assertEqual(gf.split_on_upper("one.dot_underscore"), "Dot")


class TestJsonFormatting(unittest.TestCase):

    def test_flatten_json(self):
        texturl = {"text": "text", "url": "url"}
        ontology = {"text": "text", "ontologyTerms": "url"}
        file = {"filename": "text", "url": "url"}
        textunit = {"text": "text", "unit": "url"}
        article = {"title": "text", "articleId": "url",
                   "journal": "journal", "year": "year"}
        organization = {"name": "text", "URL": "url", "role": "role"}

        # Empty json
        self.assertEqual(jf.flatten_json({}), {})

        # Flattening
        self.assertEqual(jf.flatten_json({"key": "value"}), {"key": "value"})
        self.assertEqual(jf.flatten_json(
            {"key": {"key": "value"}}), {"key.key": "value"})
        self.assertEqual(jf.flatten_json({"key": [{"key": "value"}, {"key": "value"}]}), {
                         "key": [{"key": "value"}, {"key": "value"}]})

        # Casting
        self.assertEqual(jf.flatten_json({"key": {"key": {"text": "text"}}}), {
                         "key.key": dc.TextUrl("text", "")})
        self.assertEqual(jf.flatten_json({"key": {"key": texturl}}), {
                         "key.key": dc.TextUrl(**texturl)})
        self.assertEqual(jf.flatten_json({"key": {"key": ontology}}), {
                         "key.key": dc.Ontology(**ontology)})
        self.assertEqual(jf.flatten_json({"key": {"key": file}}), {
                         "key.key": dc.File(**file)})
        self.assertEqual(jf.flatten_json({"key": {"key": textunit}}), {
                         "key.key": dc.TextUnit(**textunit)})
        self.assertEqual(jf.flatten_json({"key": {"key": article}}), {
                         "key.key": dc.Article(**article)})
        self.assertEqual(jf.flatten_json({"key": {"key": organization}}), {
                         "key.key": dc.Organization(**organization)})

    def test_reformat_json(self):
        texturl = {"text": "text", "url": "url"}
        ontology = {"text": "text", "ontologyTerms": "url"}
        file = {"filename": "text", "url": "url"}
        textunit = {"text": "text", "unit": "url"}
        article = {"title": "text", "articleId": "url",
                   "journal": "journal", "year": "year"}
        organization = {"name": "text", "URL": "url", "role": "role"}

        noFormattedFields = {
            "exp": {"field": "value", "longFieldName": "otherValue"}}
        oneFormattedField = {"exp": {"RNA-seq.rnaPurity260280ratio": "value"}}
        twoExperiments = {"exp1": {"field": "value"},
                          "exp2": {"field": "value"}}
        castingAll = {"exp1": {"texturl": texturl,
                               "ontology": ontology,
                               "file": file,
                               "textunit": textunit,
                               "article": article,
                               "organization": organization}}
        castingList = {"exp1": {"ontologyList": [ontology, ontology]}}

        # Empty json
        self.assertEqual(jf.reformat_json({}), {})

        # Field name formatting
        self.assertEqual(jf.reformat_json(noFormattedFields),
                         {"exp":
                          {"field":
                           {"value": "value", "name": "Field"},
                           "longFieldName":
                           {"value": "otherValue",
                            "name": "Long field name"}
                           }
                          })

        self.assertEqual(jf.reformat_json(oneFormattedField),
                         {"exp": {"RNA-seq.rnaPurity260280ratio":
                                  {"name": "RNA purity - 260:280 ratio",
                                   "value": "value"}
                                  }
                          })

        self.assertEqual(jf.reformat_json(twoExperiments),
                         {"exp1": {"field": {"name": "Field", "value": "value"}},
                          "exp2": {"field": {"name": "Field", "value": "value"}}})

        self.assertEqual(jf.reformat_json(castingAll),
                         {"exp1":
                          {"texturl":
                           {"name": "Texturl",
                            "value": dc.TextUrl(**texturl)},
                           "ontology":
                           {"name": "Ontology",
                            "value": dc.Ontology(**ontology)},
                           "textunit":
                           {"name": "Textunit",
                            "value": dc.TextUnit(**textunit)},
                           "file":
                           {"name": "File",
                            "value": dc.File(**file)},
                           "article":
                           {"name": "Article",
                            "value": dc.Article(**article)},
                           "organization":
                           {"name": "Organization",
                            "value": dc.Organization(**organization)}
                           }
                          })

        self.assertEqual(jf.reformat_json(castingList),
                         {"exp1":
                          {"ontologyList": {
                              "name": "Ontology list",
                              "value": [dc.Ontology(**ontology), dc.Ontology(**ontology)]
                          }
                          }
                          })
