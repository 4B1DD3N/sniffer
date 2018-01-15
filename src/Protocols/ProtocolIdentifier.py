from src.Output.Message import Message
from src.Packets.TCPPacket import TCPPacket
from src.Protocols.ProtocolsCache import ProtocolsCache


class ProtocolIdentifier:
    protocols = None
    message = None

    def __init__(self):
        self.protocols = ProtocolsCache()
        self.message = Message()
        self.message.info('Sniffer can use heuristics to identify %s different protocols' % len(self.protocols))

    def identify_protocol(self, packet):
        if isinstance(packet, TCPPacket):
            protocol = self.identity_by_port_number(packet.get_source_port())

            if protocol is not None:
                self.message.info('Identified protocol! %s' % protocol.to_string())
            else:
                self.message.info('Unable to identify protocol')
        else:
            self.message.info('Unsupported transport protocol (not TCP/UDP)')

    def identity_by_port_number(self, port_number):
        for protocol in self.protocols:
            if protocol.is_port_number_in_port_range(port_number):
                return protocol

        return None
