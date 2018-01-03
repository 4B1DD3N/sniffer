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
            '''
            If we cannot parse the HTTP stream it most likely means we have to reassemble the HTTP transfer on a higher 
            layer, for instance TCP. For now, let's assume the packet itself is just part of the HTTP body.
            '''
            self.payload = self.packet

        return self

    def to_string(self):
        return 'HTTP payload: %s' % self.payload
