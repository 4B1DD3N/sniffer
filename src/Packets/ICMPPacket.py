from struct import unpack


class ICMPPacket:
    header = None
    icmp_type = None
    code = None
    checksum = None

    def __init__(self, header):
        self.header = header
        pass

    def get_icmp_type(self):
        return str(self.icmp_type)

    def get_code(self):
        return str(self.code)

    def get_checksum(self):
        return str(self.checksum)

    def extract_data(self, packet, offset):
        return packet[offset:]

    def parse(self):
        icmp_header = unpack('!BBH', self.header)

        self.icmp_type = icmp_header[0]
        self.code = icmp_header[1]
        self.checksum = icmp_header[2]

        return self

    def to_string(self):
        return 'ICMP type: %s, Code: %s, Checksum: %s' % (self.get_icmp_type(), self.get_code(), self.get_checksum())