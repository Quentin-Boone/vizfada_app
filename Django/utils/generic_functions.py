SPLIT_EXCEPTIONS = ["poolOfSpecimens", "cellSpecimen"]

def xstr(s):
    if s == 0 or s is False:
        return s
    else:
        return s or ""


def split_on_upper(string, capitalize=True):
    parent = string[:string.rfind(".")]
    dotidx = string.rfind(".")
    if parent in SPLIT_EXCEPTIONS:
        string = parent + string[dotidx+1].upper() + string[dotidx+2:]
    else:
        string = string[dotidx+1:]
    if "_" in string:
        string = string[:string.rfind("_")]
    uppers = [i for i in string if i.isupper()]
    for i in uppers:
        string = string.replace(i, " {}".format(i.lower()))
    string = string.capitalize()
    return string
