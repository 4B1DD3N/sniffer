from struct import unpack


class ICMPPacket:
    header = None
    icmp_type = None
    code = None
    checksum = None

    def __init__(self, header):
        self.header = header
        pass

    def parse(self):
        # TODO

        return self