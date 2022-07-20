from django.http import HttpResponse
import json
import pandas as pd

from .metadata import Metadata
from utils.access_data import fetch_data, build_url
from utils.query_handler import query_handler


def index():
    pass


def metadata(request):
    heatmap = query_handler(request)
    metadata = heatmap.get_metadata().get_json()
    #meta = [{c: metadata.loc[row, c] for c in metadata.columns} for row in metadata.index]
    #results={"data": meta, "columns": metadata.columns.to_list()}
    return HttpResponse(metadata, content_type="json")


def fields(request):
    heatmap = query_handler(request)
    fields = json.dumps(heatmap.get_fields_and_count())
    #meta = [{c: metadata.loc[row, c] for c in metadata.columns} for row in metadata.index]
    #results={"data": meta, "columns": metadata.columns.to_list()}
    return HttpResponse(fields, content_type="json")


def table(request):
    heatmap = query_handler(request)
    metadata = pd.DataFrame(heatmap.get_metadata().to_dict()).transpose()
    meta = [{metadata.loc[row, c]["name"]: metadata.loc[row, c]["value"]
             if type(metadata.loc[row, c]["value"]) == type([])
             else [metadata.loc[row, c]["value"]]
             for c in metadata.columns}
            for row in metadata.index]
    results = {"data": meta, "columns": list(meta[0].keys())}
    results["columns-datatable"] = [{'name': col}
                                    for col in results["columns"]]
    return HttpResponse(json.dumps(results), content_type="json")
#    return HttpResponse(metadata.to_csv(), content_type="text")


def groups(request):
    heatmap = query_handler(request)
    fields = heatmap.get_fields_and_count()
    for f in fields:
        hierarchy = f.split('.')
        print(hierarchy)
    return HttpResponse(json.dumps(list(fields.keys())))
