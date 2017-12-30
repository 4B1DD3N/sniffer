from struct import unpack


class UDPPacket:
    header_length = 8
    packet = None
    source_port = None
    destination_port = None
    length = None
    checksum = None
    payload = None

    def __init__(self, packet=None):
        if packet is not None:
            self.packet = packet
            self.parse()

    def get_payload(self):
        return self.payload

    def parse(self):
        udp_header = unpack('!HHHH', self.packet[:self.header_length])

        self.source_port = udp_header[0]
        self.destination_port = udp_header[1]
        self.length = udp_header[2]
        self.checksum = udp_header[3]
        self.payload = self.packet[self.header_length:]

        return self

    def to_string(self):
        return 'Source Port: %s, Destination Port: %s, Length: %s, Checksum: %s' \
               % (self.source_port, self.destination_port, self.length, self.checksum)
