from .query_handler import *
import os
import requests as rq

from django.conf import settings
from .functions import fetch_index

def get_legend(request):
    # try:
    #    sessionID = request.COOKIES.get('sessionID')
    # except KeyError:
    #    return HttpResponse()
    #heatmap = query_handler(request)
    #legend = json.dumps(heatmap.annotation_legend)
    print("Test cookie worked: %s" % (str(request.session.test_cookie_worked())))
    print("Session key (legend): \n%s" % (str(request.session.session_key)))
    print("Session legend: \n%s" % (str(request.session['legend'])))
    legend = json.dumps(request.session['legend'])
    response = HttpResponse(legend, content_type="json")
    return response


def get_fields(request):
    heatmap = query_handler(request)
    fields = json.dumps(heatmap.get_fields_and_count())
    return HttpResponse(fields, content_type="json")


def get_experiments(request, species):
    qs = os.listdir(os.path.join(DATA, species))
    return HttpResponse(json.dumps(list(qs)), content_type="json")


def get_species(request):
    #q = request.GET.dict()['q']
    #params = eval(q)
    qs = fetch_index("")
    species = [file["name"] for file in qs if file["name"] != "experiments"]
    return HttpResponse(json.dumps(species), content_type="json")


def get_metadata(request):
    heatmap = query_handler(request)
    metadata = heatmap.get_metadata()
    #meta = [{c: metadata.loc[row, c] for c in metadata.columns} for row in metadata.index]
    #results={"data": meta, "columns": metadata.columns.to_list()}
    return HttpResponse(metadata, content_type="json")


def get_size(request):
    heatmap = query_handler(request)
    size = heatmap.get_size()
    return HttpResponse(size, content_type="text")


def get_json(request):
    heatmap = query_handler(request)
    size = json.dumps(heatmap.get_plotly_json())
    return HttpResponse(size, content_type="json")


def get_row_annotation(request):
    heatmap = query_handler(request)
    annotation = json.dumps(heatmap.get_row_annotation(heatmap.annotated))
    return HttpResponse(annotation, content_type="json")


def get_annotated_plotly(request):
    heatmap = query_handler(request)
    main = heatmap.get_plotly_json()
    result = [heatmap.get_row_annotation(heatmap.annotated), main]
    return HttpResponse(json.dumps(result), content_type="json")
