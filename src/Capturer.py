import datetime
import pcapy
from struct import unpack

from src.EthernetPacket import EthernetPacket
from src.IPPacket import IPPacket
from src.Message import Message
from src.TCPPacket import TCPPacket


class Capturer:
    interface = None
    message = None

    def __init__(self, interface):
        self.interface = interface
        self.message = Message()
        pass

    def parse_packet(self, packet):
        ethernet_packet = EthernetPacket(packet)

        self.message.info(ethernet_packet.to_string())

        if ethernet_packet.get_protocol() == 8:
            ip_packet = IPPacket(packet[ethernet_packet.get_length():20 + ethernet_packet.get_length()])

            self.message.info(ip_packet.to_string())

            if ip_packet.get_protocol() == 6:
                t = ip_packet.get_iph_length() + ethernet_packet.get_length()
                tcp_packet = TCPPacket(packet[t:t + 20])

                self.message.info(tcp_packet.to_string())

                h_size = ethernet_packet.get_length() + ip_packet.get_iph_length() + tcp_packet.get_tcp_header_length() * 4

                self.message.info('Data: %s' % tcp_packet.extract_data(packet, h_size))

            # ICMP Packets
            elif ip_packet.get_protocol() == 1:
                u = ip_packet.get_iph_length() + ethernet_packet.get_length()
                icmph_length = 4
                icmp_header = packet[u:u + 4]

                # now unpack them :)
                icmph = unpack('!BBH', icmp_header)

                icmp_type = icmph[0]
                code = icmph[1]
                checksum = icmph[2]

                self.message.info('Type : ' + str(icmp_type) + ' Code : ' + str(code) + ' Checksum : ' + str(checksum))

                h_size = ethernet_packet.get_length() + ip_packet.get_iph_length() + icmph_length
                data_size = len(packet) - h_size

                # get data from the packet
                data = packet[h_size:]

                self.message.info('Data : ' + data)

            # UDP packets
            elif ip_packet.get_protocol() == 17:
                u = ip_packet.get_iph_length() + ethernet_packet.get_length()
                udph_length = 8
                udp_header = packet[u:u + 8]

                # now unpack them :)
                udph = unpack('!HHHH', udp_header)

                source_port = udph[0]
                dest_port = udph[1]
                length = udph[2]
                checksum = udph[3]

                self.message.info('Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Length : ' + str(
                    length) + ' Checksum : ' + str(checksum))

                h_size = ethernet_packet.get_length() + ip_packet.get_iph_length() + udph_length
                data_size = len(packet) - h_size

                # get data from the packet
                data = packet[h_size:]

                self.message.info('Data : ' + data)

            # IGMP, ...
            else:
                self.message.info('Protocol other than TCP/UDP/ICMP')

    def start(self):
        cap = pcapy.open_live(self.interface, 65536, 1, 0)

        while True:
            (header, packet) = cap.next()
            self.message.info('%s: captured %d bytes, truncated to %d bytes' % (datetime.datetime.now(), header.getlen(), header.getcaplen()))
            self.parse_packet(packet)