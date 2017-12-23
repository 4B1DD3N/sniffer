from StringIO import StringIO
from http_parser.http import HttpStream
from http_parser.reader import IterReader


class HTTPPacket:
    packet = None
    http_stream = None
    payload = None

    def __init__(self, packet=None):
        if packet is not None:
            self.packet = packet
            self.parse()

    def parse(self):
        try:
            reader = IterReader(StringIO(self.packet))

            self.http_stream = HttpStream(reader)

            self.payload = self.http_stream.body_file().read()
        except:
            self.payload = self.packet

        return self
