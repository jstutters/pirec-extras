import json
import re
import tarfile
import StringIO
from . import archive

ARRAY_EXP = r'(?P<key>^[A-Za-z][A-Za-z0-9_\-]*)(?P<index>\[[0-9]+\])'


def walk_path(path):
    for p in path.split('.'):
        m = re.match(ARRAY_EXP, p)
        if m is not None:
            index = int(m.group('index')[1:-1])
            yield (m.group('key'), index)
        else:
            yield (p, None)


def get_report_json(tf):
    archive.get_file(tf, 'report.json')


def get_from_dict_by_path(jsondoc, keypath):
    c = jsondoc
    for key, index in walk_path(keypath):
        if index is not None:
            c = c[key][index]
        else:
            c = c[key]
    return c


def getkey(tar, keypath):
    with tarfile.open(tar, 'r:gz') as tf:
        report_file = get_report_json(tf)
        report_json = json.load(report_file)
    val = get_from_dict_by_path(report_json, keypath)
    return val


def getkeys(tar, keypaths):
    with tarfile.open(tar, 'r:gz') as tf:
        report_file = get_report_json(tf)
        report_json = json.load(report_file)
        requested_vals = {}
        for k in keypaths:
            requested_vals[k] = get_from_dict_by_path(report_json, k)
    return requested_vals


def extract_report(tar):
    report_contents = StringIO.StringIO()
    with tarfile.open(tar, 'r:gz') as tf:
        report_file = get_report_json(tf)
        report_contents.write(report_file.read())
        report_contents.seek(0)
    return report_contents
