import datetime
import pcapy

from src.Output.Message import Message
from src.Packets.EthernetPacket import EthernetPacket
from src.Packets.ICMPPacket import ICMPPacket
from src.Packets.IGMPPacket import IGMPPacket
from src.Packets.IPPacket import IPPacket
from src.Packets.TCPPacket import TCPPacket
from src.Packets.UDPPacket import UDPPacket
from src.Protocols.ProtocolIdentifier import ProtocolIdentifier
from src.Protocols.ProtocolsHolder import ProtocolsHolder


class Capturer:
    interface = None
    message = None
    verbose = 0
    protocol_identifier = None
    protocols_holder = None
    # remove
    identified_protocols_list = None
    known_protocols = None
    unknown_protocols = None

    def __init__(self, interface):
        self.interface = interface
        self.message = Message()
        self.protocol_identifier = ProtocolIdentifier()
        self.protocols_holder = ProtocolsHolder()

        # remove
        self.known_protocols = 0
        self.unknown_protocols = 0
        self.identified_protocols_list = []

        self.start()

    def display_header_information(self, header):
        self.message.info('%s: captured %d bytes, truncated to %d bytes'
                                % (datetime.datetime.now(), header.getlen(), header.getcaplen()))

    def start(self):
        try:
            cap = pcapy.open_live(self.interface, 65536, 1, 0)

            # remove
            time = datetime.datetime.now()

            while True:
                (header, packet) = cap.next()

                self.parse_packet(packet)

                # remove
                # run every x seconds
                delta = datetime.datetime.now()-time
                if delta.seconds >= 3:
                    self.message.info('[%s] %s identified protocols, %s unidentified protocols\n    %s'
                                      % (unicode(datetime.datetime.now().replace(microsecond=0)),
                                         self.known_protocols,
                                         self.unknown_protocols,
                                         self.identified_protocols_list,))
                    time = datetime.datetime.now()

        except (KeyboardInterrupt, SystemExit):
            pass

    def parse_packet(self, packet):
        ethernet_packet = EthernetPacket(packet)
        ethernet_packet_type = ethernet_packet.get_type()

        if ethernet_packet_type == 8:
            ethernet_packet_payload = ethernet_packet.get_payload()

            ip_packet = IPPacket(ethernet_packet_payload)
            ip_packet_protocol = ip_packet.get_protocol()
            ip_packet_payload = ip_packet.get_payload()

            if ip_packet_protocol == 6:
                tcp_packet = TCPPacket(ip_packet_payload)

                protocol = self.protocol_identifier.identify_protocol(tcp_packet)

                if protocol is not None:
                    self.known_protocols += 1

                    # if protocol.get_service_name() != 'ssh':
                    #    self.message.info(protocol.to_string())
                    # self.message.info('Found protocol: %s' % protocol.get_service_name())
                    # Maybe we can parse this protocol already? (HTTP, DNS, FTP, etc)
                    # self.protocols_holder.add_identified_session(protocol, [ethernet_packet, ip_packet, tcp_packet])
                    if protocol.get_service_name() not in self.identified_protocols_list:
                        self.identified_protocols_list.append(protocol.get_service_name())
                else:
                    self.unknown_protocols += 1

            elif ip_packet_protocol == 17:
                udp_packet = UDPPacket(ip_packet_payload)

                protocol = self.protocol_identifier.identify_protocol(udp_packet)

                if protocol is not None:
                    self.known_protocols += 1

                    if protocol.get_service_name() not in self.identified_protocols_list:
                        self.identified_protocols_list.append(protocol.get_service_name())
                else:
                    self.unknown_protocols += 1

            elif ip_packet_protocol == 1:
                #icmp_packet = ICMPPacket(ip_packet_payload)

                #self.message.info(icmp_packet.to_string())
                self.known_protocols += 1

            elif ip_packet_protocol == 2:
                # igmp_packet = IGMPPacket(ip_packet_payload)
                self.known_protocols += 1


                #self.message.info(igmp_packet.to_string())

            else:
                self.unknown_protocols += 1
                # self.message.info('Unsupported protocol (not UDP, TCP, ICMP, IGMP): %s' % ip_packet_protocol)

        else:
            self.unknown_protocols += 1
            # self.message.info('Unsupported data type (ARP, RARP, etc): %s' % ethernet_packet_type)
