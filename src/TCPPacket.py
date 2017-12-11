from struct import unpack


class TCPPacket:
    header = None
    source_port = None
    destination_port = None
    sequence = None
    acknowledgement = None
    doff_reserved = None
    tcp_header_length = None

    def __init__(self, header):
        self.header = header
        self.parse()
        pass

    def extract_data(self, packet, offset):
        return packet[offset:]

    def parse(self):
        tcp_header = unpack('!HHLLBBHHH', self.header)

        self.source_port = tcp_header[0]
        self.destination_port = tcp_header[1]
        self.sequence = tcp_header[2]
        self.acknowledgement = tcp_header[3]
        self.doff_reserved = tcp_header[4]
        self.tcp_header_length = self.doff_reserved >> 4

        return self

    def get_source_port(self):
        return int(self.source_port)

    def get_destination_port(self):
        return int(self.destination_port)

    def get_sequence_number(self):
        return int(self.sequence)

    def get_acknowledgement(self):
        return int(self.acknowledgement)

    def get_tcp_header_length(self):
        return int(self.tcp_header_length)

    def to_string(self):
        return 'Source port: %s, Destination Port: %s, Sequence Number: %s, Acknowledgement: %s, TCP Header Length: %s' % (self.get_source_port(), self.get_destination_port(), self.get_sequence_number(), self.get_acknowledgement(), self.get_tcp_header_length())