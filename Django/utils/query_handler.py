from heatmap.heatmap import ClusteredHeatmap
from utils.correlations import correlation

def query_handler(request):
    print(request.method)
    if request.method == "GET":
        q = request.GET.get('q')
        params = eval(q)
    elif request.method == "POST":
        q = request.body
        params = eval(q)
    # TODO: Change when seaborn options implemented in front-end
    filters = {}
    highlights = {}
    for dict in params['filters']:
        if dict['field'] != '':
            filters.setdefault(dict["field"], []).extend(dict['values'])
    for dict in params['highlights']:
        if dict['field'] != '':
            color = "#%s" % dict['color']
            highlights.setdefault(color, {}).update({dict["field"]: dict["values"]})
    options = {opt: eval(val) for opt, val in params["options"].items()}
    heatmap = ClusteredHeatmap(params["species"], params["experiment"], options)
    if params["file"]:
        heatmap = correlation(params["file"], heatmap, params["experiment"], params["species"])
    heatmap.add_filters(filters)
    if params["annotated"] != "":
        heatmap.annotate_field(params["annotated"])
    heatmap.add_highlights(highlights)
    request.session['legend'] = heatmap.annotation_legend
    print(heatmap)
    return heatmap
