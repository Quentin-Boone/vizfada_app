def format_experiment(file):
    if ("name" in file.keys()):
        return file
    else:
        d = {"name": name for name in file.keys()}
        d["type"] = "directory"
        d["expanded"] = False
        d["content"] = [format_experiment(f) for f in file[d["name"]]]
        return d
"""
def get_fastqc(request, id):
    data = os.path.join(DATA, "Experiments", id, "fastqc")
    # open(os.path.join(data, file), "r").read().replace("<html>", "").replace("</html>", "")
    fastqc = [open(os.path.join(data, file), "r").read().replace("<html>", "").replace("</html>", "") for file in os.listdir(data) if file.endswith(".html")]
    return HttpResponse(json.dumps(fastqc), content_type="json")

def get_experiment(request, id):
    heatmap = query_handler(request)
    exp = heatmap.metadata.get_single(id).to_dict()
    return HttpResponse(json.dumps(exp), content_type="json")
"""
