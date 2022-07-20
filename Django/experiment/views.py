import json
from django.http import HttpResponse

from utils.access_data import fetch_index, experiment_uri
from .experiment import format_experiment


def index():
    pass


def get_experiment_files(request, id):
    data = fetch_index(experiment_uri(id), recursive=True)
    data = format_experiment(data)
    return HttpResponse(json.dumps(data["content"]), content_type="json")
