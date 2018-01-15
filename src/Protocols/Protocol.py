class Protocol:
    service_name = None
    port_number = None
    transport_protocol = None
    description = None

    def __init__(self, service_name=None, port_number=None, transport_protocol=None, description=None):
        if service_name is not None:
            self.service_name = service_name

        if port_number is not None:
            self.port_number = port_number

        if transport_protocol is not None:
            self.transport_protocol = transport_protocol

        if description is not None:
            self.description = description

    def get_service_name(self):
        return self.service_name

    def get_port_number(self):
        if self.port_number is None:
            return None
        elif '-' in self.port_number:
            return self.port_number.split('-')

        return int(self.port_number)

    def is_port_number_in_port_range(self, port_number):
        port_numbers = self.get_port_number()

        if port_numbers is None:
            return False
        elif isinstance(port_numbers, list):
            for x in port_numbers:
                if int(x) == port_number:
                    return True
        else:
            return int(port_numbers) == port_number

        return False

    def get_transport_protocol(self):
        return self.transport_protocol

    def get_description(self):
        return self.description

    def to_string(self):
        return 'Protocol: %s, Port Number: %s, Transport Protocol: %s, Description: %s' \
               % (self.service_name, self.port_number, self.transport_protocol, self.description)
