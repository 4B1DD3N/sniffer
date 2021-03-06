from struct import unpack


class TCPPacket:
    packet = None
    header_length = 20
    payload = None
    source_port = None
    destination_port = None
    sequence_number = None
    acknowledgement_number = None
    offset = None
    flags = None
    window = None
    checksum = None
    urgent_pointer = None

    def __init__(self, packet=None):
        if packet is not None:
            self.packet = packet
            self.parse()

    def get_payload(self):
        return self.payload

    def get_source_port(self):
        return int(self.source_port)

    def get_destination_port(self):
        return int(self.destination_port)

    def parse(self):
        tcp_header = unpack('!HHLLBBHHH', self.packet[:self.header_length])

        self.source_port = tcp_header[0]
        self.destination_port = tcp_header[1]
        self.sequence_number = tcp_header[2]
        self.acknowledgement_number = tcp_header[3]
        self.offset = tcp_header[4]
        self.flags = tcp_header[5]
        self.window = tcp_header[6]
        self.checksum = tcp_header[7]
        self.urgent_pointer = tcp_header[8]
        # The data offset field stores the total size of a TCP header in multiples of four bytes.
        self.payload = self.packet[self.offset / 4:]

        return self

    def to_string(self):
        return 'TCP Source port: %s, Destination port: %s, Checmsum: %s' \
               % (self.source_port, self.destination_port, self.checksum)
