import os
import pandas as pd
import json
import base64

from django.conf import settings
#from VizFaDa.settings.base import DATA, DATA_SERVER
from django.http import HttpResponse

from utils.access_data import build_url, fetch_index

cols = {"anchor_type": "Anchor Type", "cellType": "Cell Type", "experiment": "Experiment", "notes": "Notes", "input_id": "Input DNA", "bound_id": "Bound experiment"}

def group_epistack(df):
    results = {}
    for c,name in cols.items():
        d = df.groupby(c).png.nunique()
        # print(d)
        results[c] = {"name": name, "values": {key: value for key, value in d.iteritems()}}
        results[c]['values']['All'] = sum(results[c]['values'].values())
        results[c]["count"] = len(results[c]["values"])-1
    return results


def _filter_epistack(q):
    filters = {key: value for key, value in q.items() if key != 'species' and value not in ["","All"]}
    epistackURI = "/".join(["species", q['species'], "chipseq", "epistack"])
    plotLists = [build_url("file", "cluster", epistackURI, file)
                    for file in fetch_index(epistackURI, names_only=True)
                    if file.startswith("list_of_plots")]
    plotLists = [pd.read_csv(file, sep="\t", header=0) for file in plotLists]
    df = pd.concat(plotLists)
    for field, value in filters.items():
        df = df[df[field]==value]
    return df
