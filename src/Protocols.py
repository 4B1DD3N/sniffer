class Protocols:
    ports = None

    def __init__(self):
        # @TODO Should perhaps complete the list using an API...
        # https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml
        self.ports = {
            'File Transfer Protocol (TCP)': [20, 21],
            'Secure Shell (SSH)': 22,
            'Telnet': 23,
            'Simple Mail Transfer (SMTP)': 25,
            'Domain Name System (DNS)': 53,
            'Dynamic Host Configuration Protocol (DHCP)': [67, 68],
            'Trivial File Transfer Protocol (TFTP)': 69,
            'Hypertext Transfer Protocol (HTTP)': 80,
            'Post Office Protocol (POP) version 3': 110,
            'Network Time Protocol (NTP)': 123,
            'NetBIOS': [137, 138, 139],
            'Internet Message Access Protocol (IMAP)': 143,
            'Simple Network Management Protocol (SNMP)': [161, 162],
            'Border Gateway Protocol (BGP)': 179,
            'Lightweight Directory Access Protocol (LDAP)': 389,
            'Hypertext Transfer Protocol over SSL/TLS (HTTPS)': 443,
            'Lightweight Directory Access Protocol over TLS/SSL (LDAPS)': 636,
            'FTP over TLS/SSL': [989, 990]
        }

    def identify_protocol_by_port(self, port):
        for protocol, ports in self.ports.iteritems():
            if isinstance(ports, list):
                for p in ports:
                    if p == port:
                        return protocol
            else:
                if ports == port:
                    return protocol

        return None
