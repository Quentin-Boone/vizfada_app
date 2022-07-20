import json
from django.http import HttpResponse
from django.shortcuts import render

import scipy.cluster.hierarchy as sch
from plotly.graph_objs import Heatmap
from plotly.offline import plot
import matplotlib.pyplot as plt
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt


from .heatmap import ClusteredHeatmap
from utils.query_handler import query_handler
from utils.access_data import fetch_data


def index(request):
    pass

def get_plotly(request):
    heatmap = query_handler(request)
    main = heatmap.get_plotly_json()
    result = [heatmap.get_row_annotation(heatmap.annotated), main]
    return HttpResponse(json.dumps(result), content_type="json")
    
def get_image(request):
    heatmap = query_handler(request)
    print("Kept %d/%d" % (len(heatmap.metadata), len(heatmap.ALL_METADATA)))
    print(heatmap.highlights)
    fig = heatmap.get_heatmap(highlighted=True)
    # print(heatmap)
    response = HttpResponse(content_type="image/png")
    plt.savefig(response)
    request.session['legend'] = heatmap.annotation_legend
    request.session.save()
    print("Session key (image): \n%s" % (str(request.session.session_key)))
    print("Session legend: \n%s" % (str(request.session['legend'])))
    request.session.set_test_cookie()
    print("Test cookie worked: %s" % (str(request.session.test_cookie_worked())))
    print("RESPONSE:", response)
    return response
    
@ensure_csrf_cookie
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
