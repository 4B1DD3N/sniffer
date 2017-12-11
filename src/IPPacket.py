import socket
from struct import unpack


class IPPacket:
    header = None
    version = None
    ihl = None
    iph_length = None
    protocol = None
    source_address = None
    destination_address = None
    ttl = None

    def __init__(self, header):
        self.header = header
        self.parse()
        pass

    def parse(self):
        ip_header = unpack('!BBHHHBBH4s4s', self.header)

        version_ihl = ip_header[0]
        self.version = version_ihl >> 4
        self.ihl = version_ihl & 0xF
        self.iph_length = self.ihl * 4
        self.ttl = ip_header[5]
        self.protocol = ip_header[6]
        self.source_address = socket.inet_ntoa(ip_header[8])
        self.destination_address = socket.inet_ntoa(ip_header[9])

        return self

    def get_version(self):
        return str(self.version)

    def get_protocol(self):
        return int(self.protocol)

    def get_ttl(self):
        return str(self.ttl)

    def get_source_address(self):
        return str(self.source_address)

    def get_destination_address(self):
        return str(self.destination_address)

    def get_ihl(self):
        return str(self.ihl)

    def get_iph_length(self):
        return int(self.iph_length)

    def to_string(self):
        return 'Version: %s, IP Header Length: %s, TTL: %s, Protocol: %s, Source Address: %s, Destination Address: %s ' % (self.get_version(), self.get_ihl(), self.get_ttl(), self.get_protocol(), self.get_source_address(), self.get_destination_address())