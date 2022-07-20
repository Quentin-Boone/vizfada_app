from .generic_functions import xstr, split_on_upper
from .texturl import TextUrl, Ontology, TextUnit, File, Article, Organization
from .constants import LEAVES_KEYS, FORMATTED_FIELD_NAMES


def cast(dic, verbose=False):
    keys = list(dic.keys())
    keys.sort()
    if keys == ["text"]:
        return TextUrl(dic["text"], "")
    elif keys == ["ontologyTerms", "text"]:
        return Ontology(**dic)
    elif keys == ["text", "url"]:
        return TextUrl(**dic)
    elif keys == ["text", "unit"]:
        return TextUnit(**dic)
    elif keys == ["filename", "url"]:
        return File(**dic)
    elif keys == ["articleId", "journal", "title", "year"]:
        return Article(**dic)
    elif keys == ["URL", "name", "role"]:
        return Organization(**dic)
    else:
        if verbose:
            print(f"No matching class for: {dic}")
        return dic


def metaToDict(js):
    if isinstance(js, TextUrl):
        return js.to_dict()
    elif isinstance(js, dict):
        return {metaToDict(k): metaToDict(v) for k, v in js.items()}
    elif isinstance(js, list):
        return [metaToDict(v) for v in js]
    else:
        return js


def metaToStr(js):
    if isinstance(js, TextUrl):
        return str(js)
    elif isinstance(js, dict):
        return {metaToStr(k): metaToStr(v) for k, v in js.items()}
    elif isinstance(js, list):
        return [metaToStr(v) for v in js]
    else:
        return js


def flatten_json(jsonDict, verbose=False):
    flat = {}
    # print("Dict :", jsonDict)
    for k in jsonDict.keys():
        if type(jsonDict[k]) == dict:
            if len(set(jsonDict[k].keys()).intersection(LEAVES_KEYS)) == 0:
                # print("No cast")
                sl = {f"{k}.{key}": value for key,
                      value in flatten_json(jsonDict[k]).items()}
                flat.update(sl)
            else:
                d = {k: xstr(v) for k, v in jsonDict[k].items()}
                flat[k] = cast(d, verbose)
                # print("Cast: ", cast(d))

        elif type(jsonDict[k]) == list:
            nl = [cast(i, verbose) if type(i) ==
                  dict else i for i in jsonDict[k]]
            # print("New List: ", nl)
            flat[k] = nl
        else:
            flat[k] = jsonDict[k]
    return flat


def reformat_json(jsonDict, verbose=False):
    result = {k: flatten_json(j, verbose) for k, j in jsonDict.items()}

    field_names = {}
    for j in result.values():
        field_names.update({k: split_on_upper(k) for k in j.keys()})
    for i in result.keys():
        for j in field_names.keys():
            result[i].setdefault(j, 'NA')
    field_names.update(FORMATTED_FIELD_NAMES)

    # print(field_names)

    result = {k: {field: {"name": field_names[field], "value": value}
                  for field, value in result[k].items()}
              for k in result.keys()}
    return result
