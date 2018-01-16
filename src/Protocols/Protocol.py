class Protocol:
    service_name = None
    port_number = None
    transport_protocol = None
    description = None

    def __init__(self, service_name=None, port_number=None, transport_protocol=None, description=None):
        self.service_name = service_name
        self.port_number = port_number
        self.transport_protocol = transport_protocol
        self.description = description

    def get_service_name(self):
        return self.service_name

    def get_transport_protocol(self):
        return self.transport_protocol

    def get_description(self):
        return self.description

    def get_port_numbers(self):
        port_numbers = []

        if isinstance(self.port_number, int):
            port_numbers.append(self.port_number)
        elif self.port_number is not None:
            if '-' in self.port_number:
                port_numbers.extend([int(port_number) for port_number in self.port_number.split('-')])
            else:
                port_numbers.append(int(self.port_number))

        return port_numbers

    def to_string(self):
        return 'Protocol: %s, Port Number: %s, Transport Protocol: %s, Description: %s' \
               % (self.service_name, self.port_number, self.transport_protocol, self.description)
