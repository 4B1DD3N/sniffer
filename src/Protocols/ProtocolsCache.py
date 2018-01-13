import os
import pickle
from xml.etree import ElementTree

import requests

from src.Output.Message import Message
from src.Protocols.Protocol import Protocol


class ProtocolsCache:
    message = None
    protocols = None
    path = None
    IANA_api = None

    def __init__(self):
        self.message = Message()
        self.protocols = []
        self.path = os.getcwd() + '/protocols_cache.p'
        self.IANA_api = 'https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xml'
        self.load()

    def load_from_AINA_api(self):
        self.message.info('Fetching the protocols from the IANA api')

        for record in ElementTree.fromstring(requests.get(self.IANA_api).content):
            service_name = None
            port_number = None
            transport_protocol = None
            description = None

            if record.tag == '{http://www.iana.org/assignments}record':
                for node in record:
                    if node.tag == '{http://www.iana.org/assignments}name':
                        service_name = node.text
                    elif node.tag == '{http://www.iana.org/assignments}number':
                        port_number = node.text
                    elif node.tag == '{http://www.iana.org/assignments}protocol':
                        transport_protocol = node.text
                    elif node.tag == '{http://www.iana.org/assignments}description':
                        description = node.text

                    self.protocols.append(Protocol(service_name, port_number, transport_protocol, description))

        self.message.info('Fetched %s protocols from AINA api' % len(self.protocols))

    def load(self):
        if self.exists():
            self.load_from_cache()
        else:
            self.load_from_AINA_api()

            self.serialize_protocols_cache()

    def serialize_protocols_cache(self):
        self.message.info('Creating the protocols cache for faster usage in the future')

        with open(self.path, 'wb') as protocols_cache:
            protocols_cache.write(pickle.dumps(self.protocols))

    def exists(self):
        self.message.info('Checking if the protocols cache exists')

        if not os.path.isfile(self.path):
            self.message.info('The protocols cache does not exist')

            return False
        else:
            self.message.info('The protocols cache exists')

            return True

    def load_from_cache(self):
        self.message.info('Loading the protocols cache')

        with open(self.path) as protocols_cache:
            self.protocols = pickle.load(protocols_cache)

        self.message.info('Loaded %s protocols from the cache' % len(self.protocols))

    def get_protocols(self):
        return self.protocols

    def __iter__(self):
        return iter(self.protocols)

    def __len__(self):
        return len(self.protocols)
