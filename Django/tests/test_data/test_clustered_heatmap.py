from django.test import TestCase
import os
import typing

import pytest
import pickle
import pandas as pd

from data.heatmap.heatmap import ClusteredHeatmap
from data.models import Correlation


class TestClusteredHeatmap(TestCase):

    def setUp(self):
        testcor = pd.DataFrame({"sample1": [1, 0], "sample2": [0, 1]}, index=["sample1", "sample2"])
        meta = pd.DataFrame({"run": ["run1", "run2"],
                             "cellType": ["type1", None]},
                            index=["sample1", "sample2"])
        pickle.dump(testcor, open("testcor", "wb"))
        pickle.dump(meta, open("testmeta", "wb"))
        Correlation.objects.create(species="Gallus_gallus",
                                   correlation="testcor",
                                   metadata="testmeta")

    def test_clusteredmap_empty(self):
        with pytest.raises(TypeError):
            ch = ClusteredHeatmap()

    def test_clusteredmap_species_not_in_db(self):
        with pytest.raises(Correlation.DoesNotExist):
            ch = ClusteredHeatmap("Test_species")

    def test_clusteredmap_check_attributes_exist(self):
        ch = ClusteredHeatmap("Gallus_gallus")
        self.assertTrue(hasattr(ch, "species"))
        self.assertTrue(hasattr(ch, "size"))
        self.assertTrue(hasattr(ch, "ALL_CORRELATION"))
        self.assertTrue(hasattr(ch, "ALL_METADATA"))
        self.assertTrue(hasattr(ch, "correlation"))
        self.assertTrue(hasattr(ch, "metadata"))
        self.assertTrue(hasattr(ch, "filters"))
        self.assertTrue(hasattr(ch, "highlights"))
        self.assertTrue(hasattr(ch, "seaborn_options"))
        self.assertTrue(hasattr(ch, "fig"))
        self.assertTrue(hasattr(ch, "highlighted"))
        self.assertTrue(hasattr(ch, "fields"))

    def test_clustermap_check_attributes_initial_value(self):
        ch = ClusteredHeatmap("Gallus_gallus")
        self.assertEqual(ch.species, "Gallus_gallus")
        self.assertEqual(ch.size, "10")
        self.assertEqual(ch.filters, {})
        self.assertEqual(ch.highlights, {})
        self.assertEqual(ch.fig, None)
        self.assertEqual(ch.highlighted, None)

    def test_clusteredmap_get_fields(self):
        ch = ClusteredHeatmap("Gallus_gallus")
        self.assertEqual(ch.get_fields(), {"run": ["run1", "run2"],
                                           "cellType": ["type1", "None"]})

    def test_clusteredmap_filter_meta_nonexistent_filter(self):
        ch = ClusteredHeatmap("Gallus_gallus")
        filter = {"blabla": [""]}
        ch._filter_meta(filter)
        self.assertTrue(ch.meta.empty)

    def test_clusteredmap_filter_meta_wrong_format(self):
        ch = ClusteredHeatmap("Gallus_gallus")
        filter = "hello"
        with pytest.raises(AttributeError):
            ch._filter_meta(filter)
        filter = {"run": ""}
        with pytest.raises(TypeError):
            ch._filter_meta(filter)
        filter = None
        with pytest.raises(AttributeError):
            ch._filter_meta(filter)

    def tearDown(self):
        os.remove("testcor")
        os.remove("testmeta")
