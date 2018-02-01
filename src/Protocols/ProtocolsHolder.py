from src.Output.Message import Message
from src.Packets.TCPPacket import TCPPacket
from src.Packets.UDPPacket import UDPPacket


class ProtocolsHolder:
    message = None
    unidentified_sessions = None
    identified_sessions = None

    def __init__(self):
        self.message = Message()
        self.unidentified_sessions = {}
        self.identified_sessions = {}

    @staticmethod
    def get_transport_packet_from_stream(stream):
        for packet in stream:
            if isinstance(packet, TCPPacket) or isinstance(packet, UDPPacket):
                return packet

        raise Exception('Cannot find transport packet in stream')

    def add_identified_session(self, protocol, packets):
        if not self.identified_sessions.has_key(protocol):
            self.identified_sessions[protocol] = [[packets]]
        else:
            transport_packet = ProtocolsHolder.get_transport_packet_from_stream(packets)

            for session in self.identified_sessions[protocol]:
                session_transport_packet = ProtocolsHolder.get_transport_packet_from_stream(session[0])

                if session_transport_packet.get_source_port() == transport_packet.get_source_port() and \
                        session_transport_packet.get_destination_port() == transport_packet.get_destination_port():
                    session.append(packets)
                    return

            # If we cannot find a saved session that corresponds to the packets stream, then we save it as a new whole
            # session.
            self.identified_sessions[protocol].append([packets])
