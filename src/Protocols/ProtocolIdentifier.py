from src.Output.Message import Message
from src.Protocols.ProtocolsCache import ProtocolsCache


class ProtocolIdentifier:
    protocols = None
    message = None

    def __init__(self):
        self.protocols = ProtocolsCache()
        self.message = Message()
        self.message.info('Sniffer can use heuristics to identify %s different protocols' % len(self.protocols))

    def identify(self):
        print len(self.protocols)
