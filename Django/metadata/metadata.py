import json

from utils.json_formatting import reformat_json, metaToDict, metaToStr
from utils.texturl import *
import copy


class Metadata:
    """_summary_
    """

    def __init__(self, jsonDict, reformat=True):
        """_summary_

        :param jsonDict: _description_
        :type jsonDict: dict
        :param reformat: _description_, defaults to True
        :type reformat: bool, optional
        """
        self.json = reformat_json(jsonDict) if reformat else jsonDict
        self.full_json = self.json
        self.keys = list(self.json.keys())
        self.fields = self.fields_counts()

    def __len__(self):
        return len(self.json)

    def __eq__(self, other):
        if isinstance(other, Metadata):
            return self.json == other.json
        else:
            return False

    def get(self, *args):
        res = {}
        for arg in args:
            if isinstance(arg, list):
                res.update(self._getMultiple(*arg))
            else:
                res.update(self._getMultiple(arg))
        return res
        
    """
    def get_single(self, id):
        return Metadata({id: self.json[id]}, reformat=False)
    """
    def _getMultiple(self, *accession):
        return {k: self.json[k] for k in accession if k in self.keys}

    def reset(self):
        self.json = self.full_json

    def to_dict(self):
        return metaToDict(self.json)

    def to_str(self):
        return metaToStr(self.json)

    def get_json(self):
        return json.dumps(self.to_dict())

    def get_fields(self):
        return metaToStr(self.fields)

    def fields_counts(self):
        fields = {}
        jsonDict = self.json
        for j in jsonDict.values():
            for k, v in j.items():
                fields.setdefault(k, {})
                fields[k].setdefault("values", {})
                fields[k].setdefault("count", 0)
                fields[k].setdefault("name", v["name"])
                # print(v["value"])
                add = v["value"]
                if isinstance(add, str) or isinstance(add, bool):
                    add = [add]
                elif isinstance(add, dict):
                    add = [json.dumps(add)]
                elif isinstance(add, list):
                    add = [json.dumps(val) if isinstance(
                        val, dict) else val for val in v["value"] if val]
                # print(add)
                if (not isinstance(add, type(None))) and (add):
                    # print(fields[k]["values"])
                    for val in add:
                        fields[k]["values"].setdefault(val, 0)
                        fields[k]["values"][val] += 1
                    fields[k]["count"] = len(fields[k]["values"].keys())
                    # print(fields[k]["values"])

        # res = fields.update({fields[k]: {"count": len(v["values"])} for k, v in fields.items()})
        json.fields = fields
        return metaToStr(fields)

    def get_field(self, field):
        if field in self.fields.keys():
            res = {k: v[field]["value"] for k, v in self.json.items()}
            return metaToStr(res)
        else:
            raise KeyError(f"{field} not in metadata")

    def filter(self, filters):
        filtered = copy.copy(self)
        match = set()
        for field, values in filters.items():
            if field in self.fields.keys():
                matchValues = set()
                for value in values:
                    # Find experiments with at least one matching value in specific field
                    allMatches = {k for k, v in self.json.items()
                                  if field in v.keys() and (
                        (isinstance(v[field]["value"], list)
                         and str(value) in [str(field_val) for field_val in v[field]["value"]])
                        or
                        (not isinstance(v[field]["value"], list)
                         and str(v[field]["value"]) == str(value))
                    )
                    }

                    matchValues = matchValues.union(allMatches)
                # Find experiments with at least one matching value in EVERY field
                match = match.intersection(
                    matchValues) if match != set() else matchValues
        filtered.json = filtered.get(list(match))
        filtered.fields = filtered.fields_counts()
        filtered.keys = list(filtered.json.keys())
        print(len(filtered.keys))
        return filtered
