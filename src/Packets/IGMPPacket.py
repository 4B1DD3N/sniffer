from struct import unpack


class IGMPPacket:
    header_length = 8
    group_address = None
    type = None
    max_response_time = None
    checksum = None
    type_table = None

    def __init__(self, packet=None):
        if packet is not None:
            self.packet = packet
            self.parse()

        self.type_table = {
            0x11: 'Group Membership Query',
            0x12: 'IGMPv1 Membership Report',
            0x13: 'DVMRP',
            0x14: 'PIMv1',
            0x15: 'Cisco Trace Messages',
            0x16: 'IGMPv2 Membership Report',
            0x17: 'IGMPv2 Leave Group',
            0x1E: 'Multicast Traceroute Response',
            0x1F: 'Multicast Traceroute',
            0x22: 'IGMPv3 Membership Report',
            0x30: 'MRD, Multicast Router Advertisement',
            0x31: 'MRD, Multicast Router Solicitation',
            0x32: 'MRD, Multicast Router Termination',
        }

    def parse(self):
        igmp_header = unpack('!BBH4s', self.packet[:self.header_length])

        self.type = igmp_header[0]
        self.max_response_time = igmp_header[1]
        self.checksum = igmp_header[2]
        self.group_address = igmp_header[3]

        # If length it greater than 4 bytes, it's IGMPv3.
        # Parse accordingly...

        return self

    def get_type_description(self):
        if self.type_table.has_key(self.type):
            return self.type_table[self.type]
        else:
            return 'Unknown / experimental.'

    def to_string(self):
        return 'Type: %s, Max Resp Time: %s, Checksum: %s, Group Address: %s' \
               % (self.get_type_description(), self.max_response_time, self.checksum, self.group_address)
