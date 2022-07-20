import os

DATA_DIR = os.path.abspath("./assets/data")

LEAVES_KEYS = {"ontologyTerms",
               "text",
               "unit",
               "filename",
               "url",
               "journal",
               "name"}

FORMATTED_FIELD_NAMES = {"RNA-seq.rnaPurity260280ratio":
                         "RNA purity - 260:280 ratio",
                         "RNA-seq.rnaPurity260230ratio":
                         "RNA purity - 260:230 ratio"}
