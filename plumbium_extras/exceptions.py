class ReportNotFound(Exception):
    def __init__(self):
        super(ReportNotFound, self).__init__('report.json not found in archive')


class FileNotFound(Exception):
    def __init__(self, filename):
        super(FileNotFound, self).__init__('{0} not found in archive'.format(filename))
