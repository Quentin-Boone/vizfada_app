from django.http import HttpResponse
import json

from .epistack import group_epistack, _filter_epistack
from utils.access_data import fetch_index, build_url


def index():
    pass


def filter_epistack(request):
    q = eval(request.GET.dict()['q'])
    if "species" not in q.keys() or "epistack" not in fetch_index(f"species/{q['species']}/chipseq", names_only=True):
        return HttpResponse(status=404)
    else:
        return HttpResponse(json.dumps(group_epistack(_filter_epistack(q))), content_type='json')


def imgs(request):
    q = eval(request.GET.dict()['q'])
    chipseq = fetch_index(f"species/{q['species']}/chipseq", names_only=True)
    if "species" not in q.keys() or "epistack" not in chipseq:
        return HttpResponse(status=404)
    else:
        df = _filter_epistack(q)
        df = df['png'].apply(lambda x: build_url("file", "external", "species", x))
        return HttpResponse(df.to_json(orient="records"))
