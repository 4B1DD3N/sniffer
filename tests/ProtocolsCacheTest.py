import unittest

import os

from src.Protocols.ProtocolsCache import ProtocolsCache


class ProtocolTest(unittest.TestCase):
    path = None

    def clean_up_cache_file(self):
        if os.path.isfile(self.path):
            os.remove(self.path)

    def setUp(self):
        self.path = os.getcwd() + '/protocols_cache.p'
        self.clean_up_cache_file()

    def tearDown(self):
        self.clean_up_cache_file()

    def test_load_from_AINA_api(self):
        protocols_cache = ProtocolsCache()

        self.assertIsNotNone(protocols_cache.get_protocols())
        self.assertGreater(len(protocols_cache.get_protocols()), 0)
        self.assertTrue(protocols_cache.exists())

    def test_load_from_cache(self):
        protocols_cache = ProtocolsCache()

        self.assertTrue(protocols_cache.exists())

        del protocols_cache

        # Now let's load from the serialization.
        protocols_cache = ProtocolsCache()

        self.assertIsNotNone(protocols_cache.get_protocols())
        self.assertGreater(len(protocols_cache.get_protocols()), 0)
