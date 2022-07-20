import requests as rq

from django.conf import settings


def build_url(type, access, *uri):
    uri = list(uri)
    t = type.lower()
    if (t == "download"):
        uri.insert(0, settings.DATA_DOWNLOAD)
        url = f"{settings.DATA_SERVER[access]}/{'/'.join(uri)}"
    elif (t == "index"):
        uri.insert(0, settings.DATA_INDEX)
        url = f"{settings.DATA_SERVER[access]}/{'/'.join(uri)}/"
    elif (t == "file"):
        uri.insert(0, settings.DATA_FILE)
        url = f"{settings.DATA_SERVER[access]}/{'/'.join(uri)}"
    else:
        raise ValueError("The first argument must be 'download', 'index' or 'file'")
    return url


def fetch_recursive(uri):
    all = rq.get(build_url('index', "cluster", uri)).json()
    parent = str(uri.split('/')[-1])
    finalDict = {}
    for file in all:
        if file["type"] == "file":
            finalDict.setdefault(parent, [])
            finalDict[parent].append({"url": build_url('file', "external", uri, file['name']),
                                      "download": build_url('download', "external", uri, file['name']),
                                      "parent": parent, **file})
        elif file["type"] == "directory":
            finalDict.setdefault(parent, [])
            finalDict[parent].append(fetch_recursive(f"{uri}/{file['name']}"))
    return finalDict


def fetch_index(uri, names_only=False, recursive=False):
    url = build_url('index', "cluster", uri)
    js = fetch_recursive(uri) if recursive else rq.get(build_url('index', "cluster", uri)).json()
    if names_only:
        return [file["name"] for file in js]
    else:
        return js


def fetch_data(uri):
    js = rq.get(build_url('file', "cluster", uri)).text
    return js


def experiment_uri(id):
    split = [0, 3, 6, 8]
    uri = "/".join([id[split[i]:split[i+1]] for i in range(len(split)-1)])
    return f"experiments/{uri}/{id}"