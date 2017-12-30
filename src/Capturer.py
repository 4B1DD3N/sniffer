import datetime
import pcapy

from src.Message import Message
from src.Packets.EthernetPacket import EthernetPacket
from src.Packets.HTTPPacket import HTTPPacket
from src.Packets.IPPacket import IPPacket
from src.Packets.TCPPacket import TCPPacket
from src.Packets.UDPPacket import UDPPacket


class Capturer:
    interface = None
    message = None
    verbose = 0
    http_packets = []

    def __init__(self, interface):
        self.interface = interface
        self.message = Message()

    def start(self):
        cap = pcapy.open_live(self.interface, 65536, 1, 0)

        while True:
            (header, packet) = cap.next()

            if self.verbose > 0:
                self.message.info_space('%s: captured %d bytes, truncated to %d bytes' % (datetime.datetime.now(), header.getlen(), header.getcaplen()))

            self.parse(header, packet)

    def parse(self, header, packet):
        ethernet_packet = EthernetPacket(packet)

        ethernet_packet_type = ethernet_packet.get_type()

        # IP? ARP? RARP? etc (8, 56710)
        if ethernet_packet_type == 8:
            ethernet_packet_payload = ethernet_packet.get_payload()

            ip_packet = IPPacket(ethernet_packet_payload)

            ip_packet_protocol = ip_packet.get_protocol()

            ip_packet_payload = ip_packet.get_payload()

            if ip_packet_protocol == 6:
                tcp_packet = TCPPacket(ip_packet_payload)

                tcp_packet_payload = tcp_packet.get_payload()

                if "HTTP" in tcp_packet_payload:
                    http_packet = HTTPPacket(tcp_packet_payload)

                    self.http_packets.append(http_packet)

                    self.message.info_space(self.http_packets)

            elif ip_packet_protocol == 17:
                udp_packet = UDPPacket(ip_packet_payload)

                self.message.info('UDP PACKET FOUND')
                self.message.info_space(udp_packet.to_string())
                self.message.info(udp_packet.get_payload())

            elif ip_packet_protocol == 1:
                self.message.info_space('ICMP not yet supported.')
