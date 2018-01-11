import os
import pcapy

from src.Capturer import Capturer
from src.Message import Message


class Sniffer:
    shell = True
    interface = None
    message = None
    commands = None
    aliases = None

    def __init__(self, config=None):
        self.message = Message(config)

        self.commands = {
            'exit':       self.exit,
            'commands':   self.show_commands,
            'start':      self.start,
            'devices':    self.list_devices,
            'device set': self.set_device,
            'aliases':    self.show_aliases,
            'clear':      self.clear
        }
        self.aliases = {
            'd':  'devices',
            'ds': 'device set',
            'e':  'exit',
            'c':  'commands',
            's':  'start',
            'a':  'aliases',
            'l':  'clear'
        }

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def exit(self):
        self.shell = False

    def show_commands(self):
        for command in self.commands:
            self.message.info(command)

    def start(self):
        if self.interface is None:
            self.message.info('No device set.')
        else:
            self.clear()
            Capturer(self.interface).start()

    def set_device(self):
        i = 0

        devices = pcapy.findalldevs()

        for device in devices:
            self.message.info("%s %s" % (str(i), device))
            i += 1

        i -= 1

        input = int(self.message.info_raw('Device for capturing packets [0 -> %s]: ' % str(i)))

        if input > (len(devices) - 1) or input < 0:
            self.message.info('Invalid device. Try again.')
        else:
            self.interface = devices[input]
            self.message.info('The capturing device was changed.')
            self.message.info('Capturing will take place on device: %s' % self.interface)

    def sniffer_ascii_art(self):
        with open('src/sniffer_ascii_art.txt', 'r') as ascii_art:
            for line in ascii_art.readlines():
                self.message.info(line)

    def list_devices(self):
        for device in pcapy.findalldevs():
            self.message.info(device)

    def show_aliases(self):
        for alias in self.aliases:
            self.message.info("%s => %s" % (alias, self.aliases[alias]))

    def menu(self):
        self.sniffer_ascii_art()

        try:
            while self.shell:
                input = self.message.info_raw('Sniffer> ')

                if input in self.commands:
                    self.commands.get(input)()
                elif input in self.aliases:
                    self.commands.get(self.aliases[input])()
                else:
                    os.system(input)
        except (KeyboardInterrupt, SystemExit):
            pass
