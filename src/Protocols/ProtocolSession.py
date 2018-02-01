class ProtocolSession:
    streams = None

    def __init__(self, stream=None):
        self.streams = []

        if stream is not None:
            self.streams.append(stream)
