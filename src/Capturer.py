import datetime
import pcapy

from src.Message import Message


class Capturer:
    interface = None
    message = None

    def __init__(self, interface):
        self.interface = interface
        self.message = Message()
        pass

    def start(self):
        self.message.info('The interface is %s' % self.interface)
        self.message.info('Starting capturing packets...')

        cap = pcapy.open_live(self.interface, 65536, 1, 0)

        while True:
            (header, packet) = cap.next()
            self.message.info('Capturing packet...')
            self.message.info('%s: captured %d bytes, truncated to %d bytes' % (datetime.datetime.now(), header.getlen(), header.getcaplen()))