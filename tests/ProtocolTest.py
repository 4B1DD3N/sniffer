import random
import string
import unittest

from src.Protocol import Protocol


class ProtocolTest(unittest.TestCase):
    protocol = None
    service_name = None
    port_number = None

    @staticmethod
    def random_string(length=32):
        return ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(length)])

    def setUp(self):
        self.service_name = ProtocolTest.random_string()
        self.port_number = random.randint(1, 1000)
        self.transport_protocol = ProtocolTest.random_string()
        self.description = ProtocolTest.random_string()

        self.protocol = Protocol(self.service_name, self.port_number, self.transport_protocol, self.description)

    def tearDown(self):
        self.protocol = None

    def test_service_name(self):
        self.assertIsNotNone(self.service_name)
        self.assertEqual(self.protocol.get_service_name(), self.service_name)

    def test_port_number(self):
        self.assertIsNotNone(self.port_number)
        self.assertEqual(self.protocol.get_port_number(), self.port_number)

    def test_transport_protocol(self):
        self.assertIsNotNone(self.transport_protocol)
        self.assertEqual(self.protocol.get_transport_protocol(), self.transport_protocol)

    def test_description(self):
        self.assertIsNotNone(self.description)
        self.assertEqual(self.protocol.get_description(), self.description)
