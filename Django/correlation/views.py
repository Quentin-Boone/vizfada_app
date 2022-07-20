from django.http import HttpRequest, HttpResponse
import json
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from django.views.decorators.csrf import csrf_exempt

from .correlation import jaccard_full as j, pearson as p, jaccard_user as ju
from utils.query_handler import query_handler

def index():
    pass

def jaccard(request: HttpRequest):
    heatmap = query_handler(request)
    expList = heatmap.get_metadata().keys
    jaccard = j(expList)
    #meta = [{c: metadata.loc[row, c] for c in metadata.columns} for row in metadata.index]
    #results={"data": meta, "columns": metadata.columns.to_list()}
    return HttpResponse(jaccard, content_type="text")

def pearson(request: HttpRequest):
    heatmap = query_handler(request)
    expList = heatmap.get_metadata().keys
    pearson = p(heatmap.species, expList)
    #meta = [{c: metadata.loc[row, c] for c in metadata.columns} for row in metadata.index]
    #results={"data": meta, "columns": metadata.columns.to_list()}
    return HttpResponse(pearson, content_type="text")

@csrf_exempt
def jaccard_user(request: HttpRequest):
    heatmap = query_handler(request)
    print("heatmap done")
    userFile = eval(request.body)['file']
    heatmap = ju(userFile, heatmap)
    fig = heatmap.get_heatmap(highlighted=True)
    # print(heatmap)
    response = HttpResponse(content_type="image/png")
    plt.savefig(response)
    return HttpResponse(response)