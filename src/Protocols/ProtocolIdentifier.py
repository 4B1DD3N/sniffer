from src.Output.Message import Message
from src.Packets.UDPPacket import UDPPacket
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
        if isinstance(packet, TCPPacket) or isinstance(packet, UDPPacket):
            # @TODO Use more heuristic methods to identify the protocol.
            return self.identity_protocol_by_port_numbers([packet.get_source_port(), packet.get_destination_port()])
        else:
            return None

    def identity_protocol_by_port_numbers(self, port_numbers):
        for protocol in self.protocols:
            # If intersection exists between the protocol port numbers and the given port numbers, then we have found a
            # possible protocol.
            if len(set(protocol.get_port_numbers()) & set(port_numbers)) > 0:
                return protocol

        return None
