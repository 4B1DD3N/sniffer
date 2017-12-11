import socket
from struct import unpack


class EthernetPacket:
    header = None
    protocol = None
    destination_mac = None
    source_mac = None
    length = 14

    def __init__(self, header):
        self.header = header
        self.parse()
        pass

    # Convert a string of 6 characters of ethernet address into a dash separated hex string
    def eth_addr(self, address):
        return "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(address[0]), ord(address[1]), ord(address[2]), ord(address[3]),
                                                  ord(address[4]), ord(address[5]))

    def parse(self):
        header = self.header[:self.length]

        eth = unpack('!6s6sH', header)

        self.protocol = str(socket.ntohs(eth[2]))
        self.destination_mac = self.eth_addr(self.header[0:6])
        self.source_mac = self.eth_addr(self.header[6:12])

        return self

    def get_protocol(self):
        return int(self.protocol)

    def get_destination_mac(self):
        return self.destination_mac

    def get_source_mac(self):
        return self.source_mac

    def get_length(self):
        return int(self.length)

    def to_string(self):
        return 'Destination MAC: %s, Source MAC: %s, Protocol: %s' % (self.get_destination_mac(), self.get_source_mac(), self.get_protocol())