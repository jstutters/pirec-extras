import tarfile
from .exceptions import FileNotFound


def get_file(tf, filename):
    for member in tf:
        if member.name.endswith(filename):
            return tf.extractfile(member)
    else:
        raise FileNotFound(filename)


def extract_file(tar, filename, dest_filename):
    with tarfile.open(tar, 'r:gz') as tf:
        source = get_file(tf, filename)
        with open(dest_filename, 'w') as dest:
            dest.write(source.read())
