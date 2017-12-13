import socket
from struct import unpack


class EthernetPacket:
    packet = None
    header_length = 14
    payload = None
    type = None
    destination_address = None
    source_address = None

    def __init__(self, packet=None):
        if packet is not None:
            self.packet = packet
            self.parse()

    @staticmethod
    def ethernet_address(address):
        return "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(address[0]),
                                                  ord(address[1]),
                                                  ord(address[2]),
                                                  ord(address[3]),
                                                  ord(address[4]),
                                                  ord(address[5]))

    def get_type(self):
        return self.type

    def get_payload(self):
        return self.payload

    def parse(self):
        if self.packet is None:
            raise Exception('No packet data specified.')

        header = unpack('!6s6sH', self.packet[:self.header_length])

        self.destination_address = self.ethernet_address(header[0])
        self.source_address = self.ethernet_address(header[1])
        self.type = socket.ntohs(header[2])
        self.payload = self.packet[self.header_length:]

        return self
