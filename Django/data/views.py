import json
from django.http import HttpResponse

from utils.access_data import fetch_index, fetch_data


def index(request):
    pass


def get_all_files(request, uri):
    result = fetch_index(uri, recursive=True)
    return HttpResponse(json.dumps(result), content_type="json")


def get_list(request, uri):
    result = fetch_index(uri, names_only=True)
    return HttpResponse(json.dumps(result), content_type="json")
    
def get_file(request, uri):
    result = fetch_data(uri)
    return HttpResponse(json.dumps(result), content_type="text")
