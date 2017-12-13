import socket
from struct import unpack


class IPPacket:
    packet = None
    payload = None
    header_length = 20
    version = None
    ihl = None
    type_of_service = None
    total_length = None
    identification = None
    offset = None
    ttl = None
    protocol = None
    checksum = None
    source_address = None
    destination_address = None

    def __init__(self, packet=None):
        if packet is not None:
            self.packet = packet
            self.parse()

    def get_protocol(self):
        return self.protocol

    def get_payload(self):
        return self.payload

    def parse(self):
        ip_header = unpack('!BBHHHBBH4s4s', self.packet[:self.header_length])

        self.version = ip_header[0] >> 4
        self.ihl = ip_header[0] & 0xF
        self.type_of_service = ip_header[1]
        self.total_length = ip_header[2]
        self.identification = ip_header[3]
        self.offset = ip_header[4]
        self.ttl = ip_header[5]
        self.protocol = ip_header[6]
        self.checksum = ip_header[7]
        self.source_address = socket.inet_ntoa(ip_header[8])
        self.destination_address = socket.inet_ntoa(ip_header[9])

        # Since an IPv4 header may contain a variable number of options, the IHL (Internet Header Length) field
        # specifies the size of the header (this also coincides with the offset to the data). The minimum value for this
        # field is 5, which indicates a length of 5 * 32 bits = 160 bits = 20 bytes. As a 4-bit field, the maximum value
        # is 15 words (15 * 32 bits, or 480 bits = 60 bytes).
        self.payload = self.packet[self.ihl * 4:]

        return self
