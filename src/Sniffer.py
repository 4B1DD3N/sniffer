from termcolor import colored
import os
import pcapy

from src.Capturer import Capturer
from src.Message import Message


class Sniffer:
    shell = True
    interface = None
    message = None

    def __init__(self):
        self.message = Message()
        pass

    def exit(self):
        self.shell = False

    def commands(self):
        self.message.info('commands: show all the commands')
        self.message.info('interface: set the interface to capture packets')
        self.message.info('start: start capturing packets')

    def start(self):
        Capturer()

    def set_interface(self):
        self.interface = self.message.info_raw('Interface for capturing packets: ')
        self.message.info('The capturing interface was changed.')
        self.message.info('Capturing will take place on interface: %s' % self.interface)

    def sniffer_ascii_art(self):
        with open('src/sniffer_ascii_art.txt', 'r') as ascii_art:
            for line in ascii_art.readlines():
                self.message.info(line)

    def list_devices(self):
        for device in pcapy.findalldevs():
            self.message.info(device)

    def menu(self):
        self.sniffer_ascii_art()

        while self.shell:
            commands = {
                'exit':      self.exit,
                'commands':  self.commands,
                'start':     self.start,
                'interface': self.set_interface,
                'devices':   self.list_devices
            }

            input = self.message.info_raw('Sniffer> ')

            if input in commands:
                commands.get(input)()
            else:
                os.system(input)
