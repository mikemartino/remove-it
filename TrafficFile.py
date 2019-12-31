class TrafficFile:
    def __init__(self, filename, filetype):
        self.filename = filename
        self.filetype = filetype

    def __repr__(self):
        return "[{} => filename: {}, filetype: {}]".format(__name__, self.filename, self.filetype)
