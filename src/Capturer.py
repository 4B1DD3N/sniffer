import datetime
import pcapy

from src.Message import Message
from src.Packets.EthernetPacket import EthernetPacket
from src.Packets.HTTPPacket import HTTPPacket
from src.Packets.IGMPPacket import IGMPPacket
from src.Packets.IPPacket import IPPacket
from src.Packets.TCPPacket import TCPPacket
from src.Packets.UDPPacket import UDPPacket
from src.Protocols import Protocols


class Capturer:
    interface = None
    message = None
    verbose = 0
    captured_data = None

    def __init__(self, interface):
        self.interface = interface
        self.message = Message()

    def start(self):
        try:
            cap = pcapy.open_live(self.interface, 65536, 1, 0)

            while True:
                (header, packet) = cap.next()

                if self.verbose > 0:
                    self.message.info_space('%s: captured %d bytes, truncated to %d bytes'
                                            % (datetime.datetime.now(), header.getlen(), header.getcaplen()))

                self.parse(header, packet)

        except (KeyboardInterrupt, SystemExit):
            self.message.info('Stopped capturing packets.')

    def parse(self, header, packet):
        ethernet_packet = EthernetPacket(packet)

        ethernet_packet_type = ethernet_packet.get_type()

        if ethernet_packet_type == 8:
            ethernet_packet_payload = ethernet_packet.get_payload()

            ip_packet = IPPacket(ethernet_packet_payload)

            ip_packet_protocol = ip_packet.get_protocol()

            ip_packet_payload = ip_packet.get_payload()

            if ip_packet_protocol == 6:
                tcp_packet = TCPPacket(ip_packet_payload)

                tcp_packet_payload = tcp_packet.get_payload()

                # HTTP/1.1, HTTP/2.0
                if "HTTP" in tcp_packet_payload:
                    http_packet = HTTPPacket(tcp_packet_payload)

                    self.message.info(tcp_packet_payload)

                    self.message.info_space(http_packet.to_string())

                else:
                    protocol = Protocols().identify_protocol_by_port(tcp_packet.get_source_port())

                    if protocol is not None:
                        self.message.info_space('Found protocol %s in TCP packet' % protocol)
                    else:
                        self.message.info(tcp_packet.to_string())

            elif ip_packet_protocol == 17:
                udp_packet = UDPPacket(ip_packet_payload)

                self.message.info_space(udp_packet.to_string())
                self.message.info(udp_packet.get_payload())

            elif ip_packet_protocol == 1:
                self.message.info_space('ICMP not yet fully supported.')

            elif ip_packet_protocol == 2:
                igmp_packet = IGMPPacket(ip_packet_payload)

                self.message.info(igmp_packet.to_string())

            else:
                self.message.info_space('Unsupported protocol (not UDP, TCP, ICMP): %s' % ip_packet_protocol)

        else:
            self.message.info_space('Unsupported type (ARP, RARP, etc): %s' % ethernet_packet_type)
