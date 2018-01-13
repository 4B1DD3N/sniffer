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
        return self.port_number

    def get_transport_protocol(self):
        return self.transport_protocol

    def get_description(self):
        return self.description
