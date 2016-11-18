import json
import re
import tarfile

ARRAY_EXP = r'(?P<key>^[A-Za-z][A-Za-z0-9_\-]*)(?P<index>\[[0-9]+\])'


def get_report_json(tf):
    for member in tf:
        if member.name.endswith('report.json'):
            return tf.extractfile(member)


def get_from_dict_by_path(jsondoc, keypath):
    c = jsondoc
    for p in keypath.split('.'):
        m = re.match(ARRAY_EXP, p)
        if m is not None:
            index = int(m.group('index')[1:-1])
            keyval = c.get(m.group('key'))
            c = keyval[index]
        else:
            c = c.get(p)
    return c


def getkey(tar, keypath):
    with tarfile.open(tar, 'r:gz') as tf:
        report_file = get_report_json(tf)
        report_json = json.load(report_file)
    return get_from_dict_by_path(report_json, keypath)
