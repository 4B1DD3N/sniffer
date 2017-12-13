from StringIO import StringIO

import zlib
from http_parser.http import HttpStream
from http_parser.reader import IterReader


class HTTPPacket:
    packet = None
    status_code = None
    version = None
    http_stream = None
    payload = None

    def __init__(self, packet=None):
        if packet is not None:
            self.packet = packet
            self.parse()

    def parse(self):
        reader = IterReader(StringIO(self.packet))

        self.http_stream = HttpStream(reader)

        try:
            # Bug: sometimes GZIP is not decompressed correctly...
            self.payload = self.http_stream.body_file().read()
        except:
            pass

        return self
